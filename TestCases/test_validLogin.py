from playwright.sync_api import Page,expect
from Pages.LoginPage import LoginPage
from Pages.Homepage import Homepage


def testValidLogin(setup)->None:
    page = setup
    login_credentials = {"Username":"John Doe","Password":"ThisIsNotAPassword"}

    homepageVerifcation = Homepage(page)
    homepageVerifcation.verifyHomepageTitle("CURA Healthcare Service")
    loginPage = LoginPage(page)
    login_completion = loginPage.performLogin(login_credentials)



