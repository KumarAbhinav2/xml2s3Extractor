import abc


class FileParserServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_input_xml_link(self, link):
        pass

