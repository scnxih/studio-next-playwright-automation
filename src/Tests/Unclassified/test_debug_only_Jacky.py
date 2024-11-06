import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.Common.base_page import BasePage
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.minimum_cut_pane import MinimumCutPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.branch_rows_pane import BranchRowsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.filter_rows_pane import FilterRowsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.manage_columns_pane import ManageColumnsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.StudioNext.Center.codeeditor_page import CodeEditorPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import ManageGitConnectionDialog
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import ManageShortcutsDialog
from src.Pages.StudioNext.Dialog.select_column_dialog import SelectColumnDialog
# from src.Pages.StudioNext.Dialog.select_a_column_dialog import SelectColumnDialog
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Dialog.settings_dialog_just_for_test import SettingsDialogTest
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.StudioNext.Left.sas_content_server_page import SASContentServerPage
from src.Pages.StudioNext.Left.steps_page import StepsPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import TopMenuItem, AccordionType
from src.Utilities.enums import SettingsTabPages
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import FlowNodeType
# from src.Pages.StudioNext.Dialog.select_a_column_dialog import SelectColumnDialog
from src.Pages.StudioNext.Center.Flow.DetailsPane.Integrate.load_table_pane import LoadTablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.same_birthday_pane import SameBirthdayProbabilityPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.box_plot_pane import BoxPlotPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TextAnalytics.text_parsing_and_topic_analysis_pane import \
    TextParsingAndTopicAnalysisPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.StatisticalProcessControl.capability_analysis_pane import \
    CapabilityAnalysisPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.transitive_closure_pane import \
    TransitiveClosurePane
from src.Pages.Common.dialog import Dialog
from playwright.sync_api import expect
from src.Pages.StudioNext.Dialog.new_snippets_dialog import NewSnippetsDialog


def test_00_click_show_tab_labels(page, init):
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

    select_column_dialog = SelectColumnDialog(page)
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

    flow.run(False)


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
    flow.run(False)


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

    flow.run(False)


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
    flow.run(False)

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

    flow.run(False)

    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    # flow.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + "(1)")
    flow.tab_group.click_tab_by_text("输出数据 (1)")
    time.sleep(3)

    WholePage(page).screenshot_self(pic_name="flow_results_same_birthday")


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
    flow.link_two_nodes_in_flow("class", Helper.data_locale.STEP_BOX_PLOT)
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


def test_43_lev0_text_parsing_and_topic_discovery(page, init):
    """
    Level 0 Scenarios (for topic model = SVD)
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

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("mycas")
    table_pane.set_table("getstart")
    table_pane.refresh_table()

    # Add Text Parsing and Topic Discovery node
    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.link_two_nodes_in_flow("getstart", Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    # TextParsingAndTopicAnalysisPane
    tp_ta_pane = TextParsingAndTopicAnalysisPane(page)
    tp_ta_pane.set_input_table_contains(1)
    tp_ta_pane.set_input_table_contains(0)

    tp_ta_pane.set_language(0)
    tp_ta_pane.set_language(item_value="英语")
    # tp_ta_pane.set_language(item_value="泰语")
    tp_ta_pane.set_language(26)
    tp_ta_pane.set_language(6)

    tp_ta_pane.set_text_variable("text")

    tp_ta_pane.set_scree_plot_of_singular_values()

    tp_ta_pane.set_save_term_by_document_matrix()

    # Incomplete function (Studio Next on daily.pgc)
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY,
                                            "添加输出端口",
                                            "{sasstudio-steps-gui-icu.textparsingandtopicdiscovery.outputports.topicDistOutputDSName.displayname.title}")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "添加输出端口", "父表")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("casuser")
    table_pane.set_table("tbd")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "tbd")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    tp_ta_pane.set_save_term_information()

    # Incomplete function (Studio Next on daily.pgc)
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY,
                                            "添加输出端口",
                                            "{sasstudio-steps-gui-icu.genericText.outputport.termInformationTable.title}")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "添加输出端口", "词条信息表")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("casuser")
    table_pane.set_table("terms")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "terms")
    flow.arrange_nodes()


def test_44_lev0_text_parsing_and_topic_discovery(page, init):
    """
    Level 0 Scenarios (for topic model = LDA)
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

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("mycas")
    table_pane.set_table("getstart")
    table_pane.refresh_table()

    # Add Text Parsing and Topic Discovery node
    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.link_two_nodes_in_flow("getstart", Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    # TextParsingAndTopicAnalysisPane
    tp_ta_pane = TextParsingAndTopicAnalysisPane(page)
    tp_ta_pane.set_input_table_contains(1)
    tp_ta_pane.set_input_table_contains(0)

    tp_ta_pane.set_language(0)
    tp_ta_pane.set_language(item_value="英语")

    tp_ta_pane.set_text_variable("text")
    tp_ta_pane.set_topic_model(item_index=1)
    tp_ta_pane.set_topic_model(item_index=0)
    tp_ta_pane.set_topic_model(item_index=1)

    tp_ta_pane.set_number_of_topics_to("3")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY,
                                            "添加输出端口",
                                            "{sasstudio-steps-gui-icu.textparsingandtopicdiscovery.outputports.topicDistOutputDSName.displayname.title}")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "添加输出端口", "父表")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("casuser")
    table_pane.set_table("topicsWords")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "topicsWords")
    flow.arrange_nodes()


