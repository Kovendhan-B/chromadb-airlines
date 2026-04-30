import chromadb
from chromadb.config import Settings
import os

# Use a different directory for testing persistence
persist_dir = "D:/chroma-test"
print("Persist dir:", persist_dir)
client = chromadb.Client(Settings(persist_directory=persist_dir))
collection = client.get_or_create_collection("test")
collection.upsert(ids=["1"], documents=["hello"], metadatas=[{"a": 1}])
print("Count:", collection.count())