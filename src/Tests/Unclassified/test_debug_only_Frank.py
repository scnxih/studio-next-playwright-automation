"""
@author: Frank (Feng) Jiang
@date: 2024/08/22
@description:
"""

from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.scatter_map_pane import ScatterMapPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.t_tests_pane import TTestsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.canonical_correlation_pane import CanonicalCorrelationPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.core_decomposition_pane import CoreDecompositionPane
from src.Data.input_data_zh import *
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_input_table(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.HIDDEN_MARKOV_MODELS)
    editor.run(True)


def test_scatter_map_controls_in_data_pane(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.apply_detail_layout_vertical()
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_SCATTER_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    time.sleep(0.5)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SCATTER_MAP)
    scatter_map_pane = ScatterMapPane(page)
    scatter_map_pane.collapse_windowshade_plot_data()
    time.sleep(0.5)
    scatter_map_pane.expand_windowshade_plot_data()
    time.sleep(0.5)
    scatter_map_pane.input_filter_input_data("This is expression.")
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_plot_data()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_choropleth_map_layer()
    time.sleep(0.5)
    scatter_map_pane.set_uncheck_include_choropleth_map_layer()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_choropleth_map_layer()
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_data()
    time.sleep(0.5)
    scatter_map_pane.expand_windowshade_map_data()
    time.sleep(0.5)
    scatter_map_pane.input_filter_map_data("This is expression.")
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_data()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_response_data()
    time.sleep(0.5)
    scatter_map_pane.set_uncheck_include_response_data()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_response_data()
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_response_data()
    time.sleep(0.5)
    scatter_map_pane.expand_windowshade_map_response_data()
    time.sleep(0.5)
    scatter_map_pane.input_filter_map_response_data("This is expression.")
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_response_data()
    time.sleep(0.5)
    scatter_map_pane.set_uncheck_ID_variable()
    time.sleep(0.5)
    scatter_map_pane.set_check_ID_variable()
    time.sleep(0.5)
    scatter_map_pane.select_radio_base_map(item_value=Helper.data_locale.ESRI_MAP)
    time.sleep(0.5)
    scatter_map_pane.input_Esri_URL("http://www.google.com")
    time.sleep(0.5)
    scatter_map_pane.select_radio_base_map(item_value=Helper.data_locale.OPEN_STREET_MAP)


def test_scatter_map_l0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.SCATTER_MAP)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("CITY_POP_LOC'中")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_SCATTER_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CITY_POP_LOC'中", Helper.data_locale.STEP_SCATTER_MAP)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SCATTER_MAP)

    scatter_map_pane = ScatterMapPane(page)
    scatter_map_pane.add_column_for_latitude("lat'纬度")
    time.sleep(0.5)
    scatter_map_pane.add_column_for_longitude("long'经度")
    time.sleep(0.5)
    flow.run(True)


def test_t_test_l0_one_sample(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CARS")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_T_TESTS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CARS", Helper.data_locale.STEP_T_TESTS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.add_column_for_analysis_var("马力")
    time.sleep(0.5)
    flow.run(True)


def test_t_test_l0_paired(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CARS")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_T_TESTS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CARS", Helper.data_locale.STEP_T_TESTS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.T_TEST_LOWER, item_value=Helper.data_locale.PAIRED_TEST)
    t_tests_pane.add_column_for_group1_var("城市油耗")
    t_tests_pane.add_column_for_group2_var("高速油耗")
    time.sleep(0.5)
    flow.run(True)


def test_t_test_l0_two_sample(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_T_TESTS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_T_TESTS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.T_TEST_LOWER, item_value=Helper.data_locale.TWO_SAMPLE_TEST)
    time.sleep(0.5)
    t_tests_pane.add_column_for_analysis_var("nHome'中")
    time.sleep(0.5)
    t_tests_pane.add_column_for_class_var("League'中")
    time.sleep(0.5)
    flow.run(True)


def test_t_test_l1_one_sample(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CARS")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_T_TESTS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CARS", Helper.data_locale.STEP_T_TESTS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.add_column_for_analysis_var("马力")
    time.sleep(0.5)

    t_tests_pane.click_options_tab()
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.SIGN_TEST_WILCOXON_SIGNED_RANK_TEST)
    time.sleep(0.5)
    t_tests_pane.collapse_windowshade(Helper.data_locale.PLOTS)
    time.sleep(0.5)
    t_tests_pane.expand_windowshade(Helper.data_locale.PLOTS)
    time.sleep(0.5)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.PLOTS, item_value=Helper.data_locale.SELECTED_PLOTS)
    time.sleep(0.5)
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.CONFIDENCE_INTERVAL_PLOT)
    time.sleep(0.5)

    flow.run(True)


def test_t_test_l1_paired(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CARS")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_T_TESTS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CARS", Helper.data_locale.STEP_T_TESTS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.T_TEST_LOWER, item_value=Helper.data_locale.PAIRED_TEST)
    t_tests_pane.add_column_for_group1_var("城市油耗")
    t_tests_pane.add_column_for_group2_var("高速油耗")
    time.sleep(0.5)

    t_tests_pane.click_options_tab()
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.SIGN_TEST_WILCOXON_SIGNED_RANK_TEST)
    time.sleep(0.5)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.PLOTS, item_value=Helper.data_locale.SELECTED_PLOTS)
    time.sleep(0.5)
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.CONFIDENCE_INTERVAL_PLOT)
    time.sleep(0.5)

    flow.run(True)


