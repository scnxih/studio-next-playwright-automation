"""This is test case file for step Semi-supervised Learning"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.MachineLearning.semi_supervised_learning_pane import \
    SemiSupervisedLearning
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_semi_supervised_learning_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    flow.run(False)

@pytest.mark.level1_step
def test_02_semi_supervised_learning_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("SSL'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "SSL'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    semi_supervised_learning_pane.click_options_tab()
    semi_supervised_learning_pane.set_kernel(item_index=1)
    semi_supervised_learning_pane.set_number_of_neighbors("2")
    semi_supervised_learning_pane.set_number_of_iterations("4")
    semi_supervised_learning_pane.set_rbf_kernel_width("15")

    semi_supervised_learning_pane.click_output_tab()
    semi_supervised_learning_pane.set_check_create_output_data()
    semi_supervised_learning_pane.set_check_replace_existing_output_table()
    flow.run(False)

@pytest.mark.level1_step
def test_03_semi_supervised_learning_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("SSL'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "SSL'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    semi_supervised_learning_pane.click_options_tab()
    semi_supervised_learning_pane.set_kernel(item_index=0)
    semi_supervised_learning_pane.set_code_generation(item_index=1)

    semi_supervised_learning_pane.click_output_tab()
    semi_supervised_learning_pane.set_check_create_output_data()
    semi_supervised_learning_pane.set_check_replace_existing_output_table()
    flow.run(False)

@pytest.mark.level1_step
def test_04_semi_supervised_learning_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'labeled''中文'n;
set AUTOLIB.'labeled''中文'n;
run;
data casuser.'unlabeled''中文'n;
set AUTOLIB.'unlabeled''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("labeled'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "labeled'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("unlabeled'中文")

    step_path = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                 Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("unlabeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("labeled'中文", Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("SSL'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING, "SSL'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SEMI_SUPERVISED_LEARNING)
    semi_supervised_learning_pane = SemiSupervisedLearning(page)
    semi_supervised_learning_pane.expand_windowshade_labeled()
    semi_supervised_learning_pane.add_column_for_target_variable("y'中文")
    semi_supervised_learning_pane.add_columns_for_input_variables(check_column_name_list=["x1'中文", "x2'中文"])

    semi_supervised_learning_pane.click_options_tab()
    semi_supervised_learning_pane.set_kernel(item_index=1)
    semi_supervised_learning_pane.set_number_of_neighbors("2")
    semi_supervised_learning_pane.set_number_of_iterations("4")
    semi_supervised_learning_pane.set_rbf_kernel_width("15")
    semi_supervised_learning_pane.set_code_generation(item_index=1)

    semi_supervised_learning_pane.click_output_tab()
    semi_supervised_learning_pane.set_check_create_output_data()
    semi_supervised_learning_pane.set_check_replace_existing_output_table()
    semi_supervised_learning_pane.set_include_variables_from_input_CAS_table(item_index=2)
    semi_supervised_learning_pane.add_columns_for_include_these_variables(
        check_column_name_list=["x1'中文", "y'中文", "id'中文"])
    flow.run(False)

