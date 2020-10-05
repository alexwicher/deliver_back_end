from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order, OrderItem
from order.serializers import OrderCreateSerializer, OrderGetSerializer
from product.models import Product


class OrderCreate(APIView):

    def post(self, request):
        current_user = request.user
        orderItems = request.data['orderItems']
        if (orderItems):
            order = Order(user=current_user)
            order.save()
            for key, item in orderItems.items():
                product = Product.objects.get(id=key)
                OrderItem.objects.create(order=order, product=product, price=product.price, quantity=item['quantity'])
            serializer = OrderCreateSerializer(order,many= False, read_only=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)

class OrderGet(APIView):

    def get(self, request):
        current_user = request.user
        order = Order.objects.filter(user=current_user)
        serializer = OrderGetSerializer(order,many=True,read_only=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
