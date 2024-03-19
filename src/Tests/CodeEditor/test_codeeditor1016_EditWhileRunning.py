"""
File: test_codeeditor1016_EditWhileRunning.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2024/1/16 15:07 
"""

import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_edit_while_running(page, init):
    """
    :info: \\huanghe\VTG\ECT\TESTCASE\SAS Studio\6.0\Automated\2023Created\CodeEditor1016_EditWhileRunning.docx
    :param page:
    :param init:
    :return:
    """

    # Step-1: Create a *.sas program
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)

    editor.editor.type_into_text_area(
        "data _null_;\nx=sleep(10000);\nrun;")

    # Step-2: Run the program and edit
    editor.run(True)
    editor.editor.type_into_text_area(
        "proc print\ndata=sashelp.class;\nrun;")

    # Cancel program running
    # editor.toolbar.click_btn_by_title(Helper.data_locale.CANCEL)
    editor.cancel(False)

    # Wait 3 seconds, otherwise would not work
    time.sleep(3)

    # Run the program again
    editor.run(True)

    # Wait 3 seconds, otherwise would not work
    # time.sleep(3)

    # editor.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)
    editor.open_in_browser_tab_results()


