"""This is test case file for step t Tests"""
import pytest
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.t_tests_pane import TTestsPane
from src.Data.input_data_zh import *
from src.Helper.page_factory import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


@pytest.mark.level0_step
def test_00_t_test_one_sample_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.add_column_for_analysis_var("马力")
    time.sleep(0.5)
    flow.run(True)


@pytest.mark.level0_step
def test_01_t_test_paired_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.T_TEST_LOWER, item_value=Helper.data_locale.PAIRED_TEST)
    t_tests_pane.add_column_for_group1_var("城市油耗")
    t_tests_pane.add_column_for_group2_var("高速油耗")
    time.sleep(0.5)
    flow.run(True)


@pytest.mark.level0_step
def test_02_t_test_two_sample_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_T_TESTS)

    t_tests_pane = TTestsPane(page)
    t_tests_pane.set_option_for_combobox(Helper.data_locale.T_TEST_LOWER, item_value=Helper.data_locale.TWO_SAMPLE_TEST)
    time.sleep(0.5)
    t_tests_pane.add_column_for_analysis_var("nHome'中")
    time.sleep(0.5)
    t_tests_pane.add_column_for_class_var("League'中")
    time.sleep(0.5)
    flow.run(True)


@pytest.mark.level1_step
def test_03_t_test_one_sample_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
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


@pytest.mark.level1_step
def test_04_t_test_paired_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
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


@pytest.mark.level1_step
def test_05_t_test_two_sample_in_flow(page, init):
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
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
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
