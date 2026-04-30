import os
from pathlib import Path
from dotenv import load_dotenv
import polars as pl
from db import get_collections

load_dotenv(Path(__file__).parent.parent / ".env")

BATCH_SIZE = int(os.getenv("BATCH_SIZE", 5000))
DATA_PATH = Path(__file__).parent.parent / "db" / "data" / "Airline_Reviews_Combined.xlsx"

def ingest_data():
    df = pl.read_excel(DATA_PATH)
    print("[Ingest] Starting data ingestion...")
    collections = get_collections()

    ids, docs, metadatas = [], [], []
    total = df.height
    for i, row in enumerate(df.iter_rows(named=True)):
        doc = f"{row['Title']}.{row['Review']}"

        metadata = {
            "airline": row["NAMES"],
            "country": row["Country"],
            "recommended": row["Recommended"]
        }
        ids.append(str(i))
        docs.append(doc)
        metadatas.append(metadata)
        if (i + 1) % 100 == 0 or (i + 1) == total:
            print(f"[Ingest] Processed {i + 1}/{total} rows...")

    print("[Ingest] Upserting data into collection...")

    for start in range(0, total, BATCH_SIZE):
        end = min(start + BATCH_SIZE, total)
        print(f"[Ingest] Upserting rows {start + 1} to {end}...")
        collections.upsert(
            ids=ids[start:end],
            documents=docs[start:end],
            metadatas=metadatas[start:end]
        )
    print("[Ingest] Ingestion complete.")  # ✅ moved outside the loop