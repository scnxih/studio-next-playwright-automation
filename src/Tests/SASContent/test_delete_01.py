"""
@Project: studio-next-playwright-automation 
@File: test_delete_01.py
@Author: Allison
@Date: 9/1/2023 3:06 AM 

"""
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_sas_content_delete_folder(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_content)
    folder_path1 = ["SAS Content", "Public"]
    folder_name1 = "测试íÍłŁňŇő"
    PageHelper.new_folder(page, 'ContextMenu', folder_path1, folder_name1)

    folder_path = ["SAS Content", "Public", "测试íÍłŁňŇő"]
    PageHelper.delete_single_item(page, 'Toolbar', folder_path)


def test_02_sas_content_delete_file(page, init):
    PageHelper.new_sas_program(page)
    text = "/* 中文测试自动化测试한국어日本語のふpolskiŚrŻł */"
    PageHelper.type_code_in_codeeditor(page, text)
    folder_path = ["SAS 内容", "Public"]

    PageHelper.save_program(page, folder_path, "自动化한국어日本語のふpolskiŚrŻłßüöéçàê.sas", True)
    file_path = ["SAS Content", "Public", "自动化한국어日本語のふpolskiŚrŻłßüöéçàê.sas"]
    PageHelper.delete_single_item(page, 'Toolbar', file_path)
