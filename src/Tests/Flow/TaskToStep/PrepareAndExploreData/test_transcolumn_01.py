"""This is test case file for step Transform Columns"""
"""Added by Dommy 2024-11-27"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.PrepareAndExploreData.transform_columns_pane import TransformColumns
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_transform_columns_in_flow(page, init):
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                 Helper.data_locale.STEP_TRANSFORM_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform1()
    transform_columns_pane.add_column_for_variable1("nAtBat'中")
    flow.run(True)

@pytest.mark.level1_step
def test_02_transform_columns_in_flow(page, init):
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                 Helper.data_locale.STEP_TRANSFORM_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform1()
    transform_columns_pane.add_column_for_variable1("nRuns'中")
    transform_columns_pane.set_transform_for_transform1(item_index=1)

    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform2()
    transform_columns_pane.add_column_for_variable2("nHits'中")
    transform_columns_pane.set_transform_for_transform2(item_index=2)

    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform3()
    transform_columns_pane.add_column_for_variable3("nBB'中")
    transform_columns_pane.set_transform_for_transform3(item_index=3)
    flow.run(True)


def test_03_transform_columns_in_flow(page, init):
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
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                 Helper.data_locale.STEP_TRANSFORM_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform1()
    transform_columns_pane.add_column_for_variable1("nRuns'中")
    transform_columns_pane.set_transform_for_transform1(item_index=4)

    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform2()
    transform_columns_pane.add_column_for_variable2("nHits'中")
    transform_columns_pane.set_transform_for_transform2(item_index=5)

    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform3()
    transform_columns_pane.add_column_for_variable3("nBB'中")
    transform_columns_pane.set_transform_for_transform3(item_index=6)
    transform_columns_pane.set_custom_transform("LOG('nBB''中'n)")

    transform_columns_pane.click_output_tab()
    transform_columns_pane.set_specify_data_to_show(item_index=1)
    transform_columns_pane.set_number_of_observations_default("20")
    flow.run(True)


def test_04_transform_columns_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;  
CAS;
CASLIB _ALL_ Assign;
DATA CASUSER."BASEBALL'中文测试"n;
set AUTOLIB."BASEBALL'中文测试"n;
run;

"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                 Helper.data_locale.STEP_TRANSFORM_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TS'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TRANSFORM_COLUMNS, "TS'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSFORM_COLUMNS)
    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.set_select_a_server_for_this_step(item_index=1)
    transform_columns_pane.expand_windowshade_transform1()
    transform_columns_pane.add_column_for_variable1("nRuns'中")
    transform_columns_pane.set_transform_for_transform1(item_index=4)

    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform2()
    transform_columns_pane.add_column_for_variable2("nHits'中")
    transform_columns_pane.set_transform_for_transform2(item_index=5)

    transform_columns_pane = TransformColumns(page)
    transform_columns_pane.expand_windowshade_transform3()
    transform_columns_pane.add_column_for_variable3("nBB'中")
    transform_columns_pane.set_transform_for_transform3(item_index=6)
    transform_columns_pane.set_custom_transform("LOG('nBB''中'n)")

    transform_columns_pane.click_output_tab()
    transform_columns_pane.set_specify_data_to_show(item_index=1)
    transform_columns_pane.set_number_of_observations_default("20")
    flow.run(True)