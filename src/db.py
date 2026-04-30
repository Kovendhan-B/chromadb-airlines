import chromadb
import os

_client = None
_collection = None

def get_collections():
    global _client, _collection
    if _client is None:
        persist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db"))
        _client = chromadb.PersistentClient(path=persist_dir)
        _collection = _client.get_or_create_collection("flights")
    return _collection