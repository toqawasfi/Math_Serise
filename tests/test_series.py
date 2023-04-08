import pytest
from series.seriesmethods import fibonacci
from series.seriesmethods import lucas
from series.seriesmethods import sum_series

'''
If The Base Case is 0,0,1 so its fibonacci
If The Base Case is  2, 1 so its Lucas
The 3ed Function returns an index on the required parameter other way will produce other series

'''
#  //////////////////////////////////////////////////////fibonacci_tests/////////////////////////////////////////////////////////////////

def test_fibon_test1():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibon_test2():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibon_test3():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibon_test4():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibon_test5():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibon_test6():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibon_test7():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibon_test8():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

#  //////////////////////////////////////////////////////lucas_tests/////////////////////////////////////////////////////////////////

def test_lucas_test1():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_test2():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_test3():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_test4():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_test5():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_test6():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_test7():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_lucas_test8():
    actual = lucas(7)
    expected = 29
    assert actual == expected

#  //////////////////////////////////////////////////////lucas_tests/////////////////////////////////////////////////////////////////

def test_sum_series_test1():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_test2():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_test3():
    actual = sum_series(7)
    expected = 13
    assert actual == expected

def test_sum_series_test4():
    actual = sum_series(0,2,1)
    expected = 2
    assert actual == expected

def test_sum_series_test5():
    actual = sum_series(1,2,1)
    expected = 1
    assert actual == expected

def test_sum_series_test6():
    actual = sum_series(2,1,2)
    expected = 3
    assert actual == expected

def test_sum_series_test7():
    actual = sum_series(3,2,1)
    expected = 4
    assert actual == expected

def test_sum_series_test9():
    actual = sum_series(4,2,1)
    expected = 7
    assert actual == expected

def test_sum_series_test10():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected
    
    # 3,5,8,13,21,34,55
def test_sum_series_test11():
    actual = sum_series(2,3,5)
    expected = 8
    assert actual == expected


def test_sum_series_test12():
    actual = sum_series(0,3,5)
    expected = 3
    assert actual == expected

def test_sum_series_test13():
    actual = sum_series(3,3,5)
    expected = 13
    assert actual == expected


def test_sum_series_test17():
    actual = sum_series(5,3,5)
    expected = 34
    assert actual == expected


#  7,11,18,29,47,76,...
def test_sum_series_test14():
    actual = sum_series(0,7,11)
    expected = 7
    assert actual == expected

def test_sum_series_test15():
    actual = sum_series(3,7,11)
    expected = 29
    assert actual == expected

def test_sum_series_test16():
    actual = sum_series(5,7,11)  
    expected = 76
    assert actual == expected