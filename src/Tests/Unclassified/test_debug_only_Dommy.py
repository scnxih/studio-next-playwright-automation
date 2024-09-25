from src.Pages.StudioNext.Center.Flow.DetailsPane.Enrichment.verify_with_loqate_pane import VerifyWithLoqate
from src.Pages.StudioNext.Center.Flow.DetailsPane.MachineLearning.robust_principal_component_analysis_pane import \
    RobustPrincipalComponentAnalysis
from src.Pages.StudioNext.Center.Flow.DetailsPane.MachineLearning.semi_supervised_learning_pane import \
    SemiSupervisedLearning
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.minimun_spanning_tree_pane import \
    MinimunSpanningTree
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.cluster_variables_pane import ClusterVariablesPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.coin_toss_simulation_pane import CoinTossSimulationPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.poker_hand_probability_pane import PokerHandProbabilityPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TextAnalytics.text_summarization_pane import TextSummarization
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.line_chart_pane import LineChartPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.text_map_pane import TextMapPane

from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.list_data_pane import ListDataPane


def test_01_list_data_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()
    flow.run(True)


def test_02_list_data_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["姓名1", "Team'中文"])
    list_data_pane.add_columns_for_group_analysis_by(check_column_name_list=["League'中"])
    list_data_pane.add_columns_for_total_of(check_column_name_list=["nAtBat'中", "nHits'中"])
    list_data_pane.add_columns_for_identifying_label(check_column_name_list=["nHome'中", "Div'中"])
    time.sleep(0.5)

    flow.run(True)


def test_03_list_data_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["姓名1", "Team'中文"])
    list_data_pane.add_columns_for_group_analysis_by(check_column_name_list=["League'中"])
    list_data_pane.add_columns_for_total_of(check_column_name_list=["nAtBat'中", "nHits'中"])

    time.sleep(0.5)
    list_data_pane.click_options_tab()
    list_data_pane.set_check_display_row_numbers()
    list_data_pane.set_column_label("中文")
    list_data_pane.set_check_display_number_of_rows()
    list_data_pane.set_heading_direction(item_index=2)
    list_data_pane.set_check_split_labels()
    list_data_pane.set_split_character(item_index=5)
    list_data_pane.set_rows_to_list(item_index=1)
    flow.run(True)


def test_04_list_data_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["姓名1", "Team'中文"])
    list_data_pane.add_columns_for_group_analysis_by(check_column_name_list=["League'中"])
    list_data_pane.add_columns_for_total_of(check_column_name_list=["nAtBat'中", "nHits'中"])
    list_data_pane.add_columns_for_identifying_label(check_column_name_list=["nHome'中", "Div'中"])

    time.sleep(0.5)
    list_data_pane.click_options_tab()
    list_data_pane.set_uncheck_display_row_numbers()
    list_data_pane.set_uncheck_use_labels_as_column_headings()
    list_data_pane.set_uncheck_display_number_of_rows()
    list_data_pane.set_uncheck_round_values()
    list_data_pane.set_heading_direction(item_index=1)
    list_data_pane.set_uncheck_split_labels()
    flow.run(True)


def test_05_line_chart_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LINE_CHART)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    line_chart_pane = LineChartPane(page)
    line_chart_pane.add_column_for_category("Team'中文")
    flow.run(True)


def test_06_line_chart_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LINE_CHART)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    line_chart_pane = LineChartPane(page)
    line_chart_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    line_chart_pane.add_column_for_category("Team'中文")
    line_chart_pane.add_column_for_subcategory("姓名1")
    line_chart_pane.set_display_subcategory_legend(item_index=1)
    line_chart_pane.set_measure(item_index=2)
    line_chart_pane.add_column_for_column("nHits'中")
    line_chart_pane.set_statistics(item_index=1)
    line_chart_pane.set_error_bars(item_index=2)
    line_chart_pane.set_type(item_index=1)
    line_chart_pane.set_check_specify_statistic_multiplier()
    line_chart_pane.set_multiplier("2")
    line_chart_pane.expand_windowshade_additional_roles()
    line_chart_pane.add_column_for_group_analysis_by("League'中")
    line_chart_pane.add_column_for_weight("nHome'中")
    flow.run(True)


