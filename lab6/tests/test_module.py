import pytest
from lab6.lab6 import *


@pytest.fixture
def converter_to_date():
    return TimeConverterToDate()


@pytest.fixture
def converter_to_seconds():
    return TimeConverterToSeconds()


def test_time_conversion_to_date(converter_to_date):
    assert converter_to_date.convert_time(36721) == "10:12:01"
    with pytest.raises(TimeException):
        converter_to_date.convert_time(86400)  # More than 24 hours


def test_time_conversion_to_seconds(converter_to_seconds):
    assert converter_to_seconds.convert_time("10:12:01") == 36721
    with pytest.raises(TimeException):
        converter_to_seconds.convert_time("25:00:00")  # More than 24 hours
