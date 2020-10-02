from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import TokenObtainPairSerializerCustom


class TokenObtainPairViewCustom(APIView):
    permission_classes = []

    def post(self, request):
        serializer = TokenObtainPairSerializerCustom(request.data)
        return Response(serializer.validate(request.data))
