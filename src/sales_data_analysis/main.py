from parse_data import initialise, get_metadata
from vector_embeddings import embed, embed_query
from db import add_to_collection, retrieval
from chunk_docs import chunk_data
import ollama

client = ollama.Client(host='http://localhost:11434')

def initialise_db(): #run once when starting
    # # initialise db with row descriptions:
    initialise()
    metadata = get_metadata()
    row_chunks, row_metadatas = chunk_data("row_descriptions.txt", metadata) #for row descriptions
    row_embeddings = embed(row_chunks)
    row_ids=[f"row_{i}" for i in range(len(row_chunks))]
    add_to_collection(row_ids, row_embeddings, row_chunks, row_metadatas)
    
    # initialise db with sales trend analysis (monthly/yearly):
    sales_chunks, sales_metadatas = chunk_data("trend_analysis.txt", metadata)
    sales_embeddings = embed(sales_chunks)
    sales_ids =[f"sales_{i}" for i in range(len(sales_chunks))]
    add_to_collection(sales_ids, sales_embeddings, sales_chunks, sales_metadatas)
    
    # initialise db with category analysis:
    cat_chunks, cat_metadatas = chunk_data("category_analysis.txt", metadata)
    cat_embeddings = embed(cat_chunks)
    cat_ids = [f"cat_{i}" for i in range(len(cat_chunks))]
    add_to_collection(cat_ids, cat_embeddings, cat_chunks, cat_metadatas)
    
    #initialise db with regional analysis:
    region_chunks, region_metadatas = chunk_data("region_analysis.txt", metadata)
    region_embeddings = embed(region_chunks)
    region_ids = [f"region_{i}" for i in range(len(region_chunks))]
    add_to_collection(region_ids, region_embeddings, region_chunks, region_metadatas)

def extract_metadata_from_query(query):
    metadata = get_metadata()
    query_metadata = {}
    for key, values in metadata.items():
        for value in values:
            if value.lower() in query.lower():
                query_metadata[key] = value
    
    if not query_metadata:
        return None
    if len(query_metadata) > 1:
        return {"$and": [{k: {"$eq": v}} for k, v in query_metadata.items()]}
    return query_metadata

def chat():
    while True:
        query = input("Ask a question or exit with X: ")
        if query == "X":
            break
        embedded_query = embed_query(query)
        query_metadata = extract_metadata_from_query(query)
        print(f"Query metadata: {query_metadata}")
        retrieved_result = retrieval(embedded_query, query_metadata)
        documents = retrieved_result['documents']
        llm_result = llama(query, ' '.join(documents[0]))
        print(llm_result)

def llama(query, result):
    system_role = f"“You are a helpful retail sales analyst for Superstore (2014 - 2017)."
    rules = f"Do NOT use knowledge outside context. If unsure, say insufficient data. Cite numbers."
    
    prompt = f"{system_role} Use only the following data: {result}. {rules} Question: {query}"
    print(prompt)
    
    response = client.generate(model='phi3', prompt=prompt)
    return response['response']
    


if __name__ == "__main__":
    initialise_db()
    chat()