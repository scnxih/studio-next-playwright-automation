"""
File: test_sample_17_editor_context_menu.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/29 15:16 
"""
from src.conftest import *
from src.Utilities.enums import TopMenuItem
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.Common.menu_page import MenuPage

def test_init(page,init):
    PageHelper.init_environments(page)
def test_01_sas_program_editor_context_menu(page, init):
    """
    Test context menu in text area
    Scenario: run a program and arouse find widget from context menu
    """

    sas_program = '''
    data work.my_class;
        set sashelp.class;
    run;
    '''

    # Create a sas program
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    # Fill text area with program
    sas_program_editor.fill_text_area_with(sas_program)
    # sas_program_editor.click_context_menu_by_right_click()
    # MenuPage(page).screenshot_self("editor_context_menu")


    # Click Run from context menu
    sas_program_editor.click_context_menu(sas_program_editor.div_first_line, Helper.data_locale.RUN)
    sas_program_editor.click_context_menu(sas_program_editor.div_first_line, Helper.data_locale.FIND)


def test_02_custom_code_dialog_context_menu(page, init):
    """
    Test editor context menu in custom code dialog
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

    # Run code in Preamble
    custom_code_editor.click_context_menu(custom_code_editor.div_first_line, Helper.data_locale.RUN)

    # Switch to Postamble tab page
    custom_code_dialog.tab_group.click_tab_by_text("后置代码")

    # Click the code tab page with horizontal tab groups
    # Otherwise code cannot be typed into
    custom_code_dialog.tab_group.click_tab_by_text(Helper.data_locale.CODE)
    custom_code_editor.fill_text_area_with(text)

    custom_code_editor.click_context_menu(custom_code_editor.div_first_line, Helper.data_locale.RUN)

    # Close custom code dialog
    custom_code_dialog.save()


def test_03_autoexec_dialog_context_menu(page, init):
    """
    Test context menu in Autoexec Dialog
    :param page:
    :param init:
    :return:
    """

    text = '''
    proc print data=sashelp.class;
    run;
    '''

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)

    autoexec_editor = PageHelper.create_plain_editor_factory().create_editor("autoexec", page)
    autoexec_editor.fill_text_area_with(text)
    autoexec_editor.click_context_menu(autoexec_editor.div_first_line, Helper.data_locale.RUN)

    autoexec_dialog = AutoexecDialog(page)
    autoexec_dialog.save()
