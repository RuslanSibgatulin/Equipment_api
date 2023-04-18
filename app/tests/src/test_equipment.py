import json
from http import HTTPStatus

import pytest
from equipment.models import Equipment, EquipmentType
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_types(auth_api_client: APIClient, api_url: str, equipment_type: EquipmentType):
    url = api_url + "equipment-type/"
    response = auth_api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    resp_data = response.json()
    data = [{"id": 1, "name": "D-Link DIR-300", "sn_mask": "NXXAAXZXaa"}]
    assert resp_data["results"] == data


@pytest.mark.django_db
def test_create_bad_sn_equipment(auth_api_client: APIClient, api_url: str, equipment_type: EquipmentType):
    url = api_url + "equipment/"
    data = [
        {
            "sn": "string",
            "description": "description",
            "type": equipment_type.pk
        },
    ]
    response = auth_api_client.post(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "detail" in response.json()


@pytest.mark.django_db
def test_create_many_equipment(auth_api_client: APIClient, api_url: str, equipment_type: EquipmentType):
    """Create equipment list with correct SN and type from equipment_type fixture
    """
    url = api_url + "equipment/"
    data = [
        {
            "id": 1,
            "sn": "1ACBB7-2tt",
            "description": "description",
            "type": equipment_type.pk
        },
        {
            "id": 2,
            "sn": "222BB7@2tt",
            "description": "description",
            "type": equipment_type.pk
        },
        {
            "id": 3,
            "sn": "3A2BB7_2tj",
            "description": "description",
            "type": equipment_type.pk
        },


    ]
    response = auth_api_client.post(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.CREATED
    resp_data = response.json()
    assert isinstance(resp_data, list)
    assert resp_data == data


@pytest.mark.django_db
def test_create_many_equipment_bad_sn(auth_api_client: APIClient, api_url: str, equipment_type: EquipmentType):
    """Create equipment list with correct SN and type from equipment_type fixture
    """
    url = api_url + "equipment/"
    data = [
        {
            "sn": "1ACBB7-2tt",
            "description": "description",
            "type": equipment_type.pk
        },
        {
            "sn": "222BB7@2tt",
            "description": "description",
            "type": equipment_type.pk
        },
        {
            "sn": "3A2BB7$2tj",
            "description": "description",
            "type": equipment_type.pk
        },


    ]
    response = auth_api_client.post(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response = auth_api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    resp_data = response.json()
    assert resp_data["results"] == []


@pytest.mark.django_db
def test_get_equipment_by_id(auth_api_client: APIClient, api_url: str, equipment: Equipment):
    """Get equipment by id
    """
    url = f"{api_url}equipment/{equipment.pk}"
    response = auth_api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    resp_data = response.json()

    assert resp_data == {"id": 1, "sn": "1ACBB7-2tt", "description": "", "type": 1}
