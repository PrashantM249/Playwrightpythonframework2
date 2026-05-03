from utils.base_page import BasePage


class BingAccountPage(BasePage):
    """Page Object for Bing Account Settings Page"""

    # Locators
    BING_ACCOUNT_URL = "https://www.bing.com/account/general?ru="
    SAFESEARCH_STRICT_RADIO = 'input[value="strict"]'

    def navigate_to_bing_account(self):
        """Navigate to Bing account general settings page"""
        self.navigate(self.BING_ACCOUNT_URL)
        # Use domcontentloaded instead of networkidle for faster page load detection
        try:
            self.page.wait_for_load_state("domcontentloaded")
        except Exception:
            # If timeout occurs, continue anyway as the page might still be usable
            pass

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
