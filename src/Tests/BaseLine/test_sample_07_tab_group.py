"""
File: test_sample_07_tab_group.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 9:34 
"""

import time

from src.Pages.StudioNext.Left.library_page import LibraryPage
from src.Pages.StudioNext.Left.openitems_page import OpenItemsPage
from src.Pages.StudioNext.Left.sas_content_server_page import SASContentServerPage
from src.Pages.StudioNext.Left.sasserver_page import SASServerPage
from src.Pages.StudioNext.Left.sascontent_page import SASContentPage

from src.conftest import *
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem, AccordionType


def test_init(page, init):
    PageHelper.init_environments(page)


def test_00_click_show_tab_labels(page, init):
    """

    :param page:
    :param init:
    :return:
    """

    # PageHelper.click_options(page, TopMenuItem.options.new_flow)
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_flow)

    flow_page = FlowPage(page)

    # flow_page.tab_group.click_tab_by_title("提交的代码和结果")
    flow_page.tab_group.click_tab_by_text("提交的代码和结果")
    flow_page.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA)

    # time.sleep(3)
    flow_page.tab_group.click_lower_right_show_corner_tab_labels_btn()

    time.sleep(3)
    flow_page.tab_group.click_lower_left_corner_show_tab_labels_btn()


def test_01_show_accordion_tab_labels(page, init):
    """
    Create a flow, and click the show tab labels in the lower left corner.
    NOTE: Unlike the testcase implemented already, this one
    :param page:
    :param init:
    :return:
    """
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_flow)

    flow_page = FlowPage(page)

    # WORKS FINE
    # PageHelper.show_accordion_tab_labels(page)

    # WORKS FINE
    # PageHelper.show_accordion_tab_labels(flow_page)

    # Click Accordions
    PageHelper.show_accordion(page, AccordionType.libraries)
    PageHelper.show_all_accordion(page)

    time.sleep(3)
    # Click show tab labels in the right corner
    flow_page.tab_group.click_lower_right_show_corner_tab_labels_btn()


def test_02_show_accordion_tab_labels(page, init):
    """
    Create a Custom Step and click the show tab labels button
    :param page:
    :param init:
    :return:
    """
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_custom_step)

    custom_step_page = CustomStepPage(page)

    custom_step_page.tab_group.click_lower_right_show_corner_tab_labels_btn()
    time.sleep(3)

    custom_step_page.tab_group.click_tab_by_text("提示层次")
    time.sleep(3)

    custom_step_page.tab_group.click_tab_by_text("端口详细信息")
    time.sleep(3)

    custom_step_page.tab_group.click_tab_by_text(Helper.data_locale.PROPERTIES)


@pytest.mark.xfail(reason="Disabled [Refresh] [Upload] [Properties] & [Delete] button")
def test_03_disabled_buttons_above_header(page, init):
    """
    """
    PageHelper.show_accordion(page, AccordionType.libraries)

    lib_pane = LibraryPage(page)
    lib_pane.wait_for_page_load()

    lib_pane.properties_btn()
    lib_pane.delete_btn()

    PageHelper.show_accordion(page, AccordionType.open_item)

    open_pane = OpenItemsPage(page)
    open_pane.wait_for_page_load()

    open_pane.btn_saveall()

    PageHelper.show_accordion(page, AccordionType.sas_server)

    server_pane = SASContentServerPage(page)
    server_pane.wait_for_page_load()

    server_pane.click_delete_selection_btn()
    SASServerPage(page).click_upload_to_server_btn()
    server_pane.click_refresh_selection_btn()
    server_pane.click_properties_btn()

    PageHelper.show_accordion(page, AccordionType.sas_content)

    content_pane = SASContentServerPage(page)
    content_pane.wait_for_page_load()

    content_pane.click_delete_selection_btn()
    SASContentPage(page).click_upload_to_content_btn()
    content_pane.click_refresh_selection_btn()
    content_pane.click_refresh_selection_btn()



