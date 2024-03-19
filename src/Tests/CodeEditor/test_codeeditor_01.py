from src.conftest import *


def test_01_save_program(page, init):
    PageHelper.new_sas_program(page)
    text = '''
    data test;
        set sashelp.class;
    run;'''
    PageHelper.type_code_in_codeeditor(page, text)
    folder_path = ["SAS 内容", "Public"]
    PageHelper.save_program(page, folder_path, "first.sas", True)

