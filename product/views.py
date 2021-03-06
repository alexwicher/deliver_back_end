from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Category, Product
from product.serializers import CategoriesListSerializer, ProductsListSerializer


class CategoriesList(APIView):
    permission_classes = []

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesListSerializer(categories, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ProductsList(APIView):
    permission_classes = []

    def post(self, request):
        if (request.data['category_id'] == 0):
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category_id=request.data['category_id'])
        serializer = ProductsListSerializer(products, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
