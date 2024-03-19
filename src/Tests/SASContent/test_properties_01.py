"""
@File: test_properties_01.py
@Author: Allison
@Date: 9/15/2023 4:28 AM 
@Description: 

"""
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_file_properties(page, init):
    PageHelper.new_sas_program(page)
    text = "'𠀀𠀁𠀂𠀃𠀄𪛔𪛕𪛖文件한국어のふaAkiŚŻłßüöéçàê'"
    PageHelper.type_code_in_codeeditor(page, text)

    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    PageHelper.save_program(page, folder_path,'𠀀𠀁𠀂𠀃𠀄𪛔𪛕𪛖文件한국어のふaAkiŚŻłßüöéçàê', True)

    PageHelper.close_all_tabs(page)

    file_path = ["SAS Content", "Public", "𠀀𠀁𠀂𠀃𠀄𪛔𪛕𪛖文件한국어のふaAkiŚŻłßüöéçàê.sas"]
    PageHelper.show_accordion(page, AccordionType.sas_content)
    PageHelper.show_properties(page, 'Toolbar', file_path)