from src.Pages.Common.dialog import *
from src.conftest import *
from src.Utilities.vars import *
from src.Helper.page_helper import *


def test_01_keyboard_shortcuts(page, init):
    page.click('//*[@href="#sas-svg-keyboardshortcuts"]')
    PageHelper.search_keyboard_shortcuts(page, "打开")
    PageHelper.clear_search_keyboard_shortcuts(page)
    PageHelper.close_keyboard_shortcuts(page)
