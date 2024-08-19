import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.branch_rows_pane import BranchRowsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.filter_rows_pane import FilterRowsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.manage_columns_pane import ManageColumnsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import ManageGitConnectionDialog
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import ManageShortcutsDialog
# from src.Pages.StudioNext.Dialog.select_a_column_dialog import SelectColumnDialog
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Dialog.settings_dialog_just_for_test import SettingsDialogTest
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import TopMenuItem, AccordionType
from src.Utilities.enums import SettingsTabPages
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import FlowNodeType
from src.Pages.Common.dialog import Dialog, Alert
# from src.Pages.StudioNext.Dialog.select_a_column_dialog import SelectColumnDialog
from src.Pages.StudioNext.Center.Flow.DetailsPane.load_table_pane import LoadTablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.same_birthday_pane import SameBirthdayProbabilityPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.box_plot_pane import BoxPlotPane

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


def test_27_mask_time_info_in_dialogs(page, init):
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
                         mask=[
                             '//div[@data-testid="autoexecLogViewer-detail"]//span[@class="mtk25"][contains(text(),"CPU")]',
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


def test_28_autoexec_dialog_scroll_bars(page, init):
    """
    Test editor Autoexec editor
    :param page:
    :param init:
    :return:
    """
    text = """
    
        proc means data=sashelp.class maxdec=2 fw=10 printalltypes;
           class Sex;
           var Height;
           title 'Descriptive Statistics Using PROC MEANS';
        run;
        title;
        
        ods graphics on /width=600 ;
        ods select histogram probplot;
        
        * Using SAS to Picture Your Data;
        
        proc univariate data=sashelp.class;
           var Height;
           id Name;
           histogram Height / normal(mu=est sigma=est)  NMIDPOINTS=8;
           inset skewness kurtosis / position=ne;
           probplot Height / normal(mu=est sigma=est);
           inset skewness kurtosis;
           title 'Descriptive Statistics Using PROC UNIVARIATE';
        run;
        title;
        
        proc means data=sashelp.class maxdec=2 fw=10 printalltypes n mean median std 
                var max min q1 q3;
            var Height;
            title 'Selected Descriptive Statistics for Height';
        run;
        
        title;

    """

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    autoexec_editor = PageHelper.create_plain_editor_factory().create_editor("autoexec", page)
    autoexec_editor.fill_text_area_with(text)

    autoexec_dialog = AutoexecDialog(page)

    autoexec_dialog.click_tab_log()

    autoexec_dialog.run()

    time.sleep(10)

    if autoexec_dialog.btn_run.is_enabled():
        # autoexec_dialog.screenshot_self('AutoDlg')
        autoexec_dialog.screenshot_self('AutoDlg',
                                        mask=autoexec_dialog.scroll_bar,
                                        mask_color="#01651F")

    autoexec_dialog.save()


def test_29_custom_dialog_scroll_bars(page, init):
    """
    Test code editor in Custom Code dialog
    :param page:
    :param init:
    :return:
    """

    text = '''
    proc print data=sashelp.class;
    run;
    '''

    PageHelper.click_options(page, TopMenuItem.options_custom_code)
    custom_code_editor = PageHelper.create_plain_editor_factory().create_editor("custom", page)
    custom_code_editor.fill_text_area_with(text)
    #
    custom_code_dialog = CustomCodeDialog(page)
    custom_code_dialog.run()
    custom_code_dialog.save()


def test_30_flow_manage_columns(page, init):
    """
    Test Manage Columns in flow
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.manage_columns)
    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.MANAGE_COLUMNS)

    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.MANAGE_COLUMNS)

    manage_columns = ManageColumnsPane(page)
    manage_columns.add_all_columns()
    time.sleep(3)
    manage_columns.remove_all_columns()

    list1 = ["Sex", "Name"]
    manage_columns.add_columns_by_double_click(list1)

    manage_columns.remove_all_columns()

    list2 = ["Age", "Height"]
    manage_columns.add_columns_by_toolbar_button(list2)

    manage_columns.remove_all_columns()

    list3 = ["Weight"]
    # manage_columns.add_columns_by_context_menu(list3, "添加列")
    manage_columns.add_columns_by_context_menu(list3)

    manage_columns.new_column_expression_builder()


def test_31_flow_manage_columns(page, init):
    """
    Test Manage Columns in flow
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.manage_columns)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.MANAGE_COLUMNS)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.MANAGE_COLUMNS)

    manage_columns = ManageColumnsPane(page)
    manage_columns.add_all_columns()

    manage_columns.move_column_to_the_top("Sex")

    manage_columns.move_column_to_end("Age")

    manage_columns.remove_selected_column("Height")

    manage_columns.move_up_column_by_context_menu("Age")


