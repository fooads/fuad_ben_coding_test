from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

url = "http://13.209.85.69" 

driver = webdriver.Chrome()

# Locate elements and fill the form fields
def fill_form(username, password, email, newsletter):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(email)
    checkbox = driver.find_element(By.ID, "newsletter")
    if checkbox.is_selected() != newsletter:
        checkbox.click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Wait for alert to appear and capture the text
def get_alert_text():
    time.sleep(1)  # Account for alert appearance
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    return alert_text

def test_username_min_length():
    fill_form("usr", "ValidPassword123", "user@example.com", True)
    assert get_alert_text() == "Username must be at least 5 characters."

def test_password_min_length():
    fill_form("validuser", "short", "user@example.com", True)
    assert get_alert_text() == "Password must be at least 8 characters."

def test_email_format():
    fill_form("validuser", "ValidPassword123", "userexample.com", True)
    assert get_alert_text() == "Please enter a valid email."

# We can check that no alert is triggered by assuming that page url does not change
# after 1 second of waiting after the form submissions
def test_valid_submission():
    fill_form("validuser", "ValidPassword123", "user@example.com", True)
    time.sleep(1)
    assert driver.current_url == url

# Test suite execution
try:
    driver.get(url)

    test_username_min_length()
    print("Username min length test passed")

    test_password_min_length()
    print("Password min length test passed")

    test_email_format()
    print("Email format test passed")

    test_valid_submission()
    print("Valid submission test passed")

finally:
    # Close the browser
    driver.quit()
