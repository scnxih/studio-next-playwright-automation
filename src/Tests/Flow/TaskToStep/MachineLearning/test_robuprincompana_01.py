"""This is test case file for Robust Principal Component Analysis"""
import time

"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.MachineLearning.robust_principal_component_analysis_pane import \
    RobustPrincipalComponentAnalysis
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_robust_principal_component_analysis_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.add_columns_for_interval_inputs(
        check_column_name_list=["SepalLength'中文", "SepalWidth'中文", "PetalLength'中文", "PetalWidth'中文"])
    flow.run(False)
    flow.screenshot_without_toast("run")



@pytest.mark.level1_step
def test_02_robust_principal_component_analysis_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")
    flow.run(False)
    flow.screenshot_without_toast("run")

@pytest.mark.level1_step
def test_03_robust_principal_component_analysis_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")

    robust_principal_component_analysis_pane.click_options_tab()
    robust_principal_component_analysis_pane.set_method(item_index=1)
    robust_principal_component_analysis_pane.set_lambda(item_index=1)
    robust_principal_component_analysis_pane.set_custom_lambda_value("2")
    robust_principal_component_analysis_pane.set_lambda_weight(item_index=1)
    robust_principal_component_analysis_pane.set_custom_lambda_weight_value("0.5")
    robust_principal_component_analysis_pane.set_maximum_iterations("500")
    robust_principal_component_analysis_pane.set_tolerance("0.00001")
    robust_principal_component_analysis_pane.set_check_scale_observations()
    robust_principal_component_analysis_pane.set_check_center_observations()
    robust_principal_component_analysis_pane.set_initial_mu("0.001")
    robust_principal_component_analysis_pane.set_check_use_fixed_value_for_mu()

    robust_principal_component_analysis_pane.expand_windowshade_singular_value_decomposition_options()
    robust_principal_component_analysis_pane.set_svd_method(item_index=1)
    robust_principal_component_analysis_pane.set_maximum_rank("1234")
    robust_principal_component_analysis_pane.set_power("1")
    flow.screenshot_self("options")
    flow.run(False)
    flow.screenshot_without_toast("run")

@pytest.mark.level1_step
def test_04_robust_principal_component_analysis_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.LOW_RANK_OUTPUT_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("lowrank'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "lowrank'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.SPARSE_OUTPUT_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("sparse'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "sparse'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.ERROR_OUTPUT_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("error'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "error'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.LEFT_SINGULAR_VECTORS_OUTPUT_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("left'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "left'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.SINGULAR_VALUES_OUTPUT_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("singular'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "singular'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.RIGHT_SINGULAR_VECTORS_OUTPUT_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("right'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "right'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")

    robust_principal_component_analysis_pane.click_output_tab()
    robust_principal_component_analysis_pane.set_check_save_low_rank_data()
    robust_principal_component_analysis_pane.set_check_save_sparse_data()
    robust_principal_component_analysis_pane.set_check_save_error_data()
    robust_principal_component_analysis_pane.set_decomposition_method(item_index=1)
    robust_principal_component_analysis_pane.set_check_save_left_singular_vectors_data()
    robust_principal_component_analysis_pane.set_check_save_singular_values_data()
    robust_principal_component_analysis_pane.set_check_save_right_singular_vectors_data()
    flow.screenshot_self("output")
    flow.run(False)
    flow.screenshot_without_toast("run")


@pytest.mark.level1_step
def test_05_robust_principal_component_analysis_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'IRIS''中文'n;
set AUTOLIB.'IRIS''中文'n;
'ID''中文'n=_n_;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("IRIS'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "IRIS'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("IRIS'中文", Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.COMPONENT_LOADINGS_OUTPUT_TABLE)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("component'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "component'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS,
                                                       Helper.data_locale.PC_SCORES_OUTPUT_TABLE)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("pc'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS, "pc'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS)
    robust_principal_component_analysis_pane = RobustPrincipalComponentAnalysis(page)
    robust_principal_component_analysis_pane.set_input_variables(item_index=0)
    robust_principal_component_analysis_pane.add_column_for_id_variable("ID'中文")
    flow.screenshot_self("data")
    robust_principal_component_analysis_pane.click_output_tab()
    robust_principal_component_analysis_pane.set_decomposition_method(item_index=2)
    robust_principal_component_analysis_pane.set_check_save_component_loadings_data()
    robust_principal_component_analysis_pane.set_check_save_pc_scores_data()
    flow.screenshot_self("output")
    flow.run(False)
    time.sleep(1)
    flow.screenshot_without_toast("run")
    flow.click_results_tab()
    time.sleep(2)
    flow.screenshot_without_toast("results")
    flow.click_output_data_tab()
    time.sleep(2)
    flow.screenshot_without_toast("output_data")
