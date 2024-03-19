from playwright.sync_api import Playwright, sync_playwright
from src.Pages.Common.login_page import LoginPage
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Helper.playwright_helper import PlaywrightHelper
from src.Pages.StudioNext.Top.top_right_toolbar import *
import time

from src.Utilities.enums import TopMenuItem, AccordionType


def run(pw: Playwright) -> None:
    pw_objects = PlaywrightHelper.init_create_page(pw)
    page = pw_objects[0]
    context = pw_objects[1]
    browser = pw_objects[2]
    login = LoginPage(page)
    login.login_studionext()

    studionext_base = TopMenuPage(page)
    studionext_base.new_item(TopMenuItem.new_sas_program)
    studionext_base.new_item(TopMenuItem.new_python_program)
    studionext_base.new_item(TopMenuItem.new_flow)
    studionext_base.new_item(TopMenuItem.new_query)
    studionext_base.new_item(TopMenuItem.new_custom_step)
    studionext_base.new_item(TopMenuItem.new_quick_import)
    studionext_base.new_item(TopMenuItem.new_file_types_json)
    studionext_base.new_item(TopMenuItem.new_job_definition)
    studionext_base.new_item(TopMenuItem.new_file_types_json)
    studionext_base.new_item(TopMenuItem.new_file_types_text)
    studionext_base.new_item(TopMenuItem.new_file_types_xml)
    studionext_base.new_item(TopMenuItem.new_file_types_workspace)

    acc: AccordionPage = AccordionPage(page)

    acc.show_accordion(AccordionType.open_item)
    time.sleep(1)
    acc.show_accordion(AccordionType.sas_server)
    time.sleep(1)
    acc.show_accordion(AccordionType.sas_content)
    time.sleep(1)
    acc.show_accordion(AccordionType.steps)
    time.sleep(1)
    acc.show_accordion(AccordionType.snippets)
    time.sleep(1)
    acc.show_accordion(AccordionType.libraries)
    time.sleep(1)
    acc.show_accordion(AccordionType.git)
    time.sleep(1)
    acc.show_accordion(AccordionType.sas_server)
    time.sleep(1)

    top_right = TopRightToolbar(page)
    top_right.click_sign_out()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
