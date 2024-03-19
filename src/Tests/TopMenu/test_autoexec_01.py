from src.Utilities.enums import TopMenuItem
from src.conftest import *


def set_autoexec(page,text):
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    PageHelper.set_autoexec(page, text)


def test_01_set_autoexec(page, init):
    text = '''
proc print data=sashelp.class;
run;
'''
    set_autoexec(page,text)
    text = '''
data test;
    set sashelp.cars;
run;
'''
    set_autoexec(page,text)


def test_02_clear_autoexec(page, init):
    PageHelper.clear_autoexec(page)
