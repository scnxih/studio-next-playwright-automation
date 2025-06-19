import time

from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.MachineLearning.support_vector_data_description_pane import \
    SupportVectorDataDescription
from src.Pages.StudioNext.Center.Flow.DetailsPane.PrepareAndExploreData.standardize_data_pane import StandardizeData
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.permutations_pane import Permutations
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import AccordionType, TopMenuItem, DesignerControlType, FlowNodeType
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.one_way_frequencies_pane import OneWayFrequencies
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
    properties.set_indent(1)


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
    flow.run(False)


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
    flow.run(False)


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
    flow.run(False)

    permutations.set_check_replace_existing_output_table()
    flow.run(False)


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
    flow.run(False)


def test_06_standardize_data_in_flow_level1(page, init):
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
    flow.apply_detail_layout_vertical()
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

    standardize_data.click_output_tab()
    standardize_data.set_variables_to_include(item_index=0)
    standardize_data.set_specify_data_to_show(item_index=1)
    flow.run(False)


def test_07_standardize_data_in_flow_level1(page, init):
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
    flow.apply_detail_layout_vertical()
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


def test_08_standardize_data_in_flow_level1(page, init):
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
    flow.apply_detail_layout_vertical()
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
    standardize_data.set_specify_prefix_radiobutton(item_index=0)
    standardize_data.set_prefix_for_standardized_variables(input_text="测试_std")
    standardize_data.set_specify_data_to_show(item_index=0)
    flow.run(False)


def test_09_standardize_data_in_flow_level1(page, init):
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
    flow.apply_detail_layout_vertical()
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

def test_01_support_vector_data_description_in_flow_level0(page, init):
    PageHelper.new_sas_program(page)
    sas_program_pane = SASProgramPage(page)
    code = """
libname autolib "/segatest/I18N/Autolib/";
libname mycas cas;

data mycas.'BASEBALL''中文测试'n;
    set AUTOLIB.'BASEBALL''中文测试'n;
run;"""
    sas_program_pane.editor.type_into_text_area(code)
    sas_program_pane.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING, Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)
    support_vector_data_description = SupportVectorDataDescription(page)
    support_vector_data_description.add_columns_for_interval_inputs(check_column_name_list=["nAtBat'中", "nHome'中"])

    support_vector_data_description.click_options_tab()
    support_vector_data_description.set_text_for_rbf_bandwidth_parameter("10")
    flow.run(False)

def test_02_support_vector_data_description_in_flow_level1(page, init):
        PageHelper.new_sas_program(page)
        sas_program_pane = SASProgramPage(page)
        code = """
    libname autolib "/segatest/I18N/Autolib/";
    libname mycas cas;

    data mycas.'BASEBALL''中文测试'n;
        set AUTOLIB.'BASEBALL''中文测试'n;
    run;"""
        sas_program_pane.editor.type_into_text_area(code)
        sas_program_pane.run(True)

        flow: FlowPage = PageHelper.new_flow(page)
        flow.add_node(FlowNodeType.table)
        flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
        table_pane = TablePane(page)
        table_pane.set_library("MYCAS")
        table_pane.set_table("BASEBALL'中文测试")
        time.sleep(0.8)

        step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                     Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION]
        flow.add_step_from_stepspane_to_flow(step_path)
        flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)
        flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)
        flow.apply_flow_layout_vertical()
        time.sleep(0.8)
        flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION,
                                                Helper.data_locale.ADD_OUTPUT_PORT,
                                                Helper.data_locale.SUPPORT_VECTORS_DATA_TABLE)
        flow.add_node(FlowNodeType.table)
        flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
        table_pane.set_library("MYCAS")
        table_pane.set_table("OUT'SVDD中")
        flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION, "OUT'SVDD中")
        flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)

        support_vector_data_description = SupportVectorDataDescription(page)

        support_vector_data_description.set_filter_input_data("'nAtBat''中'n> 220")

        support_vector_data_description.add_columns_for_norminal_inputs(
            check_column_name_list=["Team'中文", "Position'中"])
        support_vector_data_description.expand_windowshade_additional_roles()
        support_vector_data_description.add_column_for_weight_variables("logSalary'中")

        support_vector_data_description.click_options_tab()
        support_vector_data_description.set_text_for_rbf_bandwidth_parameter("100")
        support_vector_data_description.set_text_for_expected_outlier_fraction("0.05")
        support_vector_data_description.set_text_for_solver_tolerance("30")
        support_vector_data_description.set_maximum_iterations("200")

        support_vector_data_description.click_output_tab()
        support_vector_data_description.set_check_create_support_vectors_data()
        support_vector_data_description.set_include_variables_from_the_input_data_set(0)

        flow.run(False)
        flow.screenshot_after_run()

