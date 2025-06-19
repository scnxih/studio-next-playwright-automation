"""This is test case file for step Support Vector Data Description"""

""" Added by Allison 06/17/2025"""
import time
import pytest
"""Added by Allison 06/18/2025 """
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.MachineLearning.support_vector_data_description_pane import \
    SupportVectorDataDescription
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import AccordionType, TopMenuItem, DesignerControlType, FlowNodeType
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
@pytest.mark.level0_step
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

@pytest.mark.level1_step
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

@pytest.mark.level1_step
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

    flow.run(False)
    flow.screenshot_after_run()

@pytest.mark.level1_step
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

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION,
                                                Helper.data_locale.ADD_OUTPUT_PORT,
                                                Helper.data_locale.SUPPORT_VECTORS_DATA_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("OUT'SVDD中")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION, "OUT'SVDD中")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SUPPORT_VECTOR_DATA_DESCRIPTION,
                                                Helper.data_locale.ADD_OUTPUT_PORT,
                                                Helper.data_locale.SCORING_MODEL_TABLE)
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
    support_vector_data_description.add_columns_for_norminal_inputs(
            check_column_name_list=["Team'中文", "Position'中"])
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
    support_vector_data_description.add_columns_for_include_these_variables(
            check_column_name_list=["姓名1", "nRuns'中", "Division'中", "Div'中"])

    support_vector_data_description.set_check_save_scoring_model()

    flow.run(False)
    flow.screenshot_after_run()