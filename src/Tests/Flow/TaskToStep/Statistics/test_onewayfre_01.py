"""This is test case file for step One-Way Frequencies"""
import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.one_way_frequencies_pane import OneWayFrequencies
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Utilities.enums import FlowNodeType
from src.Helper.helper import Helper
import time
@pytest.mark.level0_step
def test_01_one_way_frequencies_in_flow_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_ONE_WAY_FREQUENCIES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_ONE_WAY_FREQUENCIES)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ONE_WAY_FREQUENCIES)
    one_way_frequencies = OneWayFrequencies(page)
    one_way_frequencies.add_columns_for_analysis_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    flow.screenshot_self("data")
    flow.run(False)
    flow.screenshot_after_run()

@pytest.mark.level1_step
def test_02_one_way_frequencies_in_flow_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_ONE_WAY_FREQUENCIES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_ONE_WAY_FREQUENCIES)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ONE_WAY_FREQUENCIES)
    # flow.apply_detail_layout_vertical()
    one_way_frequencies = OneWayFrequencies(page)
    one_way_frequencies.set_filter_input_data("'nAtBat''中'n> 220")
    one_way_frequencies.add_columns_for_analysis_variables(check_column_name_list=["nAtBat'中", "nHome'中"])
    one_way_frequencies.expand_windowshade_additional_roles()
    one_way_frequencies.add_column_for_frequency_count(column_name="nHits'中")
    one_way_frequencies.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    one_way_frequencies.click_options_tab()
    one_way_frequencies.set_row_value_order(item_index=2)
    one_way_frequencies.expand_windowshade_statistics()
    one_way_frequencies.set_check_for_asymptotic_test_binomial_proportion()
    one_way_frequencies.set_null_hypothesis_proportion("0.6")
    one_way_frequencies.set_confidence_level(item_index=3)
    one_way_frequencies.set_custom_confidence_level("86")
    one_way_frequencies.set_check_for_exact_test_binomial_proportion()
    one_way_frequencies.set_check_for_asymptotic_test_chi_square_goodness_of_fit()
    one_way_frequencies.set_check_for_exact_test_chi_square_goodness_of_fit()
    one_way_frequencies.set_check_use_monte_carlo_estimation()
    one_way_frequencies.expand_windowshade_exact_computation_methods()
    one_way_frequencies.set_maximum_time("600")

    one_way_frequencies.expand_windowshade_plots_and_missing_values()
    one_way_frequencies.set_check_include_in_frequency_table()
    flow.screenshot_self("options")
    flow.run(False)
    flow.screenshot_after_run()