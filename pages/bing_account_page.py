from utils.base_page import BasePage
import os


class BingAccountPage(BasePage):
    """Page Object for Bing Account Settings Page"""

    # Locators
    BING_ACCOUNT_URL = "https://www.bing.com/account/general?ru="
    SAFESEARCH_STRICT_RADIO = 'input[value="strict"]'

    def navigate_to_bing_account(self):
        """Navigate to Bing account general settings page"""
        self.navigate(self.BING_ACCOUNT_URL)
        # Use shorter timeout for CI environments
        timeout = 10000 if os.getenv("CI") or os.getenv("JENKINS_HOME") else 30000
        self.wait_for_load_state(timeout=timeout)

    def set_safesearch_strict(self):
        """Set SafeSearch to Strict by clicking the Strict radio button"""
        self.wait_for_selector(self.SAFESEARCH_STRICT_RADIO)
        self.click(self.SAFESEARCH_STRICT_RADIO)

    def verify_safesearch_strict_selected(self):
        """Verify that Strict SafeSearch is selected"""
        # Check if the radio button is checked
        is_checked = self.page.is_checked(self.SAFESEARCH_STRICT_RADIO)
        assert is_checked, "SafeSearch Strict radio button is not selected"
        return True
