import pytest
from pages.bing_account_page import BingAccountPage


@pytest.mark.ui
def test_navigate_to_bing_account_general_set_safesearch_strict_wait_5_sec(browser):
    """Test to navigate to Bing account, set SafeSearch to Strict, and wait"""
    bing_account_page = BingAccountPage(browser)
    
    # Navigate to Bing account general settings
    bing_account_page.navigate_to_bing_account()
    
    # Set SafeSearch to Strict
    bing_account_page.set_safesearch_strict()
    
    # Verify SafeSearch Strict is selected
    bing_account_page.verify_safesearch_strict_selected()
    
    # Wait for 5 seconds
    bing_account_page.wait_seconds(5)
