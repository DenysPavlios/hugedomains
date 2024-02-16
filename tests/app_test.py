from playwright.sync_api import sync_playwright, Page
from pages.home_page import HomePage

import pytest

my_acc = 'https://www.hugedomains.com/payment-plan-login.cfm'

@pytest.fixture
def playwright_page_index(page):
    page.goto("https://www.hugedomains.com/index.cfm")
    print(f'test # 1 ')
    return page



def test_assert(playwright_page_index):
    print(f'test # 2 ')
    link = playwright_page_index.locator("#header").get_by_role("link", name="Home")
    assert link.is_visible()


def test_click_link(playwright_page_index):
    print(f'test # 3 ')
    link = playwright_page_index.locator("#header").get_by_role("link", name="My account")
    link.click()
    assert playwright_page_index.url == my_acc
