class Homepage:
    def __init__(self,page):
        self._page = page

    def verifyHomepageTitle(self,expectedTitle):
        assert self._page.title() == expectedTitle