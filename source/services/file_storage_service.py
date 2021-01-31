import boto3
from source import logger
from source.models.file_paths import FilePaths
import datetime
from source.services.file_storage_service_interface import FileStorageServiceInterface
from source.constants import AWSConstants as aconst

log = logger.getLogger(__name__)


class AWSStorageService(FileStorageServiceInterface):
    """
    Storage Service responsible for storing the extracted csv/or any file to AWS s3 bucket

    Attributes
    ----------

    path: obj
        instance of the filePath model
    bucket: str
        AWS s3 bucket name

    Methods
    --------
    set_s3_file_object_path(path)
        saves s3 object url path
    upload_file(filename)
        Uploads file to a S3 bucket
    get_object_url(bucket, keyname)
        fetches url of the uploaded s3 object
    """
    def __init__(self):
        self.path = FilePaths()
        self.bucket = aconst.bucket

    def set_s3_file_object_path(self, path):
        """
        saves s3 object url path

        Args:
            path(str): Object url path
        """
        self.path.set_s3_file_object_path(path)

    def upload_file(self, filename):
        """
        Uploads file to a S3 bucket

        Args:
            filename(str): Name of the file to be uploaded to s3
        """
        log.info("Initiating File upload to AWS...")
        obj = filename
        s3_client = boto3.client('s3')
        s3_client.upload_file(filename, self.bucket, obj)

    def get_object_url(self, bucket, key_name):
        """
        method to return uploaded csv object url

        Args:
            bucket(str): bucket name
            key_name: AWS key name
        """
        bucket_location = boto3.client('s3').get_bucket_location(Bucket=bucket)
        object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            bucket_location['LocationConstraint'],
            bucket,
            key_name)
        self.set_s3_file_object_path(object_url)
        return object_url