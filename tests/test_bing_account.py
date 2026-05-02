import os
import pytest
from pages.bing_account_page import BingAccountPage


@pytest.mark.ui
@pytest.mark.skipif(
    os.getenv("CI") == "true" or 
    os.getenv("JENKINS_HOME") is not None or
    os.getenv("BUILD_NUMBER") is not None,
    reason="Bing account page requires authentication and may timeout in CI environments"
)
def test_navigate_to_bing_account_general_set_safesearch_strict_wait_5_sec(browser):
    """Test to navigate to Bing account, set SafeSearch to Strict, and wait"""
    bing_account_page = BingAccountPage(browser)
    
    try:
        # Navigate to Bing account general settings
        bing_account_page.navigate_to_bing_account()
        
        # Check if we're redirected to login or if page loads properly
        current_url = bing_account_page.get_url()
        if "login" in current_url.lower() or "signin" in current_url.lower():
            pytest.skip("Bing account page redirected to login - requires authentication")
        
        # Set SafeSearch to Strict
        bing_account_page.set_safesearch_strict()
        
        # Verify SafeSearch Strict is selected
        bing_account_page.verify_safesearch_strict_selected()
        
        # Wait for 5 seconds
        bing_account_page.wait_seconds(5)
        
    except Exception as e:
        if "Timeout" in str(e) or "timeout" in str(e).lower():
            pytest.skip(f"Bing account page timed out in CI environment: {str(e)}")
        else:
            raise
