import pytest

USER_NAME = "user1"
API_URL = "http://127.0.0.1:8000/api/"


@pytest.fixture
def api_url():
    return API_URL


@pytest.fixture
def api_client(request):
    """Django Rest Framework APIClient."""
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def django_user(django_user_model):
    """Creates test django user."""
    return django_user_model.objects.create_user(username=USER_NAME, password=USER_NAME)


@pytest.fixture
def auth_api_client(api_client, api_url, django_user):
    """Authenticate test user.

    Returns:
        APIClient: API client with Bearer token
    """
    data = {
        "username": USER_NAME,
        "password": USER_NAME
    }
    response = api_client.post(api_url + "token/", data=data)
    user_token = response.json()["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")
    return api_client


@pytest.fixture
def equipment_type():
    from equipment.models import EquipmentType
    return EquipmentType.objects.create(name="D-Link DIR-300", sn_mask="NXXAAXZXaa")


@pytest.fixture
def equipment():
    from equipment.models import Equipment, EquipmentType
    type = EquipmentType.objects.create(name="D-Link DIR-300", sn_mask="NXXAAXZXaa")
    return Equipment.objects.create(
        sn="1ACBB7-2tt",
        type=type
    )
