from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(sentences):
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    return embeddings

