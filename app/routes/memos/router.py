from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Memo
from app.schemas import MemoCreate, MemoResponse, MemoSummaryResponse


router = APIRouter(
    prefix="/memos",
    tags = ["memos"],
)

@router.post(
    "",
    response_model=MemoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_memo(memo: MemoCreate, db: Session = Depends(get_db)):
    new_memo = Memo(
        title=memo.title,
        content=memo.content,
    )

    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)

    return new_memo

@router.get(
        "",
        response_model=list[MemoResponse],
)
def read_memos(db: Session = Depends(get_db)):
    return db.query(Memo).all()

@router.get(
    "/{memo_id}",
    response_model = MemoResponse,
)
def read_memo(memo_id: int, db: Session = Depends(get_db)):
    memo = db.query(Memo).filter(Memo.id == memo_id).first()

    if memo is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Memo not found",
        )
    
    return memo

@router.put(
    "/{memo_id}",
    response_model = MemoResponse,
)
def update_memo(
    memo_id: int,
    updated_memo: MemoCreate,
    db: Session = Depends(get_db),
):
    memo = db.query(Memo).filter(Memo.id == memo_id).first()

    if memo is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Memo not found",
        )
    memo.title = updated_memo.title
    memo.content = updated_memo.content
    
    db.commit()
    db.refresh(memo)

    return memo

@router.delete(
    "/{memo_id}",
    response_model=MemoResponse,
)
def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    memo = db.query(Memo).filter(Memo.id == memo_id).first()

    if memo is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Memo not found"
        )
    db.delete(memo)
    db.commit()

    return memo

@router.post(
    "/{memo_id}/summarize",
    response_model=MemoSummaryResponse,
)
def summarize_memo(memo_id: int):
    for memo in memos:
        if memo["id"] == memo_id:
            summary = f"{memo['title']}에 대한 요약입니다."

            return {
                "memo_id": memo["id"],
                "summary": summary,
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Memo not found",
    )