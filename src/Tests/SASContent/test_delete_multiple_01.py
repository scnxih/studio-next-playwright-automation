"""
@Project: studio-next-playwright-automation 
@File: test_delete_multiple_01.py
@Author: Allison
@Date: 9/15/2023 2:02 AM

"""
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_sas_content_delete_multiple_folders(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_content)
    folder_path = ["SAS Content", "Public"]
    folder_name1 = "文件夹ŚrŻłßü1"
    folder_name2 = "文件夹ŚrŻłßü2"
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name1)
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name2)

    folder_path1 = ["SAS Content", "Public", "文件夹ŚrŻłßü1"]
    folder_path2 = ["SAS Content", "Public", "文件夹ŚrŻłßü2"]
    folder_path = [folder_path1, folder_path2]
    PageHelper.delete_multiple_items(page, 'ContextMenu', folder_path)


def test_02_sas_content_delete_multiple_files(page, init):
    PageHelper.new_sas_program(page)
    text = "'文件夹ŚrŻłßü1'"
    PageHelper.type_code_in_codeeditor(page, text)

    PageHelper.new_sas_program(page)
    text = "'文件夹ŚrŻłßü2'"
    PageHelper.type_code_in_codeeditor(page, text)

    PageHelper.show_accordion(page, AccordionType.open_item)
    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    folder_path_list = [folder_path, folder_path]
    file_name_list = ["𠀀𠀁𠀂𠀃𠀄文件kiŚŻłß1", "𠀀𠀁𠀂𠀃𠀄文件kiŚŻłß2"]
    PageHelper.save_all_files(page, folder_path_list, file_name_list, True)

    PageHelper.close_all_tabs(page)

    PageHelper.show_accordion(page, AccordionType.sas_content)
    folder_path1 = ["SAS Content", "Public", "𠀀𠀁𠀂𠀃𠀄文件kiŚŻłß1.sas"]
    folder_path2 = ["SAS Content", "Public", "𠀀𠀁𠀂𠀃𠀄文件kiŚŻłß2.sas"]
    folder_path = [folder_path1, folder_path2]
    PageHelper.delete_multiple_items(page, 'Toolbar', folder_path)