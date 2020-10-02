from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from address.models import Address
from address.serializers import AddressSerializer


class AddressAdd(APIView):

    def post(self, request):
        address = Address(user_id=request.user.id, address=request.data['direction']).save()
        return Response({'dirId': address.id}, status=status.HTTP_202_ACCEPTED)


class AddressDelete(APIView):

    def post(self, request):
        Address.objects.filter(id=request.data['dirId']).delete()
        return Response(None, status=status.HTTP_202_ACCEPTED)


class AddressGet(APIView):

    def get(self, request):
        addresses = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(addresses, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
