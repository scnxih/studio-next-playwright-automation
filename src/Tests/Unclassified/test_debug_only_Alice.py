from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

# def test_24_window_shade(page, init):
#     query = QueryPage(page)
#     query.click_add_table()

def test_47_custom_step(page, init):
    custom_step_page:CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step_page.apply_main_layout_standard()
    custom_step_page.apply_main_layout_horizontal()
    custom_step_page.apply_main_layout_vertical()


def test_48_create_dialog_and_accordion(page,init):
    dialog = get_dialog_page(page,DialogType.open_dialog)
    dialog = get_dialog_page(page,DialogType.save_as_dialog)
    dialog = get_dialog_page(page, DialogType.search_dialog)
    dialog = get_dialog_page(page, DialogType.about_dialog)
    dialog = get_dialog_page(page, DialogType.settings_dialog)
    dialog = get_dialog_page(page, DialogType.query_select_table_dialog)
    dialog = get_dialog_page(page, DialogType.query_output_lib_dialog)
    dialog = get_dialog_page(page, DialogType.new_folder_dialog)
    dialog = get_dialog_page(page, DialogType.manage_shortcuts_dialog)
    dialog = get_dialog_page(page, DialogType.manage_git_connection_dialog)
    dialog = get_dialog_page(page, DialogType.keyboard_shortcuts_dialog)
    dialog = get_dialog_page(page, DialogType.document_recovery_dialog)
    dialog = get_dialog_page(page, DialogType.autoexec_dialog)
    dialog = get_dialog_page(page, DialogType.add_profile_dialog)
    dialog = get_dialog_page(page, DialogType.custom_code_dialog)

    pane = get_accordion_page(page,AccordionType.open_item)
    pane = get_accordion_page(page, AccordionType.sas_server)
    pane = get_accordion_page(page, AccordionType.sas_content)
    pane = get_accordion_page(page, AccordionType.steps)
    pane = get_accordion_page(page, AccordionType.git)
    pane = get_accordion_page(page, AccordionType.libraries)
    pane = get_accordion_page(page, AccordionType.snippets)
    pane = get_accordion_page(page, AccordionType.clinical_repository)
    pane = get_accordion_page(page, AccordionType.file_references)


def test_mouse_down_move_up(page,init):
    editor:SASProgramPage = PageHelper.new_sas_program(page)
    p: Page = page

    str ="""data cars;
set sashelp.cars;
run;   
/*choose region start*/
data test; 
set sashelp.class;
run;

proc print data=test;
run;
proc sort data=test out=sorted;
by age;                         
run;
/*choose region end*/
proc sql;
create table aa as 
select * from sorted;
run;
"""
    editor.editor.type_into_text_area(str)

    # editor.run(True)
    start = p.locator("//textarea[@aria-label='编辑器内容, 按 Alt+F1 查看辅助功能选项。']/../descendant::div[@class='view-lines monaco-mouse-cursor-text']/descendant::span[contains(text(),'start')]").bounding_box()
    start_pos_x = start["x"]
    start_pos_y = start["y"]
    end = p.locator("//textarea[@aria-label='编辑器内容, 按 Alt+F1 查看辅助功能选项。']/../descendant::div[@class='view-lines monaco-mouse-cursor-text']/descendant::span[contains(text(),'end')]").bounding_box()
    end_pos_x = end["x"]+end["width"]
    end_pos_y = end["y"]+end["height"]

    p.mouse.move(start_pos_x,start_pos_y)
    time.sleep(1)
    p.mouse.down()
    time.sleep(1)
    p.mouse.move(end_pos_x,end_pos_y)
    time.sleep(1)
    p.mouse.up()
    time.sleep(1)
    editor.run(True)
    time.sleep(1)

def test_call_SDSTest():
    Helper.call_SDSTest()


