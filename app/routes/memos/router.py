from fastapi import APIRouter, status

from app.schemas import MemoCreate, MemoResponse

router = APIRouter(
    prefix="/memos",
    tags = ["memos"],
)

@router.post(
    "",
    response_model=MemoResponse,
    status_code=status.HTTP_201_CREATED
)
def create_memo(memo: MemoCreate):
    return {
        "id": 1,
        "title": memo.title,
        "content": memo.content
    }