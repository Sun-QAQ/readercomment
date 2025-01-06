from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 评论基础模型
class CommentBase(BaseModel):
    novel_id: int
    content: str
    chapter_id: Optional[int] = None
    paragraph_id: Optional[int] = None

# 创建评论请求模型
class CommentCreate(CommentBase):
    user_id: int

# 评论响应模型
class CommentResponse(CommentBase):
    id: int
    user_id: int
    likes: int
    timestamp: datetime

    class Config:
        orm_mode = True
