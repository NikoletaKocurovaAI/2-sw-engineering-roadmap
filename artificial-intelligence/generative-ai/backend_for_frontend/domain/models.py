from pydantic import BaseModel, Field


# REF-011-DATA-MODELING
class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class SearchRequest(BaseModel):
    keywords: list[str] = Field(..., description="List of keywords to search articles for")


class ArticleResponse(BaseModel):
    title: str = Field(..., description="Article title")
    intro: str = Field(..., description="Article intro content")
    body: str = Field(..., description="Article body content")
    request_duration: dict = Field(..., description="Temporary monitoring of search request duration")
