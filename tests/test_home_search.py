import time
from pages.home_page import HomePage
import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        page.close()
        browser.close()

def test_search_query(page):
    search = "DroneTe"
    search_home = HomePage(page)
    search_home.fill_input__btn_click_for_search(search)
    time.sleep(5)
    search_home.wait_locator()
    search_home.result_search()