def test_32_flow_manage_columns(page, init):
    """
    Test Manage Columns in flow
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.manage_columns)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.MANAGE_COLUMNS)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.MANAGE_COLUMNS)

    manage_columns = ManageColumnsPane(page)
    manage_columns.add_all_columns()

    print("The total number of column rows is: " + str(manage_columns.count_total_number_of_column_rows()))

    manage_columns.page.click(manage_columns.last_column)
    manage_columns.page.press(manage_columns.last_column, key='Delete')

    manage_columns.remove_all_columns()
    manage_columns.add_all_columns()


def test_33_branch_rows(page, init):
    """
    Branch rows.
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.branch_rows)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.BRANCH_ROWS)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.BRANCH_ROWS)

    branch_rows = BranchRowsPane(page)
    branch_rows.select_a_column()

    # select_column_dialog = SelectColumnDialog(page)
    # select_column_dialog.select_a_column_and_OK("Sex")


def test_33_filter_rows(page, init):
    """
    Filter rows.
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.filter_rows)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.FILTER_ROWS)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.FILTER_ROWS)

    filter_rows = FilterRowsPane(page)
    filter_rows.add_a_row()
    filter_rows.select_a_column("Sex")

    # Dialog(page, title=Helper.data_locale.SELECT_A_COLUMN).screenshot_self('select_a_col')
    # Dialog(page, title=Helper.data_locale.SELECT_A_COLUMN).close_dialog()

    filter_rows.set_filter_value()
    filter_rows.cancel_and_close_add_filter_dialog()


def test_34_filter_rows(page, init):
    """
    Test Flow/Filter Rows/Add Filter dialog
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.filter_rows)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.FILTER_ROWS)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.FILTER_ROWS)

    filter_rows = FilterRowsPane(page)
    filter_rows.select_a_column("Sex")

    filter_rows.set_condition_to("等于", "M")

    flow.run(True)


def test_35_load_table(page, init):
    """
    Test Flow/Load Table
    """
    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.load_table)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.LOAD_TABLE)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table = LoadTablePane(page)
    # load_table.tab_group.click_tab_by_text("目标表")
    # load_table.tab_group.click_tab_by_text("列结构")
    # load_table.set_load_technique()
    load_table.set_target_library('work')


def test_36_load_table_source_target(page, init):
    """
    Test Flow/Load Table
    """
    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area("data work.out_class;set SASHELP.'CLASS'n;run;")
    sas_program.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.load_table)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.LOAD_TABLE)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table = LoadTablePane(page)
    # load_table.tab_group.click_tab_by_text("目标表")
    # load_table.tab_group.click_tab_by_text("列结构")
    load_table.set_load_technique()
    load_table.set_target_library('work')
    load_table.set_target_table('out_class')
    flow.run(True)


def test_37_load_table_column_resolution(page, init):
    """
    Test Flow/Load Table/Column Resolution
    """
    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    # sas_program.editor.type_into_text_area("data work.out_class;set SASHELP.'CLASS'n;run;")

    # SAS Program
    code = """
data work.my_baseball(drop=Name);
    set sashelp.BASEBALL;
    new_column=CrAtBat;
run;
"""

    sas_program.editor.type_into_text_area(code)
    sas_program.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.load_table)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("baseball")
    time.sleep(1)
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.LOAD_TABLE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table = LoadTablePane(page)

    # load_table.set_load_technique()
    load_table.set_target_library('work')
    load_table.set_target_table('my_baseball')

    # load_table.check_column_resolution()
    load_table.filter_successful_mapping()
    load_table.filter_ignored_mapping()
    load_table.filter_informational_mapping()

    flow.run(True)


