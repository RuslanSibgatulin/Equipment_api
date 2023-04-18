import logging

from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Equipment, EquipmentType

char_map = {
    "N": "[0-9]",
    "A": "[A-Z]",
    "a": "[a-z]",
    "X": "([A-Z]|[0-9])",
    "Z": "[-|_|@]"
}

logger = logging.getLogger(__name__)


@receiver(pre_save, sender="equipment.Equipment")
def validate_equipment(sender, instance: Equipment, **kwargs):
    """Validate equipment SN by pattern of type
    """
    sn_mask = instance.type.sn_mask
    sn_pattern = ""
    for mask in sn_mask:
        sn_pattern += char_map[mask]

    logger.debug("Validate SN value: %s by pattern: %s", instance.sn, sn_pattern)
    RegexValidator(
        regex=sn_pattern,
        message=f"Invalid SN value: {instance.sn}. Enter a valid SN with mask: {sn_mask}."
    ).__call__(instance.sn)


@receiver(pre_save, sender="equipment.EquipmentType")
def validate_equipment_type(sender, instance: EquipmentType, **kwargs):
    """Validate sn_mask by pattern ^[A|N|X|Z|a]+$
    """
    allowed_chars = "|".join(char_map)
    mask_pattern = f"^[{allowed_chars}]+$"
    logger.debug("Validate SN mask: %s by pattern: %s", instance.sn_mask, mask_pattern)
    RegexValidator(
        regex=mask_pattern,
        message=f"Invalid SN mask value: {instance.sn_mask}. Use allowed chars {allowed_chars} instead."
    ).__call__(instance.sn_mask)
