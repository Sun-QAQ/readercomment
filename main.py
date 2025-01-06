from database import engine
from models import Base
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Comment, User
from schemas import CommentCreate, CommentResponse

# �������б�
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ��ȡ���ݿ�Ự
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# �������
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

# ��ȡ����
@app.get("/comments/", response_model=list[CommentResponse])
def get_comments(novel_id: int, chapter_id: int = None, paragraph_id: int = None, db: Session = Depends(get_db)):
    query = db.query(Comment).filter(Comment.novel_id == novel_id)
    if chapter_id:
        query = query.filter(Comment.chapter_id == chapter_id)
    if paragraph_id:
        query = query.filter(Comment.paragraph_id == paragraph_id)
    return query.all()

# ��������
@app.post("/comments/{comment_id}/like/")
def like_comment(comment_id: int, db: Session = Depends(get_db)):
    # ��ѯ�����Ƿ����
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    # ���ӵ�����
    comment.likes += 1
    db.commit()
    db.refresh(comment)
    return {"status": "success", "likes": comment.likes}

# ȡ������
@app.post("/comments/{comment_id}/unlike/")
def unlike_comment(comment_id: int, db: Session = Depends(get_db)):
    # ��ѯ�����Ƿ����
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    # ���ٵ�������ȷ�������� 0��
    if comment.likes > 0:
        comment.likes -= 1
        db.commit()
        db.refresh(comment)
    return {"status": "success", "likes": comment.likes}
