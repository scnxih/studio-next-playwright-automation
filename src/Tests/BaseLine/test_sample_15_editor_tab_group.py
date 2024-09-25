"""
File: test_sample_15_editor_tab_group.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/29 14:47 
"""
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper

from src.Pages.StudioNext.Center.custom_step_page_test import CustomStepPageTest
from src.Pages.StudioNext.Center.flow_page_test import FlowPageTest
from src.Pages.StudioNext.Center.quick_import_page import QuickImportPage

from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem

from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog

def test_init(page,init):
    PageHelper.init_environments(page)
def test_01_sas_program_check_log(page, init):
    """
    Check log tab page after sas program run
    :param page:
    :param init:
    :return:
    """

    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    sas_program_editor.fill_text_area_with("proc print data = sashelp.cars; run;")

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
    autoexec_editor = PageHelper.create_plain_editor_factory().create_editor("autoexec", page)
    autoexec_editor.fill_text_area_with(text)

    autoexec_dialog = AutoexecDialog(page)
    autoexec_dialog.run()

    time.sleep(5)

    autoexec_dialog.tab_group.click_tab_by_text(Helper.data_locale.CODE)

    time.sleep(5)

    autoexec_dialog.save()

    # Clear input
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
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
    PageHelper.clear_customcode_thru_keyboard(page)


def test_04_flow_double_tabs(page, init):
    """
    Test double tab groups in flow
    :param page:
    :param init:
    :return:
    """
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_flow)

    flow_page = FlowPageTest(page)

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


def test_07_python_program_check(page, init):
    """
    Test python program outputdata page
    :param page:
    :param init:
    :return:
    """
    python_program_editor = PageHelper.create_program_editor_factory().create_program_editor("python", page)
    python_program_editor.fill_text_area_with("print('Hello, world!')")

    python_program_editor.toolbar.click_btn_by_title(Helper.data_locale.RUN)
    python_program_editor.wait_toast_disappear()
    python_program_editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