def test_45_lev0_capability_analysis(page, init):
    """
    Level-0 testcase for Capability Analysis
    """
    # Create a sas program and run
    sas_program_code = """
data trans;
	input thick @@;
	label thick='Plating Thickness (mils)';
	datalines;
3.468 3.428 3.509 3.516 3.461 3.492 3.478 3.556 3.482 3.512
3.490 3.467 3.498 3.519 3.504 3.469 3.497 3.495 3.518 3.523
3.458 3.478 3.443 3.500 3.449 3.525 3.461 3.489 3.514 3.470
3.561 3.506 3.444 3.479 3.524 3.531 3.501 3.495 3.443 3.458
3.481 3.497 3.461 3.513 3.528 3.496 3.533 3.450 3.516 3.476
3.512 3.550 3.441 3.541 3.569 3.531 3.468 3.564 3.522 3.520
3.505 3.523 3.475 3.470 3.457 3.536 3.528 3.477 3.536 3.491
3.510 3.461 3.431 3.502 3.491 3.506 3.439 3.513 3.496 3.539
3.469 3.481 3.515 3.535 3.460 3.575 3.488 3.515 3.484 3.482
3.517 3.483 3.467 3.467 3.502 3.471 3.516 3.474 3.500 3.466
run;
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("work")
    table_pane.set_table("trans")
    table_pane.refresh_table()

    # Add Capability Analysis node
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                 Helper.data_locale.STEP_CAPABILITY_ANALYSIS]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.link_two_nodes_in_flow("trans", Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)

    # Set process variable
    capability_analysis = CapabilityAnalysisPane(page)
    capability_analysis.set_process_variable("thick")

    # Set upper and lower limits
    capability_analysis.set_lower_limit_to("3.45")
    capability_analysis.set_upper_limit_to("3.55")

    # Run the flow
    flow.run(False)

    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    time.sleep(3)
    flow.screenshot_self("results")


def test_46_lev1_capability_analysis(page, init):
    """
    Level-1 testcase for Capability Analysis
    """

    # Create a sas program and run

    # Set I18N library
    set_autolib_code = """
    libname AUTOLIB '/segatest/I18N/Autolib' ;
        """

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    PageHelper.set_autoexec(page, set_autolib_code)

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("Autolib")
    table_pane.set_table("BASEBALL'中文测试")
    table_pane.refresh_table()

    # Add Capability Analysis node
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                 Helper.data_locale.STEP_CAPABILITY_ANALYSIS]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)

    # Set process variable
    capability_analysis = CapabilityAnalysisPane(page)
    capability_analysis.set_process_variable("logSalary'中")

    # Set upper and lower limits
    capability_analysis.set_target_value_to("3.50")
    capability_analysis.set_lower_limit_to("3.45")
    capability_analysis.set_upper_limit_to("3.55")

    capability_analysis.set_classification_variable("Team'中文")
    capability_analysis.set_group_analysis_by("League'中")

    capability_analysis.set_histogram()
    capability_analysis.set_check_option_for_histogram_distribution("Beta")
    capability_analysis.set_check_option_for_histogram_distribution("Gamma")
    capability_analysis.set_check_option_for_histogram_distribution("指数")
    capability_analysis.set_include_inset_table()

    # Run the flow
    flow.run(False)
    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    # time.sleep(10)
    flow.screenshot_self("results")


def test_47_lev0_transitive_closure(page, init):
    """
    Level 0 Scenarios (for Transitive Closure)
    """

    # Create a sas program and run
    sas_program_code = """
cas;
caslib _all_ assign;

data CASUSER.LinkSetInTC;
    input from $ to $ @@;
    datalines;
