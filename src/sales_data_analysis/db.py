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
    return
    
def delete_collection(): 
    chroma_client.delete_collection(name="sales_collection")
    return(print("collection deleted"))
    
    
# if __name__ == "__main__":
#     delete_collection()