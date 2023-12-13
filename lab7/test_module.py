"""this module tests lab7.py"""

import pytest
from lab7 import TimeException, TimeConverterToSeconds, TimeConverterToDate


@pytest.fixture(name="test_converting_to_date_1")
def test_converting_to_date__1():
    """fixture of TimeConverterToDate"""
    return TimeConverterToDate()


@pytest.fixture(name="test_converter_to_seconds_2")
def test_converter_to_seconds__2():
    """fixture of TimeConverterToSeconds"""
    return TimeConverterToSeconds()


@pytest.mark.parametrize('seconds, error', [(86400, "Too much seconds"), (-1, "Cannot handle negative seconds")],)
def test_negative_time_conversion_to_date(test_converting_to_date_1, seconds, error):
    """negative test converter_to_date"""
    with pytest.raises(TimeException, match=error):
        test_converting_to_date_1.convert_time(seconds)


test_cases_positive_to_date = [
    (36721, "10:12:01"),
    (3600, "01:00:00"),
    (7200, "02:00:00"),
    (18000, "05:00:00"),
    (43200, "12:00:00")
]


@pytest.mark.parametrize('seconds, expected_time', test_cases_positive_to_date)
def test_positive_time_conversion_to_date(test_converting_to_date_1, seconds, expected_time):
    """positive test converter_to_date"""
    assert test_converting_to_date_1.convert_time(seconds) == expected_time


@pytest.mark.parametrize('date, error', [
    ("25:00:00", "hours cannot be more than 23"),
    ("23:00:000", "Two characters for item only"),
    ("21:76:00", "seconds or minutes cannot be more than 59"),
    ("21:00:99", "seconds or minutes cannot be more than 59"),
    (True, "Cannot handle other types except str")
])
def test_negative_time_conversion_to_seconds(test_converter_to_seconds_2, date, error):
    """negative test converter_to_seconds"""
    with pytest.raises(TimeException, match=error):
        test_converter_to_seconds_2.convert_time(date)


test_cases_to_sec = [
    ("10:12:01", 36721),
    ("01:00:00", 3600),
    ("02:00:00", 7200),
    ("05:00:00", 18000),
    ("12:00:00", 43200)
]


@pytest.mark.parametrize('time_str, expected_seconds', test_cases_to_sec)
def test_positive_time_conversion_to_seconds(test_converter_to_seconds_2,
                                             time_str, expected_seconds):
    """positive test converter_to_seconds"""
    assert test_converter_to_seconds_2.convert_time(time_str) == expected_seconds
