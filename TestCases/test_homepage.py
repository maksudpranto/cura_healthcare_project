from Pages.Homepage import Homepage

def test_verifyHomepage(setup)->None:
    page = setup
    homepage = Homepage(page)
    homepage.verifyHomepageTitle("CURA Healthcare Service")

