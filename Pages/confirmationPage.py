class ConfirmationPage:
    def __init__(self, page):
        self.page = page

        self._confirmationTitle = page.get_by_role("heading", name="Appointment Confirmation")
        self._confirmationSubtitle = page.get_by_text("Please be informed that your").click()

    def verifyConfirmationTitle(self):
        assert self._confirmationTitle == "Appointment Confirmation"

    def verifyConfirmationSubtitle(self):
        assert self._confirmationSubtitle == "Please be informed that your appointment has been booked as following:"



