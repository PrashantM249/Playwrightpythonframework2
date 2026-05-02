import pytest
from pages.saucedemo_page import SauceDemoPage


@pytest.mark.ui
def test_navigate_to_saucedemo_enter_credentials_click_login_validate_inventory_url(browser):
    """Test to navigate to saucedemo.com, login, and verify inventory page"""
    saucedemo_page = SauceDemoPage(browser)
    
    # Navigate to SauceDemo
    saucedemo_page.navigate_to_saucedemo()
    
    # Login with credentials
    saucedemo_page.login_with_credentials("standard_user", "secret_sauce")
    
    # Verify inventory page URL
    saucedemo_page.verify_inventory_page_url()
    
    # Wait for 5 seconds
    saucedemo_page.wait_seconds(5)
