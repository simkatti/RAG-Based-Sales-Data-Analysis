def chunk_data(textfile, metadata):
    chunk_size = 1000
    with  open((textfile), "r") as file:
        lines = file.readlines()
    file.close()
    
    chunks = []
    chunk_metadats = []
    current_metadata = {}
    text_chunk = ""
    
    for line in lines:
        line = line.strip()
        
        line_metadata = {}
        if textfile == "row_descriptions.txt":
            for value in metadata['segment']:
                if value in line:
                    line_metadata['segment'] = value
                    break        
        else: 
            for key,values in metadata.items():
                for value in values:
                    if value in line:
                        line_metadata[key] = value
                        break
        
        if not current_metadata:
            current_metadata = line_metadata
            
        if current_metadata != line_metadata or len(text_chunk) + len(line) > chunk_size:
            if text_chunk:
                chunks.append(text_chunk.strip())
                chunk_metadats.append(current_metadata)
            text_chunk = line
            current_metadata = line_metadata
        else:
            text_chunk += " " + line
    if text_chunk:
        chunks.append(text_chunk.strip())
        chunk_metadats.append(current_metadata)
            
    # print(len(chunks))
    # print(len(chunk_metadats))
    # for chunk in chunks:
    #     print(chunk)
    #     print("\n")
    # print(chunk_metadats)
    
    print("Docs chunked! returning chunks and metadata")
    return chunks, chunk_metadats




# if __name__ == "__main__":
#     metadata = {'segment': {'Home Office', 'Consumer', 'Corporate'}, 'year': {'2016', '2017', '2014', '2015'}, 'state': {'West Virginia', 'Oklahoma', 'Nevada', 'Missouri', 'Maryland', 'Montana', 'Indiana', 'Illinois', 'Kansas', 'Idaho', 'Vermont', 'Alabama', 'Wisconsin', 'Florida', 'Nebraska', 'Iowa', 'Tennessee', 'New Hampshire', 'Michigan', 'Ohio', 'Minnesota', 'New Jersey', 'District of Columbia', 'Georgia', 'Washington', 'Oregon', 'South Dakota', 'New York', 'Wyoming', 'Pennsylvania', 'Texas', 'Connecticut', 'Rhode Island', 'Colorado', 'Maine', 'Kentucky', 'Mississippi', 'Delaware', 'Arizona', 'Utah', 'New Mexico', 'Louisiana', 'Virginia', 'California', 'South Carolina', 'Massachusetts', 'North Dakota', 'North Carolina', 'Arkansas'}, 'region': {'South', 'West', 'East', 'Central'}, 'category': {'Technology', 'Furniture', 'Office Supplies'}}
#     chunk_data("row_descriptions.txt", metadata)