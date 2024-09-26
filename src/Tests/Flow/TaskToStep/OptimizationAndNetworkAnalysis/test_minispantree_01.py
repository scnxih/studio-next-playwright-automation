"""This is test case file for step Minimum Spanning Tree"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.minimun_spanning_tree_pane import \
    MinimunSpanningTree
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


@pytest.mark.level0_step
def test_01_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    flow.run(True)


@pytest.mark.level1_step
def test_02_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


@pytest.mark.level1_step
def test_03_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=1)
    minimum_spanning_tree_pane.set_code_generation(item_index=1)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


@pytest.mark.level1_step
def test_04_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=1)
    minimum_spanning_tree_pane.set_code_generation(item_index=0)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


@pytest.mark.level1_step
def test_05_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)
    minimum_spanning_tree_pane.set_code_generation(item_index=1)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


@pytest.mark.level1_step
def test_06_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)
    minimum_spanning_tree_pane.set_code_generation(item_index=2)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


@pytest.mark.level1_step
def test_07_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")
    minimum_spanning_tree_pane.expand_windowshade_additional_roles()
    minimum_spanning_tree_pane.add_columns_for_group_analysis_by(check_column_name_list=["group'中文"])

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=2)
    minimum_spanning_tree_pane.set_code_generation(item_index=0)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)


@pytest.mark.level1_step
def test_08_minimum_spanning_tree_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'LINKSETINDATA''中文'n;
set AUTOLIB.'LINKSETINDATA''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINDATA'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LINKSETINDATA'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_MINIMUM_SPANNING_TREE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETINDATA'中文", Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("MST'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE, "MST'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MINIMUM_SPANNING_TREE)
    minimum_spanning_tree_pane = MinimunSpanningTree(page)
    minimum_spanning_tree_pane.set_select_server_for_step(item_index=1)
    minimum_spanning_tree_pane.add_column_for_from_node("from'中文")
    minimum_spanning_tree_pane.add_column_for_to_node("to'中文")
    minimum_spanning_tree_pane.add_column_for_weight("weight'中文")
    minimum_spanning_tree_pane.expand_windowshade_additional_roles()
    minimum_spanning_tree_pane.add_columns_for_group_analysis_by(check_column_name_list=["group'中文"])

    minimum_spanning_tree_pane.click_options_tab()
    minimum_spanning_tree_pane.set_log_details(item_index=1)
    minimum_spanning_tree_pane.set_code_generation(item_index=1)

    minimum_spanning_tree_pane.click_output_tab()
    minimum_spanning_tree_pane.set_check_save_minimum_spanning_tree_information_date()
    minimum_spanning_tree_pane.set_check_replace_existing_output_table()
    flow.run(True)