def test_38_load_table_if_nonexist_create_one(page, init):
    """
    Test Flow/Load Table/Options/If non-exist create one table
    """

    # Set I18N library
    set_autolib_code = """
libname AUTOLIB '/segatest/I18N/Autolib' ;
    """

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    PageHelper.set_autoexec(page, set_autolib_code)

    acc: AccordionPage = AccordionPage(page)
    acc.show_accordion(AccordionType.libraries)

    # Create a sas program and run
    sas_program_code = """
Data Work.'中文测试'n;
	set AUTOLIB.'BASEBALL''中文测试'n;
run;
        """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.load_table)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table.set_library("AUTOLIB")
    time.sleep(1)
    table.set_table("BASEBALL'中文测试")
    time.sleep(1)
    table.refresh_table()
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.LOAD_TABLE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table = LoadTablePane(page)
    load_table.set_node_name(Helper.data_locale.LOAD_TABLE)
    load_table.set_target_library('work')
    load_table.set_target_table('中文测试1')
    load_table.refresh_target_table()

    # Load Table step is incomplete now. Warning message is shown.
    flow.screenshot_self('incomplete_status')
    flow.select_node_status_dialog_of_the_node_in_flow(Helper.data_locale.LOAD_TABLE)
    flow.screenshot_self('incomplete_status_dialog')

    # The column structure is empty
    load_table.check_column_structure()
    load_table.screenshot_self('column_structure_empty')

    # Update  Target Table.
    # Load table step is complete now.
    load_table.set_target_library('work')
    load_table.set_target_table('中文测试')
    load_table.refresh_target_table()

    # Load Table step is incomplete now. Warning message is shown.
    flow.screenshot_self('complete_status')
    flow.select_node_status_dialog_of_the_node_in_flow(Helper.data_locale.LOAD_TABLE)
    flow.screenshot_self('complete_status_dialog')

    # Click Column Structure tab.
    # The column structure is shown correctly
    load_table.check_column_structure()
    load_table.screenshot_self('column_structure_correct')

    # Work-around: Delete table cannot be done at the moment
    load_table.set_target_library('work')
    load_table.set_target_table('中文测试Target')
    load_table.refresh_target_table()

    load_table.check_options()

    # flow run with error
    # flow.run(False)

    flow.select_node_status_dialog_of_the_node_in_flow(Helper.data_locale.LOAD_TABLE)
    flow.screenshot_self('error_status_dialog')

    if not load_table.checkbox_if_not_exist_create_one.is_checked():
        load_table.checkbox_if_not_exist_create_one.set_check()

    load_table.set_target_library('work')
    load_table.set_target_table('中文测试')
    load_table.refresh_target_table()

    # flow run successfully
    flow.run(False)


def test_39_load_table_update(page, init):
    """
    Test Flow/Load Table/Options/If non-exist create one table
    """

    # Set I18N library
    set_autolib_code = """
    libname AUTOLIB '/segatest/I18N/Autolib' ;
        """

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    PageHelper.set_autoexec(page, set_autolib_code)

    # Create a sas program and run
    sas_program_code = """
cas;
caslib _all_ assign;


data CASUSER.'BASEBALL''中文测试'n work.'BASEBALL''中文测试'n;
	set AUTOLIB.'BASEBALL''中文测试'n;
run;
            """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.load_table)

    time.sleep(1)

    table = TablePane(page)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table.set_library("AUTOLIB")
    time.sleep(1)
    table.set_table("BASEBALL'中文测试")
    time.sleep(1)
    table.refresh_table()
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.LOAD_TABLE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table = LoadTablePane(page)
    load_table.set_node_name(Helper.data_locale.LOAD_TABLE)
    load_table.set_target_library('work')
    load_table.set_target_table("BASEBALL'中文测试")
    load_table.refresh_target_table()

    load_table.set_update_rows_for_load_technique()

    # Click 'Add columns' button in 'Options' tab page
    # load_table.button_add_columns()

    # load_table.select_key_column_dialog.select_key_column_grid.click_grid_cell(cell_label='姓名1')
    # load_table.select_key_column_dialog.select_key_column_grid.click_grid_cell('姓名1')
    # load_table.select_key_column_dialog.select_key_column_grid.click_grid_cell(row_index="2", col_index="2")
    # time.sleep(3)
    # load_table.select_key_column_dialog.close_dialog()

    load_table.select_key_column('姓名1')

    # Error
    # load_table.select_key_column("Team'中文")

    # Flow could run successfully
    flow.run(True)

    # Change target table
    load_table.set_target_library('CASUSER')
    load_table.set_target_table("BASEBALL'中文测试")

    load_table.check_options()


