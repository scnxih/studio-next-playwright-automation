from src.Helper.page_helper import PageHelper
from src.Helper.playwright_helper import PlaywrightHelper
from playwright.sync_api import Playwright, sync_playwright


def run(pw: Playwright) -> None:
    pw_objects = PlaywrightHelper.init_create_page(pw)
    page = pw_objects[0]
    context = pw_objects[1]
    browser = pw_objects[2]

    PageHelper.login(page)

    PageHelper.new_all_items(page)

    PageHelper.close_all_tabs(page)

    PageHelper.show_all_accordion(page)

    PageHelper.sign_out(page)

    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
