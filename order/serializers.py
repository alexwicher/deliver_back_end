from rest_framework import serializers

from order.models import Order, OrderItem


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id',)

class OrderItemsGetSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField('get_product_name')
    product_price = serializers.SerializerMethodField('get_product_price')
    total = serializers.SerializerMethodField('get_total')

    def get_product_price(self, obj):
        product_price = obj.product.price 
        return product_price

    def get_product_name(self, obj):
        product_name = obj.product.name
        return product_name

    def get_total(self, obj):
        total = obj.product.price * obj.quantity
        return total

    class Meta:
        model = OrderItem
        fields = ('quantity','product_name','product_price','total')

class OrderGetSerializer(serializers.ModelSerializer):
    items = OrderItemsGetSerializer(many=True)
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.product.price * item.quantity
        return total

    class Meta:
        model = Order
        fields = ('id','created','updated','items','total','paid')
