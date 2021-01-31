
class InvalidUrlException(Exception):
    def __init__(self):
        message = "Invalid url encountered"
        super().__init__(message)


class XMLParsingException(Exception):
    def __init__(self):
        message = "XML Parser error"
        super().__init__(message)


class ZipFileError(Exception):
    def __init__(self):
        message = "Zip File error"
        super().__init__(message)

class CSVExtractionError(Exception):
    def __init__(self):
        message = "Error while extracting to csv"
        super().__init__(message)