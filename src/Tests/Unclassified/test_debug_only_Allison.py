from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_temp(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_content)
    folder_path = ["SAS Content", "Public"]
    folder_path1 = ["SAS Content", "Public", "ßüöéçàê中文"]
    folder_name1 = "文件夹ŚrŻłßü1"
    folder_name2 = "文件夹ŚrŻłßü2"
    folder_name3 = "测试"
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name1)
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name2)
    PageHelper.new_folder(page, 'ContextMenu', folder_path1, folder_name3)

    folder_path1 = ["SAS Content", "Public", "文件夹ŚrŻłßü1"]
    folder_path2 = ["SAS Content", "Public", "文件夹ŚrŻłßü2"]
    folder_path3 = ["SAS Content", "Public", "ßüöéçàê中文", "测试"]
    folder_path = [folder_path1, folder_path2, folder_path3]
    PageHelper.delete_multiple_items(page, 'ContextMenu', folder_path)
