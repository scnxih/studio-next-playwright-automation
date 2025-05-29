import pytest
from playwright.sync_api import Page, expect

from src.Pages.StudioNext.Center.Query.query_page import QueryPage
from src.conftest import *

from src.Helper.page_helper import PageHelper


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

