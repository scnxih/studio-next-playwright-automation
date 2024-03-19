"""
File: test_sample_12_navigation_pane.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/27 11:28 
"""
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar

from src.Utilities.enums import SettingsTabPages


def test_01_click_tab_pages_via_navigation_pane(page, init):
    """
    Test tab-page navigation by using encapsulated navigation pane
    :param page:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: First switch to other tab pages to verify normality
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    # Step-3: Click Global/General via encapsulated navigation pane
    setting_dialog.switch_to_global_general_via_navigation_pane()
    setting_dialog.select_theme("深色")

    setting_dialog.switch_to_sas_studio_general_via_navigation_pane()

    setting_dialog.select_tab_type_after_submission("输出数据")

    # Step-4: Close the dialog
    setting_dialog.reset_query()
    setting_dialog.close_dialog()


def test_02_count_expand_icons(page, init):
    """
    Test counting the number of expand icons
    :param page:
    :param init:
    :return:
    """

    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Count the number of expand icons
    setting_dialog.get_number_of_expanded_icons()

    setting_dialog.close_dialog()


def test_03_expand_collapse_icons(page, init):
    """
    Test collapse and expand icons
    :param page:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Collapse all tree items
    setting_dialog.collapse_all()

    # Step-3: Expand all
    setting_dialog.expand_all()

    # Step-4: Count the number of expand icons
    setting_dialog.get_number_of_expanded_icons()
    setting_dialog.close_dialog()


def test_04_iterate_thru_tree_items(page, init):
    """
    Tried to iterate thru tree-items.
    :param pange:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: Collapse all tree items
    setting_dialog.collapse_all()

    # Step-3: Expand all
    setting_dialog.expand_all()

    # Step-4: Count the number of expand icons
    setting_dialog.iterate_thru_treeitems()

    # Step-5: Close the Settings dialog
    setting_dialog.close_dialog()


def test_05_reset_settingds_with_iteration(page, init):
    """

    :param page:
    :param init:
    :return:
    """
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-2: First switch to other tab pages to verify normality
    setting_dialog.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)
    setting_dialog.uncheck_checkbox("输入格式")

    # Step-3: Click Global/General via encapsulated navigation pane
    setting_dialog.switch_to_global_general_via_navigation_pane()
    setting_dialog.select_theme("深色")

    setting_dialog.switch_to_sas_studio_general_via_navigation_pane()

    setting_dialog.select_tab_type_after_submission("输出数据")

    # Step-4: Close the dialog
    setting_dialog.close_dialog()

    # Step-5: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting_dialog = SettingsDialog(page)

    # Step-6: Reset during iteration
    setting_dialog.reset_settings_via_iteration()

    # Step-7: Close the dialog
    setting_dialog.close_dialog()
