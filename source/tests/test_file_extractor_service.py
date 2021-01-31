import unittest
from source.services.file_extractor_service import CSVExtractorService
from source.exceptions import CSVExtractionError
from unittest.mock import patch


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.ext_obj = CSVExtractorService()
        self.ext_obj.outfile = './test.csv'

    class FilePaths:
        def set_output_file_path(self, path):
            pass

    @patch.object(FilePaths, 'set_output_file_path', side_effect = None)
    def test_set_output_file_path(self, mock_filepath):
        link = 'http://example.com'
        self.ext_obj.set_output_file_path(link)

    def test_csv_writer_exception(self):
        data = ['x', 'y', 'z']
        self.ext_obj.outfile = None
        with self.assertRaises(CSVExtractionError):
            self.ext_obj.csv_writer(data)

    def test_csv_writer(self):
        data = ['x', 'y', 'z']
        ret = self.ext_obj.csv_writer(data)
        self.assertEqual(ret, self.ext_obj.outfile)


    def tearDown(self) -> None:
        import os
        os.remove('./test.csv')