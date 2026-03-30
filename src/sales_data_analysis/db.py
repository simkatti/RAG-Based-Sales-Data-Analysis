import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="sales_collection")

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
    return

def retrieval(embeddings, query_metadata):
    print(f"collection count: {collection.count()}")
    result = collection.query(
    query_embeddings=[embeddings],
    n_results=5,
    where=query_metadata 
)
    if result:
        print("Retrieval successfull")
        return result
    return
    
def delete_collection(): 
    chroma_client.delete_collection(name="sales_collection")
    return(print("collection deleted"))

def collection_count():
    print(collection.count())
    
# if __name__ == "__main__":
#     collection_count()