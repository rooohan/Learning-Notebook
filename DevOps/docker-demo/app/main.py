from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    import aioredis
    _redis = aioredis.from_url('redis://localhost:6379')

    app.state.redis = _redis
    yield
    await _redis.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return dict(message="Hello World")

@app.get("/keys/{key}")
async def get_key(key: str):
    value = await app.state.redis.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.post("/keys/{key}")
async def set_key(key: str, value: str):    
    await app.state.redis.set(key, value)
    return {"key": key, "value": value}


if __name__ == "__main__":
    uvicorn.run(app=app)