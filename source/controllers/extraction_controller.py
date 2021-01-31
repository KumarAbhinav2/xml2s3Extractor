from source import logger
from source.constants import XML_URL, XMLConstants as xconst
from source.exceptions import InvalidUrlException
log = logger.getLogger(__name__)


class ExtractionController:
    """
    Extraction Controller

    Controller class responsible for parsing, extraction and storage management
    Takes objects from :
        - Parser service
        - Extractor Service
        - Storage Service

    Attributes:
    ----------
    extractor: object
        file extractor service instance
    storage: object
        file storage service instance
    parser: object
        file parser service instance

    Methods:
    --------
    add_xml_link(link):
        Stores the input link for base xml
    _fetch_zip_url():
        Fetches the zip url from base document
    start_processing():
        Initiates extraction and parsing process
    """
    def __init__(self, file_parser_service, file_extractor_service, file_storage_service):
        self.extractor = file_extractor_service
        self.storage = file_storage_service
        self.parser = file_parser_service

    def add_xml_link(self, link):
        """
        Stores the input link for base xml
        Args:
            link (str): Input link to start process
        """
        self.parser.add_input_xml_link(link)

    def _fetch_zip_url(self):
        """
        Fetches the zip url from base document
        """
        try:
            doc = self.parser.get_doc()
        except Exception:
            raise InvalidUrlException
        for tag in doc.iterfind(xconst.URL_TAG):
            for children in tag.items():
                if children[1] == xconst.URL_ATTRIBUTE:
                    url = tag.text
                    if url:
                        return url

    def start_processing(self):
        """
        Initiates extraction and parsing process
        """
        self.add_xml_link(XML_URL)
        log.info("Initiating Extraction process...")
        url = self._fetch_zip_url()
        log.info(f"Trying to parse xml for url: {url}")
        data = self.parser.parse_xml(url)
        xml_name = self.parser.get_extracted_xml_name()
        self.extractor.set_output_file(xml_name)
        self.extractor.csv_writer(data)
        filename = self.extractor.get_output_file()
        log.info("XML Parsing completed and extracted to csv")
        self.storage.upload_file(filename)
        log.info("CSV uploaded to AWS successfully")
