import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def browser():
    """Fixture to initialize and close browser for each test"""
    page = DriverFactory.init_browser(browser_type="chromium", headless=False)
    yield page
    DriverFactory.close_browser()
