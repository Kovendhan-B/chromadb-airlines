import os
from pathlib import Path
from dotenv import load_dotenv
from db import get_collections

load_dotenv(Path(__file__).parent.parent / ".env")

N_RESULTS = int(os.getenv("N_RESULTS", 5))

def search(query: str):
    collection = get_collections()

    results = collection.query(
        query_texts=[query],
        n_results=N_RESULTS,
        where={"recommended": "yes"}
    )

    docs = results["documents"][0]
    distances = results["distances"][0]

    return list(zip(docs, distances))