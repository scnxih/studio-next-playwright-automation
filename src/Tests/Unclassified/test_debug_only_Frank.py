"""
@author: Frank (Feng) Jiang
@date: 2024/08/22
@description:
"""

from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.scatter_map_pane import ScatterMapPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Econometrics.hidden_markov_models_pane import HiddenMarkovModelsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.traveling_salesman_problem_pane import TravelingSalesmanProblemPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TextAnalytics.segmentation_pane import SegmentationPane
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


def test_traveling_salesman_problem(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CORE_DECOMPOSITION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.apply_detail_layout_vertical()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LinkSetIn'链接")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM]
    flow.add_step_from_stepspane_to_flow(step_path)
    time.sleep(0.5)

    flow.link_two_nodes_in_flow("LinkSetIn'链接", Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM)
    traveling_salesman_problem_pane = TravelingSalesmanProblemPane(page)
    traveling_salesman_problem_pane.select_server(Helper.data_locale.CAS)
    time.sleep(0.5)
    traveling_salesman_problem_pane.expand_windowshade_note_about_server_selection()
    time.sleep(0.5)
    traveling_salesman_problem_pane.collapse_windowshade_note_about_server_selection()
    time.sleep(0.5)
    traveling_salesman_problem_pane.input_filter_links_data("This is a filter expression.")
    time.sleep(0.5)
    traveling_salesman_problem_pane.empty_filter_links_data()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_link_direction(Helper.data_locale.DIRECTED)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_link_direction(Helper.data_locale.UNDIRECTED)
    time.sleep(0.5)
    traveling_salesman_problem_pane.add_column_for_from_node("from'始")
    time.sleep(0.5)
    traveling_salesman_problem_pane.add_column_for_to_node("to'终")
    time.sleep(0.5)
    traveling_salesman_problem_pane.add_column_for_weight("weight'中")
    time.sleep(0.5)
    traveling_salesman_problem_pane.expand_windowshade_additional_roles()
    time.sleep(0.5)
    traveling_salesman_problem_pane.click_options_tab()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_max_time(Helper.data_locale.USE_CUSTOM_VALUE)
    time.sleep(0.5)
    traveling_salesman_problem_pane.input_time_in_seconds("1000")
    time.sleep(0.5)
    traveling_salesman_problem_pane.select_log_details(Helper.data_locale.DETAILED_SUMMARY)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_solution_strategy(Helper.data_locale.MIXED_INTEGER_LINEAR_PROGRAMMING)
    time.sleep(0.5)
    traveling_salesman_problem_pane.expand_windowshade_MILP_solver_options()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_target_objective_value(Helper.data_locale.USE_CUSTOM_VALUE)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_target_objective_value(Helper.data_locale.NO_LIMIT)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_absolute_gap_between_current_and_best_remaining_objective_value(Helper.data_locale.USE_CUSTOM_VALUE)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_absolute_gap_between_current_and_best_remaining_objective_value(Helper.data_locale.USE_000001)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_relative_gap_between_current_and_best_remaining_objective_value(Helper.data_locale.USE_CUSTOM_VALUE)
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_relative_gap_between_current_and_best_remaining_objective_value(Helper.data_locale.USE_0001)
    time.sleep(0.5)
    traveling_salesman_problem_pane.select_procedure(Helper.data_locale.USE_CAS_PROCEDURE)
    time.sleep(0.5)
    traveling_salesman_problem_pane.click_output_tab()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_check_save_tour_info()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_check_save_tour_nodes_info()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_uncheck_replace_existing_output_table_for_save_tour_info()
    time.sleep(0.5)
    traveling_salesman_problem_pane.set_uncheck_replace_existing_output_table_for_save_tour_nodes_info()
    time.sleep(5)


def test_segmentation(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS, Helper.data_locale.STEP_SEGMENTATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    # flow.add_node(FlowNodeType.table)
    # flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    # table_pane = TablePane(page)
    # table_pane.set_library("SASHELP")
    # table_pane.set_table("CLASS")
    # time.sleep(0.5)
    # flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.STEP_SEGMENTATION)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEGMENTATION)
    segmentation_pane = SegmentationPane(page)
    # segmentation_pane.set_key_var(Helper.data_locale.SELECT_VAR)
    # time.sleep(0.5)
    # segmentation_pane.ad
    segmentation_pane.click_output_tab()
    segmentation_pane.set_check_save_segmentation_results()
    time.sleep(0.5)
    segmentation_pane.set_uncheck_replace_existing_output_table()
    time.sleep(0.5)
    segmentation_pane.set_check_replace_existing_output_table()
    time.sleep(1)
    segmentation_pane.set_uncheck_replace_existing_output_table_for_save_segmentation_results()
    time.sleep(0.5)
    segmentation_pane.set_check_replace_existing_output_table_for_save_segmentation_results()
    time.sleep(0.5)


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


def test_hidden_markov_models_l0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.HIDDEN_MARKOV_MODELS)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("ONE'中")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_HIDDEN_MARKOV_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("ONE'中", Helper.data_locale.STEP_HIDDEN_MARKOV_MODELS)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_HIDDEN_MARKOV_MODELS)

    hidden_markov_models_pane = HiddenMarkovModelsPane(page)
    hidden_markov_models_pane.add_columns(Helper.data_locale.DEPENDENT_VARS, check_column_name_list=["y'中", "x'中"])
    time.sleep(0.8)
    hidden_markov_models_pane.add_column(Helper.data_locale.TIME_ID, "t'中")
    time.sleep(0.8)
    flow.run(True)


