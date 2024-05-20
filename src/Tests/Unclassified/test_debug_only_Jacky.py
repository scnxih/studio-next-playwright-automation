import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import ManageGitConnectionDialog
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import ManageShortcutsDialog
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Dialog.settings_dialog_just_for_test import SettingsDialogTest
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import TopMenuItem, AccordionType
from src.Utilities.enums import SettingsTabPages
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import FlowNodeType


def test_00_click_show_tab_lables(page, init):
    """
    Test commitment after switching git account.
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
    PageHelper.show_accordion_tab_labels(flow_page)

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


def test_03_reset_view(page, init):
    """
    Reset View Perspective before testcase run
    :param page:
    :param init:
    :return:
    """
    top_menu = TopMenuPage(page)
    time.sleep(3)
    top_menu.click_options(TopMenuItem.options.options_change_perspective_interactive)
    time.sleep(3)
    top_menu = TopMenuPage(page)
    time.sleep(3)
    top_menu.click_options(TopMenuItem.options.options_change_perspective_standard)
    time.sleep(3)
    top_menu = TopMenuPage(page)
    time.sleep(3)
    top_menu.click_options(TopMenuItem.options.options_change_perspective_standard)


def test_04_reset_view_pagehelper(page, init):
    """
    Test perspective-reset function in PageHelper
    :param page:
    :param init:
    :return:
    """
    PageHelper.switch_to_interactive_perspective(page)
    PageHelper.switch_to_standard_perspective(page)


def test_05_reset_preference_dialog(page, init):
    """

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
    # setting_dialog.tab_page(page, "General")

    setting_dialog.click_reset_button()

    # Disable temporarily
    """
    
    # Switch to other tab pages
    if setting.is_open():
        setting.click_tab("辅助功能")

    setting_dialog.click_reset_button()

    # Switch to other tab pages
    if setting.is_open():
        setting.click_tab("查询")

    setting_dialog.click_reset_button()
    
    """
    setting_dialog.close_dialog()


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


def test_08_reset_region_and_language_settings(page, init):
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
    setting_dialog.close_dialog()


def test_09_none_modification_settings(page, init):
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


def test_10_reset_region_and_language_settings(page, init):
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


def test_11_reset_sas_studio_general_settings(page, init):
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


def test_12_reset_sas_studio_query_settingds(page, init):
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


def test_13_click_global_general_via_aria_xpath(page, init):
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


def test_14_click_sas_studio_general_via_aria_xpath(page, init):
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


def test_15_click_tab_pages_via_aria_composation(page, init):
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


def test_16_click_tab_pages_via_aria_composition(page, init):
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


def test_17_click_tab_pages_via_navigation_pane(page, init):
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


def test_18_count_expand_icons(page, init):
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


def test_19_expand_collapse_icons(page, init):
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


def test_20_iterate_thru_tree_items(page, init):
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


def test_21_reset_settingds_with_iteration(page, init):
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


def test_22_learn_flow_canvas_operations(page, init):
    """
    Learn APIs for flow canvas operation
    :param page:
    :param init:
    :return:
    """

    # Create a flow from top menu
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a node from 'Add' drop-down list, similiar for those implemented underneath
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.file)
    flow.add_node(FlowNodeType.branch_rows)
    flow.add_node(FlowNodeType.calculate_columns)
    # flow.add_node(FlowNodeType.sas_program)
    # flow.add_node(FlowNodeType.execute_decisions)
    # flow.add_node(FlowNodeType.export)
    # flow.add_node(FlowNodeType.filter_rows)
    # flow.add_node(FlowNodeType.implement_scd)
    # flow.add_node(FlowNodeType.import_data)
    # flow.add_node(FlowNodeType.insert_rows)
    # flow.add_node(FlowNodeType.load_table)
    # flow.add_node(FlowNodeType.manage_columns)
    # flow.add_node(FlowNodeType.merge_table)
    # flow.add_node(FlowNodeType.python_program)
    # flow.add_node(FlowNodeType.query)
    # flow.add_node(FlowNodeType.sort)
    # flow.add_node(FlowNodeType.union_rows)
    # flow.add_node(FlowNodeType.notes)

    # Manipulate nodes in flow canvas by using javascript
    select_node_in_flow_canvas(page, Helper.data_locale.TABLE)
    time.sleep(1)


    select_node_in_flow_canvas(page, Helper.data_locale.FILE)
    time.sleep(1)
    select_node_in_flow_canvas(page, Helper.data_locale.BRANCH_ROWS)
    time.sleep(1)
    select_node_in_flow_canvas(page, Helper.data_locale.CALCULATE_COLUMNS)
    time.sleep(1)

