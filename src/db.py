import chromadb
import os

def get_collections():
    persist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db"))
    client = chromadb.PersistentClient(path=persist_dir)
    return client.get_or_create_collection("flights")