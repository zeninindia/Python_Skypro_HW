import pytest
from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_numbers_negative():
    assert utils.capitalize("123") == "123"

def test_capitalize_empty_negative():
    assert utils.capitalize("") == ""

#метод trim
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"

def test_trim_negative():
    assert utils.trim("skypro") == "skypro"

def test_trim_empty_negative():
    assert utils.trim("") == ""

#метод contains
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True

def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False

def test_contains_empty_negative():
    assert utils.contains("", "g") is False

#метод delete_symbol

def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_word_positive():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_negative():
    assert utils.delete_symbol("", "g") == ""

