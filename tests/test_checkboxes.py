import logging
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


def test_checkboxes_toggle(driver):
    logger.info("Step 1: Open Checkboxes page")
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    logger.info("Step 2: Locate both checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert len(checkboxes) == 2

    logger.info("Step 3: Read initial checkbox states")
    initial_first = checkboxes[0].is_selected()
    initial_second = checkboxes[1].is_selected()
    logger.info("Initial state: checkbox[0]=%s, checkbox[1]=%s", initial_first, initial_second)

    logger.info("Step 4: Toggle checkbox[0]")
    checkboxes[0].click()

    logger.info("Step 5: Toggle checkbox[1]")
    checkboxes[1].click()

    logger.info("Step 6: Verify final checkbox states (first checked, second unchecked)")
    assert checkboxes[0].is_selected()
    assert not checkboxes[1].is_selected()
