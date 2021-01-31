"""
xml2csv Extractor

As the name suggests , this script is responsible for below tasks:
 - Download the xml from the given link
 - Parses the xml and get the specific url from the tags
 - Downloads the zip from the url extracted
 - converts the xml extracted from the zip file to csv file
 - saves the csv file to the AWS s3 bucket
"""


from source.controllers.extraction_controller import ExtractionController
from source.services.file_storage_service import AWSStorageService
from source.services.file_parser_service import FileParserService
from source.services.file_extractor_service import CSVExtractorService

from source import logger
log = logger.getLogger(__name__)

parser_obj = FileParserService()
storage_obj = AWSStorageService()
extract_obj = CSVExtractorService()


def start():
    """
    Starting point of the project
    """
    try:
        obj = ExtractionController(parser_obj, extract_obj, storage_obj)
        obj.start_processing()
    except Exception as e:
        log.error(e)
        return "Something went wrong ,check with dev team", 503


if __name__ == '__main__':
    log.info("Initiating the process...")
    start()

