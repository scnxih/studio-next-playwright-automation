"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@esas.com
Date: September 12th, 2023
"""
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.custom_step_page_test import CustomStepPageTest
from src.Pages.StudioNext.Center.flow_page_test import FlowPageTest
from src.Pages.StudioNext.Center.Query.query_page import QueryPage
from src.Pages.StudioNext.Center.quick_import_page import QuickImportPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog


def test_01_sas_program_check_log(page, init):
    """
    Check log after sas program run
    :param page:
    :param init:
    :return:
    """

    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    sas_program_editor.fill_text_area_with("proc print data = sashelp.cars; run;")

    # sas_program_editor.run_and_check_results()

    sas_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)
    sas_program_editor.wait_toast_disappear()
    sas_program_editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)


def test_02_autoexec_check_log(page, init):
    """
    Check autoexec log after sas program run
    :param page:
    :param init:
    :return:
    """
    text = '''
    proc print data=sashelp.class;
    run;
    '''

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    # PageHelper.set_autoexec(page, text)
    autoexec_editor = PageHelper.create_plain_editor_factory().create_editor("autoexec", page)
    autoexec_editor.fill_text_area_with(text)

    autoexec_dialog = AutoexecDialog(page)
    autoexec_dialog.run()

    # DOES NOT WORK
    # autoexec_editor.run_and_return_to_code()

    # WORKS FINE
    # autoexec_dialog.tab_Code.click()
    time.sleep(5)

    autoexec_dialog.tab_group.click_tab_by_text(Helper.data_locale.CODE)

    time.sleep(5)

    autoexec_dialog.save()

    # Clear input
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    # PageHelper.clear_autoexec(page)
    PageHelper.clear_autoexec_thru_keyboard(page)


def test_03_custom_code_check_log(page, init):
    """
    Check log after sas program run in custom code dialog
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

    custom_code_dialog = CustomCodeDialog(page)
    custom_code_dialog.run()

    time.sleep(5)
    custom_code_dialog.tab_group.click_tab_by_text(Helper.data_locale.CODE)
    time.sleep(5)

    custom_code_dialog.tab_group.click_tab_by_text("后置代码")
    custom_code_editor.fill_text_area_with(text)
    custom_code_dialog.run()

    time.sleep(5)
    custom_code_dialog.tab_group.click_tab_by_text(Helper.data_locale.CODE)
    time.sleep(5)

    custom_code_dialog.save()

    # Clear custom code
    PageHelper.click_options(page, TopMenuItem.options_custom_code)
    # PageHelper.clear_customcode(page)
    PageHelper.clear_customcode_thru_keyboard(page)


def test_04_flow_double_tabs(page, init):
    """
    Test double tab groups in flow
    :param page:
    :param init:
    :return:
    """
    # PageHelper.click_options(page, TopMenuItem.options.new_flow)
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_flow)

    flow_page = FlowPageTest(page)

    # flow_page.tab_group.click_tab_by_title("提交的代码和结果")
    flow_page.tab_group.click_tab_by_text("提交的代码和结果")
    flow_page.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA)


def test_05_quick_import_tab_pages(page, init):
    """
    Test tab page clicking for Quick Import
    :param page:
    :param init:
    :return:
    """
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_quick_import)

    quick_import_page = QuickImportPage(page)

    quick_import_page.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA)


def test_06_custom_step(page, init):
    """
    Test tab page clicking for Custom Step
    :param page:
    :param init:
    :return:
    """
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_custom_step)

    custom_step_page = CustomStepPageTest(page)
    custom_step_page.tab_group.click_tab_by_text(Helper.data_locale.JSON)
    custom_step_page.tab_group.click_tab_by_text("设计")
    custom_step_page.tab_group.click_tab_by_text("程序")

    # tab on the very right: DOES NOT WORK
    # Plus, these tab pages should be encapsulated into another common components
    # custom_step_page.tab_group.click_tab_by_text(Helper.data_locale.PROPERTIES)


def test_07_python_program_check(page, init):
    """
    Test python program outputdata page
    :param page:
    :param init:
    :return:
    """
    python_program_editor = PageHelper.create_program_editor_factory().create_program_editor("python", page)
    python_program_editor.fill_text_area_with("print('Hello, world!')")
    # time.sleep(5)
    # python_program_editor.run_and_check_results()
    # time.sleep(5)

    python_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)
    python_program_editor.wait_toast_disappear()
    python_program_editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)


