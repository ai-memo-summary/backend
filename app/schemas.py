from pydantic import BaseModel

class MemoCreate(BaseModel):
    title: str
    content: str

class MemoResponse(BaseModel):
    id: int
    title: str
    content: str