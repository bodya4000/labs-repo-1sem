"""
This module contains classes for converting time formats.
"""

from abc import ABC, abstractmethod


def check_length_of_date_list(date):
    """
    raises TimeException if len of date is not 3
    """
    if len(date) != 3:
        raise TimeException("Please follow this example -> 12:12:12")


def validating_date_items(date):
    """validates items in list date"""
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


def check_if_value_is_string(value):
    """checks if value is string"""
    if not isinstance(value, str):
        raise TimeException("Cannot handle other types except str")


def validating_seconds_date(num):
    """validates num value"""
    if num > 86399:
        raise TimeException("Too much seconds")
    if num < 0:
        raise TimeException("Cannot handle negative seconds")


class TimeException(Exception):
    """Exception that is raised when there's unexpected"""

    def __init__(self, message="Це моя власна помилка!"):
        self.message = message
        super().__init__(self.message)


class AbstractClass(ABC):
    """this is abstract class"""

    @abstractmethod
    def hello(self):
        """this method does greet"""
        print("hello")

    @abstractmethod
    def convert_time(self, value):
        """abstract method to make polymorphism"""


class TimeConverterToDate(AbstractClass, ABC):
    """this is class that can convert seconds into date"""

    def hello(self):
        """this overriding method from abstract class"""
        print("hello from TimeConverterToDate")

    def convert_time(self, value):
        """Converts seconds into date"""
        validating_seconds_date(value)

        hours = int(value / 3600)
        minutes = int((value - hours * 3600) / 60)
        seconds = value - hours * 3600 - minutes * 60

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"  # Padding using f-string


class TimeConverterToSeconds(AbstractClass, ABC):
    """this is class that can convert date into seconds"""
    MULTIPLIERS = [3600, 60, 1]

    def hello(self):
        """this overriding method from abstract class"""

        print("hello from TimeConverterToDate")

    def __init__(self):
        """constructor"""
        self.__date = []

    def set_date(self, date):
        """Setter"""
        check_length_of_date_list(date)
        validating_date_items(date)
        self.__date = date

    def get_date(self):
        """getter"""
        return self.__date

    def convert_time(self, value: str):
        """Converts the time from seconds to HH:MM:SS format."""
        total_seconds = 0
        check_if_value_is_string(value)
        self.set_date(value.split(":"))

        for i, item in enumerate(self.get_date()):
            num = int(item)
            total_seconds += num * TimeConverterToSeconds.MULTIPLIERS[i]

        return total_seconds


if __name__ == "__main__":
    converter_to_date = TimeConverterToDate()
    converter_to_seconds = TimeConverterToSeconds()

    print(converter_to_date.convert_time(36721))
    print(converter_to_seconds.convert_time("10:12:01"))
