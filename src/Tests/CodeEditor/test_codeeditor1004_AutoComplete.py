"""
File: test_codeeditor1004_AutoComplete.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2024/1/15 14:28 
"""
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_auto_complete(page, init):
    """
    :information: \\huanghe\VTG\ECT\TESTCASE\SAS Studio\6.0\Automated\2023Created\CodeEditor1004_AutoComplete.docx
    :param page:
    :param init:
    :return:
    """

    # Step-1: Create a *.sas program
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)

    # Step-2: Type partial contents to invoke library auto-completion
    editor.editor.type_into_text_area(
        "proc print data=sash")
    time.sleep(3)

    editor.key_press('e')

    time.sleep(3)

    editor.key_press('Enter')
    time.sleep(3)

    # Step-3: Autocomplete tables
    editor.key_press('.')
    time.sleep(3)
    editor.key_press('c')
    time.sleep(1)
    editor.key_press('l')
    time.sleep(1)
    editor.key_press('a')
    time.sleep(1)
    editor.key_press('Enter')

    # Step-4: Complete the sas program
    editor.key_press(';')

    editor.key_press('r')
    editor.key_press('u')
    editor.key_press('n')
    editor.key_press(';')
    time.sleep(3)

    # Step-5: Run the sas program
    editor.key_press('F3')

