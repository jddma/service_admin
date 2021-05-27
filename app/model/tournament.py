class Tournament:

    def __init__(self, name, start_date, end_date, is_active):
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__is_active = 0

    def get_name(self):
        return self.__name

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_is_active(self):
        return self.__is_active
