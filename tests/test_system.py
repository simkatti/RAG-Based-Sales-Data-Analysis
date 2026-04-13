import unittest
import os
from src.sales_data_analysis.chunk_docs import chunk_data
from src.sales_data_analysis.main import extract_metadata_from_query


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_data.txt"
        with open(self.test_filename, "w") as f:
            f.write("This line consists of data of sales in 2015\n")
            f.write("x" * 1000 + "\n")
            f.write("This line consists of data of sales in 2017\n")

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_metadata_and_character_split(self):
        chunks, chunk_md = chunk_data(self.test_filename)
        self.assertEqual(len(chunks), 3)

    def test_metadata_extractor_with_two_metadatas(self):
        query = "This query has two metadata tags: 2016 and the city New York"
        metadata = extract_metadata_from_query(query)
        self.assertEqual(len(metadata['$and']), 2)

    def test_metadata_extractor_with_one_metadatas(self):
        query = "This query has one metadata tag: the city New York"
        metadata = extract_metadata_from_query(query)
        self.assertEqual(len(metadata['state']), 1)
