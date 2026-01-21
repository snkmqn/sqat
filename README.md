# Assignment 5 — Automated UI Testing with pytest

## Overview
This project implements automated UI testing using **Python, pytest, Selenium WebDriver**, and **pytest-html**.  
The project demonstrates test lifecycle management, logging, HTML reporting, and automatic screenshots on failure.

## Test System Selection
**Selected platform:**  
https://the-internet.herokuapp.com

This platform is commonly used for QA practice and provides stable UI elements suitable for automation testing.

---

## Technology Stack and Dependencies

### Programming Language
- Python 3.12 or newer

### Testing Framework
- **pytest** — test execution framework and lifecycle management

### Browser Automation
- **selenium** — UI automation with WebDriver (Chrome)

### Reporting
- **pytest-html** — HTML test execution report generation

### Logging
- **logging** (Python standard library) — test execution logging to file

### Browser
- Google Chrome  
  (ChromeDriver is managed automatically by Selenium Manager)

---


## Implemented Requirements

### 1. Test Lifecycle Management
- Implemented using pytest fixtures
- Setup before each test (browser initialization)
- Teardown after each test (browser cleanup)
- Clear separation between setup, test logic, and cleanup
- Minimum of 3 automated test cases implemented



### 2. Logging Framework
- Python built-in `logging` module is used
- Logs include:
  - test start and end
  - main test steps
  - test results (pass / fail / skip)
  - failure details
- Logs are written to file:

### 3. Test Report and Screenshots

#### HTML Test Execution Report
- Generated automatically using pytest-html
- Includes:
  - test execution summary (pass / fail / skip)
  - individual test case results
  - captured logs per test
  - expected vs actual results (assertion diff)
  - clear failure descriptions
  - embedded screenshots on failure

#### Screenshots on Failure
- Screenshots are captured automatically when a test fails
- Saved to: screenshots/
- Embedded directly into the HTML report
---

## Setup Instructions


### 1. Verify Python installation
```bash
python --version
```

### 2. Install required dependencies
```
pip install pytest selenium pytest-html
```
---
## Test Execution
Run all tests
```
pytest -v
```

Generate HTML test execution report
```
pytest -v --html=reports/report.html --self-contained-html
```

## After execution:

* Open reports/report.html in a browser to review test results

* Check logs/test_run.log for file-based execution logs