import unittest
from source.services.file_parser_service import FileParserService
from source.exceptions import XMLParsingException, ZipFileError
from requests.exceptions import Timeout
from unittest.mock import patch, Mock


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.parser_obj = FileParserService()

    class FilePaths:
        def set_input_xml_link(self, link):
            pass

    @patch.object(FilePaths, 'set_input_xml_link', side_effect = None)
    def test_add_input_xml_link(self, mock_filepath):
        link = 'http://example.com'
        self.parser_obj.add_input_xml_link(link)

    @patch('source.services.file_parser_service.etree')
    @patch('source.services.file_parser_service.urlopen')
    def test_get_doc(self, mock_urlopen, mock_tree):
        #XML_URL = 'http://example.com'
        mock_urlopen.side_effect = Mock()
        mock_tree.side_effect = Mock()
        self.parser_obj.get_doc()
        mock_urlopen.assert_called_once()
        mock_tree.parse.assert_called_once()

    @patch('source.services.file_parser_service.FileParserService._xml_parser')
    def test_parse_xml(self, mock_parser):
        url = 'http://example.com'
        mock_parser.side_effect = [['a', 'b', 'c']]
        res = self.parser_obj.parse_xml(url)
        self.assertIsInstance(res, list)
        self.assertEqual(res, ['a', 'b', 'c'])

    @patch('source.services.file_parser_service.FileParserService._xml_parser')
    def test_parse_xml_exception(self, mock_parser):
        url = 'http://example.com'
        mock_parser.side_effect = XMLParsingException
        with self.assertRaises(XMLParsingException):
            self.parser_obj.parse_xml(url)
            mock_parser.assert_called_once()

    @patch('source.services.file_parser_service.requests')
    def test_extract_from_zip_exception(self, mock_requests):
        url = 'http://example.com'
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(ZipFileError):
            self.parser_obj.extract_from_zip(url)
            mock_requests.get.assert_called_once()

    class requests:

        def get(self, url):
            pass

        content = b'<?xml version="1.0" encoding="UTF-8"?>\n<response>\n\n<lst name="responseHeader">\''


    @patch('source.services.file_parser_service.etree')
    @patch('source.services.file_parser_service.zipfile.ZipFile')
    @patch('source.services.file_parser_service.zipfile.is_zipfile')
    @patch.object(requests, 'get')
    def test_extnract_from_zip(self, mock_requests, mock_zip, mock_zipfile, mock_etree):
        url = 'http://example.com'
        MOCK_LISTING = ['single_file_module.py',
                        'test.zip']
        mock_zip.is_zipfile.return_value = True
        mock_zipfile.return_value.namelist.return_value = MOCK_LISTING
        mock_zipfile.return_value.open.return_value = Mock()
        mock_etree.fromstring.side_effect = Mock()
        self.parser_obj.extract_from_zip(url)
        mock_etree.fromstring.assert_called_once()


if __name__ == '__main__':
        unittest.main()