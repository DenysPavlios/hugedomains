import time
from pages.home_page import HomePage
import pytest
@pytest.fixture
def page():
    yield


def test_search_query(page):
    search = "DroneTe"
    search_home = HomePage(page)
    search_home.fill_input__btn_click_for_search(search)
    time.sleep(5)
    search_home.wait_locator()
    search_home.result_search()
