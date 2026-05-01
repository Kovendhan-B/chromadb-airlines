
# Chroma Airlines Review Search

Welcome! This project lets you ask questions about airline reviews and get smart, AI-generated answers—backed by real customer experiences.

---

## What does it do?

- You type a question (like "How is France Airlines?")
- The app finds the most relevant reviews using ChromaDB (semantic search)
- It feeds those reviews to a local Flan-T5 language model
- The model writes a concise, human-like answer just for you

---

## Getting Started

1. **Install dependencies:**
   ```bash
   uv sync
   ```
2. **Copy and edit your environment config:**
   ```bash
   cp .env.example .env
   # Edit .env to set model, batch size, etc.
   ```

---

## How to Run

**Command-line (REPL):**
```bash
python src/main.py
```

**Streamlit Web App:**
```bash
streamlit run streamlit_app.py
```
Then open the provided URL in your browser.

**API Server (FastAPI):**
```bash
uvicorn src.api:app --reload
```
Visit http://127.0.0.1:8000/docs for interactive API docs (Swagger UI).

---

## Configuration (`.env`)

| Key           | Default                | Description                        |
|---------------|------------------------|------------------------------------|
| MODEL_NAME    | google/flan-t5-base    | HuggingFace model to use           |
| N_RESULTS     | 5                      | Reviews fetched per query          |
| BATCH_SIZE    | 5000                   | Rows per upsert during ingestion   |

---

## Project Structure

```
src/
  main.py      # Command-line interface (REPL)
  query.py     # Semantic search via ChromaDB
  llm.py       # Answer generation via Flan-T5
  ingest.py    # Loads Excel data into ChromaDB
  db.py        # ChromaDB client (singleton)
  api.py       # FastAPI backend (REST API)
streamlit_app.py # Streamlit web UI
db/
  data/        # Source Excel file
  *.sqlite3    # ChromaDB store (not in git)
```

---

## Re-ingesting Data

If you want to reload the review data:
1. Uncomment `ingest_data()` in `src/main.py`
2. Run the script once to refresh the database

---

