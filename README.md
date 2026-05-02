# Playwright Python Testing Framework

A comprehensive testing framework built with Playwright and Python using the **Page Object Model (POM)** design pattern.

## 📋 Framework Overview

This framework provides a structured approach to automated testing with:
- **Page Object Model (POM)** for maintainable test code
- Pytest integration with HTML and Allure reporting
- Centralized browser driver management
- Reusable page locators and methods

## 📁 Project Structure

```
PlayWright_MCP_Project/
├── pages/                          # Page Object Models
│   ├── bing_home_page.py          # Bing home page object
│   ├── saucedemo_page.py          # SauceDemo login page object
│   ├── bing_account_page.py       # Bing account settings page object
│   ├── internet_herokuapp_page.py # Herokuapp windows page object
│   └── __init__.py
│
├── tests/                          # Test cases
│   ├── conftest.py                # Pytest fixtures (browser setup/teardown)
│   ├── test_bing_com.py           # Bing title verification test
│   ├── test_saucedemo.py          # SauceDemo login test
│   ├── test_bing_account.py       # Bing SafeSearch test
│   ├── test_herokuapp_windows.py  # Herokuapp windows test
│   └── __init__.py
│
├── utils/                          # Utilities
│   ├── base_page.py               # Base page class for all page objects
│   ├── driver_factory.py          # Browser driver management
│   └── __init__.py
│
├── reports/                        # Test execution reports (generated)
├── requirements.txt               # Project dependencies
└── pytest.ini                     # Pytest configuration
```

## 🔧 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd PlayWright_MCP_Project
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

## 📦 Dependencies

- **pytest** (7.4.3) - Testing framework
- **pytest-html** (4.1.1) - HTML reporting
- **pytest-xdist** (3.5.0) - Parallel test execution
- **allure-pytest** (2.13.2) - Allure reporting
- **playwright** (1.40.0) - Browser automation

## ▶️ Running Tests

### Run all tests
```bash
pytest
```

### Run tests with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_bing_com.py -v
```

### Run tests in parallel (using xdist)
```bash
pytest -n auto
```

### Run with HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run with Allure report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Run with specific markers
```bash
pytest -m ui
```

## 📄 Available Test Cases

### 1. test_bing_com.py
**Scenario:** Navigate to Bing home page and verify page title

**Steps:**
- Navigate to https://www.bing.com
- Verify page title is "Search - Microsoft Bing"

**Command:**
```bash
pytest tests/test_bing_com.py -v
```

### 2. test_saucedemo.py
**Scenario:** Login to SauceDemo and verify inventory page

**Steps:**
- Navigate to https://www.saucedemo.com
- Enter username: `standard_user`
- Enter password: `secret_sauce`
- Click login button
- Verify inventory page URL is https://www.saucedemo.com/inventory.html
- Wait 5 seconds

**Command:**
```bash
pytest tests/test_saucedemo.py -v
```

### 3. test_bing_account.py
**Scenario:** Set SafeSearch to Strict on Bing account settings

**Steps:**
- Navigate to https://www.bing.com/account/general
- Set SafeSearch to Strict
- Verify Strict is selected
- Wait 5 seconds

**Command:**
```bash
pytest tests/test_bing_account.py -v
```

### 4. test_herokuapp_windows.py
**Scenario:** Open new window and verify window title

**Steps:**
- Navigate to https://the-internet.herokuapp.com/windows
- Click "Click Here" link to open new window
- Switch to new window
- Verify new window title is "New Window"
- Wait 5 seconds
- Close new window

**Command:**
```bash
pytest tests/test_herokuapp_windows.py -v
```

## 🏗️ Page Object Model Implementation

### Base Page Class (utils/base_page.py)
Provides common functionality for all page objects:
- Navigation
- Element interaction (click, fill, get text)
- Wait conditions
- Title and URL verification

### Page Objects
Each page object extends `BasePage` and defines:
- **Locators:** CSS selectors for page elements
- **Methods:** Actions related to that page

Example:
```python
from utils.base_page import BasePage

