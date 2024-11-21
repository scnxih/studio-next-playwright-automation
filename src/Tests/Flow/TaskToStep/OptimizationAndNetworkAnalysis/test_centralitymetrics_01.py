import pytest

from src.Pages.Common.whole_page import WholePage
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

@pytest.mark.level0_step
def test_01_centrality_metrics_in_flow(page, init):
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

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, "添加输出端口")

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "NODESETIN")
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_CENTRALITY_METRICS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN", Helper.data_locale.STEP_CENTRALITY_METRICS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "添加输入端口",
                                            Helper.data_locale.NODES_DATA)
    flow.link_two_nodes_in_flow("NODESETIN", Helper.data_locale.STEP_CENTRALITY_METRICS)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "添加输出端口",
                                            Helper.data_locale.NODES_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("MYCAS")
    table_pane.set_table("OUTPUT_NODES")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "OUTPUT_NODES")
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "添加输出端口",
                                            Helper.data_locale.LINKS_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("MYCAS")
    table_pane.set_table("OUTPUT_LINKS")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "OUTPUT_LINKS")
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()

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
    # centrality_metrics_pane.add_columns_for_group_analysis_by(check_column_name_list=["from'从", "to'到", "community"])
    centrality_metrics_pane.add_columns_for_group_analysis_by(check_column_name_list=["community"])
    # centrality_metrics_pane.delete_columns_for_group_analysis_by(
    #     check_column_name_list=["from'从", "to'到", "community"])
    time.sleep(0.5)
    centrality_metrics_pane.collapse_windowshade_links()
    time.sleep(0.5)
    # centrality_metrics_pane.set_check_include_nodes_data()
    # time.sleep(0.5)
    # centrality_metrics_pane.expand_windowshade_nodes()
    # centrality_metrics_pane.set_filter_nodes_data("\"weight'\"n>=0")
    # centrality_metrics_pane.add_column_for_node(column_name="node'")
    # time.sleep(0.5)
    # centrality_metrics_pane.add_column_for_weight_in_nodes(column_name="weight'")
    # time.sleep(1)
    centrality_metrics_pane.screenshot_self("data")
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

    centrality_metrics_pane.set_shortest_path_distance_between_disconnected_nodes(
        item_value=Helper.data_locale.USE_ZERO)

    centrality_metrics_pane.set_check_betweenness()
    centrality_metrics_pane.set_metric_type_for_betweenness(item_index=1)
    centrality_metrics_pane.set_check_normalize_betweenness_centrality()
    centrality_metrics_pane.set_check_eigenvector()
    centrality_metrics_pane.set_metric_type_for_eigenvector(item_value=Helper.data_locale.BOTH_WEIGHTED_AND_UNWEIGHTED)
    centrality_metrics_pane.set_metric_type_for_eigenvector(item_index=1)
    centrality_metrics_pane.set_check_hub_score()
    centrality_metrics_pane.set_check_authority_score()
    time.sleep(0.5)
    centrality_metrics_pane.collapse_windowshade_centrality_metrics()
    time.sleep(0.5)

    centrality_metrics_pane.set_eigenvector_calculation_method(item_index=2)

    centrality_metrics_pane.set_maximum_number_of_iterations_for_eigenvector_calculations(item_index=1)
    centrality_metrics_pane.set_number_of_iterations("50000")

    centrality_metrics_pane.set_log_details(item_index=2)

    centrality_metrics_pane.set_code_generation(item_index=1)
    time.sleep(0.5)
    centrality_metrics_pane.screenshot_self("options")
    centrality_metrics_pane.click_output_tab()
    time.sleep(0.8)
    centrality_metrics_pane.set_check_create_output_nodes_data()
    centrality_metrics_pane.set_check_replace_existing_output_table_for_nodes()
    time.sleep(0.2)
    centrality_metrics_pane.set_check_create_output_links_data()
    centrality_metrics_pane.set_check_replace_existing_output_table_for_links()
    time.sleep(0.8)
    centrality_metrics_pane.screenshot_self("output")
    centrality_metrics_pane.set_node_description("This is test for description.")
    time.sleep(0.5)
    centrality_metrics_pane.set_notes("You can set notes here to describe the step.")
    time.sleep(0.5)

    flow.run(False)
    time.sleep(0.5)
    flow.apply_flow_layout_horizontal()
    time.sleep(1.5)
    flow.screenshot_without_toast("run")
    flow.click_log_tab()
    time.sleep(0.5)
    flow.screenshot_without_toast("log")
    flow.click_output_data_tab()
    time.sleep(0.5)
    flow.screenshot_without_toast("output_data")
