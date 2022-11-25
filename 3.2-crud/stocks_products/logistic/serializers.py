from rest_framework import serializers

from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', ]


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price', ]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions', ]
        # настройте сериализатор для склада

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for item in positions:
            item['stock'] = stock
            StockProduct.objects.create(**item)
        return stock

    def update(self, instance, validated_data):
        print('++++++++++++++++++++++++++++++++++++++')
        print('instance-->', instance)
        positions = validated_data.pop('positions')
        print('positions-->', positions)
        stock = super().update(instance, validated_data)
        print('stock-->', stock)
        print('--------------------------------------')

        for item in positions:
            print('item-->', item)
            StockProduct.objects.update_or_create(
                stock=stock, product=item.get('product'),
                defaults={'price': item.get('price'), 'quantity': item.get('quantity')},
            )
        return stock
