# RAG-Based Sales Data Analysis (under construction)
This is a course project for University of Helsinkis master level course 'Data Warehousing and Business Intelligence'. This project is a RAG system that uses a sales data set from Kaggle.
The app works by having s a integrated local LLM that answers users questions about sales, trends, patterns and insight. 

#### Components:
* `main.py` - main component that includes RAG framework and user chat
* `parse_data.py` - transforms dataset from CSV file to meaningful strings
* `db.py` - adds data into chromedb
* `vector_embeddings.py` - calculates vector embeddings for strings using sentence-transformers
* `create_database.py` - initialises and populates database
* `chunk_docs.py` - chunks documents based on chunk size and metadata tags 

#### Architecture:
```mermaid
graph TD
    %% initialise 
    subgraph Architecture
        A[create_database.py] --> |initialise app| B[parse_data.py]
        B -->|read file| SC[superstore.csv]
        B -->|generate files| TF[txt files]
        A <--> |chunk data| CD[chunk_docs.py]
        CD --> |read txt files| TF
        A <--> |embed chunks| VE[vector_embeddings.py]
        VE <--> |all-MiniLM-L6-v2| ST
        A --> |add chunks to db| DB[db.py]
        DB --> |chroma client| CDB
        C[user query] --> M[main.py]
        M --> | RAG framework with Langchain| O[output]
        M --> |initialise db| A


    end
    %% External Connections
    CDB[(ChromaDB)]
    ST[(Sentence Transformer)]
    OL[(Ollama phi3)]

```


#### Technologies
* Backend: python, pandas, poetry (for dependency management)
* Vector database: Chromadb
* LLM: Ollama Phi-3 Mini
* Embeddings: sentence-transformers (all-MiniLM-L6-v2) 
* RAG framework: LangChain
* Dataset: [Superstore dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

