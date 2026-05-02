import pytest
from pages.internet_herokuapp_page import InternetHerokuAppPage


@pytest.mark.ui
def test_navigate_to_the_internet_herokuapp_windows_click_here_new_window_verify_title(browser):
    """Test to navigate to herokuapp windows page, open new window, and verify title"""
    herokuapp_page = InternetHerokuAppPage(browser)
    
    # Navigate to the windows page
    herokuapp_page.navigate_to_windows_page()
    
    # Click on "Click Here" link to open new window
    new_page = herokuapp_page.click_here_link()
    
    # Verify the title of the new window
    herokuapp_page.verify_new_window_title(new_page, "New Window")
    
    # Wait for 5 seconds
    herokuapp_page.wait_seconds(5)
    
    # Close the new page
    new_page.close()
