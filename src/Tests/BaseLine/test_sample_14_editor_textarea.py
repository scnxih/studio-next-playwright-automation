"""
File: test_sample_14_editor_textarea.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/29 14:26 
"""
import time

from src.conftest import *
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog


def test_init(page, init):
    PageHelper.init_environments(page)


def test_01_central_editors(page, init):
    """
    Fill the central editor with text
    :param page:
    :param init:
    :return:
    """
    folder_path = ["SAS 内容", "Public"]
    # folder_path = ["SAS Content", "Public"]

    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)
    sas_program_editor.fill_text_area_with("proc print data = sashelp.cars; run;")
    sas_program_editor.save_file(folder_path, "program_factory_sas_program_file.sas", True)

    python_program_editor = PageHelper.create_program_editor_factory().create_program_editor("python", page)
    python_program_editor.fill_text_area_with("print('Hello, world!')")
    python_program_editor.save_file(folder_path, "program_factory_python_program_file.py", True)

    xml_editor = PageHelper.create_plain_editor_factory().create_editor("xml", page)
    xml_editor.fill_text_area_with("<html></html>")
    xml_editor.save_file(folder_path, "plain_factory_xml_file.xml", True)

    json_editor = PageHelper.create_plain_editor_factory().create_editor("json", page)
    json_editor.fill_text_area_with("{key: 'value'}")
    json_editor.save_file(folder_path, "plain_factory_json_file.json", True)

    text_editor = PageHelper.create_plain_editor_factory().create_editor("text", page)
    text_editor.fill_text_area_with("This is a text file.")
    text_editor.save_file(folder_path, "plain_factory_text_file.txt", True)

    wksp_editor = PageHelper.create_plain_editor_factory().create_editor("workspace", page)
    wksp_editor.fill_text_area_with("This is workspace file.")
    wksp_editor.save_file(folder_path, "plain_factory_workspace_file.workspace", True)


def test_02_autoexec_editor(page, init):
    """
    Test editor Autoexec editor
    :param page:
    :param init:
    :return:
    """
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    autoexec_editor = PageHelper.create_plain_editor_factory().create_editor("autoexec", page)
    # autoexec_editor.fill_text_area_with(text)
    autoexec_editor.editor_text_area.human_mimic_typing("%macro print_current_date_with_weekday;\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%let current_date_num = %sysfunc(date());\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%let current_date = "
                                                        "%sysfunc(putn(&current_date_num, yymmdd10.), $10.);\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%let weekday = "
                                                        "%sysfunc(putn(&current_date_num, Weekdate.), $3.);\n")

    autoexec_editor.editor_text_area.human_mimic_typing("\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%put Current Date (YYYY-MM-DD): &current_date;\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%put Weekday: &weekday;\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%mend;\n")
    autoexec_editor.editor_text_area.human_mimic_typing("\n")
    autoexec_editor.editor_text_area.human_mimic_typing("%print_current_date_with_weekday;\n")

    autoexec_dialog = AutoexecDialog(page)
    autoexec_dialog.run()
    autoexec_dialog.click_tab_log()
    autoexec_dialog.selfie('autoexec_log')
    autoexec_dialog.save()


def test_03_custom_code_editor(page, init):
    """
    Test code editor in Custom Code dialog
    :param page:
    :param init:
    :return:
    """

    text = '''
    proc print data=sashelp.class;
    run;
    '''

    PageHelper.click_options(page, TopMenuItem.options_custom_code)
    custom_code_editor = PageHelper.create_plain_editor_factory().create_editor("custom", page)
    custom_code_editor.fill_text_area_with(text)
    #
    custom_code_dialog = CustomCodeDialog(page)
    custom_code_dialog.run()
    custom_code_dialog.save()


def test_04_editor_context_menu(page, init):
    """
    Test context menu in text area
    :param page:
    :param init:
    :return:
    """
    sas_program = '''
    data work.my_class;
        set sashelp.class;
    run;
    data null;
    call sleep(5,1);
    run;
    '''

    # Create a sas program
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    # Fill text area with program
    sas_program_editor.fill_text_area_with(sas_program)

    # WORKS FINE
    sas_program_editor.click_context_menu(sas_program_editor.div_first_line, Helper.data_locale.RUN)
    sas_program_editor.wait_until_enabled(sas_program_editor.toolbar.btn_by_title(Helper.data_locale.RUN))
