"""
@Project ：studio-next-playwright-automation 
@File    ：test_openitems_01_saveall.py
@Author  ：Allison
@Date    ：8/20/2023 10:51 PM 
"""
import time

from src.Utilities.enums import AccordionType
from src.conftest import *
from playwright.sync_api import Page, expect
from src.Pages.Common.dialog import *


def test_01_saveall(page, init):
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)

    PageHelper.new_sas_program(page)
    text = "'中文测试2'"
    PageHelper.type_code_in_codeeditor(page, text)

    # PageHelper.new_flow(page)
    PageHelper.show_accordion(page, AccordionType.open_item)
    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    folder_path_list = [folder_path, folder_path]
    file_name_list = ["测试1", "测试2"]
    PageHelper.save_all_files(page, folder_path_list, file_name_list, True)
    # expect(page.get_by_text("文件“测试1.sas”保存成功。")).to_be_visible()

