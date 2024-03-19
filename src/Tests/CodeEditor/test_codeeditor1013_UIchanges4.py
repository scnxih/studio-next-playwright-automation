"""
File: test_codeeditor1013_UIchanges4.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2024/1/16 10:22 
"""
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_uichanges4(page, init):
    """
    :information: \\huanghe\VTG\ECT\TESTCASE\SAS Studio\6.0\Automated\2023Created\CodeEditor1013_UIchanges4.docx
    :param page:
    :param init:
    :return:
    """

    # Step-1.1: Create a *.sas program
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)

    # Step-1.1: Type into textarea
    editor.editor.type_into_text_area(
        "/*这是测试*/\nproc print\ndata=sashelp.class;\nrun;")

    # Step-1.2: Run the program
    editor.run(True)

    # Step-2.1: Click the overflow button in the right upper corner.
    # Step-2.2: Hover the mouse on Open in a browser tab.

    editor.open_in_browser_tab_log()
    editor.open_in_browser_tab_results()
    editor.open_in_browser_tab_code()
    editor.open_in_browser_tab_listing()
    editor.open_in_browser_tab_summary()
    # time.sleep(3)

    # Set status to zero, otherwise error would occur.
    # editor.tab_group.click_tab_by_text(Helper.data_locale.LOG)

    # Step-3.1: Hover the mouse on Print
    # editor.toolbar.click_menu_in_more_options(Helper.data_locale.PRINT)
    # time.sleep(3)

    # Set status to zero, otherwise error would occur.
    # editor.tab_group.click_tab_by_text(Helper.data_locale.LOG)

    # Step-4.1: Hover the mouse on Download
    # Works now, but comment out to keep control consistent.
    # editor.toolbar.click_menu_in_more_options(Helper.data_locale.DOWNLOAD)
    # time.sleep(3)

    editor.download_code_file()
    editor.download_log_file_html()
    editor.download_log_file_text()
    editor.download_results_file()
    editor.download_listing_file()

    # Set status to zero, otherwise error would occur.
    # editor.tab_group.click_tab_by_text(Helper.data_locale.LOG)
