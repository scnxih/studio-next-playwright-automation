"""
File: test_sample_09_switch_settings_tab.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 10:15 
"""

import time

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar

from src.Utilities.enums import SettingsTabPages

def test_init(page,init):
    PageHelper.init_environments(page)

def test_06_switch_to_global_general_tab_page(page, init):
    """
    Switch to Global/General tab page
    :param page:
    :param init:
    :return:
    """

    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Switch to Global/General tab page
    setting_dialog.click_tab_page(page, SettingsTabPages.code_and_log)
    time.sleep(1)

    # Step-3: Switch to Global/General tab page
    setting_dialog.switch_to_global_general()
    time.sleep(1)

    # Step-4: Switch to SAS Studio/General tab page
    setting_dialog.switch_to_sas_studio_general()
    time.sleep(1)

    setting_dialog.close_dialog()


def test_07_switch_to_all_tab_pages(page, init):
    """
    Test switch to tab page methods
    NOTE: Two General tab pages are hard-coded, whereas other tab pages are accesed through tab page text.
    :param page:
    :param init:
    :return:
    """
    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Switch to Global/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.code_and_log)
    time.sleep(3)

    # Step-3: Switch to Global/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.global_general)
    time.sleep(3)

    # Step-4: Switch to SAS Studio/SAS Programs/Results tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.results)
    time.sleep(3)

    # Step-5: Switch to SAS Studio/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.sas_studio_general)
    time.sleep(3)

    # Step-6: Switch to SAS Studio/query tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    time.sleep(3)

    setting_dialog.close_dialog()

