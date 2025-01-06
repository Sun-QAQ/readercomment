from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# 用户表
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50), nullable=False)
    avatar_url = Column(String(255))

# 评论表
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    novel_id = Column(Integer, nullable=False)
    chapter_id = Column(Integer, nullable=True)
    paragraph_id = Column(Integer, nullable=True)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer, default=0)

    # 关联用户信息
    user = relationship("User")
