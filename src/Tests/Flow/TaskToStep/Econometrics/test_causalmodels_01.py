"""This is test case file for step Causal Models"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Econometrics.causal_models_pane import CausalModelsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_causal_models_2sls_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("PRICEDATA")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("PRICEDATA", Helper.data_locale.STEP_CAUSAL_MODELS)
    time.sleep(0.5)
    flow.click_on_canvas_in_flow()
    time.sleep(0.5)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)
    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("('价格'n >= 30)")
    Causal_models_pane.set_select_method(item_index=0)
    Causal_models_pane.add_column_for_dependent_variable("销售")
    Causal_models_pane.add_columns_for_endogenous_explanatory_variables(check_column_name_list=["价格1", "价格2"])
    Causal_models_pane.add_columns_for_exogenous_explanatory_variables(check_column_name_list=["价格3", "价格4"])
    Causal_models_pane.add_columns_for_excluded_instrumental_variables(check_column_name_list=["价格5", "价格6"])

    flow.run(True)
@pytest.mark.level0_step
def test_02_causal_models_heckman_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("JUNKMAIL_中'文")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("JUNKMAIL_中'文", Helper.data_locale.STEP_CAUSAL_MODELS)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)
    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("'All_中''文'n > 0")
    Causal_models_pane.set_select_method(item_index=1)

    Causal_models_pane.expand_windowshade_outcome_equation()
    Causal_models_pane.add_column_for_dependent_variable_outcome_equation("Make_中'文")
    Causal_models_pane.add_columns_for_continuous_variable_outcome_equation(check_column_name_list=["Address_中'文"])
    Causal_models_pane.set_check_intercept_outcome_equation()

    Causal_models_pane.expand_windowshade_selection_equation()
    Causal_models_pane.add_column_for_dependent_variable_selection_equationn("Test_中'文")
    Causal_models_pane.set_select_distinct_value_dependent_variable(item_index=1)
    Causal_models_pane.add_columns_for_continuous_variable_selection_equation(check_column_name_list=["All_中'文","_3D_中'文"])
    Causal_models_pane.set_check_intercept_selection_equation()

    Causal_models_pane.click_output_tab()
    Causal_models_pane.set_check_create_parameter_estimates_data_set()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CAUSAL_MODELS, "添加输出端口")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CAUSAL_MODELS, "Result'中文")
    flow.arrange_nodes()

    flow.run(True)

@pytest.mark.level1_step
def test_causal_models_2sls_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("PRICEDATA")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("PRICEDATA", Helper.data_locale.STEP_CAUSAL_MODELS)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)

    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("('价格'n >= 30)")
    Causal_models_pane.set_select_method(item_index=0)
    Causal_models_pane.add_column_for_dependent_variable("销售")
    Causal_models_pane.add_columns_for_endogenous_explanatory_variables(check_column_name_list=["价格1", "价格2"])
    Causal_models_pane.add_columns_for_exogenous_explanatory_variables(check_column_name_list=["价格3", "价格4"])
    Causal_models_pane.add_columns_for_excluded_instrumental_variables(check_column_name_list=["价格5", "价格6"])
    Causal_models_pane.expand_windowshade_additional_roles()
    Causal_models_pane.add_columns_for_group_analysis_by(check_column_name_list=["日期"])

    Causal_models_pane.click_options_tab()
    Causal_models_pane.set_select_optimization_method(item_index=1)
    Causal_models_pane.set_select_maximum_number_of_iterations(item_index=1)
    Causal_models_pane.set_maximum_number_of_iterations_text(input_text="200")
    Causal_models_pane.set_select_statistics_to_display(item_index=2)
    Causal_models_pane.set_select_pots_display(item_index=2)

    flow.arrange_nodes()
    flow.run(True)

@pytest.mark.level1_step
def test_03_causal_models_heckman_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("JUNKMAIL_中'文")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("JUNKMAIL_中'文", Helper.data_locale.STEP_CAUSAL_MODELS)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)
    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("'All_中''文'n > 0")
    Causal_models_pane.set_select_method(item_index=1)

    Causal_models_pane.expand_windowshade_outcome_equation()
    Causal_models_pane.add_column_for_dependent_variable_outcome_equation("Make_中'文")
    Causal_models_pane.add_columns_for_continuous_variable_outcome_equation(check_column_name_list=["Address_中'文"])
    Causal_models_pane.set_check_intercept_outcome_equation()

    Causal_models_pane.expand_windowshade_selection_equation()
    Causal_models_pane.add_column_for_dependent_variable_selection_equationn("Test_中'文")
    Causal_models_pane.set_select_distinct_value_dependent_variable(item_index=1)
    Causal_models_pane.add_columns_for_continuous_variable_selection_equation(check_column_name_list=["All_中'文","_3D_中'文"])
    Causal_models_pane.set_check_intercept_selection_equation()

    Causal_models_pane.click_options_tab()
    Causal_models_pane.set_select_optimization_method(item_index=1)
    Causal_models_pane.set_select_maximum_number_of_iterations(item_index=1)
    Causal_models_pane.set_maximum_number_of_iterations_text("200")
    Causal_models_pane.set_select_variance_estimation_method(item_index=1)
    Causal_models_pane.set_select_Type_covariances_parameter_estimates(item_index=1)
    Causal_models_pane.set_select_statistics_to_display(item_index=1)
    Causal_models_pane.set_check_correlations_parameter_estimates()
    Causal_models_pane.set_check_covariances_parameter_estimates()
    Causal_models_pane.set_check_iteration_history_objective_function()

    Causal_models_pane.click_output_tab()
    Causal_models_pane.set_check_create_parameter_estimates_data_set()
    Causal_models_pane.set_check_covariance_matrix_estimates()
    Causal_models_pane.set_check_correlation_matrix_estimates()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CAUSAL_MODELS, "添加输出端口")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CAUSAL_MODELS, "Result'中文")
    flow.arrange_nodes()

    flow.run(True)