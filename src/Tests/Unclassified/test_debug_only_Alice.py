import time

from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.centrality_metrics_pane import CentralityMetricsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.table_pane import TablePane

from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

# def test_24_window_shade(page, init):
#     query = QueryPage(page)
#     query.click_add_table()

def test_01_custom_step(page, init):
    custom_step_page:CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step_page.apply_main_layout_standard()
    custom_step_page.apply_main_layout_horizontal()
    custom_step_page.apply_main_layout_vertical()


def test_02_create_dialog_and_accordion(page,init):
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


def test_03_mouse_down_move_up(page,init):
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

def test_04_call_SDSTest():
    Helper.call_SDSTest()


def test_05_centrality_metrics_in_flow(page,init):
    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
cas; 
libname mycas cas;
data &_output1;
input "from'从"n $ "to'到"n $ community "weight'权重"n "wt'_另一个权重"n;
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

data &_output2;
input "node'"n $ "weight'"n;
datalines;
A 4
B 2
C 4
D 1
E 3
F 7
G 4
H 8
I 5
J 1
K 6
L 3
M 9
N 1   
;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETIN")
    time.sleep(0.8)

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETIN")
    flow.arrange_nodes()

    flow.add_node(FlowNodeType.table)

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("NODESETIN")

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.SAS_PROGRAM, "添加输出端口")

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "NODESETIN")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,Helper.data_locale.STEP_CENTRALITY_METRICS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN",Helper.data_locale.STEP_CENTRALITY_METRICS)
    flow.arrange_nodes()

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS,"添加输入端口", "{sasstudio-steps-gui-icu.genericText.inputport.nodesData.title}")
    flow.link_two_nodes_in_flow("NODESETIN", Helper.data_locale.STEP_CENTRALITY_METRICS)
    flow.arrange_nodes()

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS,"添加输出端口","{sasstudio-steps-gui-icu.centralitymetrics.outputports.outputNodesDSName.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("MYCAS")
    table_pane.set_table("OUTPUT_NODES")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS,"OUTPUT_NODES")
    flow.arrange_nodes()

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS,"添加输出端口","{sasstudio-steps-gui-icu.centralitymetrics.outputports.outputLinksDSName.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("MYCAS")
    table_pane.set_table("OUTPUT_LINKS")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS,"OUTPUT_LINKS")
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CENTRALITY_METRICS)
    centrality_metrics_pane = CentralityMetricsPane(page)
    centrality_metrics_pane.set_filter_input_data("\"weight'权重\"n>=0")
    centrality_metrics_pane.set_link_direction(item_index=1)
    centrality_metrics_pane.set_link_direction(item_index=0)
    centrality_metrics_pane.add_column_for_from_node("from'从")
    time.sleep(0.5)
    centrality_metrics_pane.add_column_for_to_node("to'到")
    time.sleep(0.5)
    centrality_metrics_pane.add_column_for_weight_in_links("weight'权重")
    time.sleep(0.5)
    centrality_metrics_pane.add_column_for_auxiliary_weight("wt'_另一个权重")
    time.sleep(0.5)
    centrality_metrics_pane.expand_windowshade_additional_roles()
    time.sleep(0.5)
    centrality_metrics_pane.add_columns_for_group_analysis_by(check_column_name_list=["from'从", "to'到", "community"])
    centrality_metrics_pane.delete_columns_for_group_analysis_by(check_column_name_list=["from'从", "to'到","community"])
    time.sleep(0.5)
    centrality_metrics_pane.collapse_windowshade_links()
    time.sleep(0.5)
    centrality_metrics_pane.set_check_include_nodes_data()
    time.sleep(0.5)
    centrality_metrics_pane.expand_windowshade_nodes()
    centrality_metrics_pane.set_filter_nodes_data("\"weight'\"n>=0")
    centrality_metrics_pane.add_column_for_node(column_name="node'")
    time.sleep(0.5)
    centrality_metrics_pane.add_column_for_weight_in_nodes(column_name="weight'")
    time.sleep(1)



    centrality_metrics_pane.click_options_tab()
    centrality_metrics_pane.set_check_degree()

    centrality_metrics_pane.set_uncheck_degree()
    centrality_metrics_pane.set_check_influence()
    centrality_metrics_pane.set_metric_type_for_influence(item_index=1)

    centrality_metrics_pane.set_metric_type_for_influence(item_value=Helper.data_locale.BOTH_WEIGHTED_AND_UNWEIGHTED)
    centrality_metrics_pane.set_check_clustering_coefficient()
    centrality_metrics_pane.set_check_closeness()
    centrality_metrics_pane.set_metric_type_for_closeness(item_index=2)
    centrality_metrics_pane.set_shortest_path_distance_between_disconnected_nodes(item_index=0)

    centrality_metrics_pane.set_shortest_path_distance_between_disconnected_nodes(item_value=Helper.data_locale.USE_ZERO)

    centrality_metrics_pane.set_check_betweenness()
    centrality_metrics_pane.set_metric_type_for_betweenness(item_index=1)
    centrality_metrics_pane.set_check_normalize_betweenness_centrality()
    centrality_metrics_pane.set_check_eigenvector()
    centrality_metrics_pane.set_metric_type_for_eigenvector(item_value=Helper.data_locale.BOTH_WEIGHTED_AND_UNWEIGHTED)
    centrality_metrics_pane.set_metric_type_for_eigenvector(item_index=1)
    centrality_metrics_pane.set_check_hub_score()
    centrality_metrics_pane.set_check_authority_score()


    centrality_metrics_pane.set_eigenvector_calculation_method(item_index = 2)


    centrality_metrics_pane.set_maximum_number_of_iterations_for_eigenvector_calculations(item_index=1)
    centrality_metrics_pane.set_number_of_iterations("50000")

    centrality_metrics_pane.set_log_details(item_index=2)

    centrality_metrics_pane.set_code_generation(item_index=1)
    time.sleep(0.5)
    centrality_metrics_pane.click_output_tab()
    time.sleep(0.8)
    centrality_metrics_pane.set_check_create_output_nodes_data()
    centrality_metrics_pane.set_check_replace_existing_output_table_for_nodes()
    time.sleep(0.2)
    centrality_metrics_pane.set_check_create_output_links_data()
    centrality_metrics_pane.set_check_replace_existing_output_table_for_links()
    time.sleep(0.8)
    centrality_metrics_pane.set_node_description("This is test for description.")
    time.sleep(0.5)
    centrality_metrics_pane.set_notes("You can set notes here to describe the step.")
    time.sleep(0.5)
    flow.run(True)


def test_06_sasprogram_table(page,init):
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

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETIN")

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETIN")
    flow.arrange_nodes()

    flow.add_node(FlowNodeType.table)

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("NODESETIN")

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.SAS_PROGRAM, "添加输出端口")

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "NODESETIN")
    flow.arrange_nodes()
    flow.run(True)
























