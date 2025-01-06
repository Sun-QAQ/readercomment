from database import engine
from models import Base
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Comment, User
from schemas import CommentCreate, CommentResponse

# 创建所有表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 添加评论
@app.post("/comments/", response_model=CommentResponse)
def add_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = Comment(
        user_id=comment.user_id,
        novel_id=comment.novel_id,
        content=comment.content,
        chapter_id=comment.chapter_id,
        paragraph_id=comment.paragraph_id,
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# 获取评论
@app.get("/comments/", response_model=list[CommentResponse])
def get_comments(novel_id: int, chapter_id: int = None, paragraph_id: int = None, db: Session = Depends(get_db)):
    query = db.query(Comment).filter(Comment.novel_id == novel_id)
    if chapter_id:
        query = query.filter(Comment.chapter_id == chapter_id)
    if paragraph_id:
        query = query.filter(Comment.paragraph_id == paragraph_id)
    return query.all()
