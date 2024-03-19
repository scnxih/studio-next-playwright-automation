"""
@File: test_sasserver_folder_properties_01.py
@Author: Allison
@Date: 9/25/2023 4:59 AM 
@Description: 

"""
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_folder_properties(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_server)
    folder_path = ["SAS Server", "Home", "tmp"]
    folder_name = 'ßüöéçàê中文𠀀𠀁𠀂𠀃𠀄𪛔𪛕𪛖'
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name)

    PageHelper.close_all_tabs(page)

    file_path = ["SAS Server", "Home", "tmp", "ßüöéçàê中文𠀀𠀁𠀂𠀃𠀄𪛔𪛕𪛖"]
    PageHelper.show_properties(page, 'ContextMenu', file_path)
