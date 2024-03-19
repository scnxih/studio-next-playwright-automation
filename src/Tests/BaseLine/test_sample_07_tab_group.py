"""
File: test_sample_07_tab_group.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 9:34 
"""

import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem, AccordionType


def test_00_click_show_tab_lables(page, init):
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