def test_t_test_l1_two_sample(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_T_TESTS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_T_TESTS)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.T_TEST_LOWER, item_value=Helper.data_locale.TWO_SAMPLE_TEST)
    time.sleep(0.5)
    t_tests_pane.add_column_for_analysis_var("nHome'中")
    time.sleep(0.5)
    t_tests_pane.add_column_for_class_var("League'中")
    time.sleep(0.5)

    t_tests_pane.click_options_tab()
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.COX_COCHRAN_PROB_APPR_FOR_UNEQUAL_VARIANCES)
    time.sleep(0.5)
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.WILCOXON_RANK_SUM_TEST)
    time.sleep(0.5)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.PLOTS, item_value=Helper.data_locale.SELECTED_PLOTS)
    time.sleep(0.5)
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.CONFIDENCE_INTERVAL_PLOT)
    time.sleep(0.5)
    t_tests_pane.set_check_for_checkbox(Helper.data_locale.WILCOXON_BOX_PLOT)
    time.sleep(0.5)
    flow.run(True)


def test_canonical_correlation_l0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CANONICAL_CORRELATION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("JOBS'中")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CANONICAL_CORRELATION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("JOBS'中", Helper.data_locale.STEP_CANONICAL_CORRELATION)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CANONICAL_CORRELATION)

    canonical_correlation_pane = CanonicalCorrelationPane(page)
    canonical_correlation_pane.add_columns_for_var_set1(["career'中", "supervisor'中", "finance'中"])
    time.sleep(0.5)
    canonical_correlation_pane.add_columns_for_var_set2(["variety'中", "feedback'中", "autonomy'中"])
    time.sleep(0.5)
    flow.run(True)


def test_canonical_correlation_l1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CANONICAL_CORRELATION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("JOBS'中")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CANONICAL_CORRELATION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("JOBS'中", Helper.data_locale.STEP_CANONICAL_CORRELATION)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CANONICAL_CORRELATION)

    canonical_correlation_pane = CanonicalCorrelationPane(page)
    canonical_correlation_pane.add_columns_for_var_set1(["career'中", "supervisor'中", "finance'中"])
    time.sleep(0.5)
    canonical_correlation_pane.add_columns_for_var_set2(["variety'中", "feedback'中", "autonomy'中"])
    time.sleep(0.5)

    canonical_correlation_pane.click_options_tab()
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CANONICAL_VAR_SCORE_PLOTS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.PERFORM_REGRESSION)
    time.sleep(0.5)
    canonical_correlation_pane.expand_windowshade(Helper.data_locale.CORRELATIONS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CORRELATIONS_OF_REGRESSION_COEFFICIENTS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.PARTIAL_CORRELATIONS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SQUARED_PARTIAL_CORRELATIONS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SEMIPARTIAL_CORRELATIONS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SQUARED_SEMIPARTIAL_CORRELATIONS)
    time.sleep(0.5)

    canonical_correlation_pane.expand_windowshade(Helper.data_locale.REGRESSION_STAT)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.STANDARDIZED_REGRESSION_COEFFICIENTS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.STANDARD_ERROR_OF_COEFFICIENTS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.T_STAT_FOR_COEFFICIENTS)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SQUARED_MULTIPLE_CORRELATION)
    time.sleep(0.5)

    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SPECIFY_NUM_OF_CANONICAL_VARIATES)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CANONICAL_REDUNDANCY_STAT)
    time.sleep(0.5)

    canonical_correlation_pane.click_output_tab()
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CREATE_SCORE_DATASET)
    time.sleep(0.5)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CREATE_STAT_DATASET)
    time.sleep(0.5)

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "添加输出端口",
                                                 "{sasstudio-steps-gui-icu.canonicalcorrelation.outputports.outputTableOne.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("SCORE'数据'")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "SCOREDATA")
    flow.arrange_nodes()

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "添加输出端口",
                                                 "{sasstudio-steps-gui-icu.genericText.outputport.statisticsTable.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("STAT'数据'")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "STATDATA")
    flow.arrange_nodes()
    flow.run(True)


def test_core_decomposition_l0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CORE_DECOMPOSITION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETIN'链接")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_CORE_DECOMPOSITION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CORE_DECOMPOSITION)

    core_decomposition_pane = CoreDecompositionPane(page)
    core_decomposition_pane.add_column_for_from_node("from'始")
    core_decomposition_pane.add_column_for_to_node("to'终")
    time.sleep(1)

    core_decomposition_pane.click_output_tab()
    core_decomposition_pane.set_check_for_checkbox(Helper.data_locale.CREATE_NODES_TABLE)

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    time.sleep(0.5)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("输出节点表")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "输出节点表")
    flow.run(True)


def test_core_decomposition_l1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CORE_DECOMPOSITION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETIN'链接")
    time.sleep(0.8)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("NODESETIN'节点")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_CORE_DECOMPOSITION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "添加输入端口",
                                                 "{sasstudio-steps-gui-icu.coredecomposition.inputports.nodesdataset.displayname.title}")
    flow.link_two_nodes_in_flow("NODESETIN'节点", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CORE_DECOMPOSITION)

    core_decomposition_pane = CoreDecompositionPane(page)
    core_decomposition_pane.add_column_for_from_node("from'始")
    core_decomposition_pane.add_column_for_to_node("to'终")

    core_decomposition_pane.set_check_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)
    core_decomposition_pane.expand_windowshade(Helper.data_locale.NODES)
    core_decomposition_pane.add_column_for_node("node'中")
    time.sleep(0.8)
    flow.run(True)