B C  B D  C B  D A  D C
;
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINTC")
    table_pane.refresh_table()

    # Add Transitive Closure node
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_TRANSITIVE_CLOSURE]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.link_two_nodes_in_flow("LINKSETINTC", Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)

    # Set process variable
    transitive_closure_pane = TransitiveClosurePane(page)
    transitive_closure_pane.set_select_a_server_for_this_step(item_index=1)

    transitive_closure_pane.set_from_node("from")
    transitive_closure_pane.set_to_node("to")

    flow.run(False)


def test_48_lev1_transitive_closure(page, init):
    """
    Level 0 Scenarios (for Transitive Closure)
    """

    # Create a sas program and run
    sas_program_code = """
data 'LinkSetInTC''générer ='n;
	input 'from''从'n $ 'to''到'n $ @@;
	datalines;
'B''乙'n 'C''丙'n  'B''乙'n 'D''丁'n  'C''丙'n 'B''乙'n  'D''丁'n 'A''甲'n  'D''丁'n 'C''丙'n
;

libname mycas cas;

proc casutil;
	load data=WORK.'LINKSETINTC''GÉNÉRER ='n casout="linksetintc''GÉNÉRER=";
run;
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.run(True)

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETINTC''GÉNÉRER=")
    table_pane.refresh_table()

    # Add Transitive Closure node
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_TRANSITIVE_CLOSURE]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.link_two_nodes_in_flow("LINKSETINTC''GÉNÉRER=", Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)

    # Set process variable
    transitive_closure_pane = TransitiveClosurePane(page)
    transitive_closure_pane.set_select_a_server_for_this_step(item_index=1)

    transitive_closure_pane.set_from_node("from'从")
    transitive_closure_pane.set_to_node("to'到")
    transitive_closure_pane.set_log_details(item_index=1)
    transitive_closure_pane.set_log_details(item_value=Helper.data_locale.NO_SUMMARY)

    transitive_closure_pane.set_code_generation(item_index=1)
    transitive_closure_pane.set_code_generation(item_value=Helper.data_locale.USE_CAS_PROCEDURE)

    # Run the flow
    flow.run(False)
    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    time.sleep(3)
    flow.screenshot_self("results")


def test_49_accordion_steps(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps.navigate_to_step(step_path)

    # steps.tree.navigate_to_element_and_click_context_menu([Helper.data_locale.STEP_CATEGORY_DATA], "折叠")

    # Original
    AccordionPage(page).screenshot_self("Data")

    # Collapse after screenshot steps.tree.navigate_to_element_and_click_context_menu([
    # Helper.data_locale.STEP_CATEGORY_DATA], Helper.data_locale.COLLAPSE)

    steps.tree.navigate_to_element_and_click_context_menu([step_path[0]],
                                                          Helper.data_locale.COLLAPSE)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA_QUALITY, Helper.data_locale.STEP_PARSE_DATA]
    steps.navigate_to_step(step_path)

    AccordionPage(page).screenshot_self("Data_Quality",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')
    # Collapse after screenshot
    steps.tree.navigate_to_element_and_click_context_menu([Helper.data_locale.STEP_CATEGORY_DATA_QUALITY],
                                                          Helper.data_locale.COLLAPSE)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_PYTHON_PROGRAM]
    steps.navigate_to_step(step_path)
    AccordionPage(page).screenshot_self("Develop")

    # Collapse after screenshot
    steps.tree.navigate_to_element_and_click_context_menu([Helper.data_locale.STEP_CATEGORY_DEVELOP],
                                                          Helper.data_locale.COLLAPSE)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    # steps.navigate_to_step(step_path)
    steps.navigate_to_step_then_collapse_parent(step_path)
    AccordionPage(page).screenshot_self("Econometrics")

    # steps.collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_PHONE_NUMBERS]
    steps.navigate_to_step(step_path)
    AccordionPage(page).screenshot_self("Enrichment")

    step_path: list = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_TABLE_ATTRIBUTES]
    steps.navigate_to_step(step_path)

    AccordionPage(page).screenshot_self("Examine_Data",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_INTEGRATE, Helper.data_locale.STEP_MERGE_TABLE]
    steps.navigate_to_step(step_path)

    AccordionPage(page).screenshot_self("Merge_Table",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                       Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Machine_Learning")
    AccordionPage(page).screenshot_self("Machine_Learning",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MANAGE_MODELS,
                       Helper.data_locale.STEP_REGISTER_PYTHON_MODEL]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Register_Python")
    AccordionPage(page).screenshot_self("Register_Python",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                       Helper.data_locale.STEP_CORE_DECOMPOSITION]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Core")
    AccordionPage(page).screenshot_self("Core",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # Collapse after screenshot
    # steps.tree.icon_expand_element().click()

    step_path: list = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                       Helper.data_locale.STEP_STANDARDIZE_DATA]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Standardize_Data")
    AccordionPage(page).screenshot_self("Standardize_Data",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                       Helper.data_locale.STEP_PARETO_ANALYSIS]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Pareto")
    AccordionPage(page).screenshot_self("Pareto",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS,
                       Helper.data_locale.STEP_MULTIDIMENSIONAL_PREFERENCE_ANALYSIS]
    steps.navigate_to_step(step_path)

    AccordionPage(page).screenshot_self("Multidimensional",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA,
                       Helper.data_locale.STEP_TRANSPOSE_DATA]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Transpose")
    AccordionPage(page).screenshot_self("Transpose",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                       Helper.data_locale.STEP_TEXT_MAP]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Text_Map")
    AccordionPage(page).screenshot_self("Text_Map",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')


def test_50_accordion_steps(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    # steps.navigate_to_step(step_path)
    steps.navigate_to_step_then_collapse_parent(step_path)
    # steps.tree.navigate_to_element_and_click_context_menu([Helper.data_locale.STEP_CATEGORY_DATA], "折叠")

    # Original
    # AccordionPage(page).screenshot_self("Data")

    # Collapse after screenshot steps.tree.navigate_to_element_and_click_context_menu([
    # Helper.data_locale.STEP_CATEGORY_DATA], Helper.data_locale.COLLAPSE)

    # steps.tree.navigate_to_element_and_click_context_menu([step_path[0]], Helper.data_locale.COLLAPSE)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA_QUALITY, Helper.data_locale.STEP_PARSE_DATA]
    # steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Data_Quality", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')
    # Collapse after screenshot
    # steps.tree.navigate_to_element_and_click_context_menu([Helper.data_locale.STEP_CATEGORY_DATA_QUALITY], Helper.data_locale.COLLAPSE)

    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_PYTHON_PROGRAM]
    # steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Develop")

    # Collapse after screenshot
    # steps.tree.navigate_to_element_and_click_context_menu([Helper.data_locale.STEP_CATEGORY_DEVELOP], Helper.data_locale.COLLAPSE)
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    steps.navigate_to_step_then_collapse_parent(step_path)
    # AccordionPage(page).screenshot_self("Econometrics")

    # steps.collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_PHONE_NUMBERS]
    # steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Enrichment")

    step_path: list = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_TABLE_ATTRIBUTES]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # AccordionPage(page).screenshot_self("Examine_Data", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_INTEGRATE, Helper.data_locale.STEP_MERGE_TABLE]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # AccordionPage(page).screenshot_self("Merge_Table", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                       Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)
    # AccordionPage(page).screenshot_self("Machine_Learning")
    # AccordionPage(page).screenshot_self("Machine_Learning", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MANAGE_MODELS, Helper.data_locale.STEP_REGISTER_PYTHON_MODEL]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # AccordionPage(page).screenshot_self("Register_Python")
    # AccordionPage(page).screenshot_self("Register_Python", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                       Helper.data_locale.STEP_CORE_DECOMPOSITION]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # AccordionPage(page).screenshot_self("Core")
    # AccordionPage(page).screenshot_self("Core", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    # Collapse after screenshot
    # steps.tree.icon_expand_element().click()

    step_path: list = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                       Helper.data_locale.STEP_STANDARDIZE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # AccordionPage(page).screenshot_self("Standardize_Data")
    # AccordionPage(page).screenshot_self("Standardize_Data", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                       Helper.data_locale.STEP_PARETO_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)
    # AccordionPage(page).screenshot_self("Pareto")
    # AccordionPage(page).screenshot_self("Pareto", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS,
                       Helper.data_locale.STEP_MULTIDIMENSIONAL_PREFERENCE_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # AccordionPage(page).screenshot_self("Multidimensional", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA,
                       Helper.data_locale.STEP_TRANSPOSE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)
    # AccordionPage(page).screenshot_self("Transpose")
    # AccordionPage(page).screenshot_self("Transpose", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                       Helper.data_locale.STEP_TEXT_MAP]
    steps.navigate_to_step_then_collapse_parent(step_path)
    # AccordionPage(page).screenshot_self("Text_Map")
    # AccordionPage(page).screenshot_self("Text_Map", mask=[AccordionPage(page).ag_body_vertical_scroll_bar], mask_color='#000000')


def test_51_accordion_steps_backup(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA_QUALITY, Helper.data_locale.STEP_PARSE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_PYTHON_PROGRAM]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_PHONE_NUMBERS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_TABLE_ATTRIBUTES]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_INTEGRATE, Helper.data_locale.STEP_MERGE_TABLE]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                       Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MANAGE_MODELS, Helper.data_locale.STEP_REGISTER_PYTHON_MODEL]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                       Helper.data_locale.STEP_CORE_DECOMPOSITION]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                       Helper.data_locale.STEP_STANDARDIZE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                       Helper.data_locale.STEP_PARETO_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # ERROR
    # step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_MULTIDIMENSIONAL_PREFERENCE_ANALYSIS]

    # WORKS FINE
    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY]

    # step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SUMMARY_STATISTICS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA, Helper.data_locale.STEP_TRANSPOSE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_TEXT_MAP]
    steps.navigate_to_step_then_collapse_parent(step_path)


def test_52_accordion_steps(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)

    # step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    # steps.navigate_to_step(step_path)

    # expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text 3"])

    # expect(steps.page.locator('//div[@role="gridcell"]//span[@data-sas-usetruncationtooltip="true"]')).to_have_text(["数据（输入和输出）", "数据质量", "开发"])
    expect(steps.page.locator('//div[@role="gridcell"]//span[@data-sas-usetruncationtooltip="true"]')).to_have_text(
        ['云分析服务', '数据（输入和输出）', '数据质量', '开发', '计量经济学', '扩充', '检查数据', '集成', '机器学习',
         '管理模型', '优化和网络分析', '准备和探索数据', '统计过程控制', '统计量', '文本分析', '转换数据',
         '可视化数据'])


def test_53_accordion_steps(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps.navigate_to_step(step_path)

    # ERROR: Inconsistent number
    # expect(steps.page.locator('//div[@role="gridcell"]//span[@data-sas-usetruncationtooltip="true"]')).to_have_text(["数据（输入和输出）", "数据质量", "开发"])

    # ERROR: Incorrect order
    # expect(steps.page.locator('//div[@role="gridcell"]//span[@data-sas-usetruncationtooltip="true"]')).to_have_text(['云分析服务', '数据（输入和输出）', '数据质量', '开发', '计量经济学', '扩充', '检查数据', '集成', '机器学习', '管理模型', '优化和网络分析', '准备和探索数据', '统计过程控制', '统计量', '文本分析', '转换数据', '可视化数据', '表', '导出', '文件', '导入文件'])

    # ERROR: Incorrect amount or order
    # expect(steps.page.locator('//div[@role="gridcell"]//span[@data-sas-usetruncationtooltip="true"]')).to_have_text(['云分析服务', '数据质量', '开发', '计量经济学', '扩充', '检查数据', '集成', '机器学习', '管理模型', '优化和网络分析', '准备和探索数据', '统计过程控制', '统计量', '文本分析', '转换数据', '可视化数据', '表', '导出', '文件', '导入文件'])

    # WORKS
    expect(steps.page.locator('//div[@role="gridcell"]//span[@data-sas-usetruncationtooltip="true"]')).to_have_text(
        ['云分析服务', '数据（输入和输出）', '数据质量', '开发', '计量经济学', '扩充', '检查数据', '集成', '机器学习',
         '管理模型', '优化和网络分析', '准备和探索数据', '统计过程控制', '统计量', '文本分析', '转换数据', '可视化数据',
         '导出', '文件', '导入文件', '表'])


def test_54_hover_info_assertion(page, init):
    """
    Test title-assertion
    """
    PageHelper.new_sas_program(page)

    editor = CodeEditorPage(page)

    expect(editor.toolbar.get_by_test_id("programViewPane-toolbar-runButton")).to_have_accessible_description(
        Helper.data_locale.RUN)


def test_55_locator_assertion(page, init):
    """
    Locator Assertions
    """
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_sas_content)
    acc: AccordionPage = AccordionPage(page)

    acc.show_accordion(AccordionType.sas_content)

    # ERROR
    # //button[@data-testid="sascontentNavPane-deleteButton"]
    # expect(acc.get_by_test_id("sascontentNavPane-deleteButton")).to_have_accessible_description(Helper.data_locale.DELETE)

    # ERROR
    # expect(acc.get_by_test_id("sascontentNavPane-deleteButton")).to_have_accessible_name(Helper.data_locale.DELETE)

    expect(acc.get_by_test_id("sascontentNavPane-deleteButton")).to_have_accessible_name("删除选择")

    expect(acc.get_by_test_id("sascontentNavPane-deleteButton")).to_have_accessible_description("删除选择")

    expect(acc.get_by_test_id("sascontentNavPane-deleteButton")).to_have_role("button")


def test_56_page_assertions(page, init):
    """
    Test Page Assertions
    """
    expect(page).to_have_title("SAS® Studio Next")
    expect(page).not_to_have_title("SAS Studio")

    expect(page).to_have_url("https://daily.pgc.unx.sas.com/SASStudioNext/")
    expect(page).not_to_have_url("https://daily.pgc.unx.sas.com/SASStudio/")


def test_57_api_response_assertion(page, init):
    """

    """
    # ERROR
    # response = page.request.get('https://daily.pgc.unx.sas.com')

    # WORKS
    response = page.request.get('https://playwright.dev')
    expect(response).to_be_ok()


def test_58_press_sequentially(page, init):
    """
    Mock human-typing
    """
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)

    # Type instantly
    # editor.editor.type_into_text_area("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")

    # Mimic human-typing
    editor.get_by_test_id("programView-editorPane-editor").press_sequentially(
        "data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;", delay=500)


def test_59_drag_and_drop_integrated(page, init):
    """
    Reference: https://playwright.dev/python/docs/input#drag-and-drop
    Create a flow then DnD a table node to flow canvas
    """
    # flow: FlowPage = PageHelper.new_flow(page)
    sas_content = SASContentServerPage(page)
    PageHelper.show_accordion(page, AccordionType.sas_content)

    # file_path: list = [Helper.data_locale.SAS_CONTENT, "Public", "plain_factory_text_file.txt"]
    sas_content.navigate_to_folder_or_file([Helper.public_folder_path])

    # //div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]
    # steps.locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(flow.locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'))

    # tab-group-overflow-_root_
    sas_content.locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(
        page.locator('//div[@data-testid="tab-group-overflow-_root_"]'))


def test_60_hover_information(page, init):
    """
    Reference:
    https://playwright.dev/python/docs/api/class-locatorassertions#locator-assertions-to-have-accessible-description
    """
    PageHelper.new_sas_program(page)

    editor = CodeEditorPage(page)

    editor.type_code_in_codeeditor("data test;set sashelp.class;run;")

    # data-testid="programViewPane-toolbar-snippet"
    expect(editor.get_by_test_id("programViewPane-toolbar-snippet")).to_have_accessible_description("另存为代码段。")


def test_61_drag_and_drop_integrated(page, init):
    """
    Reference: https://playwright.dev/python/docs/input#drag-and-drop
    Create a flow then DnD a table node to flow canvas
    """
    flow: FlowPage = PageHelper.new_flow(page)
    steps_content = StepsPage(page)
    PageHelper.show_accordion(page, AccordionType.steps)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps_content.navigate_to_step(step_path)

    # //div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]
    # steps_content.locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(flow.locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'))
    # steps_content.locate_xpath('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(flow.locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'))
    # steps_content.click('//div[@role="row"][@row-index="5"]')

    # Works
    # steps_content.dblclick('//div[@role="row"][@row-index="5"]')

    # steps_content.locate_xpath('//div[@role="row"][@row-index="5"]').drag_to(flow.locate_xpath('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'))

    # tab-group-overflow-_root_
    # steps_content.locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(page.locator('//div[@data-testid="tab-group-overflow-_root_"]'))

    steps_content.locate_xpath('//div[@role="row"][@row-index="5"]').hover(force=True, timeout=5000)
    # steps_content.locate_xpath('//div[@role="row"][@row-index="5"]').screenshot()
    # page.locator('//div[@role="row"][@row-index="5"]').()
    # time.sleep(1)

    steps_content.page.mouse.down(button="left")
    # time.sleep(1)

    flow.locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]').hover(force=True, timeout=500)
    # time.sleep(1)

    page.locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]').hover(force=True, timeout=500)
    # time.sleep(1)

    page.mouse.up(button="left")
    # time.sleep(1)


def test_62_drag_and_drop_integrated(page, init):
    """
    Reference: https://playwright.dev/python/docs/input#drag-and-drop
    Create a flow then DnD a table node to flow canvas
    """
    PageHelper.new_item(page, TopMenuItem.new_sas_program)
    PageHelper.new_item(page, TopMenuItem.new_custom_step)
    PageHelper.new_item(page, TopMenuItem.new_quick_import)
    PageHelper.new_item(page, TopMenuItem.new_python_program)

    # //div[@role="tab"][@aria-label="SAS 程序.sas"]
    WholePage(page).locator('//div[@role="tab"][@aria-label="SAS 程序.sas"]').drag_to(WholePage(page).locator('//div[@role="tab"][@aria-label="Python.py"]'))
    # //div[@role="tab"][@aria-label="Python.py"]

def test_63_drag_and_drop_integrated(page, init):
    """
    Reference: https://playwright.dev/python/docs/input#drag-and-drop
    Create a flow then DnD a table node to flow canvas
    """
    flow: FlowPage = PageHelper.new_flow(page)
    steps_content = StepsPage(page)
    PageHelper.show_accordion(page, AccordionType.steps)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps_content.navigate_to_step(step_path)

    # //div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]
    # WholePage(page).locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(WholePage(page).locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'))
    # WholePage(page).locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(target=WholePage(page).locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'), target_position= [{'x': 540, 'y': 480}, None])
    WholePage(page).locator('//div[@role="row"][@row-id="GENERIC_TABLE_TRANSFORMATION"]').drag_to(target=WholePage(page).locator('//canvas[text()="This text is displayed if your browser does not support the Canvas HTML element."]'), target_position= [{540, 480}, None])


def test_64_drag_and_drop_custom_step(page, init):
    """
    Reference: https://playwright.dev/python/docs/input#drag-and-drop
    Create a flow then DnD a table node to flow canvas
    """
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()

    time.sleep(1)
    # //li[@role="option"]//span[contains(@class,"sas_components-ListBox-List_item-text")][text()="第 1 页"]

    # WholePage(page).locator('//li[@role="option"]//span[contains(@class,"sas_components-ListBox-List_item-text")][text()="第 3 页"]').drag_to(WholePage(page).locator('//li[@role="option"]//span[contains(@class,"sas_components-ListBox-List_item-text")][text()="第 1 页"]'))

    WholePage(page).locator('//li[@role="option"]//span[contains(@class,"sas_components-ListBox-List_item-text")][text()="第 3 页"]').drag_to(WholePage(page).locator('//button[@data-testid="deletePageButton"]'))

    # source = '//li[@role="option"][@aria-label="复选框, 复选框"]'

    # target = '//div[@data-testid="designCanvasTestID"]'

    # WholePage(page).locator(source).drag_to(WholePage(page).locator(target))
    # custom_step.locator('//li[@role="option"][@aria-label="复选框, 复选框"]').drag_to(custom_step.locator('//div[@data-testid="designCanvasTestID"]'))


def test_65_drag_and_drop_custom_step(page, init):
    """
    Reference: https://playwright.dev/python/docs/input#drag-and-drop
    Create a flow then DnD a table node to flow canvas
    """
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()

    WholePage(page).locator('//li[@role="option"]//span[contains(@class,"sas_components-ListBox-List_item-text")][text()="第 5 页"]').hover()
    # time.sleep(0.5)
    WholePage(page).page.mouse.down()
    time.sleep(1.0)
    WholePage(page).locator('//li[@role="option"]//span[contains(@class,"sas_components-ListBox-List_item-text")][text()="第 1 页"]').hover()
    # WholePage(page).locator('//div[@data-testid="designCanvasTestID"]').hover()
    time.sleep(1.0)
    WholePage(page).page.mouse.up()


def test_66_cluster_observation_lev0(page, init):
    """
    https://go.documentation.sas.com/doc/en/webeditorcdc/v_034/webeditorref/n1j31r9w1hjtejn1ntv83oubrosf.htm
    """
    # Create a sas program and run
    sas_program_code = """
