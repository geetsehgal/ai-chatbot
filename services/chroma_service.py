import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

documents_collection = client.get_or_create_collection(
    "documents"
)

memory_collection = client.get_or_create_collection(
    "memory"
)
