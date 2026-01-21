import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

logger = logging.getLogger(__name__)


def test_dropdown_state_transitions(driver):
    logger.info("Step 1: Open Dropdown page")
    driver.get("https://the-internet.herokuapp.com/dropdown")

    logger.info("Step 2: Locate dropdown element")
    dropdown_element = driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)

    logger.info("Step 3: Verify default option is selected")
    default_selected = dropdown.first_selected_option.text
    logger.info("Default selected option: %s", default_selected)
    assert default_selected == "Please select an option"

    logger.info("Step 4: Select 'Option 1'")
    dropdown.select_by_visible_text("Option 1")

    logger.info("Step 5: Verify 'Option 1' is selected")
    selected_option_1 = dropdown.first_selected_option.text
    logger.info("Selected option after Option 1: %s", selected_option_1)
    assert selected_option_1 == "Option 1"

    logger.info("Step 6: Select 'Option 2'")
    dropdown.select_by_visible_text("Option 2")

    logger.info("Step 7: Verify 'Option 2' is selected")
    selected_option_2 = dropdown.first_selected_option.text
    logger.info("Selected option after Option 2: %s", selected_option_2)
    assert selected_option_2 == "Option 2"
