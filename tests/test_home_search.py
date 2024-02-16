import time
from pages.home_page import HomePage
import pytest
from playwright.sync_api import sync_playwright, Page



def test_search_query():
    search = "DroneTe"
    search_home = HomePage()
    search_home.fill_input__btn_click_for_search(search)
    time.sleep(5)
    search_home.wait_locator()
    search_home.result_search()