def test_03_support_vector_data_description_in_flow_level1(page, init):
        PageHelper.new_sas_program(page)
        sas_program_pane = SASProgramPage(page)
        code = """
    libname autolib "/segatest/I18N/Autolib/";
    libname mycas cas;

    data mycas.'BASEBALL''中文测试'n;
        set AUTOLIB.'BASEBALL''中文测试'n;
    run;"""
        sas_program_pane.editor.type_into_text_area(code)
        sas_program_pane.run(True)

        flow: FlowPage = PageHelper.new_flow(page)
        flow.add_node(FlowNodeType.table)
        flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
        table_pane = TablePane(page)
        table_pane.set_library("MYCAS")
        table_pane.set_table("BASEBALL'中文测试")
        time.sleep(0.8)

        step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                     Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION]
        flow.add_step_from_stepspane_to_flow(step_path)
        flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)
        flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)
        flow.apply_flow_layout_vertical()
        time.sleep(0.8)
        flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION,
                                                Helper.data_locale.ADD_OUTPUT_PORT,
                                                Helper.data_locale.SUPPORT_VECTORS_DATA_TABLE)
        flow.add_node(FlowNodeType.table)
        flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
        table_pane.set_library("MYCAS")
        table_pane.set_table("OUT'SVDD中")
        flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION, "OUT'SVDD中")
        flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)

        support_vector_data_description = SupportVectorDataDescription(page)

        support_vector_data_description.set_filter_input_data("'nAtBat''中'n> 220")
        support_vector_data_description.add_columns_for_interval_inputs(
            check_column_name_list=["nAtBat'中", "nHits'中"])
        support_vector_data_description.add_columns_for_norminal_inputs(check_column_name_list=["Team'中文", "Position'中"])
        support_vector_data_description.expand_windowshade_additional_roles()
        support_vector_data_description.add_column_for_weight_variables("logSalary'中")

        support_vector_data_description.click_options_tab()
        support_vector_data_description.set_text_for_rbf_bandwidth_parameter("100")
        support_vector_data_description.set_text_for_expected_outlier_fraction("0.05")
        support_vector_data_description.set_text_for_solver_tolerance("30")
        support_vector_data_description.set_maximum_iterations("200")

        support_vector_data_description.click_output_tab()
        support_vector_data_description.set_check_create_support_vectors_data()

        flow.run(False)
        flow.screenshot_after_run()


def test_04_support_vector_data_description_in_flow_level1(page, init):
    PageHelper.new_sas_program(page)
    sas_program_pane = SASProgramPage(page)
    code = """
libname autolib "/segatest/I18N/Autolib/";
cas;
caslib _all_ assign;

data public.'BASEBALL''中文测试'n;
    set AUTOLIB.'BASEBALL''中文测试'n;
run;"""
    sas_program_pane.editor.type_into_text_area(code)
    sas_program_pane.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("Public")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION, Helper.data_locale.ADD_OUTPUT_PORT, Helper.data_locale.SUPPORT_VECTORS_DATA_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("OUT'SVDD中")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION, "OUT'SVDD中")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION,Helper.data_locale.ADD_OUTPUT_PORT, Helper.data_locale.SCORING_MODEL_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("PUBLIC")
    table_pane.set_table("Model'SVDD中")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION, "Model'SVDD中")

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION)
    flow.apply_flow_layout_vertical()
    time.sleep(0.8)

    support_vector_data_description = SupportVectorDataDescription(page)
    support_vector_data_description.set_filter_input_data("'nAtBat''中'n IS NOT MISSING")
    support_vector_data_description.add_columns_for_interval_inputs(
        check_column_name_list=["nAtBat'中", "nHits'中"])
    support_vector_data_description.add_columns_for_norminal_inputs(check_column_name_list=["Team'中文", "Position'中"])
    support_vector_data_description.expand_windowshade_additional_roles()
    support_vector_data_description.add_column_for_weight_variables("logSalary'中")

    support_vector_data_description.click_options_tab()
    support_vector_data_description.set_optimization_solver(1)

    support_vector_data_description.set_text_for_rbf_bandwidth_parameter("1")
    support_vector_data_description.set_text_for_solver_tolerance("0.26")
    support_vector_data_description.set_maximum_iterations("500")

    support_vector_data_description.set_stochastic_parameters(1)
    support_vector_data_description.set_maximum_support_vectors("1000")
    support_vector_data_description.set_observations_sampled("200")
    support_vector_data_description.set_text_for_threshold_tolerance("0.05")
    support_vector_data_description.set_text_for_center_tolerance("0.003")
    support_vector_data_description.set_convergence_criterion("10")

    support_vector_data_description.click_output_tab()
    support_vector_data_description.set_check_create_support_vectors_data()
    support_vector_data_description.set_include_variables_from_the_input_data_set(2)
    support_vector_data_description.add_columns_for_include_these_variables(check_column_name_list=["姓名1","nRuns'中","Division'中","Div'中"])

    support_vector_data_description.set_check_save_scoring_model()

    flow.run(False)
    flow.screenshot_after_run()