import csv
from source import logger
from source.models.file_paths import FilePaths
from source.constants import CSVConstants as cconst
from source.exceptions import CSVExtractionError
from source.services.file_extractor_service_interface import FileExtractorServiceInterface

log = logger.getLogger(__name__)


class CSVExtractorService(FileExtractorServiceInterface):
    """
    CSVExtractorService

    This class takes care of writing data buffer to csv file.
    currently, writes the file on the disk

    Attributes:
    ----------
    path: object
        instance of the filePath model
    outfile: str
        path of the output csv file
    writer: object
        handle of the csv writer

    Methods:
    --------
    set_output_file_path(outfile)
        saves the outfile path
    csv_writer
        simple csv file writer
    get_writer
        returns writer handle
    get_outfile
        returns output file path
    """

    def __init__(self):
        self.path = FilePaths()
        # TODO - make this dynamic with unique name
        self.outfile = None

    def set_output_file_path(self, outfile):
        """
        Saves the output file path
        Args:
            outfile (str): path to the file
        """
        return self.path.set_output_file_path(outfile)

    def csv_writer(self, data):
        """
        Simple csv file writer
        """
        try:
            log.info(f"Initiating extracting csv from xml at {self.outfile}")
            f = open(self.outfile, 'w', newline='', encoding='utf-8')
            csvwriter = csv.writer(f)
            csvwriter.writerow(cconst.cols)
            for row in data:
                csvwriter.writerow(row)
            return self.outfile
        except Exception:
            import traceback as tb
            log.error(tb.format_exc())
            raise CSVExtractionError

    def set_output_file(self, filename):
        prefix = filename.split('.xml', 1)[0]
        self.outfile = prefix+'.csv'

    def get_output_file(self):
        """
        returns output file path
        """
        return self.outfile
