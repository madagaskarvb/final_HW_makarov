from fastapi import FastAPI
from internal.routers.user_router import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users")


@app.get("/ping")
def ping():
    return {"message": "pong"}
