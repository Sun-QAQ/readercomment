## 项目README

### 项目简介
本项目是一个基于FastAPI的读者评论系统，用户可以对小说的不同章节和段落发表评论。系统提供了添加评论、获取评论的功能，并且支持按小说ID、章节ID、段落ID进行过滤查询。

### 目录结构
```plaintext
readercomment/
├── main.py           # FastAPI应用入口
├── database.py       # 数据库配置
├── models.py         # 数据库模型定义
├── schemas.py        # Pydantic数据验证模型
└── README.md         # 项目说明文档
```

### 环境依赖
- Python 3.8+
- FastAPI
- SQLAlchemy
- psycopg2 (PostgreSQL驱动)
- Pydantic

### 安装步骤
1. **克隆仓库**
   ```bash
   git clone <repository-url>
   cd readercomment
   ```

2. **创建虚拟环境并激活**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary uvicorn pydantic
   ```

4. **配置数据库**
   - 修改`database.py`中的`DATABASE_URL`以匹配你的PostgreSQL配置。
   - 确保PostgreSQL服务已启动，并创建名为`reader`的数据库。

5. **初始化数据库**
   ```bash
   python main.py
   ```
   这将根据`models.py`中的定义自动创建所需的数据库表。

### 使用说明
#### 启动服务
```bash
uvicorn main:app --reload
```
默认情况下，服务将在`http://127.0.0.1:8000`上运行。

#### API接口
- **添加评论**
  - URL: `/comments/`
  - 方法: `POST`
  - 请求体:
    ```json
    {
      "user_id": 1,
      "novel_id": 1,
      "chapter_id": 1,  // 可选
      "paragraph_id": 1,  // 可选
      "content": "这是一条评论"
    }
    ```

- **获取评论**
  - URL: `/comments/`
  - 方法: `GET`
  - 查询参数:
    - `novel_id`: 必填，小说ID
    - `chapter_id`: 可选，章节ID
    - `paragraph_id`: 可选，段落ID

### 示例
#### 添加评论
```bash
curl -X POST "http://127.0.0.1:8000/comments/" -H "Content-Type: application/json" -d '{
  "user_id": 1,
  "novel_id": 1,
  "chapter_id": 1,
  "paragraph_id": 1,
  "content": "这是一条评论"
}'
```

#### 获取评论
```bash
curl -X GET "http://127.0.0.1:8000/comments/?novel_id=1&chapter_id=1"
```

---