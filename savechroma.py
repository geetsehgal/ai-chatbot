collection.add(
    ids=[chunk_id],
    documents=[chunk],
    embeddings=[embedding],
    metadatas=[
        {
            "user_id": user_id,
            "document": file_name
        }
    ]
)
