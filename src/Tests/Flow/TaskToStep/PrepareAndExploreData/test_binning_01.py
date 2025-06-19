"""This is test case file for step Binning"""
"""Added by Percy 2025-6-18"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.PrepareAndExploreData.binning_pane import BinningPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_binning_in_flow(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(""" 
libname AUTOLIB '/segatest/I18N/Autolib' ;  
CAS;
CASLIB _ALL_ Assign;
DATA CASUSER."BASEBALL'中文测试"n;
set AUTOLIB."BASEBALL'中文测试"n;
run;

""")
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_Binning]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_Binning)
    flow.click_on_canvas_in_flow()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_Binning)
    BinningPane_pane =BinningPane(page)
    BinningPane_pane.add_columns_for_interval_inputs_to_bin(check_column_name_list=["nHits'中", "nAtBat'中"])
    flow.run(True)

@pytest.mark.level1_step
def test_02_binning_in_flow(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(""" 
libname AUTOLIB '/segatest/I18N/Autolib' ;  
CAS;
CASLIB _ALL_ Assign;
DATA CASUSER."BASEBALL'中文测试"n;
set AUTOLIB."BASEBALL'中文测试"n;
run;

""")
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_Binning]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_Binning)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_Binning)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("OUT'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_Binning, "OUT'中文")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_Binning)
    BinningPane_pane =BinningPane(page)
    BinningPane_pane.add_columns_for_interval_inputs_to_bin(check_column_name_list=["nHits'中", "nAtBat'中"])
    BinningPane_pane.expand_windowshade_additional_roles()
    BinningPane_pane.add_column_for_frequency_count(column_name="nRBI'中")

    BinningPane_pane.click_options_tab()
    BinningPane_pane.set_number_of_bins("10")
    BinningPane_pane.set_method(1)

    BinningPane_pane.click_output_tab()
    BinningPane_pane.set_check_save_binned_data()
    BinningPane_pane.set_include_variables_from_input(1)

    BinningPane_pane.set_check_save_Scoring_code()
    BinningPane_pane.set_specify_data_to_show(1)
    BinningPane_pane.set_number_of_observations_increment(3)

    flow.run(True)