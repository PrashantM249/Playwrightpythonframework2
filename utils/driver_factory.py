from playwright.sync_api import sync_playwright, Browser, Page


class DriverFactory:
    """Factory class for managing browser driver instances"""

    playwright = None
    browser = None
    page = None

    @staticmethod
    def init_browser(browser_type: str = "chromium", headless: bool = False):
        """Initialize and launch browser"""
        DriverFactory.playwright = sync_playwright().start()
        
        if browser_type.lower() == "chromium":
            DriverFactory.browser = DriverFactory.playwright.chromium.launch(headless=headless)
        elif browser_type.lower() == "firefox":
            DriverFactory.browser = DriverFactory.playwright.firefox.launch(headless=headless)
        elif browser_type.lower() == "webkit":
            DriverFactory.browser = DriverFactory.playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Invalid browser type: {browser_type}")
        
        DriverFactory.page = DriverFactory.browser.new_page()
        return DriverFactory.page

    @staticmethod
    def get_page():
        """Get the current page instance"""
        return DriverFactory.page

    @staticmethod
    def close_browser():
        """Close the browser and stop playwright"""
        if DriverFactory.page:
            DriverFactory.page.close()
        if DriverFactory.browser:
            DriverFactory.browser.close()
        if DriverFactory.playwright:
            DriverFactory.playwright.stop()
