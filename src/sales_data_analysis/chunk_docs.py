def chunk_data(textfile):
    chunk_size = 2000
    with open((textfile), "r") as file:
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
            for key, values in metadata.items():
                for value in values:
                    if value in line:
                        line_metadata[key] = value
                        break

        if not current_metadata:
            current_metadata = line_metadata

        if current_metadata != line_metadata or len(
                text_chunk) + len(line) > chunk_size:
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

    print("Docs chunked! returning chunks and metadata")
    # print(chunk_metadats)
    return chunks, chunk_metadats


metadata = {
    'segment': {
        'Corporate',
        'Home Office',
        'Consumer'},
    'year': {
        '2015',
        '2017',
        '2016',
        '2014'},
    'state': {
        'New Mexico',
        'Kentucky',
        'Michigan',
        'South Carolina',
        'Missouri',
        'New Jersey',
        'Rhode Island',
        'Maryland',
        'New York',
        'Vermont',
        'Tennessee',
        'California',
        'Nevada',
        'Kansas',
        'Mississippi',
        'Minnesota',
        'Wyoming',
        'Arizona',
        'Montana',
        'Massachusetts',
        'District of Columbia',
        'Iowa',
        'Ohio',
        'Oklahoma',
        'Illinois',
        'Louisiana',
        'Georgia',
        'Utah',
        'Pennsylvania',
        'Florida',
        'Arkansas',
        'North Dakota',
        'Colorado',
        'Connecticut',
        'North Carolina',
        'Maine',
        'New Hampshire',
        'West Virginia',
        'South Dakota',
        'Idaho',
        'Oregon',
        'Washington',
        'Alabama',
        'Virginia',
        'Wisconsin',
        'Texas',
        'Indiana',
        'Delaware',
        'Nebraska'},
    'region': {
        'East',
        'West',
        'South',
        'Central'},
    'category': {
        'Technology',
        'Office Supplies',
        'Furniture'},
    'sub-category': {
        'Chairs',
        'Tables',
        'Furnishings',
        'Art',
        'Binders',
        'Appliances',
        'Paper',
        'Supplies',
        'Accessories',
        'Phones',
        'Bookcases',
        'Copiers',
        'Fasteners',
        'Storage',
        'Machines',
        'Labels',
        'Envelopes'}}


def get_metadata():
    return metadata