def test_07_line_chart_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LINE_CHART)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    line_chart_pane = LineChartPane(page)
    line_chart_pane.add_column_for_category("Team'中文")
    line_chart_pane.set_measure(item_index=2)
    line_chart_pane.add_column_for_column("nHits'中")
    line_chart_pane.expand_windowshade_additional_roles()
    line_chart_pane.add_column_for_group_analysis_by("League'中")

    line_chart_pane.click_options_tab()
    line_chart_pane.expand_windowshade_lines()
    line_chart_pane.set_check_show_data_labels()
    line_chart_pane.set_check_show_line_label()
    line_chart_pane.set_label("中文'测试")
    line_chart_pane.set_check_set_color()
    line_chart_pane.set_color_transparency(item_index=2)
    line_chart_pane.set_line_style(item_index=5)
    line_chart_pane.add_column_for_url_variable("Div'中")

    line_chart_pane.expand_windowshade_x_axis()
    line_chart_pane.set_check_reverse_tick_values()
    line_chart_pane.set_check_show_tick_values_in_data_order()
    line_chart_pane.set_option_for_display_label_for_x_axis(item_index=2)
    line_chart_pane.set_text_for_first_label_for_x_axis("x轴标签")
    line_chart_pane.set_check_rotate_values_in_case_of_tick_collisions()
    line_chart_pane.set_rotate_degree(item_index=1)
    line_chart_pane.set_check_for_create_reference_line_for_x_axis()
    line_chart_pane.set_reference_values_x(item_index=15)
    line_chart_pane.set_line_offset(item_index=3)

    line_chart_pane.expand_windowshade_y_axis()
    line_chart_pane.set_check_specify_minimum_value()
    line_chart_pane.set_minimum_value("1200")
    line_chart_pane.set_check_specify_maximum_value()
    line_chart_pane.set_maximum_value("2000")
    line_chart_pane.set_option_for_display_label_for_y_axis(item_index=4)
    line_chart_pane.set_text_for_first_label_for_y_axis("y轴标签")
    line_chart_pane.set_check_use_logarithmic_scale()
    line_chart_pane.set_base_value(item_index=1)
    line_chart_pane.set_check_for_create_reference_line_for_y_axis()
    line_chart_pane.set_reference_values_y("1500")


    line_chart_pane.expand_windowshade_title_footnote()
    line_chart_pane.set_title("线图中文标题")
    line_chart_pane.set_footnote("线图中文脚注")

    flow.run(True)


def test_08_coin_toss_simulation_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_COIN_TOSS_SIMULATION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.run(True)


def test_09_coin_toss_simulation_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_COIN_TOSS_SIMULATION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_COIN_TOSS_SIMULATION)
    coin_toss_simulation_pane = CoinTossSimulationPane(page)
    coin_toss_simulation_pane.set_check_show_graph_table()
    coin_toss_simulation_pane.set_check_grid_lines()
    coin_toss_simulation_pane.set_check_gradient_fill()
    coin_toss_simulation_pane.set_check_data_skin()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("输出'cointest")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_COIN_TOSS_SIMULATION, "输出'cointest")
    flow.arrange_nodes()
    flow.run(True)


def test_10_poker_hand_probablity_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("一手牌'INPUT")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "一手牌'INPUT")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_POKER_HAND_PROBABILITY]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("一手牌'INPUT", Helper.data_locale.STEP_POKER_HAND_PROBABILITY)
    flow.arrange_nodes()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("一手牌输出'data")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_POKER_HAND_PROBABILITY, "一手牌输出'data")
    flow.arrange_nodes()
    flow.run(True)


def test_11_cluster_variables_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    flow.run(True)


def test_12_cluster_variables_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    cluster_variables_pane.expand_windowshade_additional_roles()
    cluster_variables_pane.add_columns_for_variables_to_partial_out(check_column_name_list=["nHome'中", "nRuns'中"])
    cluster_variables_pane.add_column_for_frequency_count("nRBI'中")
    cluster_variables_pane.add_column_for_weight("YrMajor'中")
    cluster_variables_pane.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    cluster_variables_pane.click_options_tab()
    cluster_variables_pane.set_maximum_number_of_clusters(item_index=1)
    cluster_variables_pane.set_check_maximum_second_eigenvalue()
    cluster_variables_pane.set_eigenvalue("2")
    flow.run(True)


