import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="sales_collection")

def add_to_collection(ids, embeddings, metadata, docs):
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=docs,
        metadatas=metadata
    )

def delete_collection(): 
    chroma_client.delete_collection(name="sales_collection")