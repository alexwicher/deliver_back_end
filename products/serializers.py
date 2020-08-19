from rest_framework import serializers

from products.models import Category, Product


class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class ProductsListSerializer(serializers.ModelSerializer):
    category = CategoriesListSerializer()
    class Meta:
        model = Product
        fields = ('id','name','price','category','image')