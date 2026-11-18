from rest_framework import serializers

from booking_manager.models import Booking, BookingService


# class BookingSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     is_active = serializers.BooleanField()
#
#
#     def create(self, validated_data):
#         return Booking(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.is_active = validated_data.get('is_active')
#         return instance

class BookingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Booking
        fields = ("id","name","is_active")



class BookingServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingService
        fields = ("id","name","category", "price")


class BookingListSerializer(serializers.ModelSerializer):
    booking_service = BookingServiceSerializer()

    class Meta:
        model = Booking
        fields = ("id","name","is_active","booking_service","barber")



