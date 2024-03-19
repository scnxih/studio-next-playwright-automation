from src.conftest import *


def test_01_show_tabs(page, init):
    PageHelper.new_all_items(page)


def test_02_show_accordion(page, init):
    PageHelper.show_all_accordion(page)
