from fast_app.create_app import app
from fastapi import APIRouter, HTTPException

redis_router = APIRouter(tags=["Redis"], prefix="/redis")


@redis_router.get("/keys/{key}")
async def get_key(key: str):
    value = await app.state.redis.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}


@redis_router.post("/keys/{key}")
async def set_key(key: str, value: str):
    await app.state.redis.set(key, value)
    return {"key": key, "value": value}
