import time

from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.table_pane import TablePane
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




def test_01_add_step_to_flow(page,init):
    flow:FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    time.sleep(0.8)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)
    # time.sleep(1)
    sasprogram_pane = SASProgramPane(page)
    program = """
cas; 
libname mycas cas;
data mycas.LinkSetIn;
   input from $ to $ community weight wt;
   datalines;
A B 1 3 3 
A C 1 2 2
A D 1 1 1
B C 1 5 5
C D 1 7 7
C E 1 2 2
D F . 3 3
F G 2 9 9
F H 2 3 3
F I 2 5 5
G H 2 7 7
G I 2 3 3
I J . 3 3
J K 3 1 2
J L 3 6 6
K L 3 3 3
;
data mycas.NodeSetIn;
   input node $ @@;
   datalines;
A    M   N
;
"""
    time.sleep(0.5)
    sasprogram_pane.type_into_text_area(program)

    sasprogram_pane.set_node_name("Create table")

    flow.add_node(FlowNodeType.table)


    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table_pane = TablePane(page)
    table_pane.set_library("mycas")
    table_pane.set_table("LinkSetIn")


    flow.link_two_nodes_in_flow("Create table", "LinkSetIn")

    flow.arrange_nodes()
    step_path = ["优化和网络分析", "中心性量度"]
    flow.add_step_from_stepspane_to_flow(step_path)
    time.sleep(1)
    flow.link_two_nodes_in_flow("LinkSetIn","中心性量度")
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas("中心性量度")
    basic_step_pane = BasicStepPane(page)
    basic_step_pane.set_filter_input_date("sssss")
    time.sleep(2)

    # flow.select_node_in_flow_canvas("CLASS")
    # # table_pane.click_Tab("预览数据")
    #
    # # Original
    # # table_pane.click_Tab("Preview Data")
    #
    # # Revised
    # table_pane.click_Tab(Helper.data_locale.PREVIEW_DATA)
    #
    # time.sleep(3)
    # WholePage(page).screenshot_self(pic_name="07_preview_before_sorted")
    # flow.add_node(FlowNodeType.sort)
    # # time.sleep(1)
    # flow.arrange_nodes()
    #
    # # flow.link_two_nodes_in_flow("CLASS","排序")
    #
    # # Original
    # # flow.link_two_nodes_in_flow("CLASS", "Sort")
    #
    # flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)
    #
    # # time.sleep(1)
    # flow.arrange_nodes()
    #
    # # flow.select_node_in_flow_canvas("排序")
    #
    # # Original
    # # flow.select_node_in_flow_canvas("Sort")
    #
    # flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)
    #
    # sort_pane = SortPane(page)
    #
    # list1 = ["Class", "Name"]
    # sort_pane.add_sort(list1, SortWay.descending)
    # # time.sleep(1)
    # WholePage(page).screenshot_self(pic_name="08_add_sort")
    # flow.add_node(FlowNodeType.table)
    # # flow.select_node_in_flow_canvas("表")
    #
    # # Original
    # # flow.select_node_in_flow_canvas("Table")
    #
    # flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    #
    # table_pane.set_node_name("SORTED")
    # table_pane.set_library("WORK")
    # table_pane.set_table("SORTED")
    # table_pane.refresh_table()
    # # flow.link_two_nodes_in_flow("排序","SORTED")
    # # flow.link_two_nodes_in_flow("Sort", "SORTED")
    # flow.link_two_nodes_in_flow(Helper.data_locale.SORT, "SORTED")
    # # time.sleep(1)
    # flow.arrange_nodes()
    #
    #
    #
    #
    #
