class Person:

    def __init__(self):
        self.id = None
        self.__document = None
        self.__lastnames = None
        self.__names = None

    def get_document(self):
        return self.__document

    def get_lastnames(self):
        return self.__lastnames

    def get_names(self):
        return self.__names