def test_23_column_resolution_load_table(page, init):
    """
    Learn by implementing testcase for 'Column Resolution tab for Load Table'
    URL: https://rndjira.sas.com/browse/SASSTUDIO-29697

    :param page:
    :param init:
    :return:
    """
    # Step-1: Create a new flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Step-2: Add a 'Table' & 'Load Table' node to flow canvas
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.load_table)

    # Manipulate nodes in flow canvas by using javascript
    select_node_in_flow_canvas(page, Helper.data_locale.TABLE)
    time.sleep(1)

    link_two_nodes_in_flow(page, Helper.data_locale.TABLE, Helper.data_locale.LOAD_TABLE)

    flow.arrange_nodes()

def test_24_flow_canvas_node_context_menu(page, init):
    """
    Learn to use context menu of node in flow canvas
    :param page:
    :param init:
    :return:
    """
    # Step-1: Create a new flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Step-2: Add a 'Table' node to flow canvas
    flow.add_node(FlowNodeType.table)

    # Step-3: Delete the node
    select_node_in_flow_canvas(page, Helper.data_locale.TABLE)
    open_context_menu_for_the_node_in_flow(page, Helper.data_locale.TABLE)
    time.sleep(1)

    # NOTE: Exact has to be added otherwise would NOT work
    page.get_by_text(Helper.data_locale.DELETE, exact=True).click()

def test_25_flow_canvas_multiple_nodes_context_menu(page, init):
    """

    :param page:
    :param init:
    :return:
    """
    # Step-1: Create a new flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Step-2: Add a 'Table' & 'Load Table' node to flow canvas
    flow.add_node(FlowNodeType.load_table)

    # Step-3: Try to use context menu
    # The following auto-arrange MUST be added, otherwise context menu operation would NOT work
    flow.arrange_nodes()

    select_node_in_flow_canvas(page, Helper.data_locale.LOAD_TABLE)
    open_context_menu_for_the_node_in_flow(page, Helper.data_locale.LOAD_TABLE)
    time.sleep(1)

    # Step-4: Copy the node
    page.get_by_text(Helper.data_locale.COPY).click()
    time.sleep(1)
    #
    open_context_menu_for_canvas_in_flow(page)
    time.sleep(1)

    # Step-5: Paste the node
    page.get_by_text(Helper.data_locale.PASTE).click()
    # time.sleep(1)

    # Step-6: Delete the node

    select_node_in_flow_canvas(page, Helper.data_locale.LOAD_TABLE)
    open_context_menu_for_the_node_in_flow(page, Helper.data_locale.LOAD_TABLE)
    time.sleep(1)

    page.get_by_text(Helper.data_locale.DELETE, exact=True).click()
    # page.get_by_text(Helper.data_locale.CUT).click()
    time.sleep(1)

    flow.view_expand_all_ports()
    time.sleep(2)
    flow.view_collapse_all_ports()
    time.sleep(2)

    flow.show_over_view_map()
    time.sleep(2)
    flow.hide_over_view_map()
    time.sleep(2)

    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    flow.saveas(folder_path, "test_flow.sas", True, True)

    # Flow Toolbar by obtaining xpath
    flow.copy_step()
    flow.paste_step()

    flow.cut_step()

    flow.undo()
    flow.redo()

    flow.schedule_as_job()
    flow.add_to_my_favorites()

    flow.apply_detail_layout_horizontal()
    time.sleep(1)
    flow.apply_detail_layout_vertical()
    time.sleep(1)

    flow.apply_main_layout_vertical()
    time.sleep(1)
    flow.apply_main_layout_standard()
    time.sleep(1)
    flow.apply_main_layout_horizontal()
    time.sleep(1)

    flow.reload()
    time.sleep(1)


