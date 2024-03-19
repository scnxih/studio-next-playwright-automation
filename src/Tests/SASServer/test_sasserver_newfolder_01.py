"""
@File: test_sasserver_newfolder_01
@Author: Allison
@Date: 9/20/2023 4:31 AM 
@Description: 

"""
from src.Helper.page_helper import PageHelper
from src.Utilities.enums import AccordionType


def test_01_sas_server_new_folder(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_server)
    folder_path = ["SAS Server", "Home", "tmp"]
    folder_name = 'ßüöéçàê中文'
    PageHelper.new_folder(page, 'Toolbar', folder_path, folder_name)
