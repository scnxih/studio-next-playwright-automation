"""
File: test_sample_08_reset_perspective.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 10:04 
"""
import time
from src.Helper.page_helper import PageHelper

from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem


def test_00_reset_view(page, init):
    """
    Reset View Perspective before testcase run
    :param page:
    :param init:
    :return:
    """
    pass
    # Comment this method since Change perspective in options is missing now. Will recover it once the problem is fixed.
    # top_menu = TopMenuPage(page)
    # time.sleep(3)
    # top_menu.click_options(TopMenuItem.options.options_change_perspective_interactive)
    # time.sleep(3)
    # top_menu = TopMenuPage(page)
    # time.sleep(3)
    # top_menu.click_options(TopMenuItem.options.options_change_perspective_standard)
    # time.sleep(3)
    # top_menu = TopMenuPage(page)
    # time.sleep(3)
    # top_menu.click_options(TopMenuItem.options.options_change_perspective_standard)


def test_01_reset_view_pagehelper(page, init):
    """
    Test perspective-reset function in PageHelper
    :param page:
    :param init:
    :return:
    """
    PageHelper.switch_to_interactive_perspective(page)
    PageHelper.switch_to_standard_perspective(page)
