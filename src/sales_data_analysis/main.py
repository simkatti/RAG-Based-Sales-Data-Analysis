from parse_data import read_file, convert_rows
from vector_embeddings import embed
from db import add_to_collection


def transactions():
    df = read_file()
    docs, metadata = convert_rows(df)
    ids = [f"id_{i}" for i in range(len(docs))]
    
    chunk_size = 1000
    for i in range(0, len(docs), chunk_size):
        end = min(i+chunk_size, len(docs))
        embeddings = embed(docs[i:end])
        add_to_collection(ids[i:end], embeddings, metadata[i:end], docs[i:end])
        print(f"added {end} rows to db")

    return

# def chunk_data(): 
    # df = read_file()
    # strings, metadata = convert_rows(df)
    # chunk_size = 1000
    # current_chunk = 0
    # doc_chunk = []
    # start_index = 0
    # for i, sentence in enumerate(strings):
    #     if current_chunk + len(sentence) <= chunk_size:
    #         doc_chunk.append(sentence)
    #         current_chunk += len(sentence)
    #     else:
            
        
        # current_chunk += len(sentence)
        # if current_chunk <= chunk_size:
        #     doc_chunk.append(sentence)
        # else:
        #     metadata_chunk = metadata[:i]
        #     ids = [f"id{j}" for j in range(0, i-1)]
        #     embeddings = embed(doc_chunk)
        #     add_to_collection(ids, metadata_chunk, embeddings)
        #     doc_chunk = [sentence]
        #     current_chunk = len(sentence)
            
            
            

if __name__ == "__main__":
    transactions()