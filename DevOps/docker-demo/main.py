import uvicorn

from fast_app.create_app import app
from fast_app.api.redis_api import redis_router


app.include_router(redis_router)


@app.get("/")
async def healthcheck():
    return dict(message="Hello World")

if __name__ == "__main__":
    uvicorn.run(app=app)