def test_hidden_markov_models_l1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.HIDDEN_MARKOV_MODELS)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("ONE'中")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_HIDDEN_MARKOV_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("ONE'中", Helper.data_locale.STEP_HIDDEN_MARKOV_MODELS)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_HIDDEN_MARKOV_MODELS)

    hidden_markov_models_pane = HiddenMarkovModelsPane(page)
    hidden_markov_models_pane.add_columns(Helper.data_locale.DEPENDENT_VARS, check_column_name_list=["y'中", "x'中"])
    time.sleep(0.8)
    hidden_markov_models_pane.add_column(Helper.data_locale.TIME_ID, "t'中")
    time.sleep(0.8)

    hidden_markov_models_pane.click_model_tab()
    hidden_markov_models_pane.set_option_for_combobox(Helper.data_locale.MODEL_TYPE,
                                                      item_value=Helper.data_locale.REGIME_SWITCHING_AUTOREGRESSION)
    time.sleep(0.5)
    hidden_markov_models_pane.set_check_for_checkbox(Helper.data_locale.ADD_SEASONAL_DUMMIES_AS_REGRESSORS)
    hidden_markov_models_pane.set_check_for_checkbox(Helper.data_locale.ADD_TIME_TRENDS_AS_REGRESSORS)
    hidden_markov_models_pane.set_check_for_checkbox(Helper.data_locale.ADD_LAGS_OF_THE_INDEPENDENT_VARS)
    hidden_markov_models_pane.set_check_for_checkbox(Helper.data_locale.INCLUDE_ONLY_THE_LAGGED_VALUES_OF_THE_INDEPENDENT_VARS)
    time.sleep(0.8)

    hidden_markov_models_pane.click_options_tab()
    time.sleep(0.5)
    hidden_markov_models_pane.set_check_for_checkbox(Helper.data_locale.ESTIMATE_THE_NONSTATIONARY_MARKOV_CHAIN)
    hidden_markov_models_pane.expand_windowshade_nonlinear_optimization()
    hidden_markov_models_pane.set_check_for_checkbox(Helper.data_locale.ENABLE_MULTISTART_MODE)
    hidden_markov_models_pane.select_procedure(Helper.data_locale.USE_CAS_PROCEDURE)
    time.sleep(0.8)

    flow.run(True)


def test_traveling_salesman_problem_l0(page, init):
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
    time.sleep(0.5)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM)
    flow.arrange_nodes()
    time.sleep(0.5)

    traveling_salesman_problem_pane = TravelingSalesmanProblemPane(page)
    traveling_salesman_problem_pane.add_column_for_from_node("from'始")
    traveling_salesman_problem_pane.add_column_for_to_node("to'终")
    time.sleep(0.5)
    flow.run(True)


def test_traveling_salesman_problem_l1(page, init):
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
    time.sleep(0.5)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    time.sleep(0.5)

    traveling_salesman_problem_pane = TravelingSalesmanProblemPane(page)
    traveling_salesman_problem_pane.add_column_for_from_node("from'始")
    traveling_salesman_problem_pane.add_column_for_to_node("to'终")
    time.sleep(0.5)

    traveling_salesman_problem_pane.click_options_tab()
    traveling_salesman_problem_pane.select_log_details(Helper.data_locale.DETAILED_SUMMARY)
    traveling_salesman_problem_pane.select_procedure(Helper.data_locale.USE_OPTMODEL_PROCEDURE)
    time.sleep(0.5)

    traveling_salesman_problem_pane.click_output_tab()
    traveling_salesman_problem_pane.set_check_save_tour_info()
    traveling_salesman_problem_pane.set_check_save_tour_nodes_info()
    time.sleep(0.5)

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.travelingsalesmanproblem.outputports.outDSName.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("输出表")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM, "输出表")
    time.sleep(0.5)
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.travelingsalesmanproblem.outputports.outNodesDSName.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("输出节点表")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TRAVELING_SALESMAN_PROBLEM, "输出节点表")
    flow.arrange_nodes()
    time.sleep(0.5)
    flow.run(True)
