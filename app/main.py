from fastapi import FastAPI

from app import models
from app.database import Base, engine
from app.routes.memos.router import router as memos_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(memos_router)

