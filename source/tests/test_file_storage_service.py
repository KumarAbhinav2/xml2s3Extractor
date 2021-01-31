import unittest
from unittest.mock import patch, Mock
from source.services.file_storage_service import AWSStorageService
import boto3
import moto
from tempfile import NamedTemporaryFile
from source.exceptions import XMLParsingException, ZipFileError

BUCKET_NAME = 's3-simple-exp'
BUCKET_KEY = 'fake_key'

@moto.mock_s3
class TestAWSStorageService(unittest.TestCase):

    def setUp(self) -> None:
        self.storage_obj = AWSStorageService()
        self.client = boto3.client('s3', region_name='us-east-1')
        self.client.create_bucket(Bucket=BUCKET_NAME)
        self.bucket = BUCKET_NAME
        self.text = 'test\n'
        self.data = self.text.encode('utf-8')

    def test_upload_file(self):
        with NamedTemporaryFile(delete=True, suffix='.txt') as tmp:
            with open(tmp.name, 'w', encoding='UTF-8') as f:
                f.write(self.text)
            self.storage_obj.upload_file(BUCKET_KEY)

        bucket_obj = self.client.get_object(Bucket=BUCKET_NAME, Key=BUCKET_KEY)

        expected = self.data
        result = bucket_obj['Body'].read()

        self.assertEqual(expected, result)
