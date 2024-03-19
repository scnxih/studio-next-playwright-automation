"""
@File: test_sasserver_delete_multiple_01.py
@Author: Allison
@Date: 9/21/2023 4:16 AM 
@Description: 

"""
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_sas_server_delete_multiple_folders(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_server)
    folder_path = ["SAS Server", "Home", "tmp"]
    folder_name1 = "文件夹ŚrŻłßü1"
    folder_name2 = "文件夹ŚrŻłßü2"
    folder_name3 = "测试"
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name1)
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name2)
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name3)

    folder_path1 = ["SAS Server", "Home", "tmp", "文件夹ŚrŻłßü1"]
    folder_path2 = ["SAS Server", "Home", "tmp", "文件夹ŚrŻłßü2"]
    folder_path3 = ["SAS Server", "Home", "tmp", "ßüöéçàê中文", "测试"]
    folder_path = [folder_path1, folder_path2, folder_path3]
    PageHelper.delete_multiple_items(page, 'ContextMenu', folder_path)