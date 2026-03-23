
def chunk_data(textfile, tag, metadata_position):
    chunk_size = 1000
    with  open((textfile), "r") as file:
        lines = file.readlines()
    file.close()
    
    chunks = []
    chunk_metadats = []
    current_meta_tag = None
    text_chunk = ""
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("Home Office"):
            metadata_tag = "Home Office"
        elif line.split()[metadata_position] == "Office":
            metadata_tag = "Office Supplies"
        else:
            metadata_tag = line.split()[metadata_position]
        
        if current_meta_tag == None:
            current_meta_tag = metadata_tag
            
        if current_meta_tag != metadata_tag or len(text_chunk) + len(line) > chunk_size:
            if text_chunk:
                chunks.append(text_chunk.strip())
                chunk_metadats.append({tag: current_meta_tag})
            text_chunk = line
            current_meta_tag = metadata_tag
        else:
            text_chunk += " " + line
    if text_chunk:
        chunks.append(text_chunk.strip())
        chunk_metadats.append({tag: current_meta_tag})
            
    # print(len(chunks))
    # print(len(chunk_metadats))
    # for chunk in chunks:
    #     print(chunk)
    #     print("\n")
    # print(chunk_metadats)
    
    print("Docs chunked! returning chunks and metadata")
    return chunks, chunk_metadats


# if __name__ == "__main__":
#     chunk_data("region_analysis.txt", "region", -17)