def test_08_sas_program_output_tab_toolbar_operation(page, init):
    """
    Test toolbar in Output tab page
    :param page:
    :param init:
    :return:
    """
    sas_program = """ 
    data work.my_class;
    set sashelp.class;
    run;
    """

    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    sas_program_editor.fill_text_area_with(sas_program)

    # sas_program_editor.run_and_check_results()

    sas_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)
    sas_program_editor.wait_toast_disappear()
    sas_program_editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    # Click Output Tab Page
    sas_program_editor.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA)

    # DOES NOT WORK
    # Turns out to be the UPPER one, NOT that in output tab page
    # sas_program_editor.toolbar.click_btn_by_title(Helper.data_locale.MORE_OPTIONS)
    # time.sleep(5)

    # WORKS FINE
    # Click "Column View" button
    # sas_program_editor.toolbar.click_btn_by_title_contains("列")
    # time.sleep(5)

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.21st, 2023

    # Click Name Column Twice
    sas_program_editor.tree_grid_table.col_header("1").click()
    sas_program_editor.tree_grid_table.col_header("1").click()

    # Hide Column from Header Menu
    # Open Header Menu for Column-Name
    sas_program_editor.tree_grid_table.btn_col_header_menu("1").click()
    # Select Hide from Menu
    sas_program_editor.tree_grid_table.click_menu_item("隐藏")

    # Pin Column from Header Menu
    # Open Header Menu for Column-Sex
    sas_program_editor.tree_grid_table.btn_col_header_menu("2").click()
    # Select Pin Right from Menu
    sas_program_editor.tree_grid_table.click_menu_item("Pin Column")
    sas_program_editor.tree_grid_table.click_menu_item("Pin Right")

    # time.sleep(5)

    # Added by Jacky(ID: jawang) on Sept.21st, 2023 >>>

    # Click log tab page
    sas_program_editor.tab_group.click_tab_by_text(Helper.data_locale.LOG)
    # Click Gutter-Notes
    sas_program_editor.toolbar.click_btn_by_test_id("programView-log-content-summary-toolbar-informationButton")


def test_09_query_tab_pages(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_query)

    query_page = QueryPage(page)
    query_page.tab_group.click_tab_by_text(Helper.data_locale.SORT)
    query_page.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)
    # query_page.tab_group.click_tab_by_text(Helper.data_locale.Col)


def test_10_sas_program_output_tab_menu_tablist(page, init):
    """

    :param page:
    :param init:
    :return:
    """
    sas_program = """ 
    data work.my_class;
    set sashelp.class;
    run;
    """

    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    sas_program_editor.fill_text_area_with(sas_program)

    # sas_program_editor.run_and_check_results()

    sas_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)
    sas_program_editor.wait_toast_disappear()
    sas_program_editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    # Click Output Tab Page
    sas_program_editor.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA)

    # Open Header Menu for Column-Age
    sas_program_editor.tree_grid_table.btn_col_header_menu("3").click()

    # Work-around to select the other tab
    sas_program_editor.key_press("Tab")
    sas_program_editor.key_press("ArrowRight")

    # TO-DO: listbox
    # sas_program_editor.click_menu_item("Greater than or equals")
    # sas_program_editor.tree_grid_table.fill("//input[@placeholder='Filter...']", 14)
    # sas_program_editor.click(" //button[@ref='applyFilterButton']")


def test_11_pinpoint_tab_group_from_descendant_text(page, init):
    """
    Pinpointing tab-group testing
    :param page:
    :param init:
    :return:
    """
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    sas_program_editor.fill_text_area_with("proc print data = sashelp.cars; run;")
    sas_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)

    # sas_program_editor.tab_group.current_tab_group_by_descendant_text(Helper.data_locale.RESULTS).click()

    print("*** Tab Group Xpath:" + str(
        sas_program_editor.tab_group.current_tab_group_by_descendant_text(Helper.data_locale.RESULTS)))

    # Get __screenshot of current tab group according to descendant tab text
    sas_program_editor.screenshot(
        sas_program_editor.tab_group.current_tab_group_by_descendant_text(Helper.data_locale.RESULTS),
        "check_tab_group", user_assigned_xpath=True)


