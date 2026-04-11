from parse_data import get_metadata
from langchain_ollama import ChatOllama
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from db import get_client, collection_count
from langchain_chroma import Chroma
from create_database import initialise_db

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma(
    client=get_client(),
    collection_name="sales_collection",
    embedding_function=embeddings
)

llm = ChatOllama(model="phi3")


def chat():
    db_count = collection_count()
    while True:
        db_question = input(
            f"Currently the database has {db_count} records. Initialise db y/n?: ")
        if db_question == "y":
            initialise_db()
        else:
            print("skipping database initialisation")
        break
    while True:
        query = input("Ask a question or exit with X: ")
        if query == "X":
            break
        print("Extracting metadata from query")
        query_metadata = extract_metadata_from_query(query)
        print(query_metadata)
        print("Extraction done. Running a similiarity search next")
        results = vectorstore.similarity_search(
            query, k=2, filter=query_metadata)
        print("Similarity search done, constructing prompt next")
        context = "\n\n".join(doc.page_content for doc in results)
        print(f"Context length: {len(context)} characters")
        final_prompt = construct_prompt(query, context)
        response = llm.invoke(final_prompt)
        print(response.content)


def construct_prompt(query, context):
    system_role = f"“You are a helpful retail sales analyst for Superstore (2014 - 2017)."
    rules = f"Do NOT use knowledge outside context. If unsure, say insufficient data. Always cite specific numbers from the context."
    prompt = f"{system_role} {rules} Use only the following data: {context}. {rules} Question: {query}"
    return prompt


def extract_metadata_from_query(query):
    metadata = get_metadata()
    query_metadata = {}
    for key, values in metadata.items():
        for value in values:
            if value.lower() in query.lower():
                if key not in query_metadata:
                    query_metadata[key] = [value]
                else:
                    query_metadata[key].append(value)

    print(query_metadata)
    if not query_metadata:
        return None
    filters = []
    for key, values in query_metadata.items():
        if len(values) > 1:
            filters.append({key: {"$in": values}})
        else:
            filters.append({key: {"$eq": values[0]}})

    if len(filters) > 1:
        return {"$and": filters}
    return filters[0]


if __name__ == "__main__":
    chat()
