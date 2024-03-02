import pytest
from working import convert

def test_convert_9am_to_5pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_900am_to_500pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"  

def test_convert_10pm_to_8am():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_convert_1030pm_to_850am():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_convert_invalid_time_raises():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert_invalid_format_raises():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_convert_invalid_24hour_format_raises():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")