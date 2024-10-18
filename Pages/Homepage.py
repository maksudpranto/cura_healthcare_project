class Homepage:
    def __init__(self,page):
        self.page = page

    def verifyHomepageTitle(self,expectedTitle):
        assert self.page.title() == expectedTitle