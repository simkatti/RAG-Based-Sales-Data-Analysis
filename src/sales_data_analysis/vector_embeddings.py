from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(chunks):
    embeddings = []
    print("Embedding chunks....")
    for chunk in chunks:
        embedded_chunk = model.encode(chunk)
        embeddings.append(embedded_chunk)
    print("Embedding done!")
    return embeddings

