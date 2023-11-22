from abc import ABC, abstractmethod

def check_zeros(date):
    str_date = str(date)
    return "0" + str_date if len(str_date) == 1 else str_date
def check_length_of_date_list(date):
    if len(date) != 3:
        raise TimeException("Please follow this example -> 12:12:12")

def check_date_items(date):
    for i, item in enumerate(date):
        num = int(item)
        if len(item) != 2:
            raise TimeException("Two characters for item only")
        if not item.isdigit():
            raise TimeException("Integer argument required")
        if i == 0 and num > 23:
            raise TimeException("hours cannot be more than 23")
        if num > 59 and i in (1, 2):
            raise TimeException("seconds or minutes cannot be more than 59")
        if num < 0:
            raise TimeException("Cannot handle negative seconds")


class TimeException(Exception):
    def __init__(self, message="Це моя власна помилка!"):
        self.message = message
        super().__init__(self.message)


class AbstractClass(ABC):
    @abstractmethod
    def convert_time(self, value):
        pass


class TimeConverterToDate(AbstractClass):
    def convert_time(self, value):
        if value > 86399:
            raise TimeException("Too much seconds")
        if value < 0:
            raise TimeException("Cannot handle negative seconds")

        hours = int(value / 3600)
        minutes = int((value - hours * 3600) / 60)
        seconds = value - hours * 3600 - minutes * 60

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"  # f string padding


class TimeConverterToSeconds(AbstractClass):
    MULTIPLIERS = [3600, 60, 1]

    def __init__(self):
        self.__date = []

    def set_date(self, date):
        check_length_of_date_list(date)
        check_date_items(date)
        self.__date = date

    def get_date(self):
        return self.__date

    def convert_time(self, date_str):
        total_seconds = 0
        self.set_date(date_str.split(":"))

        for i, item in enumerate(self.get_date()):
            num = int(item)
            total_seconds += num * TimeConverterToSeconds.MULTIPLIERS[i]

        return total_seconds


converter_to_date = TimeConverterToDate()
converter_to_seconds = TimeConverterToSeconds()

converter_to_date.convert_time(36721)
converter_to_seconds.convert_time("10:12:01")
