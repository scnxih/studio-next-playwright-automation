import time

from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.centrality_metrics_pane import \
    CentralityMetricsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.stack_columns_pane import StackColumnsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.one_way_frequencies_pane import OneWayFrequencies
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.line_chart_pane import LineChartPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.scatter_map_pane import ScatterMapPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.text_map_pane import TextMapPane

from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


def test_01_custom_step(page, init):
    custom_step_page: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step_page.apply_main_layout_standard()
    custom_step_page.apply_main_layout_horizontal()
    custom_step_page.apply_main_layout_vertical()


# def test_02_create_dialog_and_accordion(page, init):
#     dialog = get_dialog_page(page, DialogType.open_dialog)
#     dialog = get_dialog_page(page, DialogType.save_as_dialog)
#     dialog = get_dialog_page(page, DialogType.search_dialog)
#     dialog = get_dialog_page(page, DialogType.about_dialog)
#     dialog = get_dialog_page(page, DialogType.settings_dialog)
#     dialog = get_dialog_page(page, DialogType.query_select_table_dialog)
#     dialog = get_dialog_page(page, DialogType.query_output_lib_dialog)
#     dialog = get_dialog_page(page, DialogType.new_folder_dialog)
#     dialog = get_dialog_page(page, DialogType.manage_shortcuts_dialog)
#     dialog = get_dialog_page(page, DialogType.manage_git_connection_dialog)
#     dialog = get_dialog_page(page, DialogType.keyboard_shortcuts_dialog)
#     dialog = get_dialog_page(page, DialogType.document_recovery_dialog)
#     dialog = get_dialog_page(page, DialogType.autoexec_dialog)
#     dialog = get_dialog_page(page, DialogType.add_profile_dialog)
#     dialog = get_dialog_page(page, DialogType.custom_code_dialog)
#
#     pane = get_accordion_page(page, AccordionType.open_item)
#     pane = get_accordion_page(page, AccordionType.sas_server)
#     pane = get_accordion_page(page, AccordionType.sas_content)
#     pane = get_accordion_page(page, AccordionType.steps)
#     pane = get_accordion_page(page, AccordionType.git)
#     pane = get_accordion_page(page, AccordionType.libraries)
#     pane = get_accordion_page(page, AccordionType.snippets)
#     pane = get_accordion_page(page, AccordionType.clinical_repository)
#     pane = get_accordion_page(page, AccordionType.file_references)


def test_03_mouse_down_move_up(page, init):
    editor: SASProgramPage = PageHelper.new_sas_program(page)
    p: Page = page

    str = """data cars;
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
    start = p.locator(
        "//textarea[@aria-label='编辑器内容, 按 Alt+F1 查看辅助功能选项。']/../descendant::div[@class='view-lines monaco-mouse-cursor-text']/descendant::span[contains(text(),'start')]").bounding_box()
    start_pos_x = start["x"]
    start_pos_y = start["y"]
    end = p.locator(
        "//textarea[@aria-label='编辑器内容, 按 Alt+F1 查看辅助功能选项。']/../descendant::div[@class='view-lines monaco-mouse-cursor-text']/descendant::span[contains(text(),'end')]").bounding_box()
    end_pos_x = end["x"] + end["width"]
    end_pos_y = end["y"] + end["height"]

    p.mouse.move(start_pos_x, start_pos_y)
    time.sleep(1)
    p.mouse.down()
    time.sleep(1)
    p.mouse.move(end_pos_x, end_pos_y)
    time.sleep(1)
    p.mouse.up()
    time.sleep(1)
    editor.run(True)
    time.sleep(1)


# def test_04_call_SDSTest():
#     Helper.call_SDSTest()







def test_08_link_nodes_with_multiple_ports(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
cas; 
libname mycas cas;
data aa;
input "from'从"n $ "to'到 "n$ community "weight'权重"n "wt'_另一个权重"n;
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

data bb;
input "node'"n $ "weight'"n;
datalines;
A 4
M 5
N 7    
;
"""
    sas_program_pane.type_into_text_area(code)

    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)

    flow.add_node(FlowNodeType.table)
    table = TablePane(page)
    table.set_library("work")
    table.set_table("aa")
    flow.add_node(FlowNodeType.table)
    table = TablePane(page)
    table.set_library("work")
    table.set_table("bb")

    flow.add_node(FlowNodeType.table)
    table = TablePane(page)
    table.set_library("work")
    table.set_table("c")

    flow.add_node(FlowNodeType.table)
    table = TablePane(page)
    table.set_library("work")
    table.set_table("d")

    flow.add_node(FlowNodeType.table)
    table = TablePane(page)
    table.set_library("work")
    table.set_table("e")

    flow.add_node(FlowNodeType.table)
    table = TablePane(page)
    table.set_library("work")
    table.set_table("f")

    flow.arrange_nodes()
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "aa")

    flow.arrange_nodes()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "bb")
    flow.arrange_nodes()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "c")
    flow.arrange_nodes()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "d")
    flow.arrange_nodes()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "e")
    flow.arrange_nodes()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "f")
    flow.arrange_nodes()
    flow.view_expand_all_ports()

    time.sleep(3)


