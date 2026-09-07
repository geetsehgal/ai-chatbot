def save_memory(
    user_id,
    fact
):

    memory_collection.add(
        ids=[uuid4()],
        documents=[fact],
        metadatas=[
            {
                "user_id": user_id
            }
        ]
    )
