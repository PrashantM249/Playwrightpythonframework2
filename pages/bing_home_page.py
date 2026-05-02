from utils.base_page import BasePage


class BingHomePage(BasePage):
    """Page Object for Bing Home Page"""

    # Locators
    BING_URL = "https://www.bing.com"
    SEARCH_BOX = "#sb_form_q"

    def navigate_to_bing(self):
        """Navigate to Bing home page"""
        self.navigate(self.BING_URL)

    def get_page_title(self):
        """Get the title of Bing home page"""
        return self.get_title()

    def verify_page_title(self, expected_title: str):
        """Verify the page title matches expected title"""
        actual_title = self.get_page_title()
        assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"
        return True
