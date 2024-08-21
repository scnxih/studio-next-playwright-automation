from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.centrality_metrics_pane import \
    CentralityMetricsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane

from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.list_data_pane import ListDataPane


def test_01_list_data_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()
    flow.run(True)


def test_02_list_data_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["姓名1", "Team'中文"])
    list_data_pane.add_columns_for_group_analysis_by(check_column_name_list=["League'中"])
    list_data_pane.add_columns_for_total_of(check_column_name_list=["nAtBat'中", "nHits'中"])
    list_data_pane.add_columns_for_identifying_label(check_column_name_list=["nHome'中", "Div'中"])
    time.sleep(0.5)

    flow.run(True)


def test_03_list_data_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["姓名1", "Team'中文"])
    list_data_pane.add_columns_for_group_analysis_by(check_column_name_list=["League'中"])
    list_data_pane.add_columns_for_total_of(check_column_name_list=["nAtBat'中", "nHits'中"])

    time.sleep(0.5)
    list_data_pane.click_options_tab()
    list_data_pane.set_check_display_row_numbers()
    list_data_pane.set_column_label("中文")
    list_data_pane.set_check_display_number_of_rows()
    list_data_pane.set_heading_direction(item_index=2)
    list_data_pane.set_check_split_labels()
    list_data_pane.set_split_character(item_index=5)
    list_data_pane.set_rows_to_list(item_index=1)
    flow.run(True)


def test_04_list_data_in_flow_l1(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["姓名1", "Team'中文"])
    list_data_pane.add_columns_for_group_analysis_by(check_column_name_list=["League'中"])
    list_data_pane.add_columns_for_total_of(check_column_name_list=["nAtBat'中", "nHits'中"])
    list_data_pane.add_columns_for_identifying_label(check_column_name_list=["nHome'中", "Div'中"])

    time.sleep(0.5)
    list_data_pane.click_options_tab()
    list_data_pane.set_uncheck_display_row_numbers()
    list_data_pane.set_uncheck_use_labels_as_column_headings()
    list_data_pane.set_uncheck_display_number_of_rows()
    list_data_pane.set_uncheck_round_values()
    list_data_pane.set_heading_direction(item_index=1)
    list_data_pane.set_uncheck_split_labels()
    flow.run(True)
