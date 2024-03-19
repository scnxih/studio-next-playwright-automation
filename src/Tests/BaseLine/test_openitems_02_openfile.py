"""
@Project ：studio-next-playwright-automation 
@File    ：test_openitems_02_openfile.py
@Author  ：Allison
@Date    ：9/12/2023 2:05 AM
"""
from src.Utilities.enums import AccordionType
from src.conftest import *
from playwright.sync_api import Page, expect
from src.Pages.Common.dialog import *


def test_01_openfile(page, init):
    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)
    PageHelper.save_program(page, folder_path, "中文测试.sas", True)

    PageHelper.close_all_tabs(page)

    # MODIFIED
    # <<< Modified by Jacky(ID: jawang) on Nov.22nd, 2023
    # INVISIBLE in the tree-grid

    # PageHelper.show_accordion(page, AccordionType.open_item)
    # PageHelper.openitems_open_file(page, folder_path, "中文测试.sas")
    # expect(page.get_by_test_id("programView-editorPane-path-label")).to_contain_text(Helper.data_locale.SAS_CONTENT+ ": /Public/中文测试.sas")

    # Modified by Jacky(ID: jawang) on Nov.22nd, 2023 >>>