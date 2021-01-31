import io
from lxml import etree
import requests
import zipfile
from urllib.request import urlopen
from source import logger
import traceback as tb
from source.models.file_paths import FilePaths
from source.constants import XML_URL , XMLConstants as xconst
from source.services.file_parser_service_interface import FileParserServiceInterface
from source.exceptions import XMLParsingException, ZipFileError

log = logger.getLogger(__name__)


class FileParserService(FileParserServiceInterface):
    """
    File Parser Service

    Responsible for Downloading and Parsing the xml downloaded.

    Attributes:
    ----------
    paths: object
        instance of the filePath model

    Methods:
    -------
    add_input_xml_link(link)
        saves input xml link
    get_doc:
        fetches the document from the url
    parse_xml:
        parses the xml based on the xml template
    extract_from_zip:
        Extract the xml from the zip file url
    """
    def __init__(self):
        self.paths = FilePaths()

    def add_input_xml_link(self, link):
        """
        saves input xml link
        Args:
            link(str): url pointing to xml file
        """
        self.paths.set_input_xml_link(link)

    def get_doc(self):
        """
        fetches the document from the url
        """
        var_url = urlopen(XML_URL)
        return etree.parse(var_url)

    def parse_xml(self, url):
        """
        parses the xml based on the xml template
        Args:
            url(str): url of the xml doc
        """
        try:
            return self._xml_parser(url)
        except Exception:
            log.error(tb.format_exc())
            raise XMLParsingException

    def extract_from_zip(self, url):
        """
        Extract the xml from the zip file url
        Args:
            url(str): Zip file url
        """
        try:
            r = requests.get(url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            for name in z.namelist():
                log.info(f"XML extracted from zip file is {name}")
                self.extracted_xml_name = name
                ex_file = z.open(name)  # this is a file like object
                content = ex_file.read()
                return etree.fromstring(content)
        except Exception:
            log.error(tb.format_exc())
            raise ZipFileError

    def _xml_parser(self, xml_url):
        """
        Core xml parser logic
        Args:
            xml_url(str): url of the xml
            csv_writer(object): file like object to write the xml to csv
        """
        root = self.extract_from_zip(xml_url)
        parsed_data = []
        for termntRcd in root.findall(xconst.record_tag, xconst.nmap):
            data = []
            for gnl_attrbts in termntRcd.findall(xconst.child1, xconst.nmap):
                data.extend([attr.text for attr in gnl_attrbts if attr.tag != '{{{0}}}{1}'.format(xconst.nmap["auth"], xconst.skip_child)])
            for gnl_attrbts in termntRcd.findall(xconst.child2, xconst.nmap):
                data.append(gnl_attrbts.text)
            parsed_data.append(data)
        return parsed_data

    def get_extracted_xml_name(self):
        return self.extracted_xml_name

