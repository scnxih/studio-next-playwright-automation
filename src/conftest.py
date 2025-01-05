import sys, os

from src.Utilities.enums import TopMenuItem, AccordionType

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from src.Helper.playwright_helper import PlaywrightHelper
from src.Helper.page_helper import PageHelper
from playwright.sync_api import sync_playwright

""" Added by Jacky(ID: jawang) on Sept. 1st, 2023 """
from src.Helper.helper import *

""" Added by Jacky(ID: jawang) on Sept. 1st, 2023 """


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as playwright:
        pw_objects = PlaywrightHelper.init_create_page(playwright)
        page = pw_objects[0]
        context = pw_objects[1]
        browser = pw_objects[2]
        yield page
        # PageHelper.init_environments(page)
        PageHelper.sign_out(page)
        page.close()
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def init(page):
    PageHelper.login(page)
    ''' Added by Jacky(ID: jawang) on Sept. 4th, 2023 '''

    # output_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../..")), "Output\\")
    output_path = "C:\\studio-next-playwright-automation\\src\\Output\\"
    testfile_abbreviation = Helper.get_testfile_abbreviation()

    testmethod_number = Helper.get_testmethod_number()

    # FORMULA:
    # screenshot_file_base = output_path + "\\" + testfile_abbreviation + "_" + testmethod_number + "\\" + testfile_abbreviation + "_" + testmethod_number + "_" + class_name + "_" + pic_name

    if os.path.exists(Helper.get_storage_path(output_path, testfile_abbreviation, testmethod_number)):
        Helper.delete_folder(Helper.get_storage_path(output_path, testfile_abbreviation, testmethod_number))

    Helper.create_folder(Helper.get_storage_path(output_path, testfile_abbreviation, testmethod_number), True)
    Helper.logger.debug("Created folder:" + Helper.get_storage_path(output_path, testfile_abbreviation,
                                                                    testmethod_number) + " in fixture")

    ''' Added by Jacky(ID: jawang) on Sept. 4th, 2023 '''
    PageHelper.close_license_warning(page)
    PageHelper.close_all_tabs(page)
    """Added by Alice on 2024/03/22 start"""
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_file_references)
    PageHelper.show_accordion(page, AccordionType.open_item)
    """Added by Alice on 2024/03/22 end"""
