from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.centrality_metrics_pane import \
    CentralityMetricsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.cluster_variables_pane import ClusterVariablesPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.coin_toss_simulation_pane import CoinTossSimulationPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.poker_hand_probability_pane import PokerHandProbabilityPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.line_chart_pane import LineChartPane

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