def test_13_cluster_variables_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    cluster_variables_pane.expand_windowshade_additional_roles()
    cluster_variables_pane.add_columns_for_variables_to_partial_out(check_column_name_list=["nHome'中", "nRuns'中"])
    cluster_variables_pane.add_column_for_frequency_count("nRBI'中")
    cluster_variables_pane.add_column_for_weight("YrMajor'中")
    cluster_variables_pane.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    cluster_variables_pane.click_options_tab()
    cluster_variables_pane.set_method(item_index=1)
    cluster_variables_pane.set_check_minimum_proportion_of_variation()
    cluster_variables_pane.set_proportion("0.2")
    cluster_variables_pane.expand_windowshade_deatails()
    cluster_variables_pane.set_analyze(item_index=1)
    cluster_variables_pane.set_check_maximum_number_of_iterations()
    cluster_variables_pane.set_iterations("5")
    flow.run(True)


def test_14_cluster_variables_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.clustervariables.outputports"
                                            ".statDSName.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("输出'stat")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, "输出'stat")
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.clustervariables.outputports"
                                            ".treeDSName.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("输出'tree")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, "输出'tree")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    cluster_variables_pane.expand_windowshade_additional_roles()
    cluster_variables_pane.add_columns_for_variables_to_partial_out(check_column_name_list=["nHome'中", "nRuns'中"])
    cluster_variables_pane.add_column_for_frequency_count("nRBI'中")
    cluster_variables_pane.add_column_for_weight("YrMajor'中")
    cluster_variables_pane.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    cluster_variables_pane.click_options_tab()
    cluster_variables_pane.set_method(item_index=1)
    cluster_variables_pane.set_check_minimum_proportion_of_variation()
    cluster_variables_pane.set_proportion("0.2")
    cluster_variables_pane.expand_windowshade_deatails()
    cluster_variables_pane.set_analyze(item_index=1)
    cluster_variables_pane.set_check_maximum_number_of_iterations()
    cluster_variables_pane.set_iterations("5")

    cluster_variables_pane.click_output_tab()
    cluster_variables_pane.set_check_create_statistics_data()
    cluster_variables_pane.set_check_replace_existing_output_table_for_statistics()
    cluster_variables_pane.set_check_create_tree_information_data()
    cluster_variables_pane.set_check_replace_existing_output_table_for_tree_information()
    flow.run(True)


def test_15_text_map_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CITY_POP_LOC'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "CITY_POP_LOC'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_TEXT_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("CITY_POP_LOC'中文", Helper.data_locale.STEP_TEXT_MAP)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_MAP)
    text_map_pane = TextMapPane(page)
    text_map_pane.expand_windowshade_plot_data()
    text_map_pane.add_column_for_latitude("LAT'中文")
    text_map_pane.add_column_for_longitude("LONG'中文")
    text_map_pane.add_column_for_text("COUNTY_NAME'中文")
    flow.run(True)


def test_16_text_map_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CITY_POP_LOC'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "CITY_POP_LOC'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_TEXT_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("CITY_POP_LOC'中文", Helper.data_locale.STEP_TEXT_MAP)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_MAP, "添加输入端口",
                                            "{sasstudio-steps-gui-icu.genericText.inputport.mapInputData.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("NEVADA'中文")
    flow.link_two_nodes_in_flow("NEVADA'中文", Helper.data_locale.STEP_TEXT_MAP)
    flow.arrange_nodes()

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_MAP, "添加输入端口",
    # "{sasstudio-steps-gui-icu.genericText.inputport.mapResponseData.title}")
    # flow.view_expand_all_ports()
    # flow.add_node(FlowNodeType.table)
    # flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    # table_pane.set_library("AUTOLIB")
    # flow.link_two_nodes_in_flow("COUNTY_POP'中文", Helper.data_locale.STEP_TEXT_MAP)
    # flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_MAP)
    text_map_pane = TextMapPane(page)
    text_map_pane.expand_windowshade_plot_data()
    text_map_pane.add_column_for_latitude("LAT'中文")
    text_map_pane.add_column_for_longitude("LONG'中文")
    text_map_pane.add_column_for_text("COUNTY_NAME'中文")

    text_map_pane.set_check_include_choropleth_map_layer()
    text_map_pane.add_column_for_id_variable("ID'中文")

    text_map_pane.click_options_tab()
    text_map_pane.expand_windowshade_text()
    text_map_pane.set_check_specify_predefined_style()
    text_map_pane.set_style(item_index=5)
    text_map_pane.set_check_specify_text_options()
    text_map_pane.set_check_set_font_color()
    text_map_pane.set_font_family(item_index=2)
    text_map_pane.set_font_style(item_index=1)
    text_map_pane.set_font_weight(item_index=1)
    text_map_pane.set_label_position(item_index=5)

    text_map_pane.expand_windowshade_choromap()
    text_map_pane.set_check_set_color()
    text_map_pane.set_line_style(item_index=5)
    text_map_pane.click_options_tab()

    flow.run(True)


