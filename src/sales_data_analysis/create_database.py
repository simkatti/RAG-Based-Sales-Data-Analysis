from .parse_data import initialise
from .vector_embeddings import embed
from .db import add_to_collection
from .chunk_docs import chunk_data, get_metadata


def initialise_db():  # run once when starting
    # # initialise db with row descriptions:
    initialise()
    metadata = get_metadata()
    row_chunks, row_metadatas = chunk_data(
        "row_descriptions.txt")  # for row descriptions
    row_embeddings = embed(row_chunks)
    row_ids = [f"row_{i}" for i in range(len(row_chunks))]
    add_to_collection(row_ids, row_embeddings, row_chunks, row_metadatas)

    # initialise db with sales trend analysis (monthly/yearly):
    sales_chunks, sales_metadatas = chunk_data("trend_analysis.txt")
    sales_embeddings = embed(sales_chunks)
    sales_ids = [f"sales_{i}" for i in range(len(sales_chunks))]
    add_to_collection(
        sales_ids,
        sales_embeddings,
        sales_chunks,
        sales_metadatas)

    # initialise db with category analysis:
    cat_chunks, cat_metadatas = chunk_data("category_analysis.txt")
    cat_embeddings = embed(cat_chunks)
    cat_ids = [f"cat_{i}" for i in range(len(cat_chunks))]
    add_to_collection(cat_ids, cat_embeddings, cat_chunks, cat_metadatas)

    # initialise db with regional analysis:
    region_chunks, region_metadatas = chunk_data(
        "region_analysis.txt")
    region_embeddings = embed(region_chunks)
    region_ids = [f"region_{i}" for i in range(len(region_chunks))]
    add_to_collection(
        region_ids,
        region_embeddings,
        region_chunks,
        region_metadatas)
