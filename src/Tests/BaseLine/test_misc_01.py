from src.Pages.StudioNext.Center.codeeditor_page import CodeEditorPage
from src.conftest import *
from src.Pages.Common.text import *
from src.Helper.page_factory import *

def test_init(page,init):
    PageHelper.init_environments(page)
def new_program_and_type_code(page):
    PageHelper.new_sas_program(page)
    text = '''
data test;
    set sashelp.class;
run;'''
    PageHelper.type_code_in_codeeditor(page, text)


def test_01_type_code(page, init):
    new_program_and_type_code(page)
    PageHelper.close_all_tabs(page)
    PageHelper.show_accordion(page, AccordionType.open_item)


def test_02_save_program(page, init):
    PageHelper.new_sas_program(page)
    text = '''
    data test;
        set sashelp.class;
    run;'''
    PageHelper.type_code_in_codeeditor(page, text)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    PageHelper.save_program(page, Helper.public_folder_path, "first.sas", True)


def test_03_screenshot(page, init):
    # global_screenshot_level = "middle"
    PageHelper.new_sas_program(page)

    code = CodeEditorPage(page)
    code.type_code_in_codeeditor("ttt")
    time.sleep(1)
    code.page.screenshot(path="page.png")
    code.locate_xpath("//textarea[@aria-label='" + Helper.data_locale.EDITOR_CONTENT + "']").screenshot(
        path="textarea.png")
    code.locate_xpath("//textarea[@aria-label='" + Helper.data_locale.EDITOR_CONTENT + "']/..").screenshot(
        path="parent_div.png")

    # code.textarea_codeeditor.screenshot(path="a.png")
    time.sleep(1)


def test_04_page_base_locator(page, init):
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    auto = AutoexecDialog(page)
    auto.base_locator.screenshot(path="auto.png")
    auto.cancel()
    Helper.logger.debug("auto base path=" + auto.base_xpath)

    PageHelper.show_accordion(page, AccordionType.sas_server)
    server = SASServerPage(page)

    Helper.logger.debug("sas server base path= " + server.base_xpath)
    server.base_locator.screenshot(path="sas_server.png")


def test_05_page_base_locator_2(page, init):
    PageHelper.new_sas_program(page)
    code = CodeEditorPage(page)
    code.base_locator.screenshot(path="code_editor.png")


def test_06_type_code(page, init):
    for i in range(3):
        new_program_and_type_code(page)

    PageHelper.close_all_tabs(page)


def test_07_save_program(page, init):
    PageHelper.new_sas_program(page)
    text = '''
    data test;
        set sashelp.class;
    run;'''
    PageHelper.type_code_in_codeeditor(page, text)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    PageHelper.save_program(page, Helper.public_folder_path, "first.sas", True)


def test_08_screenshot(page, init):
    # global_screenshot_level = "middle"
    PageHelper.new_sas_program(page)

    code = CodeEditorPage(page)
    code.type_code_in_codeeditor("ttt")
    time.sleep(1)
    code.page.screenshot(path="page.png")
    code.locate_xpath("//textarea[@aria-label='" + Helper.data_locale.EDITOR_CONTENT + "']").screenshot(
        path="textarea.png")
    code.locate_xpath("//textarea[@aria-label='" + Helper.data_locale.EDITOR_CONTENT + "']/..").screenshot(
        path="parent_div.png")

    # code.textarea_codeeditor.screenshot(path="a.png")
    time.sleep(1)


def test_09_page_base_locator(page, init):
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    auto = AutoexecDialog(page)
    auto.base_locator.screenshot(path="auto.png")
    auto.cancel()
    Helper.logger.debug("auto base path=" + auto.base_xpath)

    PageHelper.show_accordion(page, AccordionType.sas_server)
    server = SASServerPage(page)

    Helper.logger.debug("sas server base path= " + server.base_xpath)
    server.base_locator.screenshot(path="sas_server.png")


def test_10_page_base_locator_2(page, init):
    PageHelper.new_sas_program(page)
    code = CodeEditorPage(page)
    code.base_locator.screenshot(path="code_editor.png")


def test_11_save(page, init):
    PageHelper.new_sas_program(page)
    text = "data test;\n set sashelp.class;\n run;"
    PageHelper.type_code_in_codeeditor(page, text)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    PageHelper.save_program(page, Helper.public_folder_path, "first.sas", True)


