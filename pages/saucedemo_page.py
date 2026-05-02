from utils.base_page import BasePage


class SauceDemoPage(BasePage):
    """Page Object for Sauce Demo Application"""

    # Locators
    SAUCEDEMO_URL = "https://www.saucedemo.com"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    def navigate_to_saucedemo(self):
        """Navigate to SauceDemo login page"""
        self.navigate(self.SAUCEDEMO_URL)

    def enter_username(self, username: str):
        """Enter username in the username field"""
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Enter password in the password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)

    def verify_inventory_page_url(self):
        """Verify that user is on inventory page"""
        current_url = self.get_url()
        assert current_url == self.INVENTORY_URL, f"Expected URL '{self.INVENTORY_URL}' but got '{current_url}'"
        return True

    def login_with_credentials(self, username: str, password: str):
        """Complete login flow with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_load_state()
