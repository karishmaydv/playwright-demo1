#impot page object from playwright.sync_api from tests/test_login_orangehrm.py

from playwright.sync_api import Page, expect

class HomePage:
    
    # this is constructor of the class here we are initializing the page object and the locators for the elements on the home page
    def __init__(self, page: Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        self.performance_link = page.get_by_role("link", name="Performance")

    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible()
    #this is the action method to click the upgrade button
    def click_upgrade(self):
        self.upgrade_button.click()

    #this is the action method to click the dashboard link
    def click_dashboard(self):
        self.dashboard_link.click()

    def click_performance(self):
        self.performance_link.click()    