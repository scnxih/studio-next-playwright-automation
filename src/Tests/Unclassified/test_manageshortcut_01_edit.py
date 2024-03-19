from src.conftest import *
from src.Utilities.vars import *
from src.Helper.page_helper import *
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import *


def test_01_manage_keyboard_shortcuts(page, init):
    PageHelper.click_options(page, TopMenuItem.options_manage_keyboard_shortcuts)
    PageHelper.mange_keyboard_reset_all(page)
    time.sleep(2)
    PageHelper.mange_keyboard_export_shortcuts(page)
    time.sleep(2)
    label = "打开:"
    PageHelper.mange_keyboard_input_shortcut(page, label, 1, 'Control+F6', 'cancel')
    time.sleep(2)
    PageHelper.mange_keyboard_input_shortcut(page, label, 1, 'Control+F6', 'reassign')
    time.sleep(2)
    PageHelper.mange_keyboard_input_shortcut(page, label, 1, 'Shift+F10', 'close')
    time.sleep(2)
    PageHelper.mange_keyboard_clear_shortcut(page, label, 1)
    time.sleep(2)
    PageHelper.mange_keyboard_reset_shortcut(page, label, 1)
    time.sleep(2)
    PageHelper.mange_keyboard_reset_all(page)
    time.sleep(2)
    PageHelper.mange_keyboard_check_help(page)
    time.sleep(2)
    PageHelper.mange_keyboard_save(page)
