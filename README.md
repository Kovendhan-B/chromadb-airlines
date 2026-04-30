# Chroma Airlines Review Search

This project lets you search through airline reviews using AI-powered search with ChromaDB.

## How to Use

1. **Install dependencies**
   - Make sure you have Python 3.8+
   - Install requirements: `pip install -r requirements.txt` 
2. **Ingest Data (optional)**
   - If you want to add new data, run the ingestion part in `src/main.py` (uncomment the relevant line).

3. **Search Reviews**
   - Run: `python src/main.py`
   - Enter your search query when prompted.
   - The app will show the most relevant airline reviews.

## Project Structure
- `src/` — Main code (ingest, search, database setup)
- `db/` — Database files (not tracked in git)
- `main.py` — Entry point

## Notes
- The database file (`db/chroma.sqlite3`) is ignored by git.
- For large datasets, use batch ingestion for better performance.

---

