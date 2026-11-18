from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from account.models import User
from booking_manager.api.v1.serializers import BookingSerializer, BookingListSerializer
from booking_manager.models import Booking
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from booking_manager.permissions import CustomUserPermission
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)

#
# @api_view(['POST',"GET","PUT"])
# @renderer_classes([JSONRenderer])
# def hello_world(request, pk: int | None = None):
#
#     if request.method == "PUT":
#         instance = User.objects.get(id=id)
#         if instance:
#             serializer = BookingSerializer(data=request.data)
#             serializer.update(instance=instance, validated_data=serializer.validated_data)
#     if request.method == "POST":
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             instance = serializer.create(request.data)
#             instance.save()
#
#     if request.method == "GET" and pk:
#         instance = Booking.objects.get(id=pk)
#
#         serializer = BookingSerializer(data={"name":instance.name,"is_active": instance.is_active})
#
#         serializer.is_valid(raise_exception=True)
#         return Response({"name":serializer.validated_data["name"],"is_active":serializer.validated_data["is_active"]})
#
#     return Response({200:"OK"})
#     # if request.method == "GET":
    #     return Response({422:"validation error"})


# class BookingViewList(APIView):
#
#     def get(self, request, format=None):
#         instance = Booking.objects.all()
#         serializer = BookingListSerializer(instance, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             instance = serializer.create(serializer.validated_data)
#             instance.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingViewList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, CustomUserPermission]
    # authentication_classes = [TokenAuthentication]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
#
# class BookingDetailView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Booking.objects.get(pk=pk)
#         except Booking.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         instance = self.get_object(pk)
#         serializer = BookingSerializer(instance)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         instance = self.get_object(pk)
#         serializer = BookingSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             instance = serializer.update(instance,serializer.validated_data)
#             instance.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         instance = self.get_object(pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)