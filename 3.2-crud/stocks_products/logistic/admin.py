from django.contrib import admin
from .models import Stock, StockProduct, Product
# Register your models here.





class StockProductInline(admin.TabularInline):
    model = StockProduct

    extra = 1

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
@admin.register(StockProduct)
class ProductAdmin(admin.ModelAdmin):
    model = StockProduct