def test_26_mask_time_in_log(page, init):
    """
    Run a *.sas program, then open summary/code/log/results/listing in a new tab.
    """
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")
    editor.format_program()
    editor.run(True)

    time.sleep(1)

    # Click log tab page
    editor.tab_group.click_tab_by_text(Helper.data_locale.LOG)

    '''
    WholePage(page).screenshot_self("sas_whole")

    CenterPage(page).screenshot_self("center")

    CenterPage(page).screenshot_self("center_with_mask",
                                     mask=[CenterPage(page).toolbar.btn_by_title(Helper.data_locale.RUN)],
                                     mask_color="#000000")

    CenterPage(page).screenshot_self("center_with_mask2",
                                     mask=['//span[@class="mtk25"][contains(text(),"cpu")]/../../'],
                                     mask_color="#000000")

    CenterPage(page).screenshot_self("real_time",
                                     mask=[CenterPage(page).page.get_by_text("实际时间")],
                                     mask_color="#000000")

    CenterPage(page).screenshot_self("cpu_time",
                                     mask=[CenterPage(page).page.get_by_text("CPU 时间")],
                                     mask_color="#000000")
    '''

    CenterPage(page).screenshot_self("times",
                                     mask=[CenterPage(page).page.get_by_text("实际时间"),
                                           CenterPage(page).page.get_by_text("CPU 时间")],
                                     mask_color="#000000")

def test_27_mask_time_infor_in_dialogs(page, init):
    top_menu_page: TopMenuPage = TopMenuPage(page)
    top_menu_page.click_options(TopMenuItem.options_autoexec_file)
    time.sleep(1)
    auto = AutoexecDialog(page)
    auto.screenshot_self("auto_code")

    # put in code
    auto.type_codes("proc print data = sashelp.class;\n run;")

    # run
    auto.run()

    # wait 0.5 sec
    time.sleep(0.5)
    auto.click_tab_log()

    # Mask the time info and take screenshots
    time.sleep(0.5)
    auto.screenshot_self("auto_log",
                         mask=['//div[@data-testid="autoexecLogViewer-detail"]//span[@class="mtk25"][contains(text(),"CPU")]',
                               '//div[@data-testid="autoexecLogViewer-detail"]//span[@class="mtk25"][contains(text(),"实际")]'],
                         mask_color="#000000")

    auto.screenshot_self("auto_log2",
                         mask=auto.time_info_in_log_tab2,
                         mask_color="#123456")

    auto.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_custom_code)
    time.sleep(1)
    cus = CustomCodeDialog(page)

    cus.tab_preamble.click()
    cus.type_codes_in_preamble("proc print data = sashelp.class;\n run;")
    cus.run()

    cus.screenshot_self("custom_pre")

    cus.click_tab_postamble()

    time.sleep(0.5)
    cus.screenshot_self("custom_post")
    cus.click_tab_option()

    time.sleep(0.5)
    cus.screenshot_self("custom_options")
    cus.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_manage_git_connections)
    git = ManageGitConnectionDialog(page)
    time.sleep(0.5)
    git.screenshot_self("git_profile")
    git.click_tab_repository()
    git.screenshot_self("git_repository")
    git.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_manage_keyboard_shortcuts)
    short = ManageShortcutsDialog(page)
    short.screenshot_self("shortcut")
    short.close_dialog()
