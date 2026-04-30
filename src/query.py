from db import get_collections

def search(query: str):
    collection = get_collections()

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    docs = results["documents"][0]
    distances = results["distances"][0]

    return list(zip(docs, distances))