class BingHomePage(BasePage):
    # Locators
    SEARCH_BOX = "#sb_form_q"
    
    # Methods
    def navigate_to_bing(self):
        self.navigate("https://www.bing.com")
    
    def verify_page_title(self, expected_title: str):
        actual_title = self.get_title()
        assert actual_title == expected_title
```

## 🧪 Test Implementation

Tests use page objects and fixtures:
```python
@pytest.mark.ui
def test_navigate_to_bing_com_verify_title(browser):
    bing_page = BingHomePage(browser)
    bing_page.navigate_to_bing()
    bing_page.verify_page_title("Search - Microsoft Bing")
```

## 🔌 Browser Driver Management

### DriverFactory (utils/driver_factory.py)
Manages browser lifecycle:
- **init_browser()** - Launch browser and create page
- **get_page()** - Get current page instance
- **close_browser()** - Close browser and cleanup

### conftest.py
Pytest fixture that:
- Initializes browser before each test
- Provides browser to test functions
- Closes browser after test completes

```python
@pytest.fixture(scope="function")
def browser():
    page = DriverFactory.init_browser(browser_type="chromium", headless=False)
    yield page
    DriverFactory.close_browser()
```

## 📊 Reports

### HTML Report
Generated at: `reports/report.html`
```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report
Generated at: `reports/allure-results`
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Test Log
Generated at: `reports/test_execution.log`

## 🎯 pytest.ini Configuration

The framework includes pytest.ini with:
- Test discovery patterns
- Test markers (smoke, regression, sanity, ui, slow)
- HTML and Allure report configuration
- Logging setup
- Test paths

## 🚀 Adding New Tests

### 1. Create Page Object
```python
# pages/new_page.py
from utils.base_page import BasePage

class NewPage(BasePage):
    ELEMENT_LOCATOR = "#element_id"
    
    def perform_action(self):
        self.click(self.ELEMENT_LOCATOR)
```

### 2. Create Test Case
```python
# tests/test_new_feature.py
import pytest
from pages.new_page import NewPage

@pytest.mark.ui
def test_new_scenario(browser):
    page = NewPage(browser)
    page.perform_action()
    # Add assertions
```

### 3. Run Test
```bash
pytest tests/test_new_feature.py -v
```

## ⚙️ Configuration

### Browser Options
Edit `utils/driver_factory.py` to customize:
- Browser type (chromium, firefox, webkit)
- Headless mode
- Viewport size
- Timeout values

### Test Markers
Add custom markers in `pytest.ini`:
```ini
markers =
    custom_marker: custom test marker
```

## 🐛 Troubleshooting

### Playwright browsers not installed
```bash
playwright install
```

### Import errors
Ensure you're running from project root and virtual environment is activated.

### Element not found
- Check selector in page object
- Verify page has loaded with `wait_for_load_state()`
- Use `page.pause()` to debug in browser

### Timeout errors
Increase timeout in `base_page.py` wait methods:
```python
def wait_for_selector(self, selector: str, timeout: int = 10000):
```

## 📝 Best Practices

1. **Use Page Objects** - Keep locators and methods in page objects
2. **Reusable Methods** - Create methods in BasePage for common actions
3. **Clear Naming** - Use descriptive test and method names
4. **Assertions** - Use assertions in page object methods
5. **Wait Conditions** - Always wait for page load state
6. **DRY Principle** - Don't repeat code; use fixtures and page objects
7. **Test Independence** - Tests should not depend on each other
8. **Logging** - Use meaningful assertion messages

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Allure Reporting](https://docs.qameta.io/allure/)

## 📧 Support

For issues or questions, refer to the official documentation of respective tools.

---

**Framework Version:** 1.0  
**Last Updated:** May 2, 2026
