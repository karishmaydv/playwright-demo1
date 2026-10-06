import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_home_page import HomePage
# this was the pom design pattern implementation of the test case in the test_login_orangehrm.py file. The test case was refactored to use the page object model design pattern. The test case is now more readable and maintainable. The test case is now using the LoginPage and HomePage classes to perform the actions on the login and home pages respectively. The test case is now more readable and maintainable.


def test_example(page: Page) -> None:

    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()


    home_page.is_upgrade_button_visible()
    home_page.click_upgrade()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview")
    home_page.click_dashboard()