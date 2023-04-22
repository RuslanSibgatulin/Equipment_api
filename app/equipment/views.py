from django.core.exceptions import ValidationError
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Equipment, EquipmentType
from .serializers import EquipmentSerializer, EquipmentTypeSerializer


class EquipmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all().order_by("id")
    serializer_class = EquipmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ["type__name", "sn"]

    def get_serializer(self, *args, **kwargs):
        data = kwargs.get("data", {})
        if isinstance(data, list):
            kwargs["many"] = True
        return super(EquipmentListCreateAPIView, self).get_serializer(*args, **kwargs)

    @swagger_auto_schema(
        request_body=EquipmentSerializer(many=True)
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class EquipmentUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ["get", "put", "delete"]


class EquipmentTypeListAPIView(generics.ListAPIView):
    queryset = EquipmentType.objects.all().order_by("name")
    serializer_class = EquipmentTypeSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "sn_mask"]
