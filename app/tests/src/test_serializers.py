from equipment.serializers import EquipmentSerializer, EquipmentTypeSerializer


def test_EquipmentSerializer():
    serializer = EquipmentSerializer()
    assert set(serializer.get_fields()) == {"id", "type", "sn", "description"}


def test_EquipmentTypeSerializer():
    serializer = EquipmentTypeSerializer()
    assert set(serializer.get_fields()) == {"id", "name", "sn_mask"}
