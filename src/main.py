from ingest import ingest_data
from query import search

# ingest_data()

query = input("Search: ")
results = search(query)

for doc, score in results:
    print(f"\nScore: {score:.4f}")
    print(doc)