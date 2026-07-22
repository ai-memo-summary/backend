from fastapi import APIRouter, status

from app.schemas import MemoCreate, MemoResponse

memos =[]
next_memo_id = 1

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
    global next_memo_id
    new_memo = {
        "id": next_memo_id,
        "title": memo.title,
        "content": memo.content
    }
    memos.append(new_memo)
    next_memo_id += 1
    
    return new_memo

@router.get(
    "",
    response_model = list[MemoResponse],
)
def read_memos():
    return memos