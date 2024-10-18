import pytest

@pytest.fixture
def setup(page)->None:
    page.goto("https://katalon-demo-cura.herokuapp.com/")
    yield page

