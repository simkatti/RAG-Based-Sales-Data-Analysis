from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(chunks):
    embeddings = []
    print("Embedding chunks....")
    start = time.time()
    for chunk in chunks:
        embedded_chunk = model.encode(chunk)
        embeddings.append(embedded_chunk)
    print("Embedding done!")
    end = time.time()
    print(end - start)
    return embeddings
