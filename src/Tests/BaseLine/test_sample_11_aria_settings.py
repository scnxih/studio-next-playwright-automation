"""
File: test_sample_11_aria_settings.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 11:04 
"""
import time

from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import SettingsTabPages


def test_01_click_global_general_via_aria_xpath(page, init):
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
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    setting_dialog.switch_to_sas_studio_general_via_aria()
    setting_dialog.select_tab_type_after_submission("输出数据")

    # Step-5: Close the dialog
    setting_dialog.close_dialog()


def test_02_click_sas_studio_general_via_aria_xpath(page, init):
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
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    setting_dialog.switch_to_global_general_via_aria()
    setting_dialog.select_theme("深色")

    # Step-5: Close the dialog
    setting_dialog.close_dialog()


def test_03_click_tab_pages_via_aria_composation(page, init):
    """
    Test aria-combination in Settingds dialog
    :param page:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Reset before operations
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    # setting_dialog.switch_to_global_general_via_aria()
    setting_dialog.switch_to_tab_page_via_aria(setting_tab_page=SettingsTabPages.global_general)
    setting_dialog.select_theme("深色")

    # setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.sas_studio_general)
    setting_dialog.switch_to_tab_page_via_aria(setting_tab_page=SettingsTabPages.sas_studio_general)
    setting_dialog.select_tab_type_after_submission("输出数据")

    # Step-2: Switch to Global/General tab page
    # setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.code_and_log)
    setting_dialog.switch_to_tab_page_via_aria(setting_tab_page=SettingsTabPages.code_and_log)
    time.sleep(3)

    # Step-5: Close the dialog
    setting_dialog.close_dialog()


def test_04_click_tab_pages_via_aria_composition(page, init):
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Reset before operations
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    # setting_dialog.switch_to_global_general_via_aria()
    # setting_dialog.switch_to_tab_page_via_aria(setting_tab_page=SettingsTabPages.global_general)
    setting_dialog.switch_to_tab_page_aria_xpath_dict(setting_tab_page=SettingsTabPages.global_general)
    setting_dialog.select_theme("深色")

    # setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.sas_studio_general)
    # setting_dialog.switch_to_tab_page_via_aria(setting_tab_page=SettingsTabPages.sas_studio_general)
    setting_dialog.switch_to_tab_page_aria_xpath_dict(setting_tab_page=SettingsTabPages.sas_studio_general)
    setting_dialog.select_tab_type_after_submission("输出数据")

    # Step-2: Switch to Global/General tab page
    # setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.code_and_log)
    # setting_dialog.switch_to_tab_page_via_aria(setting_tab_page=SettingsTabPages.code_and_log)
    setting_dialog.switch_to_tab_page_aria_xpath_dict(setting_tab_page=SettingsTabPages.code_and_log)
    time.sleep(3)

    setting_dialog.reset_query()

    # Step-5: Close the dialog
    setting_dialog.close_dialog()

