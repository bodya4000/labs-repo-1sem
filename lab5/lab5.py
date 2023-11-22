from abc import ABC, abstractmethod


def check_zeros(date):
    str_date = str(date)
    return "0" + str_date if len(str_date) == 1 else str_date


class AbstractClass(ABC):
    @abstractmethod
    def convert_time(self, value):
        pass


class TimeConverterToSeconds(AbstractClass):
    def convert_time(self, value):
        hours = int(value / 3600)
        minutes = int((value - hours * 3600) / 60)
        seconds = value - hours * 3600 - minutes * 60

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}") # f string padding


class TimeConverterToDate(AbstractClass):
    def convert_time(self, value):
        date = list(reversed(value.split(":")))
        summ = 0
        for i in range(0, len(date)):
            summ += int(date[i]) * 60 ** i
        print(summ)


converter1 = TimeConverterToDate()
converter2 = TimeConverterToSeconds()

converter2.convert_time(3700)
converter1.convert_time("10:12:01")


