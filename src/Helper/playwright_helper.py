from playwright.sync_api import Playwright, Page
from src.Utilities.vars import *


class PlaywrightHelper:

    @staticmethod
    def get_head_mode(head_mode):
        if head_mode == "headless":
            return True
        else:
            return False

    @staticmethod
    def get_browser(browser, head_mode, playwright: Playwright):
        if browser == "chrome":
            browser = playwright.chromium.launch(channel="chrome", headless=PlaywrightHelper.get_head_mode(head_mode))
        elif browser == "firefox":
            browser = playwright.firefox.launch(headless=PlaywrightHelper.get_head_mode(head_mode))
        elif browser == "webkit":
            browser = playwright.webkit.launch(headless=PlaywrightHelper.get_head_mode(head_mode))
        elif browser == "chromium":
            browser = playwright.chromium.launch(headless=PlaywrightHelper.get_head_mode(head_mode))
        return browser

    @staticmethod
    def get_context(browser, str_locale):
        context = browser.new_context(locale=str_locale, viewport ={"width":1920,"height":1080})
        # context = browser.new_context(locale=str_locale, viewport ={"width":1280,"height":1084})
        # context = browser.new_context(locale=str_locale)
        return context

    @staticmethod
    def get_page(context) -> Page:
        page = context.new_page()
        return page

    # @staticmethod
    # def get_basepage(context):
    #     page = PlaywrightHelper.get_page(context)
    #     base_page = BasePage(page)
    #     return base_page

    # @staticmethod
    # def init_create_base_page(playwright):
    #     browser = PlaywrightHelper.get_browser(global_browser,global_head_mode,playwright)
    #     context = PlaywrightHelper.get_context(browser,global_locale)
    #     base_page = PlaywrightHelper.get_basepage(context)
    #     return base_page,context,browser
    @staticmethod
    def init_create_page(playwright):
        browser = PlaywrightHelper.get_browser(global_browser, global_head_mode, playwright)
        context = PlaywrightHelper.get_context(browser, global_locale)
        page = context.new_page()
        return page, context, browser
