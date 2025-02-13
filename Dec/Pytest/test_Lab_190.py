import pytest
import ctypes

class MyClass:
    _type = "exampe_type"
def test_add():

    result = 2+2
    assert result == 4
# pytest -v --alluredir=allure-results
# allure generate allure-results -o allure-report --clean
# allure serve allure-results