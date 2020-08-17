from math_series import __version__
from math_series.math_series import *

def test_version():
    assert __version__ == '0.1.0'

def test_1(): 
    expected = 21
    actual = fibonacci(9) 
    assert expected == actual 

def test_2(): 
    expected = 13
    actual = fibonacci(8)
    assert expected == actual

def test_3(): 
    expected = 0
    actual = fibonacci(1)
    assert expected == actual

def test_4(): 
    expected = 1
    actual = fibonacci(2)
    assert expected == actual 
def test_0(): 
    expected = 'plese the number must more than 0'
    actual = fibonacci(0)
    assert expected == actual







#  lucas test
def test_2_1(): 
    expected = 2
    actual = lucas(1) 
    assert expected == actual 

def test_2_2(): 
    expected = 1
    actual = lucas(2)
    assert expected == actual

def test_2_3(): 
    expected = 4
    actual = lucas(4)
    assert expected == actual

def test_2_4(): 
    expected = 7
    actual = lucas(5)
    assert expected == actual 
def test_2_5(): 
    expected = 'plese the number must more than 0'
    actual = lucas(0)
    assert expected == actual


#  test for sum_series

def test_2_1(): 
    expected = 0
    actual = sum_series(1)
    assert expected == actual

def test_3_2(): 
    expected = 2
    actual = sum_series(1,2,1) 
    assert expected == actual 

def test_3_3(): 
    expected = 1
    actual = sum_series(2,4,1)
    assert expected == actual

def test_3_4(): 
    expected = 3
    actual = sum_series(1,3,3)
    assert expected == actual 

def test_3_6(): 
    expected = 12
    actual = sum_series(4,4,4)
    assert expected == actual 

def test_3_6(): 
    expected = 25
    actual = sum_series(5,5,5)
    assert expected == actual 

def test_3_6(): 
    expected = 19
    actual = sum_series(5,5,3)
    assert expected == actual 


def test_3_5(): 
    expected = 'plese the number must more than 0'
    actual = sum_series(0)
    assert expected == actual

