# Chroma Airlines Review Search

Search through airline reviews using natural language. Ask a question, get an AI-generated answer backed by real review data.

## How it works

1. Your question is matched against airline reviews stored in ChromaDB (semantic search)
2. The top results are passed as context to a local Flan-T5 model
3. The model generates a concise answer

## Setup

```bash
uv sync          # install dependencies
cp .env.example .env   # configure settings (model, batch size, etc.)
```

Run it:
```bash
python src/main.py
```

## Config (`.env`)

| Key | Default | What it does |
|---|---|---|
| `MODEL_NAME` | `google/flan-t5-base` | HuggingFace model to use |
| `N_RESULTS` | `5` | Reviews fetched per query |
| `BATCH_SIZE` | `5000` | Rows per upsert during ingestion |

## Project Structure

```
src/
  main.py    — REPL loop (entry point)
  query.py   — semantic search via ChromaDB
  llm.py     — answer generation via Flan-T5
  ingest.py  — loads Excel data into ChromaDB
  db.py      — ChromaDB client (singleton)
db/
  data/      — source Excel file
  *.sqlite3  — ChromaDB store (not in git)
```

## Re-ingesting data

Uncomment `ingest_data()` in `src/main.py` and run once.
