from parse_data import initialise
from vector_embeddings import embed
from db import add_to_collection
from chunk_docs import chunk_data


def initialise_db(): #run once when starting
    # initialise db with row descriptions:
    initialise()
    row_chunks, row_metadatas = chunk_data("row_descriptions.txt", "segment", 0) #for row descriptions
    row_embeddings = embed(row_chunks)
    row_ids=[str(i) for i in range(len(row_chunks))]
    add_to_collection(row_ids, row_embeddings, row_chunks, row_metadatas)
    
    # initialise db with sales trend analysis (monthly/yearly):
    sales_chunks, sales_metadatas = chunk_data("trend_analysis.txt", "year", 2)
    sales_embeddings = embed(sales_chunks)
    sales_ids =[str(i) for i in range(len(sales_chunks))]
    add_to_collection(sales_ids, sales_embeddings, sales_chunks, sales_metadatas)
    
    # initialise db with category analysis:
    cat_chunks, cat_metadatas = chunk_data("category_analysis.txt", "category", 6)
    cat_embeddings = embed(cat_chunks)
    cat_ids = [str(i) for i in range(len(cat_chunks))]
    add_to_collection(cat_ids, cat_embeddings, cat_chunks, cat_metadatas)
    

    #initialise db with regional analysis:
    region_chunks, region_metadatas = chunk_data("region_analysis.txt", "region", -17)
    region_embeddings = embed(region_chunks)
    region_ids = [str(i) for i in range(len(region_chunks))]
    add_to_collection(region_ids, region_embeddings, region_chunks, region_metadatas)
            
                 

if __name__ == "__main__":
    initialise_db()