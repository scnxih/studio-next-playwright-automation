"""This is test case file for step Canonical Correlation"""
import pytest
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.canonical_correlation_pane import CanonicalCorrelationPane
from src.Data.input_data_zh import *
from src.Helper.page_factory import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


@pytest.mark.level0_step
def test_00_canonical_correlation_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CANONICAL_CORRELATION)

    canonical_correlation_pane = CanonicalCorrelationPane(page)
    canonical_correlation_pane.add_columns_for_var_set1(["career'中", "supervisor'中", "finance'中"])
    time.sleep(0.5)
    canonical_correlation_pane.add_columns_for_var_set2(["variety'中", "feedback'中", "autonomy'中"])
    time.sleep(0.5)
    flow.run(False)


@pytest.mark.level1_step
def test_00_canonical_correlation_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CANONICAL_CORRELATION)

    canonical_correlation_pane = CanonicalCorrelationPane(page)
    canonical_correlation_pane.add_columns_for_var_set1(["career'中", "supervisor'中", "finance'中"])
    time.sleep(0.5)
    canonical_correlation_pane.add_columns_for_var_set2(["variety'中", "feedback'中", "autonomy'中"])
    time.sleep(0.5)

    canonical_correlation_pane.click_options_tab()
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CANONICAL_VAR_SCORE_PLOTS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.PERFORM_REGRESSION)
    time.sleep(0.2)
    canonical_correlation_pane.expand_windowshade(Helper.data_locale.CORRELATIONS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CORRELATIONS_OF_REGRESSION_COEFFICIENTS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.PARTIAL_CORRELATIONS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SQUARED_PARTIAL_CORRELATIONS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SEMIPARTIAL_CORRELATIONS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SQUARED_SEMIPARTIAL_CORRELATIONS)
    time.sleep(0.2)

    canonical_correlation_pane.expand_windowshade(Helper.data_locale.REGRESSION_STAT)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.STANDARDIZED_REGRESSION_COEFFICIENTS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.STANDARD_ERROR_OF_COEFFICIENTS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.T_STAT_FOR_COEFFICIENTS)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SQUARED_MULTIPLE_CORRELATION)
    time.sleep(0.2)

    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.SPECIFY_NUM_OF_CANONICAL_VARIATES)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CANONICAL_REDUNDANCY_STAT)
    time.sleep(0.2)

    canonical_correlation_pane.click_output_tab()
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CREATE_SCORE_DATASET)
    time.sleep(0.2)
    canonical_correlation_pane.set_check_for_checkbox(Helper.data_locale.CREATE_STAT_DATASET)
    time.sleep(0.2)

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.canonicalcorrelation.outputports.outputTableOne.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("SCORE'数据")
    time.sleep(0.5)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "SCORE'数据")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.genericText.outputport.statisticsTable.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("STAT'数据")
    time.sleep(0.5)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CANONICAL_CORRELATION, "STAT'数据")
    flow.arrange_nodes()
    flow.run(False)
