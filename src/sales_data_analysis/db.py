import chromadb

# chroma client for testing
# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="sales_collection")

# db stays in memory
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="sales_collection")


def get_client():
    return chroma_client


def add_to_collection(ids, embeddings, chunks, metadatas):
    print(f"ids: {len(ids)}, embeddings: {len(embeddings)}, chunks: {len(chunks)}, metadatas: {len(metadatas)}")
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas
    )
    print("Added to db successfully!")
    print(f"collection count: {collection.count()}")


def delete_collection():
    chroma_client.delete_collection(name="sales_collection")
    return print("collection deleted")


def collection_count():
    print(collection.count())
    return collection.count()


# if __name__ == "__main__":
#     delete_collection()
