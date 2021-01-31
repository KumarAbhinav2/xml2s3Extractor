class FilePaths:
    """
    Model to store different paths encountered throughout the session starting from
    xml link to s3 bucket
    """
    def __init__(self):
        self.input_xml_link = None
        self.zip_file_path = None
        self.downloaded_xml_path = None
        self.output_file_path = None
        self.s3_file_object_path = None
        self.status = None

    def set_input_xml_link(self, link):
        self.input_xml_link = link

    def get_input_xml_link(self):
        return self.input_xml_link

    def set_zip_file_path(self, path):
        self.zip_file_path = path

    def get_zip_file_path(self):
        return self.downloaded_xml_path

    def set_output_file_path(self, path):
        self.output_file_path = path

    def get_output_file_path(self):
        return self.output_file_path

    def set_s3_file_object_path(self, path):
        self.s3_file_object_path = path

    def get_s3_file_object_path(self):
        return self.s3_file_object_path

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status