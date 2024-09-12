"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@esas.com
Date: September 7th, 2023
"""
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Utilities.enums import TopMenuItem
# Rest of your code goes here...
from src.conftest import *

# ADDED
"""<<< Added by Jacky(ID: jawang) on Sept.7th, 2023 """

# ADDED
"""<<< Added by Jacky(ID: jawang) on Sept.11th, 2023 """
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog

""" Added by Jacky(ID: jawang) on Sept.11th, 2023 >>>"""


def test_01_central_editors(page, init):
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
    :param page:
    :param init:
    :return:
    """

    text = '''
    proc print data=sashelp.class;
    run;
    '''

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    # PageHelper.set_autoexec(page, text)
    autoexec_editor = PageHelper.create_plain_editor_factory().create_editor("autoexec", page)
    autoexec_editor.fill_text_area_with(text)

    autoexec_dialog = AutoexecDialog(page)
    autoexec_dialog.run()
    autoexec_dialog.save()
    # autoexec_dialog.close_dialog()


""" Added by Jacky(ID: jawang) on Sept.7th, 2023 >>>"""

# ADDED
"""<<< Added by Jacky(ID: jawang) on Sept.11th, 2023 """


def test_03_custom_code_editor(page, init):
    """
    Test code editor in custom code dialog
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


""" Added by Jacky(ID: jawang) on Sept.11th, 2023 >>>"""


# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.15th, 2023
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
    '''

    # Create a sas program
    sas_program_editor = PageHelper.create_program_editor_factory().create_program_editor("sas_program", page)

    # Fill text area with program
    sas_program_editor.fill_text_area_with(sas_program)

    ''' Obsolete API
    
    # Open SAS Program Code Editor Context Menu
    # sas_program_editor.open_context_menu()

    # Click Run from context menu
    # sas_program_editor.context_menu.click_menu_item_by_text(Helper.data_locale.RUN)

    '''

    # Revision: NOTE: xpath or locator haave to been properly chosen to make sure click() method used in
    # __invoke_context_menu  or __invoke_context_menu_by_right_click of base_page.py work

    # DOES NOT WORK: sas_program_editor.click_context_menu(sas_program_editor.editor_text_area.get_text_area(), Helper.data_locale.RUN)
    # DOES NOT WORK: page.click_context_menu_by_right_click("//div[contains(@data-testid, 'container')][contains(@class, 'EditorPane')]//textarea[@aria-label='编辑器内容, 按 Alt+F1 查看辅助功能选项。']", Helper.data_locale.RUN)
    # DOES NOT WORK: sas_program_editor.click_context_menu(sas_program_editor.editor_text_area.get_text_area(), Helper.data_locale.RUN)
    # DOES NOT WORK: sas_program_editor.click_context_menu_by_right_click("//div[contains(@data-testid, 'container')][contains(@class, 'EditorPane')]//textarea", Helper.data_locale.RUN)

    # WORKS FINE
    # sas_program_editor.click_context_menu_by_right_click(sas_program_editor.div_first_line, Helper.data_locale.RUN)

    # WORKS FINE
    sas_program_editor.click_context_menu(sas_program_editor.div_first_line, Helper.data_locale.RUN)

# Added by Jacky(ID: jawang) on Sept.15th, 2023 >>>
