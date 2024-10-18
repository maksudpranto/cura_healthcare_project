from playwright.sync_api import Page,expect
from Pages.LoginPage import LoginPage


def testValidLogin(setup)->None:
    page = setup
    login_credentials = {"Username":"John Doe","Password":"ThisIsNotAPassword"}
    loginPage = LoginPage(page)
    login_completion = loginPage.performLogin(login_credentials)



