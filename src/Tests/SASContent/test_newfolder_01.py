"""
@Project: studio-next-playwright-automation 
@File: test_newfolder_01.py
@Author: Allison
@Date: 8/25/2023 4:54 AM 

"""
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_sas_content_new_folder(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_content)
    folder_path1 = ["SAS Content", "Public"]
    folder_path2 = ["SAS Content", "Public", "ßüöéçàê中文"]
    folder_name1 = 'ßüöéçàê中文'
    folder_name2 = "测试íÍłŁňŇő"
    PageHelper.new_folder(page, 'Toolbar', folder_path1, folder_name1)
    PageHelper.new_folder(page, 'ContextMenu', folder_path2, folder_name2)
