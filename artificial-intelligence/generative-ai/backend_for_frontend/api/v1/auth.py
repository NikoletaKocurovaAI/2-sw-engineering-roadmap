"""
REF-007-API-ENDPOINT-TESTING
Request example to test the endpoint:
POST http://127.0.0.1:8000/v1/auth/login
Payload
{
    "username": "test-username",
    "password": "test-password"
}
"""

from domain.models import LoginRequest, TokenResponse
from fastapi import APIRouter

router = APIRouter()


# REF-011-HTTP-METHOD, REF-011-RESOURCE-NAMING, REF-011-SYNCHRONICITY, REF-011-DATA-DESERIALIZATION
# REF-011-INPUT-VALIDATION, REF-011-RESPONSE-VALIDATION, REF-011-API-STATUS-CODES
@router.post("/login", response_model=TokenResponse, status_code=200)
def login(data: LoginRequest) -> TokenResponse:
    # REF-008-SPHINX-DOCSTRING
    """
    Authentication endpoint using Username & password with JWT.

    :param data: LoginRequest with username and password
    :type data: LoginRequest
    :return: JWT token response
    :rtype: TokenResponse
    """
    # if not authenticate_user(data.username, data.password) raise 401

    # REF-011-DATA-SERIALIZATION
    return TokenResponse(access_token="token123", token_type="bearer", expires_in=3600)
