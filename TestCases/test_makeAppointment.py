from Pages.makeAppointmentPage import MakeAppointmentPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import Homepage
from TestCases import test_validLogin

def test_makeAppointment(setup):
    page = setup
    page = setup
    login_credentials = {"Username": "John Doe", "Password": "ThisIsNotAPassword"}

    homepageVerifcation = Homepage(page)
    homepageVerifcation.verifyHomepageTitle("CURA Healthcare Service")
    loginPage = LoginPage(page)
    login_completion = loginPage.performLogin(login_credentials)

    appointment = MakeAppointmentPage(page)
    appointment.performAppointment()


