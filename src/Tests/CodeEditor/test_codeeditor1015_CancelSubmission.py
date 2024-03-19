"""
File: test_codeeditor1015_CancelSubmission.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2024/1/16 11:30 
"""
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_cancel_submission(page, init):
    """
    :info: \\huanghe\VTG\ECT\TESTCASE\SAS Studio\6.0\Automated\2023Created\CodeEditor1015_CancelSubmission.docx
    :param page:
    :param init:
    :return:
    """

    # Step-1: Create a sas program that would take a long time to run
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)

    editor.editor.type_into_text_area("data _null_;\nx=sleep(30000);\nrun;")

    # Step-2: Run the program
    editor.run(True)
    time.sleep(3)

    # Step-3: Cancel the submission
    # editor.toolbar.click_btn_by_title(Helper.data_locale.CANCEL)
    editor.cancel(False)
