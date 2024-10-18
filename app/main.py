from fastapi import FastAPI
import uvicorn

from app.settings import settings
from app import controller as root_controller
from app.chat import controller as chat_controller
from app.ind import controller as ind_controller
from app.sow import controller as sow_controller

app = FastAPI(title=settings.application_name)

app.include_router(root_controller.router, prefix="/api/v1")
app.include_router(chat_controller.router, prefix="/api/v1/chat")
app.include_router(ind_controller.router, prefix="/api/v1/ind")
app.include_router(sow_controller.router, prefix="/api/v1/sow")


@app.get("/")
async def root():
    return {"message": f"{settings.application_name}!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
