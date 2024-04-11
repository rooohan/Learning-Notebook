from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    import os
    import aioredis

    _url = os.getenv('REDIS_URL', 'redis://localhost:6379')
    _redis = aioredis.from_url(_url)

    app.state.redis = _redis
    yield
    await _redis.close()

app = FastAPI(lifespan=lifespan)
