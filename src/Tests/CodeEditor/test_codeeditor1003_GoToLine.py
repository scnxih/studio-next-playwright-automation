"""
File: test_codeeditor1003_GoToLine.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2024/1/12 14:54 
"""

import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_go_to_line(page, init):
    """

    :information: \\huanghe\vtg\ECT\TESTCASE\SAS Studio\6.0\Automated\2023Created\CodeEditor1003_GoToLine.docx
    :param page:
    :param init:
    :return:
    """

    # Create a *.sas program
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(
        "proc print data=sashelp.cars; \n run; \n proc print data=sashelp.class; \n run; \n proc print data=sashelp.air;run;")

    editor.key_press('Control+G')
    time.sleep(3)

    editor.widget.fill_input_by_placeholder("", "5")
    time.sleep(3)

    editor.key_press('Escape')
    time.sleep(3)