@pytest.mark.level1_step
def test_02_centrality_metrics_in_flow(page,init):
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

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, "添加输出端口")

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "NODESETIN")
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_CENTRALITY_METRICS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN", Helper.data_locale.STEP_CENTRALITY_METRICS)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "添加输入端口",
                                            Helper.data_locale.NODES_DATA)

    flow.link_two_nodes_in_flow("NODESETIN", Helper.data_locale.STEP_CENTRALITY_METRICS)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "添加输出端口",
                                            Helper.data_locale.NODES_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("MYCAS")
    table_pane.set_table("OUTPUT_NODES")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "OUTPUT_NODES")
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "添加输出端口",
                                            Helper.data_locale.LINKS_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("MYCAS")
    table_pane.set_table("OUTPUT_LINKS")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CENTRALITY_METRICS, "OUTPUT_LINKS")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()

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
    # centrality_metrics_pane.add_columns_for_group_analysis_by(check_column_name_list=["from'从", "to'到", "community"])
    # centrality_metrics_pane.add_columns_for_group_analysis_by(check_column_name_list=["community"])
    # centrality_metrics_pane.delete_columns_for_group_analysis_by(
    #     check_column_name_list=["from'从", "to'到", "community"])
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
    centrality_metrics_pane.set_metric_type_for_influence(item_index=0)

    centrality_metrics_pane.set_metric_type_for_influence(item_value=Helper.data_locale.BOTH_WEIGHTED_AND_UNWEIGHTED)
    centrality_metrics_pane.set_check_clustering_coefficient()
    centrality_metrics_pane.set_check_closeness()
    centrality_metrics_pane.set_metric_type_for_closeness(item_index=0)
    centrality_metrics_pane.set_shortest_path_distance_between_disconnected_nodes(item_index=0)

    centrality_metrics_pane.set_shortest_path_distance_between_disconnected_nodes(
        item_value=Helper.data_locale.USE_ZERO)

    centrality_metrics_pane.set_check_betweenness()
    centrality_metrics_pane.set_metric_type_for_betweenness(item_index=1)
    centrality_metrics_pane.set_check_normalize_betweenness_centrality()
    centrality_metrics_pane.set_check_eigenvector()
    centrality_metrics_pane.set_metric_type_for_eigenvector(item_value=Helper.data_locale.BOTH_WEIGHTED_AND_UNWEIGHTED)
    centrality_metrics_pane.set_metric_type_for_eigenvector(item_index=1)
    centrality_metrics_pane.set_check_hub_score()
    centrality_metrics_pane.set_check_authority_score()
    time.sleep(0.5)
    centrality_metrics_pane.collapse_windowshade_centrality_metrics()
    time.sleep(0.5)

    centrality_metrics_pane.set_eigenvector_calculation_method(item_index=2)

    centrality_metrics_pane.set_maximum_number_of_iterations_for_eigenvector_calculations(item_index=1)
    centrality_metrics_pane.set_number_of_iterations("50000")

    centrality_metrics_pane.set_log_details(item_index=1)

    centrality_metrics_pane.set_code_generation(item_index=0)
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
    flow.run(False)


def test_03_color_picker(page,init):
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
    time.sleep(1)
@pytest.mark.level1_step
def test_04_combobox_exact_label(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                 Helper.data_locale.STEP_TEXT_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_MAP)
    flow.apply_flow_layout_vertical()
    pane = TextMapPane(page)

    pane.set_check_include_choropleth_map_layer()
    pane.click_options_tab()
    pane.expand_windowshade_text()
    pane.set_option_for_style(item_index=2)
    pane.expand_windowshade_choromap()
    pane.expand_windowshade_line_attributes()
    pane.set_option_for_line_style(item_index=3)
    time.sleep(4)