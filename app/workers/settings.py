"""ARQ worker configuration.

No actual background tasks for now—they will be added here as webhooks and cron jobs are
implemented. arq requires at least one registered function or cron_job; otherwise, the
worker crashes with a `RuntimeError` upon startup. That is why a `noop` placeholder is
used here instead of an empty list.
"""

from arq.connections import RedisSettings

from app.core.config import get_settings

settings = get_settings()


async def startup(ctx: dict) -> None:
    pass


async def shutdown(ctx: dict) -> None:
    pass


async def noop(ctx: dict) -> None:
    """Placeholder task — arq requires a non-empty functions[]."""


class WorkerSettings:
    functions = [noop]
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = RedisSettings.from_dsn(settings.redis_url)
