from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./memo.db"

# 어떤 DB에 연결할지
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# DB 조작을 위함
sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# 테이블 설계도 양식
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()