import time
import pytest
from playwright.sync_api import sync_playwright, Page, expect
from pages.home_page import HomePage
# @pytest.mark.skip
def test_search_query(page):

    search = "DroneTe"
    search_home = HomePage(page)
    search_home.fill_input__btn_click_for_search(search)
    time.sleep(5)
    search_home.wait_locator()
    search_home.result_search()

