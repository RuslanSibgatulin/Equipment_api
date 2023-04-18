from django.db import models
from django.utils.translation import gettext_lazy as _


class EquipmentType(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    sn_mask = models.CharField(_("SN mask"), max_length=50)

    def __str__(self) -> str:
        return f"Type {self.name}"


class Equipment(models.Model):
    type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        verbose_name=_("Type"),
    )
    sn = models.CharField(_("SN"), max_length=50)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["type", "sn"],
                name="type_sn_idx")
        ]

    def __str__(self) -> str:
        return f"Equipment {self.sn}"
