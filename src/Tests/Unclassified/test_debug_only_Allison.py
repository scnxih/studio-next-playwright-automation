import time

from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.PrepareAndExploreData.standardize_data import StandardizeData
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.permutations import Permutations
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import AccordionType, TopMenuItem, DesignerControlType, FlowNodeType
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.one_way_frequencies import OneWayFrequencies
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_temp(page, init):
    PageHelper.show_accordion(page, AccordionType.sas_content)
    folder_path = ["SAS 内容", "Public"]
    folder_path1 = ["SAS 内容", "Public", "ßüöéçàê中文"]
    folder_name1 = "文件夹ŚrŻłßü1"
    folder_name2 = "文件夹ŚrŻłßü2"
    folder_name3 = "测试"
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name1)
    PageHelper.new_folder(page, 'ContextMenu', folder_path, folder_name2)
    PageHelper.new_folder(page, 'ContextMenu', folder_path1, folder_name3)

    folder_path1 = ["SAS 内容", "Public", "文件夹ŚrŻłßü1"]
    folder_path2 = ["SAS 内容", "Public", "文件夹ŚrŻłßü2"]
    folder_path3 = ["SAS 内容", "Public", "ßüöéçàê中文", "测试"]
    folder_path = [folder_path1, folder_path2, folder_path3]
    PageHelper.delete_multiple_items(page, 'ContextMenu', folder_path)


def test_01_custom_step(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.insert_control(DesignerControlType.input_table)
    properties.set_label("输入中文表")
    properties.set_uncheck_required()
    properties.set_indent("1")


def test_02_one_way_frequencies_in_flow_level0(page, init):
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
    flow.run(True)


def test_03_one_way_frequencies_in_flow_level1(page, init):
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
    flow.apply_detail_layout_vertical()
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
    flow.run(True)


def test_04_permutations_level0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_PERMUTATIONS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("OUT'中文测试")
    time.sleep(0.8)

    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_PERMUTATIONS, "OUT'中文测试")
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_PERMUTATIONS)
    permutations = Permutations(page)
    permutations.set_uncheck_replace_existing_output_table()
    flow.run(True)

    permutations.set_check_replace_existing_output_table()
    flow.run(True)

def test_05_standardize_data_in_flow_level0(page, init):
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
    standardize_data.expand_windowshade_additional_roles()
    standardize_data.add_column_for_frequency_count(column_name="nHome'中")
    standardize_data.add_column_for_weight(column_name="nRBI'中")
    standardize_data.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])
    flow.run(True)