data Protein;
length Country $ 14;
input RedMeat WhiteMeat Eggs Milk Fish Cereal Starch Nuts FruitVeg Country &$;
datalines;
10.1 1.4 0.5 8.9 0.2 42.3 0.6 5.5 1.7 Albania
8.9 14.0 4.3 19.9 2.1 28.0 3.6 1.3 4.3 Austria
13.5 9.3 4.1 17.5 4.5 26.6 5.7 2.1 4.0 Belgium
7.8 6.0 1.6 8.3 1.2 56.7 1.1 3.7 4.2 Bulgaria
9.7 11.4 2.8 12.5 2.0 34.3 5.0 1.1 4.0 Czechoslovakia
10.6 10.8 3.7 25.0 9.9 21.9 4.8 0.7 2.4 Denmark
8.4 11.6 3.7 11.1 5.4 24.6 6.5 0.8 3.6 E Germany
9.5 4.9 2.7 33.7 5.8 26.3 5.1 1.0 1.4 Finland
18.0 9.9 3.3 19.5 5.7 28.1 4.8 2.4 6.5 France
10.2 3.0 2.8 17.6 5.9 41.7 2.2 7.8 6.5 Greece
5.3 12.4 2.9 9.7 0.3 40.1 4.0 5.4 4.2 Hungary
13.9 10.0 4.7 25.8 2.2 24.0 6.2 1.6 2.9 Ireland
9.0 5.1 2.9 13.7 3.4 36.8 2.1 4.3 6.7 Italy
9.5 13.6 3.6 23.4 2.5 22.4 4.2 1.8 3.7 Netherlands
9.4 4.7 2.7 23.3 9.7 23.0 4.6 1.6 2.7 Norway
6.9 10.2 2.7 19.3 3.0 36.1 5.9 2.0 6.6 Poland
6.2 3.7 1.1 4.9 14.2 27.0 5.9 4.7 7.9 Portugal
6.2 6.3 1.5 11.1 1.0 49.6 3.1 5.3 2.8 Romania
7.1 3.4 3.1 8.6 7.0 29.2 5.7 5.9 7.2 Spain 
9.9 7.8 3.5 4.7 7.5 19.5 3.7 1.4 2.0 Sweden
13.1 10.1 3.1 23.8 2.3 25.6 2.8 2.4 4.9 Switzerland
17.4 5.7 4.7 20.6 4.3 24.3 4.7 3.4 3.3 UK
9.3 4.6 2.1 16.6 3.0 43.6 6.4 3.4 2.9 USSR
11.4 12.5 4.1 18.8 3.4 18.6 5.2 1.5 3.8 W Germany
4.4 5.0 1.2 9.5 0.6 55.9 3.0 5.7 3.2 Yugoslavia
;
    """
    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.format_program()
    sas_program.run(True)
    sas_program.wait_toast_disappear()
    sas_program.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + " (1)")

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)

    # Set lib and table
    table_pane.set_library("WORK")
    table_pane.set_table("PROTEIN")
    table_pane.refresh_table()

    # Add Transitive Closure node
    step_path = [Helper.data_locale.STATISTICS,
                 Helper.data_locale.STEP_HIERARCHICAL_CLUSTERING]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas("PROTEIN")
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_HIERARCHICAL_CLUSTERING)
    flow.link_two_nodes_in_flow("PROTEIN", Helper.data_locale.STEP_HIERARCHICAL_CLUSTERING)
    flow.arrange_nodes()

    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas("PROTEIN")

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_HIERARCHICAL_CLUSTERING)


def test_67_minimum_cut_lev0(page, init):
    """
    Optimization and Network Analysis/Minimum Cut
    https://go.documentation.sas.com/doc/en/sasstudiocdc/v_049/webeditorcdc/webeditorref/p00i6dsk2daifen1ugvuno9lwrad.htm
    """
    # Create a sas program and run
    sas_program_code = """
