from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ���ۻ���ģ��
class CommentBase(BaseModel):
    novel_id: int
    content: str
    chapter_id: Optional[int] = None
    paragraph_id: Optional[int] = None

# ������������ģ��
class CommentCreate(CommentBase):
    user_id: int

# ������Ӧģ��
class CommentResponse(CommentBase):
    id: int
    user_id: int
    likes: int
    timestamp: datetime

    class Config:
        orm_mode = True
