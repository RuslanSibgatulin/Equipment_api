from django.contrib import admin

from .models import Equipment, EquipmentType


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("name", "sn_mask")

    # Поиск по полям
    search_fields = ("name", )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("type", "sn")

    # Поиск по полям
    search_fields = ("sn", )

    # Фильтрация в списке
    list_filter = ("type", )
