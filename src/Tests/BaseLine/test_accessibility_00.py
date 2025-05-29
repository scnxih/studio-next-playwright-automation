import pytest
from playwright.sync_api import Page, expect
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.Query.query_page import QueryPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.conftest import *
from src.Pages.StudioNext.Dialog.about_dialog import AboutDialog

from src.Helper.page_helper import PageHelper
from src.Pages.Common.dialog import Dialog


def test_init(page, init):
    PageHelper.init_environments(page)


# @pytest.mark.xfail(reason='Start page is derived of toolbar')
def test_01_start_page_elements(page, init):
    """

    """
    start_page = PageHelper.show_start_page(page)

    start_page.wait_for_page_load()

    print('Accessibility snapshot tree: ' + str(start_page.page.accessibility.snapshot()["name"]))

    # expect(start_page.page.accessibility.snapshot()).to_be_empty()
    # expect(start_page.page.accessibility).to_be_empty()

    if start_page.page.accessibility.snapshot()["name"] == "SAS® Studio":
        Helper.logger.debug('A11Y App title check passed')
    else:
        Helper.logger.debug('A11Y App title check failed')


@pytest.mark.xfail(reason='Query')
def test_02_query_page_elements(page, init):
    """

    """
    query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)

    query.wait_for_page_load()
    print('Query snapshot tree: ' + str(query.page.accessibility.snapshot()))

    # expect(query.page.accessibility.snapshot()).to_be_empty()
    expect(query.btn_add_table_zero).to_be_focused()


# @pytest.mark.xfail(reason='A11Y Focus')
def test_03_show_about_dialog(page, init):
    """
    A11Y Test of the About dialog
    """
    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_about()
    about_dialog = AboutDialog(page)

    # Step-2: Take the screenshot with mask
    about_dialog.wait_for_page_load()

    # Step-3: Close the dialog
    about_dialog.close_dialog()
    # about_dialog.key_press("Escape")

    #
    # WholePage(page).wait_for_page_load()

    expect(top_right.toolbar.div_by_title(Helper.data_locale.USER_OPTION)).to_be_focused()
    # expect(top_right.toolbar.div_by_title(Helper.data_locale.USER_OPTION)).not_to_be_focused()


def test_04_whats_new_dialog(page, init):
    """
    A11Y Test of the About dialog
    """
    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_new_features()
    whats_new_dialog = Dialog(page)

    whats_new_dialog.page.wait_for_load_state("load")
    expect(whats_new_dialog.page.locator("//div[@role='dialog']//span[contains(text(), 'SAS')]")).to_contain_text("新功能")

    # whats_new_dialog.wait_for_page_load()
    # whats_new_dialog.key_press("Escape")

    whats_new_dialog.close_dialog()
