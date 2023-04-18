from django.urls import path

from .views import (EquipmentListCreateAPIView, EquipmentTypeListAPIView,
                    EquipmentUpdateDeleteAPIView)

app_name = "equipment_api"

urlpatterns = [
    path("equipment/", EquipmentListCreateAPIView.as_view()),
    path("equipment/<int:pk>", EquipmentUpdateDeleteAPIView.as_view()),
    path("equipment-type/", EquipmentTypeListAPIView.as_view()),
]
