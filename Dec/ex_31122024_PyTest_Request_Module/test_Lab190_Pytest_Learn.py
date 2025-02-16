import pytest
import allure
import requests
@allure.title("TC#1-Verify that 2-2==0")
@allure.description("this is BASIC Math Test")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2 ==0

@allure.title("TC#2 Verify that 3-3==0")
@allure.description("this is BASIC Math Test")
@pytest.mark.regression
def test_sub1():
    assert 3-3==0

@allure.title("TC#3 Verify that 1-1==0")
@allure.description("this is BASIC Math Test")
@pytest.mark.smoke
def test_sub2():
    assert 1-1==0