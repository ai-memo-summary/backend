from fastapi import FastAPI

from app.routes.memos.router import router as memos_router

app = FastAPI()

app.include_router(memos_router)

