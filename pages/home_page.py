from playwright.sync_api import sync_playwright, Page

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.page.goto("https://www.hugedomains.com/index.cfm")
        self.input_search_home = self.page.get_by_label("Home Page Domain Search")
        self.btn_search = self.page.locator("button#hdv3HomeSearchButtonID")

    def fill_input__btn_click_for_search(self, query):
        self.input_search_home.fill(query)
        self.btn_search.click()

    def wait_locator(self):
        self.page.wait_for_load_state("load")

    def result_search(self):
        for result in self.page.locator("div.domain-row").all():
            x = result.inner_text()
            print(f'list in terminal: {x}')
        return self.page.locator("div.domain-table")

