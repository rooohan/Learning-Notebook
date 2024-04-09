from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    import aioredis
    _redis = aioredis.from_url('redis://localhost:6379')

    app.state.redis = _redis
    yield
    await _redis.close()

app = FastAPI(lifespan=lifespan)
