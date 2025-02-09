import pytest
import allure
import requests

@allure.title("Verify the GEt Request of Restful Booker")
@allure.description("This Testcase check booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
   URL = "https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking"
   response_data = requests.get(url=URL)
   print(response_data.text)
   assert response_data.status_code ==200