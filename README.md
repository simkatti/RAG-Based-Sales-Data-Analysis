# RAG-Based Sales Data Analysis (under construction)
This is a course project for University of Helsinkis master level course 'Data Warehousing and Business Intelligence'. This project is a RAG system that uses a sales data set from Kaggle.
The app works by having s a integrated local LLM that answers users questions about sales, trends, patterns and insight. 

#### Components:
* `main.py` - main component connecting all other components. Works as a interface for user questions and LLM answers
* `parse_data.py` - transforms dataset from CSV file to meaningful strings
* `db.py` - adds data into chromedb
* `vector_embeddings.py` - calculates vector embeddings for strings using sentence-transformers

#### Architecture:
```mermaid
graph TD
    %% initialise 
    subgraph Architecture
        A[main.py] --> |initialise app| B[parse_data.py]
        B -->|read file| SC[superstore.csv]
        B -->|generate files| TF[txt files]
        A <--> |chunk data| CD[chunk_docs.py]
        CD --> |read txt files| TF
        A <--> |embed chunks| VE[vector_embeddings.py]
        VE <--> |all-MiniLM-L6-v2| ST
        A --> |add chunks to db| DB[db.py]
        DB --> |chroma client| CDB
        C[user query] --> A
        A <--> |embed user query & extract metadata| VE
        VE <--> ST
        A <--> |similarity search| DB
        DB <--> CDB
        A --> |add search results to prompt| OL
        OL --> |query results| A
        A --> output

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

