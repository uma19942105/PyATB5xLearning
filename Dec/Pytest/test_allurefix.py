import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Allure annotations for test suite and description
@allure.feature("Login Test")
@allure.story("Enter email and password")
def test_enter_email_and_password():
    # Set up WebDriver (replace with the path to your WebDriver if not in PATH)
    driver = webdriver.Chrome()  # Use webdriver.Firefox() for Firefox

    try:
        # Open the login page
        with allure.step("Open login page"):
            driver.get("https://www.idrive360.com/enterprise/login")
            print("Login page opened successfully")

        # Wait for the email input box to be visible and enter email
        with allure.step("Enter email"):
            email_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
            email_input.click()
            email_input.send_keys("dipak@gmail.com")  # Enter email
            print("Email entered successfully")

        # Wait for the password input box to be visible and enter password
        with allure.step("Enter password"):
            password_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            password_input.click()
            password_input.send_keys("123456@")  # Enter password
            print("Password entered successfully")

    except Exception as e:
        # Attach screenshot and error message to Allure report on failure
        with allure.step("Capture screenshot on failure"):
            allure.attach(driver.get_screenshot_as_png(), name="Test_Failure", attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed: {e}")

    finally:
        # Close the browser
        driver.quit()
        print("Browser closed successfully")