import pytest
from pages.bing_home_page import BingHomePage


@pytest.mark.ui
def test_navigate_to_bing_com_verify_title_search_microsoft_bing(browser):
    """Test to navigate to bing.com and verify page title"""
    bing_page = BingHomePage(browser)
    bing_page.navigate_to_bing()
    bing_page.verify_page_title("Search - Microsoft Bing")
