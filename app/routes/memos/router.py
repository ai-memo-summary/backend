from fastapi import APIRouter, status, HTTPException

from app.schemas import MemoCreate, MemoResponse

memos = [
  {
    "id": 1,
    "title": "제목",
    "content": "본문"
  },
  {
    "id": 2,
    "title": "제목",
    "content": "본문"
  },
  {
    "id": 3,
    "title": "제목2",
    "content": "본문2"
  },
  {
    "id": 4,
    "title": "제목3",
    "content": "본문3"
  }
]
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

@router.get(
    "/{memo_id}",
    response_model = MemoResponse,
)
def read_memo(memo_id: int):
    for memo in memos:
        if memo['id'] == memo_id:
            return memo
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Memo not found",
    )

@router.put(
    "/{memo_id}",
    response_model = MemoResponse,
)
def update_memo(memo_id: int, update_memo: MemoCreate):
    for memo in memos:
        if memo['id']==memo_id:
            memo["title"] = update_memo.title
            memo["content"] = update_memo.content
            return memo
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Memo not found"
    )

@router.delete(
    "/{memo_id}",
)
def delete_memo(memo_id: int):
    for memo in memos:
        if memo['id']==memo_id:
            memos.remove(memo)
            return memo
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Memo not found"
    )