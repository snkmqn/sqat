import logging
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


def test_login_success(driver):
    logger.info("Step 1: Open login page")
    driver.get("https://the-internet.herokuapp.com/login")

    logger.info("Step 2: Enter username = tomsmith")
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    logger.info("Step 3: Enter password")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    logger.info("Step 4: Click Login button")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    logger.info("Step 5: Verify successful login message is displayed")
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message

    logger.info("Step 6: Verify user is on Secure Area page")
    assert "/secure" in driver.current_url
