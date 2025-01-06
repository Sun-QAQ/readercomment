from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ���ݿ���������
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/reader"

# �������ݿ�����
engine = create_engine(DATABASE_URL)

# �������ݿ�Ự
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# �����࣬���ڶ���ģ��
Base = declarative_base()
