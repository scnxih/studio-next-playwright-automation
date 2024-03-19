"""
File: test_codeeditor_07_widgets.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/9/20 14:05 
"""

import time
from src.conftest import *
from src.Utilities.enums import TopMenuItem
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog


def test_01_sas_program_editor_widget(page, init):
    """
    Test find function in code editor
    :param page:
    :param init:
    :return:
    """

    sas_program = '''
    data work.my_class;
        set sashelp.cars;
    run;
    '''

    # Create a sas program
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    # Fill text area with program
    sas_program_editor.fill_text_area_with(sas_program)


    ''' OBSOLETE
    # Open SAS Program Code Editor Context Menu again
    sas_program_editor.open_context_menu()

    # Click Find from context menu
    sas_program_editor.context_menu.click_menu_item_by_test_id("editorPane-find-text")
    '''
    sas_program_editor.click_context_menu(sas_program_editor.div_first_line, Helper.data_locale.FIND)

    # Fill in widget textarea
    sas_program_editor.widget.fill_textarea_by_placeholder("查找", "cars")

    # Toggle Match Case checkbox next to textarea widget
    sas_program_editor.widget.toggle_checkbox_by_title("区分大小写 (Alt+C)")
    # time.sleep(3)

    # Toggle Match Case checkbox next to textarea widget
    sas_program_editor.widget.toggle_checkbox_by_title("全字匹配 (Alt+W)")
    # time.sleep(3)

    # Click Toggle Replace button
    sas_program_editor.widget.click_btn_by_title("切换替换")

    # Fill in widget textarea
    sas_program_editor.widget.fill_textarea_by_placeholder("替换", "class")

    # Click toggle button
    sas_program_editor.widget.click_btn_by_title("替换 (Enter)")

    # Click close button
    sas_program_editor.widget.click_btn_by_aria_label("关闭 (Escape)")

    # Close widget by keyboard action
    # sas_program_editor.key_press('Escape')

    # Arouse Go-to-line widget
    sas_program_editor.key_press('Control+G')

    # Fill in widget input
    sas_program_editor.widget.fill_input_by_placeholder("", "3")

    # Close widget by keyboard action
    sas_program_editor.key_press('Escape')

    ''' OBSOLETE
    # Open SAS Program Code Editor Context Menu again
    sas_program_editor.open_context_menu()

    # Click Find from context menu
    sas_program_editor.context_menu.click_menu_item_by_test_id("editorPane-commands-text")
    '''
    sas_program_editor.click_context_menu(sas_program_editor.div_first_line, "命令面板")

    # Fill in widget input
    sas_program_editor.widget.fill_input_by_placeholder("", ">")


def test_02_custom_code_dialog_widget(page, init):
    """
    Test widgets in custom code dialog
    :param page:
    :param init:
    :return:
    """

    text = '''
    proc print data=sashelp.class;
    run;
    '''

    # Arouse Custom Code Dialog
    PageHelper.click_options(page, TopMenuItem.options_custom_code)

    # Editor Instance
    custom_code_editor = PageHelper.create_plain_editor_factory().create_editor("custom", page)
    # Type in Code
    custom_code_editor.fill_text_area_with(text)

    # Dialog Instance
    custom_code_dialog = CustomCodeDialog(page)

    # Arouse context menu
    # custom_code_editor.open_context_menu()

    ''' OBSOLETE
    custom_code_editor.context_menu.click_menu_item_by_test_id("editorPane-find-text")
    '''
    custom_code_editor.click_context_menu(custom_code_editor.div_first_line, Helper.data_locale.FIND)

    # Fill in widget textarea
    custom_code_editor.widget.fill_textarea_by_placeholder("查找", "cars")

    # Toggle Match Case checkbox next to textarea widget
    custom_code_editor.widget.toggle_checkbox_by_title("区分大小写 (Alt+C)")
    # time.sleep(3)

    # Toggle Match Case checkbox next to textarea widget
    custom_code_editor.widget.toggle_checkbox_by_title("全字匹配 (Alt+W)")
    # time.sleep(3)

    # Click Toggle Replace button
    custom_code_editor.widget.click_btn_by_title("切换替换")

    # Fill in widget textarea
    custom_code_editor.widget.fill_textarea_by_placeholder("替换", "class")

    # Click toggle button
    custom_code_editor.widget.click_btn_by_title("替换 (Enter)")

    # Click close button
    custom_code_editor.widget.click_btn_by_aria_label("关闭 (Escape)")

    # Close custom code dialog
    custom_code_dialog.save()

