## 1. 프로젝트 소개

AI Memo Summary App은 FastAPI를 사용해 메모를 작성, 조회, 수정, 삭제할 수 있는 백엔드 API 프로젝트입니다.  
기본적인 메모 CRUD 기능을 먼저 구현한 뒤, 이후 LLM API를 연결하여 저장된 메모 내용을 자동으로 요약하는 기능을 추가하는 것을 목표로 합니다.

## 2. 프로젝트 목표

- FastAPI를 사용해 REST API의 기본 구조와 동작 흐름을 이해한다.
- Pydantic을 사용해 클라이언트가 보낸 요청 데이터를 검증하고, 응답 데이터의 형태를 명확하게 정의한다.
- SQLAlchemy와 SQLite를 사용해 메모 데이터를 데이터베이스에 저장하고 조회하는 과정을 익힌다.
- 메모 작성, 목록 조회, 상세 조회, 수정, 삭제 기능을 구현하며 CRUD API의 전체 흐름을 학습한다.
- 이후 LLM API를 연결해 저장된 메모 내용을 요약하는 기능을 구현한다.

## 3. 주요 기능

- 메모 작성
- 메모 목록 조회
- 메모 상세 조회
- 메모 수정
- 메모 삭제 
- 메모 요약

## 4. API 설계

POST /memos
GET /memos
GET /memos/{memo_id}
PUT /memos/{memo_id}
DELETE /memos/{memo_id}
POST /memos/{memo_id}/summarize

## 5. MEMOS 테이블

- id
- title
- content
- created_at
- updated_at

## 6. 기술 스택

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- LLM API

## 7. 실행 방법

아직 작성 예정