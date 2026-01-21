import pytest


def test_demo_failure_logging(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert False, "Demo failure to verify logging"
