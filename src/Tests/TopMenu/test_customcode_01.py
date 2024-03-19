from src.conftest import *
from src.Utilities.enums import *


def set_customcode(page, text, tabenum):
    PageHelper.click_options(page, TopMenuItem.options_custom_code)
    PageHelper.set_customcode(page, text, tabenum)


def set_option(page):
    PageHelper.click_options(page, TopMenuItem.options_custom_code)
    PageHelper.set_option(page)


def test_01_set_front_customcode(page, init):
    text = '''
    proc print data=sashelp.class;
    run;
    '''
    set_customcode(page, text, DialogTab.Tab_front)


def test_02_set_back_customcode(page, init):
    text = '''
    data test;
        set sashelp.cars;
    run;
    '''
    set_customcode(page, text, DialogTab.Tab_back)


def test_03_set_option(page, init):
    set_option(page)


def test_04_clear_customcode(page, init):
    PageHelper.clear_customcode(page)
