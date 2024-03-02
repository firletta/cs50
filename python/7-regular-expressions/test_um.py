import pytest
from um import count

def test_valid_response():
    assert count("Um, Hello. How are You?") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Yummy Cake,!") == 0
    assert count("um, its nice to meet you emmy, um, i gotta go") == 2

def test_invalid_response():
    assert count("") == 0
    assert count("UMY YUM muy UMa umma") == 0