def test_09_duplicate_checkbox(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS,
                 Helper.data_locale.STEP_ONE_WAY_FREQUENCIES]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ONE_WAY_FREQUENCIES)
    # flow.apply_detail_layout_vertical()
    flow.apply_flow_layout_vertical()

    pane = OneWayFrequencies(page)
    pane.click_options_tab()
    pane.expand_windowshade_statistics()
    time.sleep(1)
    pane.set_check_for_asymptotic_test_binomial_proportion()
    pane.set_check_for_asymptotic_test_chi_square_goodness_of_fit()
    pane.set_check_for_exact_test_binomial_proportion()
    pane.set_check_for_exact_test_chi_square_goodness_of_fit()

    time.sleep(3)

    pane.set_uncheck_for_exact_test_binomial_proportion()
    pane.set_uncheck_for_exact_test_chi_square_goodness_of_fit()
    pane.set_uncheck_for_asymptotic_test_binomial_proportion()
    pane.set_uncheck_for_asymptotic_test_chi_square_goodness_of_fit()
    time.sleep(3)


def test_10_numeric_stepper(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA,
                 Helper.data_locale.STEP_STACK_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_STACK_COLUMNS)
    flow.apply_detail_layout_vertical()
    pane = StackColumnsPane(page)
    time.sleep(1)
    pane.set_number_of_stacked_cariables_to_create("4")
    time.sleep(1)
    pane.click_increment_value_for_number_of_stacked_variables_to_create(8)
    time.sleep(1)
    pane.click_decrement_value_for_number_of_stacked_variables_to_create(3)
    time.sleep(1)



