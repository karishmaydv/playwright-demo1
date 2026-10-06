#impot page object from playwright.sync_api from tests/test_login_orangehrm.py

from playwright.sync_api import Page, expect



class LoginPage:

    # this is constructor of the class here we are initializing the page object and the locators for the elements on the login page
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
#this is the action method to enter the username in the username input field
    def enter_username(self, username: str):
        self.username_input.click()
        self.username_input.fill(username)
        

#this is the action method to enter the password in the password input field
    def enter_password(self, password: str):
        self.password_input.click()
        self.password_input.fill(password)
        

#this is the action method to click the login button
    def click_login(self):
        self.login_button.click()

        #this is the action method to perform the login action by calling the enter_username, enter_password and click_login methods

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()    