"""
File: test_sample_13_editor_save_files.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/29 11:31 
"""
from src.Pages.StudioNext.Center.codeeditor_page import CodeEditorPage
from src.conftest import *


def test_init(page, init):
    PageHelper.init_environments(page)


def test_01_save_all_files(page, init):
    """
    Save *.xml *.json *.text *.workspace to SAS/Content/Public
    :param page:
    :param init:
    :return:
    """
    # folder_path = ["SAS 内容", "Public"]
    folder_path = Helper.public_folder_path
    # folder_path = ["SAS Content", "Public"]

    xml_editor = PageHelper.create_plain_editor_factory().create_editor("xml", page)
    xml_editor.fill_text_area_with("<html></html>")
    xml_editor.save_file(folder_path, "plain_factory_xml_file.xml", True)

    json_editor = PageHelper.create_plain_editor_factory().create_editor("json", page)
    json_editor.save_file(folder_path, "plain_factory_json_file.json", True)

    text_editor = PageHelper.create_plain_editor_factory().create_editor("text", page)
    text_editor.save_file(folder_path, "plain_factory_text_file.txt", True)

    wksp_editor = PageHelper.create_plain_editor_factory().create_editor("workspace", page)
    wksp_editor.save_file(folder_path, "plain_factory_workspace_file.workspace", True)


def test_02_save_program_files(page, init):
    """
    Save *.sas *.py to SAS Content
    :param page:
    :param init:
    :return:
    """
    # folder_path = ["SAS 内容", "Public"]
    folder_path = Helper.public_folder_path
    # folder_path = ["SAS Content", "Public"]

    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    sas_program_editor.save_file(folder_path, "program_factory_sas_program_file.sas", True)

    python_program_editor = PageHelper.create_program_editor_factory().create_program_editor("python", page)
    python_program_editor.save_file(folder_path, "program_factory_python_program_file.py", True)
