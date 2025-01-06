from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库连接配置
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/reader"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基础类，用于定义模型
Base = declarative_base()