data LinkSetIn;
	input from to weight @@;
	datalines;
1 2 2  1 5 3  2 3 3  2 5 2  2 6 2
3 4 4  3 7 2  4 7 2  4 8 2  5 6 3
6 7 1  7 8 3
;
"""

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.format_program()
    sas_program.run(True)
    sas_program.wait_toast_disappear()
    sas_program.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + " (1)")

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)

    # Set lib and table
    table_pane.set_library("WORK")
    table_pane.set_table("LinkSetIn")
    table_pane.refresh_table()

    # Add Transitive Closure node
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_CUT]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas("LinkSetIn")
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_CUT)
    flow.link_two_nodes_in_flow("LinkSetIn", Helper.data_locale.STEP_MINIMUM_CUT)
    flow.arrange_nodes()

    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas("LinkSetIn")

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_CUT)

    # Set process variable
    minimum_cut_pane = MinimumCutPane(page)
    minimum_cut_pane.set_select_a_server_for_this_step(item_index=1)

    minimum_cut_pane.set_from_node("from")
    minimum_cut_pane.set_to_node("to")

    flow.run(False)


def test_68_undo_redo_run_format_debug_codetoflow_snippets_clear(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")
    editor.toolbar.click_btn_by_test_id_contains("toolbar-snippet")
    if NewSnippetsDialog(page).is_open():
        Helper.logger.debug("New Snippets dialog is open: ")
        NewSnippetsDialog(page).new_snippet('test_snippet_name',
                                            'test_snippet_abbreviation',
                                            'test_snippet_description')
        # NewSnippetsDialog(page).new_abbreviation('test_snippet_abbreviation')
