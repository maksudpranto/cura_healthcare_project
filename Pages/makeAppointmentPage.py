class MakeAppointmentPage:
    def __init__(self, page):
        self.page = page

        self._facility = page.get_by_label("Facility")
        self._reAdmission = page.get_by_text("Apply for hospital readmission")
        self._program = page.get_by_text("Medicaid")
        self._date = page.locator("form div").filter(has_text="Visit Date (Required)").locator("div").nth(2)
        self._selectDate = page.get_by_role("cell", name="24", exact=True)
        self._commentClick = page.get_by_placeholder("Comment")
        self._addComment = page.get_by_placeholder("Comment")
        self._bookAppointmentButton = page.get_by_role("button", name="Book Appointment")


    def performAppointment(self):
        self._facility.select_option("Seoul CURA Healthcare Center")
        self._reAdmission.click()
        self._program.click()
        self._date.click()
        self._selectDate.click()
        self._commentClick.click()
        self._addComment.fill("This is an automation test by Pranto.")
        self._bookAppointmentButton.click()