def test_11_section_label_for_checkbox_combobox(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                 Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    flow.apply_detail_layout_vertical()
    pane = LineChartPane(page)
    pane.click_options_tab()
    pane.collapse_windowshade_lines()
    pane.expand_windowshade_x_axis()
    pane.set_check_for_create_reference_line_for_x_axis()
    time.sleep(1)
    pane.set_option_for_radio_group(section_label="X 轴",item_index=0)
    time.sleep(1)
    pane.set_option_for_radio_group(section_label="X 轴", item_value="自定义标签")
    time.sleep(1)
    pane.set_option_for_dispaly_label_for_x_axis(item_index=2)
    time.sleep(1)
    pane.set_text_for_first_label_for_x_axis("test first label")
    time.sleep(1)
    pane.set_text_for_second_label_for_x_axis("test second label")
    time.sleep(1)
    pane.collapse_windowshade_x_axis()

    pane.expand_windowshade_y_axis()
    pane.set_check_for_create_reference_line_for_y_axis()
    time.sleep(1)
    pane.set_option_for_radio_group(section_label="Y 轴",item_index=0)
    time.sleep(1)
    pane.set_option_for_radio_group(section_label="Y 轴", item_value="自定义标签")

    time.sleep(1)
    pane.set_option_for_dispaly_label_for_y_axis(item_index=2)
    time.sleep(1)
    pane.set_text_for_first_label_for_y_axis("Y 标签1")
    time.sleep(1)
    pane.set_text_for_second_label_for_y_axis("Y label 2")
    time.sleep(1)

def test_12_contextmenu(page,init):
    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.sas_program)
    pane = SASProgramPane(page)
    pane.type_into_text_area("proc print data=sashelp.class;run;")
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)

    flow.click_remove_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    flow.click_remove_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)

    flow.click_add_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)

    flow.click_add_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)

    flow.click_add_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)

    time.sleep(2)

    flow.click_remove_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM,"输入表 1")
    flow.click_remove_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM,"输入表 2")
    flow.click_remove_input_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    flow.click_expand_ports_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    flow.click_collapse_ports_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)

    flow.click_remove_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM,"输出表 1")
    flow.click_remove_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM,"输出表 2")
    flow.click_remove_output_port_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)

    time.sleep(1)
    
    flow.click_run_node_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(2)
    flow.click_run_from_node_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(2)
    flow.click_go_to_last_submitted_code_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    flow.click_flow_tab()
    flow.click_go_to_last_submitted_log_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    flow.click_flow_tab()
    flow.click_code_tab()
    time.sleep(1)
    flow.click_log_tab()
    time.sleep(1)
    flow.click_results_tab()
    time.sleep(1)
    flow.click_output_data_tab()
    time.sleep(1)
    flow.click_flow_tab()
    time.sleep(1)


    flow.click_copy_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    flow.click_cut_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    flow.click_paste_in_context_menu_on_canvas()
    time.sleep(1)
    flow.click_run_now_in_context_menu_on_canvas()
    time.sleep(2)

    flow.click_add_note_in_context_menu_on_canvas()
    time.sleep(1)

    flow.click_collapse_all_ports_in_context_menu_on_canvas()
    flow.click_expand_all_ports_in_context_menu_on_canvas()
    time.sleep(2)

    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    flow.click_delete_in_context_menu_on_node(Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)

def test_13_combobox_exact_label(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                 Helper.data_locale.STEP_TEXT_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_MAP)
    flow.apply_detail_layout_vertical()
    pane = TextMapPane(page)

    pane.set_check_include_choropleth_map_layer()
    pane.click_options_tab()
    pane.expand_windowshade_text()
    pane.set_option_for_style(item_index=2)
    pane.expand_windowshade_choromap()
    pane.expand_windowshade_line_attributes()
    pane.set_option_for_line_style(item_index=3)
    time.sleep(4)


def test_14_color_picker(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                 Helper.data_locale.STEP_SCATTER_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SCATTER_MAP)
    pane = ScatterMapPane(page)
    pane.click_options_tab()
    pane.expand_windowshade_markers()
    pane.set_check_for_set_color_in_markers()
    pane.set_rgb_for_color_in_marker(100,100,200)
    time.sleep(2)





def test_15_no_node_name(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas("")

def test_16_link_to_input_port(page,init):
    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table = TablePane(page)
    table.set_library("sashelp")
    table.set_table("class")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table = TablePane(page)
    table.set_library("sashelp")
    table.set_table("cars")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table = TablePane(page)
    table.set_library("sashelp")
    table.set_table("prdsale")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table = TablePane(page)
    table.set_library("sashelp")
    table.set_table("air")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table = TablePane(page)
    table.set_library("sashelp")
    table.set_table("buy")

    flow.arrange_nodes()
    flow.add_node(node_type=FlowNodeType.union_rows)


    flow.link_from_node_to_input_port_in_flow_first_of_two("class","联合行")
    flow.arrange_nodes()
    flow.link_two_nodes_in_flow("cars","联合行")
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow("联合行",Helper.data_locale.ADD_INPUT_PORT)

    flow.view_expand_all_ports()


    flow.link_from_node_to_input_port_in_flow("prdsale","联合行",3)

    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow("联合行", Helper.data_locale.ADD_INPUT_PORT)

    flow.link_from_node_to_input_port_in_flow("air", "联合行", 4)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow("联合行", Helper.data_locale.ADD_INPUT_PORT)
    flow.arrange_nodes()

    flow.link_from_node_to_input_port_in_flow("buy", "联合行", 5)
    flow.arrange_nodes()