def test_12_pinpoint_tab_group_from_ancestor_testid(page, init):
    """
    Pinpointing tab-group from ancestor's data-testid
    :param page:
    :param init:
    :return:
    """
    # Create multiple central pages
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    xml_editor = PageHelper.create_plain_editor_factory().create_editor("xml", page)
    json_editor = PageHelper.create_plain_editor_factory().create_editor("json", page)
    text_editor = PageHelper.create_plain_editor_factory().create_editor("text", page)
    wksp_editor = PageHelper.create_plain_editor_factory().create_editor("workspace", page)
    python_program_editor = PageHelper.create_program_editor_factory().create_program_editor("python", page)

    print("*** Tab Group Xpath:" + str(
        python_program_editor.tab_group.current_tab_group_by_ancestor_div_test_id("tab-group-bar-_root_")))

    # Get __screenshot of current tab group according based on descendant
    python_program_editor.screenshot(
        python_program_editor.tab_group.current_tab_group_by_ancestor_div_test_id("tab-group-bar-_root_"),
        "check_tab_group", user_assigned_xpath=True)


def test_13_first_tab_page(page, init):
    """
    Test tab-page clicking in tab-group
    :param page:
    :param init:
    :return:
    """
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    xml_editor = PageHelper.create_plain_editor_factory().create_editor("xml", page)
    json_editor = PageHelper.create_plain_editor_factory().create_editor("json", page)
    text_editor = PageHelper.create_plain_editor_factory().create_editor("text", page)
    wksp_editor = PageHelper.create_plain_editor_factory().create_editor("workspace", page)
    python_program_editor = PageHelper.create_program_editor_factory().create_program_editor("python", page)

    # Check sanity of returned xpath
    python_program_editor.tab_group.first_tab_page_by_text("Python.py").click()
    time.sleep(3)

    # Check implemented method
    python_program_editor.tab_group.click_last_tab_page_by_text("Python.py")
    time.sleep(3)

    # Check implemented method
    python_program_editor.tab_group.click_first_tab_page_by_text("Python.py")
    time.sleep(3)

    python_program_editor.tab_group.screenshot(
        python_program_editor.tab_group.selected_tab_page_text("Python.py"),
        "selected_tab_group1",
        user_assigned_xpath=True)

    # Check sanity of returned xpath
    python_program_editor.tab_group.last_tab_page_by_text("Python.py").click()
    time.sleep(3)

    python_program_editor.tab_group.screenshot(
        python_program_editor.tab_group.selected_tab_page_text("Python.py"),
        "selected_tab_group2",
        user_assigned_xpath=True)


def test_14_sas_program_tab_group_from_descendant_text(page, init):
    """
    Pinpointing sas program tab-group testing
    :param page:
    :param init:
    :return:
    """
    # Create a program
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    # Code
    sas_program_editor.fill_text_area_with("proc print data = sashelp.cars; run;")

    # Run the program
    sas_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)

    # Test the tab group which composed of Output/Result/Log
    # Click the Output tab after run
    sas_program_editor.tab_group.click_last_tab_page_by_text(Helper.data_locale.LOG)
    time.sleep(3)

    # Switch back to Log tab
    sas_program_editor.tab_group.click_first_tab_page_by_text(Helper.data_locale.OUTPUT_DATA)
    time.sleep(3)

    # Screenshot should be Log
    sas_program_editor.tab_group.screenshot(
        sas_program_editor.tab_group.selected_tab_page_text(Helper.data_locale.OUTPUT_DATA),
        "selected_tab_group3",
        user_assigned_xpath=True
    )

    print(sas_program_editor.tab_group.tag_group_layout_by_text(Helper.data_locale.OUTPUT_DATA))


def test_15_custom_code_tab_group_layout(page, init):
    """

    :param page:
    :param init:
    :return:
    """
    PageHelper.click_options(page, TopMenuItem.options_custom_code)

    custom_code_editor = PageHelper.create_plain_editor_factory().create_editor("custom", page)
    # NOTE: It seems that tab group might take several seconds to be loaded. Thus, time.sleep() was added.

    # custom_code_editor.wait_for_timeout(30*1000)
    # time.sleep(5)
    print("Tab-group1 Layout:" + custom_code_editor.tab_group.tag_group_layout_by_text(Helper.data_locale.LOG))
    print("Tab-group2 Layout:" + custom_code_editor.tab_group.tag_group_layout_by_text("选项"))

    time.sleep(5)
    # custom_code_editor.tab_group.nth_tab_page_by_text(Helper.data_locale.CODE, 2).click()
    custom_code_editor.tab_group.click_the_nth_tab_in_a_group_containing_text(Helper.data_locale.CODE, 2)
    time.sleep(5)
    custom_code_dialog = CustomCodeDialog(page)
    custom_code_dialog.save()
