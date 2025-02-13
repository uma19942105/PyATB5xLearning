import pytest
import allure
from jinja2.compiler import generate


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This Testcase check for the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
   # assert 1-1 == 2
   #  assert 1+1 == 2

# allure generate allure-result -o allure-report --clean


