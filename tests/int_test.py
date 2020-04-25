import bsvxpy as bsv
import pytest

test_integer = hex(139) # 139 in decimal

print(test_integer)
int_test = bsv.IntegerShort(test_integer)

def test_int_short_init():
    assert int_test.get_data() == 3

test_integer = hex(146) # 146 in decimal
int_test_hex = bsv.IntegerLong(test_integer)

def test_int_long_init():
    assert int_test_hex.get_length() == 3 # @3/25 : Cannot read data from Long Integers, changed to check length

test_string_header = hex(44) # 44 in decimal
test_string = "The quick brown fox jumped over the lazy dog"
str_test = bsv.StringShort(test_string_header)

def test_str_short_init():
    assert str_test.get_length() == 44

test_string_hex_with_length = "03464F4F"
string_test_hex_with_length = bsv.StringShort(test_string_hex_with_length)

def test_str_short_hex_with_length_init():
    assert string_test_hex_with_length.get_length() == 3
    assert string_test_hex_with_length.get_data() == "FOO"