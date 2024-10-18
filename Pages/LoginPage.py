class LoginPage:
    def __init__(self, page):
        self.page = page

        self._makeAppointmentButton = page.locator("//a[@id='btn-make-appointment']")
        self._username = page.locator("//input[@id='txt-username']")
        self._password = page.locator("//input[@id='txt-password']")
        self._loginButton = page.locator("//button[@id='btn-login']")

        self._appointmentText = page.locator("//h2[normalize-space()='Make Appointment']")



    def clickAppointment(self):
        self._makeAppointmentButton.click()

    def enter_username(self, username):
        self._username.clear()
        self._username.fill(username)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def clickLoginButton(self):
        self._loginButton.click()

    def performLogin(self,credentials):
        self.clickAppointment()
        self.enter_username(credentials["Username"])
        self.enter_password(credentials["Password"])
        self.clickLoginButton()


