import pytest
from practice_day1 import add_numbers, is_adult, calculate_discount, count_even_ids

def test_add_positive_numbers():
    assert add_numbers(10,20) == 30

def test_add_negative_numbers():
    assert add_numbers(-5, -3) == -8

def test_add_zero():
    assert add_numbers(10, 0) == 10



def test_is_adult():
      assert is_adult(17) == False

def test_is_adult_Under_eighteen():
      assert is_adult(9) == False

def test_is_adult_exactly_eighteen():
      assert is_adult(18) == True    

def test_is_adult_over_eighteen():
      assert is_adult(30) == True          


@pytest.mark.parametrize("age, expected", [
    (17, False),
    (9, False),
    (18, True),
    (30, True),
])
def test_is_adult_multiple_ages(age, expected):
    assert is_adult(age) == expected


@pytest.mark.parametrize("price ,discount_percent,expected_final_price" ,[
    (100,10,90),
    (200,25,150),
    (50,0,50),
    (100,100,0)
])
def test_calculate_discount_multiple_prices(price ,discount_percent , expected_final_price):
    assert calculate_discount(price ,discount_percent) == expected_final_price



@pytest.mark.parametrize("applications_ids , expected_count" ,[
    ([101, 102, 103, 104] , 2),
    ([101, 103, 105], 0),
    ([102, 104, 106] , 3),
    ([],0)
])
 
def test_count_even_ids(applications_ids,expected_count):
    assert count_even_ids(applications_ids) == expected_count  