class Person:

    def __init__(
            self,
            document=None,
            names=None,
            lastnames=None,
            phone=None,
            address=None,
            email=None
    ):
        self._document = document
        self._names = names
        self._lastnames = lastnames
        self._phone = phone
        self._address = address
        self._email = email

    def get_document(self):
        return self._document

    def get_lastnames(self):
        return self._lastnames

    def get_names(self):
        return self._names

    def get_phone(self):
        return self._phone

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def set_email(self):
        return self._email

    def get_id(self):
        return self.id

    def set_document(self, document: str):
        self._document = document

    def set_lastnames(self, lastnames: str):
        self._lastnames = lastnames

    def set_names(self, names: str):
        self._names = names

    def set_phone(self, phone: str):
        self._phone = phone

    def set_address(self, address: str):
        self._address = address

    def set_email(self, email: str):
        self._email = email

    def set_id(self, id: int):
        self.id = id
