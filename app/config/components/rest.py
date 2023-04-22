import os

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "config.exc_handler.api_exception_handler",
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated"
        "rest_framework.permissions.AllowAny"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": os.environ.get("DRF_PAGE_SIZE", 100),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ]
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Auth Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}
