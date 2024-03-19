"""
@File: test_sasserver_delete_single_01.py
@Author: Allison
@Date: 9/20/2023 4:41 AM 
@Description: 

"""
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_sas_server_delete_folder(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_server)
    folder_path = ["SAS Server", "Home", "tmp"]
    folder_name = 'ßüöéçàê中文测试íÍłŁňŇő'
    PageHelper.new_folder(page, 'Toolbar', folder_path, folder_name)

    folder_path = ["SAS Server", "Home", "tmp", "ßüöéçàê中文测试íÍłŁňŇő"]
    PageHelper.delete_single_item(page, 'Toolbar', folder_path)