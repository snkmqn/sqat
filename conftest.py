import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import base64
import pytest_html


def _configure_logging():
    os.makedirs("logs", exist_ok=True)

    root = logging.getLogger()
    root.setLevel(logging.INFO)

    log_path = os.path.abspath(os.path.join("logs", "test_run.log"))

    for h in root.handlers:
        if isinstance(h, logging.FileHandler):
            try:
                if os.path.abspath(getattr(h, "baseFilename", "")) == log_path:
                    return
            except Exception:
                pass

    file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)

    root.info("Logging initialized. File: %s", log_path)


def pytest_configure(config):
    _configure_logging()
    logging.getLogger(__name__).info("=== Test run started ===")


def pytest_unconfigure(config):
    logging.getLogger(__name__).info("=== Test run finished ===")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        test_logger = logging.getLogger(item.name)

        if report.passed:
            test_logger.info("TEST RESULT: PASSED | %s", item.nodeid)

        elif report.failed:
            test_logger.error("TEST RESULT: FAILED | %s", item.nodeid)

            screenshots_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "screenshots"
            )
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(
                screenshots_dir, f"{item.name}_{timestamp}.png"
            )

            driver = getattr(item, "driver", None)
            if driver:
                driver.save_screenshot(screenshot_path)
                test_logger.error("Screenshot saved: %s", screenshot_path)

                png_bytes = driver.get_screenshot_as_png()
                png_b64 = base64.b64encode(png_bytes).decode("utf-8")

                extras_list = getattr(report, "extras", [])
                extras_list.append(
                    pytest_html.extras.png(png_b64, name="Screenshot")
                )
                report.extras = extras_list
            else:
                test_logger.error("Screenshot not captured: driver not available")

            test_logger.error("FAILURE DETAILS:\n%s", report.longreprtext)

        elif report.skipped:
            test_logger.warning("TEST RESULT: SKIPPED | %s", item.nodeid)


@pytest.fixture(scope="function")
def driver(request):

    test_logger = logging.getLogger(request.node.name)
    test_logger.info("TEST START: %s", request.node.nodeid)

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    request.node.driver = driver
    yield driver

    driver.quit()
    test_logger.info("TEST END: %s", request.node.nodeid)
