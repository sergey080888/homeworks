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
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(f'--------------------{positions}')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for a in positions:
            StockProduct.objects.create(stock=stock,product=a['product'],quantity=a['quantity'],price=a['price'])
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for a in positions:
            StockProduct.objects.create(stock=stock,product=a['product'],quantity=a['quantity'],price=a['price'])
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions


        return stock
