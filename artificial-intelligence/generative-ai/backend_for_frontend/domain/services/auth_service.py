"""
Business rules for authentication.
"""

from domain.models import LoginRequest, TokenResponse


def login_user(data: LoginRequest) -> TokenResponse:
    # user = get_user_by_username(data.username)
    # ... validate password, create token, etc.

    return TokenResponse(access_token="token123", token_type="bearer", expires_in=3600)
