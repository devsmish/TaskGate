from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    app_name: str = "TaskGate"
    environment: str = "local"
    debug: bool = True

    database_url: str
    redis_url: str
    jwt_secret_key: str

    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30

    # Webhooks
    webhook_max_attempts: int = 3

    # Project lifecycle
    project_auto_archive_days: int = 30
    task_ready_auto_done_days: int = 7
    developer_wip_limit: int = 2


@lru_cache
def get_settings() -> Settings:
    return Settings()