def test_17_minimum_spanning_tree_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    flow.run(True)


def test_18_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_19_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=1)
    minimum_spanning_tree_pane.set_code_generation(item_index=1)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_20_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=1)
    minimum_spanning_tree_pane.set_code_generation(item_index=0)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_21_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)
    minimum_spanning_tree_pane.set_code_generation(item_index=1)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_22_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)
    minimum_spanning_tree_pane.set_code_generation(item_index=2)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_23_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")
    minimum_spanning_tree_pane.expand_windowshade_additional_roles()
    minimum_spanning_tree_pane.add_columns_for_group_analysis_by(check_column_name_list=["group'中文"])

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)
    minimum_spanning_tree_pane.set_code_generation(item_index=0)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_24_minimum_spanning_tree_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")
    minimum_spanning_tree_pane.expand_windowshade_additional_roles()
    minimum_spanning_tree_pane.add_columns_for_group_analysis_by(check_column_name_list=["group'中文"])

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=1)
    minimum_spanning_tree_pane.set_code_generation(item_index=1)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_25_semi_supervised_learning_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.arrange_nodes()
    flow.run(True)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    flow.run(True)


def test_26_semi_supervised_learning_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.arrange_nodes()
    flow.run(True)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("SSL'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "SSL'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    semi_supervised_learning_pane.click_options_tab()
    semi_supervised_learning_pane.set_kernel(item_index=1)
    semi_supervised_learning_pane.set_number_of_neighbors("2")
    semi_supervised_learning_pane.set_number_of_iterations("4")
    semi_supervised_learning_pane.set_rbf_kernel_width("15")

    semi_supervised_learning_pane.click_output_tab()
    semi_supervised_learning_pane.set_check_create_output_data()
    semi_supervised_learning_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_27_semi_supervised_learning_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.arrange_nodes()
    flow.run(True)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("SSL'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "SSL'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    semi_supervised_learning_pane.click_options_tab()
    semi_supervised_learning_pane.set_kernel(item_index=0)
    semi_supervised_learning_pane.set_code_generation(item_index=1)

    semi_supervised_learning_pane.click_output_tab()
    semi_supervised_learning_pane.set_check_create_output_data()
    semi_supervised_learning_pane.set_check_replace_existing_output_table()
    flow.run(True)


def test_28_semi_supervised_learning_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.arrange_nodes()
    flow.run(True)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("SSL'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "SSL'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    semi_supervised_learning_pane.click_options_tab()
    semi_supervised_learning_pane.set_kernel(item_index=1)
    semi_supervised_learning_pane.set_number_of_neighbors("2")
    semi_supervised_learning_pane.set_number_of_iterations("4")
    semi_supervised_learning_pane.set_rbf_kernel_width("15")
    semi_supervised_learning_pane.set_code_generation(item_index=1)

    semi_supervised_learning_pane.click_output_tab()
    semi_supervised_learning_pane.set_check_create_output_data()
    semi_supervised_learning_pane.set_check_replace_existing_output_table()
    semi_supervised_learning_pane.set_include_variables_from_input_CAS_table(item_index=2)
    semi_supervised_learning_pane.add_columns_for_include_these_variables(
        check_column_name_list=["x1'中文", "y'中文", "id'中文"])
    flow.run(True)


def test_29_text_summarization_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    flow.run(True)


def test_30_text_summarization_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_check_use_entities_and_noun_groups()
    flow.run(True)


def test_31_text_summarization_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.corpusSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Corpus'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Corpus'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_check_entire_corpus()
    text_summarization_pane.set_check_use_entities_and_noun_groups()

    flow.run(True)


def test_32_text_summarization_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.corpusSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Corpus'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Corpus'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_check_entire_corpus()
    text_summarization_pane.set_check_use_entities_and_noun_groups()

    text_summarization_pane.click_output_tab()
    text_summarization_pane.set_include_variables_from_input_CAS_table(item_index=3)
    text_summarization_pane.add_columns_for_include_these_variables(check_column_name_list=["text'中文"])
    text_summarization_pane.expand_windowshade_corpus_summary()
    text_summarization_pane.set_check_show_output_data()
    flow.run(True)


def test_33_text_summarization_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.corpusSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Corpus'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Corpus'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_uncheck_each_document()
    text_summarization_pane.set_check_entire_corpus()
    text_summarization_pane.set_check_use_entities_and_noun_groups()

    text_summarization_pane.click_output_tab()
    text_summarization_pane.expand_windowshade_corpus_summary()
    text_summarization_pane.set_check_show_output_data()
    flow.run(True)


def test_34_robust_principal_component_analysis_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.add_columns_for_interval_inputs(
        check_column_name_list=["SepalLength'中文", "SepalWidth'中文", "PetalLength'中文", "PetalWidth'中文"])
    flow.run(True)


def test_35_robust_principal_component_analysis_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")
    flow.run(True)


def test_36_robust_principal_component_analysis_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
    libname AUTOLIB '/segatest/I18N/Autolib' ;
    cas;
    caslib _all_ assign;
    data casuser.'IRIS''中文'n;
    set AUTOLIB.'IRIS''中文'n;
    'ID''中文'n=_n_;
    run;
    """
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")

    robust_principal_component_analysis_pane.click_options_tab()
    robust_principal_component_analysis_pane.set_method(item_index=1)
    robust_principal_component_analysis_pane.set_lambda(item_index=1)
    robust_principal_component_analysis_pane.set_custom_lambda_value("2")
    robust_principal_component_analysis_pane.set_lambda_weight(item_index=1)
    robust_principal_component_analysis_pane.set_custom_lambda_weight_value("0.5")
    robust_principal_component_analysis_pane.set_maximum_iterations("500")
    robust_principal_component_analysis_pane.set_tolerance("0.00001")
    robust_principal_component_analysis_pane.set_check_scale_observations()
    robust_principal_component_analysis_pane.set_check_center_observations()
    robust_principal_component_analysis_pane.set_initial_mu("0.001")
    robust_principal_component_analysis_pane.set_check_use_fixed_value_for_mu()

    robust_principal_component_analysis_pane.expand_windowshade_Singular_Value_Decomposition_Options()
    robust_principal_component_analysis_pane.set_svd_method(item_index=1)
    robust_principal_component_analysis_pane.set_maximum_rank("1234")
    robust_principal_component_analysis_pane.set_power("1")

    flow.run(True)


def test_37_robust_principal_component_analysis_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.lowrankoutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("lowrank'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "lowrank'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.sparseoutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("sparse'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "sparse'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.erroroutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("error'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "error'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.lsvoutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("left'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "left'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.svoutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("singular'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "singular'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.rsvoutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("right'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "right'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")

    robust_principal_component_analysis_pane.click_output_tab()
    robust_principal_component_analysis_pane.set_check_save_low_rank_data()
    robust_principal_component_analysis_pane.set_check_save_sparse_data()
    robust_principal_component_analysis_pane.set_check_save_error_data()
    robust_principal_component_analysis_pane.set_decomposition_method(item_index=1)
    robust_principal_component_analysis_pane.set_check_save_left_singular_vectors_data()
    robust_principal_component_analysis_pane.set_check_save_singular_values_data()
    robust_principal_component_analysis_pane.set_check_save_right_singular_vectors_data()
    flow.run(True)


def test_38_robust_principal_component_analysis_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.cloutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("component'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "component'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       "{sasstudio-steps-gui-icu.rpca.outputports.pcoutputtable.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("pc'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "pc'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")

    robust_principal_component_analysis_pane.click_output_tab()
    robust_principal_component_analysis_pane.set_decomposition_method(item_index=2)
    robust_principal_component_analysis_pane.set_check_save_component_loadings_data()
    robust_principal_component_analysis_pane.set_check_save_pc_scores_data()

    flow.run(True)


def test_39_verify_with_loqate_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.set_check_enable_address_verification()
    verify_with_loqate_pane.expand_windowshade_map_the_fields_for_address_verification()
    verify_with_loqate_pane.add_column_for_country("Country'测试")
    verify_with_loqate_pane.add_column_for_address_1("City'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)


def test_40_verify_with_loqate_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.set_check_enable_address_verification()
    verify_with_loqate_pane.set_check_geocode_the_address()
    verify_with_loqate_pane.set_check_perform_country_ISO_standardization_before_processing_address()
    verify_with_loqate_pane.set_check_show_api_input_and_output_json_in_the_log()
    verify_with_loqate_pane.set_batch_size_500_max("300")

    verify_with_loqate_pane.expand_windowshade_map_the_fields_for_address_verification()
    verify_with_loqate_pane.add_column_for_country("Country'测试")
    verify_with_loqate_pane.add_column_for_address_1("Street Name'测试")
    verify_with_loqate_pane.add_column_for_postal_code("Postal_Code'测试")
    verify_with_loqate_pane.add_column_for_locality_city_municipality("City'测试")
    verify_with_loqate_pane.add_column_for_administrative_area_state_province("State'测试")
    verify_with_loqate_pane.add_column_for_sub_administrative_area_county_region("Regione'测试")
    verify_with_loqate_pane.add_column_for_organization("Organization'测试")
    verify_with_loqate_pane.add_column_for_building("Building'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)


def test_41_verify_with_loqate_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.click_verify_email_tab()
    verify_with_loqate_pane.set_check_enable_email_verification()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_email()
    verify_with_loqate_pane.set_batch_size_100_max("50")
    verify_with_loqate_pane.add_column_for_email_address("Email'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)


def test_42_verify_with_loqate_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.click_verify_phone_numbers_tab()
    verify_with_loqate_pane.set_check_enable_phone_verification()
    verify_with_loqate_pane.set_check_perform_country_iso_standardization_before_processing_phone()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_phone()
    verify_with_loqate_pane.add_column_for_phone_number("Phone'测试")
    verify_with_loqate_pane.add_column_for_country_phone("Country'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)


def test_43_verify_with_loqate_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.set_check_enable_address_verification()
    verify_with_loqate_pane.set_check_geocode_the_address()
    verify_with_loqate_pane.set_check_perform_country_ISO_standardization_before_processing_address()
    verify_with_loqate_pane.set_check_show_api_input_and_output_json_in_the_log()
    verify_with_loqate_pane.set_batch_size_500_max("300")

    verify_with_loqate_pane.expand_windowshade_map_the_fields_for_address_verification()
    verify_with_loqate_pane.add_column_for_country("Country'测试")
    verify_with_loqate_pane.add_column_for_address_1("Street Name'测试")
    verify_with_loqate_pane.add_column_for_postal_code("Postal_Code'测试")
    verify_with_loqate_pane.add_column_for_locality_city_municipality("City'测试")
    verify_with_loqate_pane.add_column_for_administrative_area_state_province("State'测试")
    verify_with_loqate_pane.add_column_for_sub_administrative_area_county_region("Regione'测试")
    verify_with_loqate_pane.add_column_for_organization("Organization'测试")
    verify_with_loqate_pane.add_column_for_building("Building'测试")

    verify_with_loqate_pane.click_verify_email_tab()
    verify_with_loqate_pane.set_check_enable_email_verification()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_email()
    verify_with_loqate_pane.set_batch_size_100_max("50")
    verify_with_loqate_pane.add_column_for_email_address("Email'测试")

    verify_with_loqate_pane.click_verify_phone_numbers_tab()
    verify_with_loqate_pane.set_check_enable_phone_verification()
    verify_with_loqate_pane.set_check_perform_country_iso_standardization_before_processing_phone_both()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_phone_both()
    verify_with_loqate_pane.add_column_for_phone_number("Phone'测试")


    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)