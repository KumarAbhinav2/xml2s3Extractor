import abc


class FileStorageServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_s3_file_object_path(self, path):
        pass