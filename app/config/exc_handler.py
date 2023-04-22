from http import HTTPStatus
from typing import Any, Dict

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.views import Response, exception_handler


def api_exception_handler(exc: Exception, context: Dict[str, Any]) -> Response:
    """Custom API exception handler."""

    response = exception_handler(exc, context)

    if isinstance(exc, DjangoValidationError):
        data = {
            "error": exc.__class__.__name__,
            "detail": exc
        }
        response = Response(data, status=HTTPStatus.BAD_REQUEST)

    return response
