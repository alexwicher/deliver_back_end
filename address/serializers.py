from rest_framework import serializers


class AddressListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        dict = {}
        for item in validated_data:
            dict[item.id] = item.address
        return dict


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = AddressListSerializer
