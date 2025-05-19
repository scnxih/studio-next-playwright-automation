"""
File: test_sample_10_reset_settings.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 10:34 
"""

import time

import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Dialog.settings_dialog_just_for_test import SettingsDialogTest

from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import SettingsTabPages
from playwright.sync_api import Page, expect


def test_init(page, init):
    PageHelper.init_environments(page)


@pytest.mark.xfail(reason="Disabled [Reset] button in Settings dialog")
def test_00_default_reset_btn_status(page, init):
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()

    settings_dialog = SettingsDialog(page)

    # Step-2: Check [Reset] button status
    expect(settings_dialog.enabled_reset_btn_in_current_tab_page).to_be_enabled(enabled=True, timeout=3000)


def test_01_reset_preference_dialog(page, init):
    """
    Change the language in Settings dialog and reset afterward
    :param page:
    :param init:
    :return:
    """

    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting = SettingsDialogTest(page)

    # Step-2: Change language
    if setting.is_open():
        setting.click_tab("区域和语言")
        setting.select_language("日语 (日本) - 日本語 (日本)‎")
        setting.select_offline_language("阿拉伯语 (巴林) - العربية (البحرين)‏")

    # Step-3: Reset change above
    setting_dialog = SettingsDialog(page)
    setting_dialog.click_reset_button()

    # Step-4: Close Settings dialog
    setting_dialog.close_dialog()


def test_02_none_modification_settings(page, init):
    """
    Test if the reset method can work well if no modification has been made
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

    # Step-4: Reset Global/General tab page
    setting_dialog.reset_global_general()

    # Step-5: Close the setting dialog
    setting_dialog.close_dialog()


def test_03_reset_region_and_language_settings(page, init):
    """
    Reset settings in 'Region and Language' tab page
    :param page:
    :param init:
    :return:
    """
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting = SettingsDialogTest(page)
    if setting.is_open():
        setting.click_tab("区域和语言")
        setting.select_language("日语 (日本) - 日本語 (日本)‎")
        setting.select_offline_language("阿拉伯语 (巴林) - العربية (البحرين)‏")

    # PageHelper.show_settings_dialog(page)
    setting_dialog = SettingsDialog(page)
    setting_dialog.reset_region_and_language()

    # Step-2: Switch to Global/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.code_and_log)
    time.sleep(3)

    # Step-3: Switch to Global/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.global_general)
    time.sleep(3)

    if setting.is_open():
        setting.click_tab("区域和语言")

    setting_dialog.reset_region_and_language()

    setting_dialog.close_dialog()


def test_04_reset_sas_studio_general_settings(page, init):
    """
    Reset settings in 'SAS Studio/General' tab page
    :param page:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Reset before operations
    setting_dialog.reset_global_general()

    # Step-3:
    # Switch to Global/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.global_general)
    setting_dialog.select_theme("深色")

    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.sas_studio_general)
    setting_dialog.select_tab_type_after_submission("输出数据")

    setting_dialog.close_dialog()

    # Step-4: Reset the theme settings
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.global_general)
    setting_dialog.reset_global_general()

    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.sas_studio_general)
    setting_dialog.reset_sas_studio_general()

    # Step-5: Close the dialog
    setting_dialog.close_dialog()


def test_05_reset_sas_studio_query_settings(page, init):
    """

    :param page:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Reset before operations
    setting_dialog.reset_query()

    # Step-3:
    # Switch to Global/General tab page
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    setting_dialog.reset_query()

    # Step-5: Close the dialog
    setting_dialog.close_dialog()