def test_40_load_table_truncate_technique(page, init):
    """
    """
    # Set I18N library
    set_autolib_code = """
    libname AUTOLIB '/segatest/I18N/Autolib' ;
        """

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    PageHelper.set_autoexec(page, set_autolib_code)

    # Create a sas program and run
    sas_program_code = """
/* Teradata */
libname teralib teradata server=vat user=nlssort password=nlssort
database=nlssort PRESERVE_COL_NAMES=YES PRESERVE_TAB_NAMES=YES;

/* Oracle */

libname oralib oracle user=AMLCORE password=amlcore schema=AMLCORE path=EXADAT
PRESERVE_COL_NAMES=YES PRESERVE_TAB_NAMES=YES;
    
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.load_table)

    load_table = LoadTablePane(page)
    load_table.set_node_name(Helper.data_locale.LOAD_TABLE)

    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table.set_target_library("Teralib")
    load_table.set_target_table("Dommy输出")

    load_table.check_options()

    flow.add_node(FlowNodeType.table)
    table = TablePane(page)

    # Go to Libraries pane, Drag  AUTOLIB.BASEBALL'中文测试to the flow and connect to Load Table step
    table.set_library("AUTOLIB")
    time.sleep(1)
    table.set_table("BASEBALL'中文测试")
    time.sleep(1)
    table.refresh_table()
    table.set_node_name(Helper.data_locale.TABLE)
    time.sleep(1)

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE,
                                Helper.data_locale.LOAD_TABLE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.LOAD_TABLE)

    load_table = LoadTablePane(page)
    load_table.set_node_name(Helper.data_locale.LOAD_TABLE)

    # Click on Load Table step, update the Target table to oralib.Dommy_中文'BASEBALL
    load_table.set_target_library('oralib')
    load_table.set_target_table("Dommy_中文'BASEBALL")
    load_table.refresh_target_table()

    load_table.check_options()

    time.sleep(30)

    if load_table.is_visible(load_table.page.get_by_test_id("loadTableInsertPreprocessTruncate")):
        # Check Truncate Table option
        load_table.set_truncate_table_option_for_preprocessing_actions()


def test_41_same_birthday_in_flow(page, init):
    """
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table node
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    # Set output table
    table_pane = TablePane(page)
    table_pane.set_library("work")
    table_pane.set_table("prob_same_birthday")

    # Add STEP_SAME_BIRTHDAY_PROBABILITY
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY]
    flow.add_step_from_stepspane_to_flow(step_path)

    # Connect output port with same birthday node
    flow.select_output_port_node_in_flow(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY, "prob_same_birthday")
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY)

    same_birthday_probability_pane = SameBirthdayProbabilityPane(page)
    same_birthday_probability_pane.set_number_of_people_in_a_room("2")

    flow.run(True)


def test_42_box_plot_in_flow(page, init):
    """
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table node
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    # Set input table
    table_pane = TablePane(page)
    table_pane.set_library("sashelp")
    table_pane.set_table("class")

    # Add STEP_CATEGORY_VISUALIZE_DATA/STEP_BOX_PLOT
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BOX_PLOT]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)
    flow.link_two_nodes_in_flow( "class", Helper.data_locale.STEP_BOX_PLOT)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)

    box_plot_pane = BoxPlotPane(page)
    box_plot_pane.set_filter_input_data("Weight IS NOT MISSING")
    box_plot_pane.set_analysis_variable("Weight")
    box_plot_pane.set_subcategory("Sex")
    box_plot_pane.set_group_analysis_by("Age")

    box_plot_pane.set_plot_orientation(item_index=1)
    time.sleep(0.5)
    box_plot_pane.set_plot_orientation(item_index=0)
    time.sleep(0.5)
    box_plot_pane.set_check_notches()

    box_plot_pane.set_color_transparency_percentage(item_index=2)
    box_plot_pane.set_color_transparency_percentage(item_index=1)
    box_plot_pane.set_color_transparency_percentage(item_index=0)

    box_plot_pane.set_effect(item_index=2)
    box_plot_pane.set_effect(item_index=1)
    box_plot_pane.set_effect(item_index=0)

    box_plot_pane.set_graph_size_unit(item_index=1)
    box_plot_pane.set_graph_size_width_to("7")

    box_plot_pane.set_title_as("MyTitle")
    box_plot_pane.set_footnote_as("MyFootNote")

def test_43_text_parsing_and_topic_discovery(page, init):
    """

    """
    # Create a sas program and run
    sas_program_code = """
libname mycas cas caslib="CASUSER";
 
data mycas.getstart;
    infile datalines delimiter='|' missover;
    length text $150;
    input text$ apple_fruit did$;
    datalines;
Delicious and crunchy apple is one of the popular fruits | 1 |d01
Apple was the king of all fruits. | 1 |d02
Custard apple or Sitaphal is a sweet pulpy fruit | 1 |d03
apples are a common tree throughout the tropics | 1 |d04
apple is round in shape, and tasts sweet | 1 |d05
Tropical apple trees produce sweet apple| 1| d06
Fans of sweet apple adore Fuji because it is the sweetest of| 1 |d07
this apple tree is small | 1 |d08
Apple Store shop iPhone x and iPhone x Plus.| 0 |d09
See a list of Apple phone numbers around the world.| 0 |d10
Find links to user guides and contact Apple Support, | 0 |d11
Apple counters Samsung Galaxy launch with iPhone gallery | 0 |d12
Apple Smartphones - Verizon Wireless.| 0 |d13
Apple mercurial chief executive, was furious.| 0 |d14
Apple has upgraded the phone.| 0 |d15
the great features of the new Apple iPhone x.| 0 |d16
Apple sweet apple iphone.| 0 |d17
Apple apple will make cars | 0 |d18
Apple apple also makes watches| 0 |d19
Apple apple makes computers too| 0 |d20
;
run;
        """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("getstart")
