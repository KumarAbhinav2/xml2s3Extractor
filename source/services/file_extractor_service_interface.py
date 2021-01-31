import abc


class FileExtractorServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_output_file_path(self, path):
        pass



