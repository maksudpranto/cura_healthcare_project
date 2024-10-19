from Pages.makeAppointmentPage import MakeAppointmentPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import Homepage
from Pages.confirmationPage import ConfirmationPage
from TestCases import test_validLogin

def test_makeAppointment(setup):
    page = setup
    login_credentials = {"Username": "John Doe", "Password": "ThisIsNotAPassword"}

    homepageVerifcation = Homepage(page)
    homepageVerifcation.verifyHomepageTitle("CURA Healthcare Service")

    loginPage = LoginPage(page)
    loginPage.performLogin(login_credentials)

    appointment = MakeAppointmentPage(page)
    appointment.performAppointment()

    confirmationPage = ConfirmationPage(page)

    confirmationPage.verifyConfirmationTitle()
    confirmationPage.verifyConfirmationSubtitle()



