"""This is test case file for step Cluster Variables"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.cluster_variables_pane import ClusterVariablesPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


@pytest.mark.level0_step
def test_01_cluster_variables_in_flow(page, init):
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
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    flow.screenshot_self("data")
    flow.run(False)
    flow.screenshot_after_run()



@pytest.mark.level1_step
def test_02_cluster_variables_in_flow(page, init):
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
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    cluster_variables_pane.expand_windowshade_additional_roles()
    cluster_variables_pane.add_columns_for_variables_to_partial_out(check_column_name_list=["nHome'中", "nRuns'中"])
    cluster_variables_pane.add_column_for_frequency_count("nRBI'中")
    cluster_variables_pane.add_column_for_weight("YrMajor'中")
    cluster_variables_pane.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    cluster_variables_pane.click_options_tab()
    cluster_variables_pane.set_maximum_number_of_clusters(item_index=1)
    cluster_variables_pane.set_check_maximum_second_eigenvalue()
    cluster_variables_pane.set_eigenvalue("2")
    flow.screenshot_self("options")
    flow.run(False)
    flow.screenshot_after_run()


@pytest.mark.level1_step
def test_03_cluster_variables_in_flow(page, init):
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
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)

    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    cluster_variables_pane.expand_windowshade_additional_roles()
    cluster_variables_pane.add_columns_for_variables_to_partial_out(check_column_name_list=["nHome'中", "nRuns'中"])
    cluster_variables_pane.add_column_for_frequency_count("nRBI'中")
    cluster_variables_pane.add_column_for_weight("YrMajor'中")
    cluster_variables_pane.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    cluster_variables_pane.click_options_tab()
    cluster_variables_pane.set_method(item_index=1)
    cluster_variables_pane.set_check_minimum_proportion_of_variation()
    cluster_variables_pane.set_proportion("0.2")
    cluster_variables_pane.expand_windowshade_deatails()
    cluster_variables_pane.set_analyze(item_index=1)
    cluster_variables_pane.set_check_maximum_number_of_iterations()
    cluster_variables_pane.set_iterations("5")
    flow.screenshot_self("options")
    flow.run(False)
    flow.screenshot_after_run()



@pytest.mark.level1_step
def test_04_cluster_variables_in_flow(page, init):
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
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(False)

    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_CLUSTER_VARIABLES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CLUSTER_VARIABLES)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, Helper.data_locale.ADD_OUTPUT_PORT,
                                            Helper.data_locale.STATISTICS_DATA)
                                            # "{sasstudio-steps-gui-icu.clustervariables.outputports"
                                            # ".statDSName.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("输出'stat")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, "输出'stat")
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, Helper.data_locale.ADD_OUTPUT_PORT,
                                            Helper.data_locale.TREE_INFORMATION_DATA)
                                            # "{sasstudio-steps-gui-icu.clustervariables.outputports"
                                            # ".treeDSName.displayname.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("work")
    table_pane.set_table("输出'tree")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CLUSTER_VARIABLES, "输出'tree")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CLUSTER_VARIABLES)
    cluster_variables_pane = ClusterVariablesPane(page)
    cluster_variables_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    cluster_variables_pane.add_columns_for_variables_to_cluster(check_column_name_list=["nAtBat'中", "nHits'中"])
    cluster_variables_pane.expand_windowshade_additional_roles()
    cluster_variables_pane.add_columns_for_variables_to_partial_out(check_column_name_list=["nHome'中", "nRuns'中"])
    cluster_variables_pane.add_column_for_frequency_count("nRBI'中")
    cluster_variables_pane.add_column_for_weight("YrMajor'中")
    cluster_variables_pane.add_columns_for_group_analysis_by(check_column_name_list=["Team'中文"])

    cluster_variables_pane.click_options_tab()
    cluster_variables_pane.set_method(item_index=1)
    cluster_variables_pane.set_check_minimum_proportion_of_variation()
    cluster_variables_pane.set_proportion("0.2")
    cluster_variables_pane.expand_windowshade_deatails()
    cluster_variables_pane.set_analyze(item_index=1)
    cluster_variables_pane.set_check_maximum_number_of_iterations()
    cluster_variables_pane.set_iterations("5")

    cluster_variables_pane.click_output_tab()
    cluster_variables_pane.set_check_create_statistics_data()
    cluster_variables_pane.set_check_replace_existing_output_table_for_statistics()
    cluster_variables_pane.set_check_create_tree_information_data()
    cluster_variables_pane.set_check_replace_existing_output_table_for_tree_information()
    flow.screenshot_self("output")
    flow.run(False)
    flow.screenshot_after_run_slow()