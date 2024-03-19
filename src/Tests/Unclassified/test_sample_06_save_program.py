from src.conftest import *


def test_01_save_program(page, init):
    PageHelper.new_sas_program(page)
    text = "data test;\n set sashelp.class;\n run;"
    PageHelper.type_code_in_codeeditor(page, text)
    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]

    PageHelper.save_program(page, folder_path, "first.sas", True)
#     test for git again ...
