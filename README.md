## ��ĿREADME

### ��Ŀ���
����Ŀ��һ������FastAPI�Ķ�������ϵͳ���û����Զ�С˵�Ĳ�ͬ�½ںͶ��䷢�����ۡ�ϵͳ�ṩ��������ۡ���ȡ���۵Ĺ��ܣ�����֧�ְ�С˵ID���½�ID������ID���й��˲�ѯ��

### Ŀ¼�ṹ
```plaintext
readercomment/
������ main.py           # FastAPIӦ�����
������ database.py       # ���ݿ�����
������ models.py         # ���ݿ�ģ�Ͷ���
������ schemas.py        # Pydantic������֤ģ��
������ README.md         # ��Ŀ˵���ĵ�
```

### ��������
- Python 3.8+
- FastAPI
- SQLAlchemy
- psycopg2 (PostgreSQL����)
- Pydantic

### ��װ����
1. **��¡�ֿ�**
   ```bash
   git clone <repository-url>
   cd readercomment
   ```

2. **�������⻷��������**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **��װ����**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary uvicorn pydantic
   ```

4. **�������ݿ�**
   - �޸�`database.py`�е�`DATABASE_URL`��ƥ�����PostgreSQL���á�
   - ȷ��PostgreSQL��������������������Ϊ`reader`�����ݿ⡣

5. **��ʼ�����ݿ�**
   ```bash
   python main.py
   ```
   �⽫����`models.py`�еĶ����Զ�������������ݿ��

### ʹ��˵��
#### ��������
```bash
uvicorn main:app --reload
```
Ĭ������£�������`http://127.0.0.1:8000`�����С�

#### API�ӿ�
- **�������**
  - URL: `/comments/`
  - ����: `POST`
  - ������:
    ```json
    {
      "user_id": 1,
      "novel_id": 1,
      "chapter_id": 1,  // ��ѡ
      "paragraph_id": 1,  // ��ѡ
      "content": "����һ������"
    }
    ```

- **��ȡ����**
  - URL: `/comments/`
  - ����: `GET`
  - ��ѯ����:
    - `novel_id`: ���С˵ID
    - `chapter_id`: ��ѡ���½�ID
    - `paragraph_id`: ��ѡ������ID

### ʾ��
#### �������
```bash
curl -X POST "http://127.0.0.1:8000/comments/" -H "Content-Type: application/json" -d '{
  "user_id": 1,
  "novel_id": 1,
  "chapter_id": 1,
  "paragraph_id": 1,
  "content": "����һ������"
}'
```

#### ��ȡ����
```bash
curl -X GET "http://127.0.0.1:8000/comments/?novel_id=1&chapter_id=1"
```

---