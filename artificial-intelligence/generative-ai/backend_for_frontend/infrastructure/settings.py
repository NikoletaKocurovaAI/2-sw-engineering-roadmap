from pydantic import BaseSettings


# REF-009-DB-CONNECTION-CONFIG
class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