"""Comment this test case since open file does not work now """
# def test_13_sas_content_tree_nova_aggrid(page, init):
#     PageHelper.new_sas_program(page)
#     text = "data test;\n set sashelp.class;\n run;"
#     PageHelper.type_code_in_codeeditor(page, text)
#     folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
#     PageHelper.save_program(page, folder_path, "first.sas", True)
#     time.sleep(1)
#     PageHelper.new_sas_program(page)
#     text = "data test;\n set sashelp.class;\n run;"
#     PageHelper.type_code_in_codeeditor(page, text)
#     folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
#     PageHelper.show_accordion(page, AccordionType.sas_content)
#     folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
#     PageHelper.save_program(page, folder_path, "second.sas", True)
#     time.sleep(1)
#     PageHelper.close_all_tabs(page)
#     folder_file_path = [Helper.data_locale.SAS_CONTENT, "Public", "first.sas"]
#     sas_content = SASContentPage(page)
#     sas_content.open_file(folder_file_path)
#     time.sleep(1)
#     sas_content.delete_file(folder_file_path)
#     time.sleep(1)

"""Comment this test case since open file does not work now """


# def test_14_sas_server_tree_aggrid_scroll(page, init):
#     PageHelper.show_accordion(page, AccordionType.sas_server)
#     folder_file_path = ["SAS Server", "Home", "segatest", "I18N", "自动化测试_SASCompute", "CLASS_中文_U8.txt"]
#     sas_server = SASServerPage(page)
#     sas_server.open_file(folder_file_path)
#     time.sleep(2)


def test_12_sas_server_tree_aggrid_combobox(page, init):
    PageHelper.new_sas_program(page)
    text = "data test;\n set sashelp.class;\n run;"
    PageHelper.type_code_in_codeeditor(page, text)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    PageHelper.save_program_test_tile_view_combobox(page, Helper.public_folder_path, "first.sas", True)


def test_13_other_method(page, init):
    # PageHelper.new_flow(page)
    # PageHelper.search_keyboard_shortcuts(page)

    PageHelper.new_sas_program(page)
    text = "'中文测试1'"
    PageHelper.type_code_in_codeeditor(page, text)

    PageHelper.new_sas_program(page)
    text = "'中文测试2'"
    PageHelper.type_code_in_codeeditor(page, text)
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)
    PageHelper.new_sas_program(page)
    text = "'中文测试'"
    PageHelper.type_code_in_codeeditor(page, text)

    # PageHelper.new_flow(page)
    PageHelper.show_accordion(page, AccordionType.open_item)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    folder_path_list = [folder_path, folder_path, folder_path, folder_path, folder_path, folder_path, folder_path]
    file_name_list = ["测试1", "测试2", "测试3", "测试4", "测试5", "测试6", "测试7"]
    PageHelper.save_all_files(page, folder_path_list, file_name_list, True)


def test_14_textarea(page, init):
    PageHelper.new_sas_program(page)
    page1: Page = page

    textarea = "//textarea[@aria-label='" + Helper.data_locale.EDITOR_CONTENT + "']"

    xpath1 = "xpath=" + textarea
    xpath1_parent = xpath1 + "/.."

    xpath2 = "xpath=//div[contains(@class,'monaco-editor no-user-select  showUnused showDeprecated vs')]" + textarea
    xpath2_parent = xpath2 + "/.."

    xpath3 = "xpath=//div[@data-testid='programView-editorPane-editor']" + textarea
    xpath3_parent = xpath3 + "/.."

    loc1 = page1.locator(xpath1)
    loc2 = page1.locator(xpath2)
    loc3 = page1.locator(xpath3)

    loc1.fill("loc1")
    time.sleep(1)
    loc2.fill("loc2")
    time.sleep(1)
    loc3.fill("loc3")
    time.sleep(1)

    loc1.clear()
    loc2.clear()
    loc3.clear()

    loc1.click(force=True)
    loc2.click(force=True)
    loc3.click(force=True)

    # loc1.click(button="right", force=True)
    # loc2.click(button="right", force=True)
    # loc3.click(button="right", force=True)
    #

    loc1_parent = page1.locator(xpath1_parent)
    loc2_parent = page1.locator(xpath2_parent)
    loc3_parent = page1.locator(xpath3_parent)

    loc1_parent.click()
    loc2_parent.click()
    loc3_parent.click()

    loc1_parent.click(button="right")
    loc1_parent.click()
    loc2_parent.click(button="right")
    loc2_parent.click()
    loc3_parent.click(button="right")
    loc3_parent.click()

    loc1_parent.screenshot(path="1.png")
    loc2_parent.screenshot(path="2.png")
    loc3_parent.screenshot(path="3.png")
