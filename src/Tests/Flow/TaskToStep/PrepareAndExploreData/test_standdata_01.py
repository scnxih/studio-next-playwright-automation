"""This is test case file for step Standardize Data"""
"""Added by Allison 8/21/2024 """
import time
import pytest
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.PrepareAndExploreData.standardize_data_pane import StandardizeData
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.permutations_pane import Permutations
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import AccordionType, TopMenuItem, DesignerControlType, FlowNodeType
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.one_way_frequencies_pane import OneWayFrequencies
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
@pytest.mark.level0_step
def test_01_standardize_data_in_flow_level0(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_STANDARDIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_STANDARDIZE_DATA)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_STANDARDIZE_DATA)
    standardize_data = StandardizeData(page)
    standardize_data.add_columns_for_variables_to_standardize(check_column_name_list=["nAtBat'中", "nHits'中"])
    time.sleep(1)
    flow.screenshot_self("data")
    flow.run(False)
    flow.screenshot_after_run_slow()


@pytest.mark.level1_step
def test_02_standardize_data_in_flow_level1(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_STANDARDIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_STANDARDIZE_DATA)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_STANDARDIZE_DATA)
    # flow.apply_detail_layout_vertical()
    standardize_data = StandardizeData(page)
    standardize_data.add_columns_for_variables_to_standardize(check_column_name_list=["nAtBat'中", "nHits'中"])
    standardize_data.expand_windowshade_additional_roles()
    standardize_data.add_column_for_frequency_count(column_name="nHome'中")
    standardize_data.add_column_for_weight(column_name="nRBI'中")
    standardize_data.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    standardize_data.click_options_tab()
    standardize_data.set_check_center_data_only()
    standardize_data.set_centering_method(item_index=1)
    standardize_data.set_missing_values_method(item_index=1)
    standardize_data.set_check_for_display_location_and_scale_measures()
    time.sleep(0.5)
    flow.screenshot_self("options")
    standardize_data.click_output_tab()
    standardize_data.set_variables_to_include(item_index=0)
    # standardize_data.set_specify_data_to_show(item_index=1)
    time.sleep(0.5)
    flow.screenshot_self("output")
    flow.run(False)
    flow.screenshot_after_run_slow()

#@pytest.mark.level1_step
def test_03_standardize_data_in_flow_level1(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_STANDARDIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_STANDARDIZE_DATA)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_STANDARDIZE_DATA)
    # flow.apply_detail_layout_vertical()
    standardize_data = StandardizeData(page)
    standardize_data.set_filter_input_data("'nAtBat''中'n> 220")
    standardize_data.add_columns_for_variables_to_standardize(check_column_name_list=["nAtBat'中", "nHits'中"])
    standardize_data.expand_windowshade_additional_roles()
    standardize_data.add_column_for_frequency_count(column_name="nHome'中")
    standardize_data.add_column_for_weight(column_name="nRBI'中")
    standardize_data.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    standardize_data.click_options_tab()
    standardize_data.set_standardization_method(item_index=1)
    standardize_data.set_tuning_constant("3.5")

    standardize_data.click_output_tab()
    standardize_data.set_specify_prefix_radiobutton(item_index=1)
    standardize_data.set_prefix_for_original_variables(input_text="测试")
    standardize_data.set_specify_data_to_show(item_index=2)
    flow.run(False)
    flow.screenshot_after_run_slow()

@pytest.mark.level1_step
def test_04_standardize_data_in_flow_level1(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_STANDARDIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_STANDARDIZE_DATA)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_STANDARDIZE_DATA)
    # flow.apply_detail_layout_vertical()
    standardize_data = StandardizeData(page)
    standardize_data.set_filter_input_data("'nAtBat''中'n> 220")
    standardize_data.add_columns_for_variables_to_standardize(check_column_name_list=["nAtBat'中", "nHits'中"])
    standardize_data.expand_windowshade_additional_roles()
    standardize_data.add_column_for_frequency_count(column_name="nHome'中")
    standardize_data.add_column_for_weight(column_name="nRBI'中")
    standardize_data.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文","League'中"])

    standardize_data.click_options_tab()
    standardize_data.set_standardization_method(item_index=7)
    standardize_data.set_lambda("20")
    standardize_data.set_missing_values_method(item_index=1)
    standardize_data.set_replace_missing_values_with(item_index=4)
    standardize_data.set_custom_value("1000")

    standardize_data.click_output_tab()
    standardize_data.set_prefix_for_standardized_variables(input_text="测试_std")
    flow.run(False)
    flow.screenshot_after_run_slow()

@pytest.mark.level1_step
def test_05_standardize_data_in_flow_level1(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_STANDARDIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_STANDARDIZE_DATA)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_STANDARDIZE_DATA)
    # flow.apply_detail_layout_vertical()
    standardize_data = StandardizeData(page)
    standardize_data.set_filter_input_data("'nAtBat''中'n> 220")
    standardize_data.add_columns_for_variables_to_standardize(check_column_name_list=["nAtBat'中", "nHits'中"])
    standardize_data.expand_windowshade_additional_roles()
    standardize_data.add_column_for_frequency_count(column_name="nHome'中")
    standardize_data.add_column_for_weight(column_name="nRBI'中")
    standardize_data.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文","League'中"])

    standardize_data.click_options_tab()
    standardize_data.set_standardization_method(item_index=11)
    standardize_data.set_proportion_of_pairs("0.6")
    standardize_data.set_missing_values_method(item_index=1)
    standardize_data.set_replace_missing_values_with(item_index=2)

    standardize_data.click_output_tab()
    standardize_data.set_variables_to_include(item_index=0)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("out'标准化")
    time.sleep(0.6)

    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_STANDARDIZE_DATA, "out'标准化")
    flow.run(False)
    flow.screenshot_after_run_slow()