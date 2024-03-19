"""
File: test_codeeditor1001_clearlog.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/30 14:46 
"""

import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_clear_log(page, init):
    """
    Run a *.sas program and clear log
    NOTE: In StudioNext the 'Clear/Log' is always enabled
    :information: \\huanghe\VTG\ECT\TESTCASE\SAS Studio\6.0\Automated\2023Created\CodeEditor1001_ClearLog.docx
    :param page:
    :param init:
    :return:
    """
    # Create a *.sas program
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")

    editor.run(True)
    # editor.screenshot_critical(editor.editor, 'ProgramEditor')

    editor.tab_group.click_tab_by_text(Helper.data_locale.LOG)
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "before_clear_log", user_assigned_xpath=True)
    editor.clear_log()
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "after_clear_log", user_assigned_xpath=True)

    editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "before_clear_results", user_assigned_xpath=True)
    editor.clear_results()
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "after_clear_results", user_assigned_xpath=True)

    editor.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA)
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "before_clear_output", user_assigned_xpath=True)
    editor.clear_output_data()
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "after_clear_output", user_assigned_xpath=True)

    editor.clear_code()
    time.sleep(3)
    editor.screenshot_critical(editor.base_xpath, "after_clear_code", user_assigned_xpath=True)

