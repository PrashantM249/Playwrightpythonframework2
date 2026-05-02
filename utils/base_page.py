import time
from playwright.sync_api import Page, expect


class BasePage:
    """Base page class for all page objects"""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to the given URL"""
        self.page.goto(url)

    def click(self, selector: str):
        """Click on an element"""
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill input field with text"""
        self.page.fill(selector, text)

    def get_title(self):
        """Get the current page title"""
        return self.page.title()

    def get_url(self):
        """Get the current page URL"""
        return self.page.url

    def wait_for_load_state(self, state: str = "networkidle"):
        """Wait for page to load"""
        self.page.wait_for_load_state(state)

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        """Wait for a selector to appear"""
        self.page.wait_for_selector(selector, timeout=timeout)

    def get_text(self, selector: str):
        """Get text content of an element"""
        return self.page.text_content(selector)

    def is_visible(self, selector: str):
        """Check if element is visible"""
        return self.page.is_visible(selector)

    def wait_seconds(self, seconds: int):
        """Wait for specified seconds"""
        time.sleep(seconds)

    def close(self):
        """Close the page"""
        self.page.close()

    def expect_popup(self):
        """Expect a popup/new page to open"""
        return self.page.expect_popup()

    def get_current_page_title(self):
        """Get current page title"""
        return self.page.title()

    def get_current_page_url(self):
        """Get current page URL"""
        return self.page.url
