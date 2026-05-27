"""
REF-011-RUN-WEB-SERVER
Run with: poetry run uvicorn main:app --reload
"""

import os

from api.v1 import articles, auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# REF-011-API-SECURITY-CORS
frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware, allow_origins=frontend_url, allow_credentials=False, allow_methods=["POST"], allow_headers=["*"]
)

# REF-011-API-VERSIONING
app.include_router(auth.router, prefix="/v1/auth")
app.include_router(articles.router, prefix="/v1/articles")
