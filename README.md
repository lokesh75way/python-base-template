# Backend

FastAPI backend service using PostgreSQL, SQLAlchemy, and Alembic.

---

## 🚀 Getting Started

### 1️⃣ Create & Activate Virtual Environment

```bash

source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Environment Variables

Create a `.env` file in the project root:

```env
DB_USERNAME=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db-name
```

---

### 4️⃣ Database Migration (Alembic)

Generate migrations (only once or after model changes):

```bash
alembic revision --autogenerate -m "message here"
```

Apply migrations:

```bash
alembic upgrade heads
```

Rollback last migration (if needed):

```bash
alembic downgrade -1
```

---

### 5️⃣ Run the Application

Start the FastAPI server with Uvicorn:

```bash
uvicorn app.main:app --reload
fastapi dev
```

- `--reload` enables auto-reload in development
- App runs at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📚 API Docs

Once the server is running, access:

- Swagger UI:
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- ReDoc:
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---