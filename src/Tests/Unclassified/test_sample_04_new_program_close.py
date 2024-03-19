from src.conftest import *


def new_program_and_type_code(page):
    PageHelper.new_sas_program(page)
    text = '''
data test;
    set sashelp.class;
run;'''
    PageHelper.type_code_in_codeeditor(page, text)


def test_01_type_code(page, init):
    for i in range(3):
        new_program_and_type_code(page)
    PageHelper.close_all_tabs(page)
