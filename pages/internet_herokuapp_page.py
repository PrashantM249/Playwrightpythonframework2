from utils.base_page import BasePage


class InternetHerokuAppPage(BasePage):
    """Page Object for The Internet Herokuapp Windows Page"""

    # Locators
    INTERNET_HEROKUAPP_URL = "https://the-internet.herokuapp.com/windows"
    CLICK_HERE_LINK = 'a[href="/windows/new"]'

    def navigate_to_windows_page(self):
        """Navigate to The Internet Herokuapp windows page"""
        self.navigate(self.INTERNET_HEROKUAPP_URL)
        self.wait_for_load_state()

    def click_here_link(self):
        """Click on 'Click Here' link to open a new window"""
        with self.page.expect_popup() as popup_info:
            self.click(self.CLICK_HERE_LINK)
        return popup_info.value

    def verify_new_window_title(self, new_page, expected_title: str):
        """Verify the title of the new window"""
        new_page.wait_for_load_state()
        actual_title = new_page.title()
        assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"
        return True
