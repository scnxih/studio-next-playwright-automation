import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.transitive_closure_pane import \
    TransitiveClosurePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.StatisticalProcessControl.capability_analysis_pane import \
    CapabilityAnalysisPane
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Utilities.enums import FlowNodeType, TopMenuItem

"""This is test case file for step Transitive Closure"""





@pytest.mark.level0_step
def test_01_trans_cls_lev0(page, init):
    """
    Level 0 Scenarios (for Transitive Closure)
    """

    # Create a sas program and run
    sas_program_code = """
cas;
caslib _all_ assign;

data CASUSER.LinkSetInTC;
input from $ to $ @@;
datalines;
B C  B D  C B  D A  D C
;
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.format_program()
    sas_program.run(True)
    sas_program.wait_toast_disappear()

    sas_program.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + " (1)")

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("LINKSETINTC")
    table_pane.refresh_table()

    # Add Transitive Closure node
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_TRANSITIVE_CLOSURE]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.link_two_nodes_in_flow("LINKSETINTC", Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.arrange_nodes()
    # flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)

    # NOTE: Extra Refresh Operations Are Added Owing to CAS Server Instability
    flow.select_node_in_flow_canvas("LINKSETINTC")
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.NOTES)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.PREVIEW_DATA)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.TABLE_PROPERTIES)
    table_pane.refresh_table()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)

    # Set process variable
    transitive_closure_pane = TransitiveClosurePane(page)
    transitive_closure_pane.set_select_a_server_for_this_step(item_index=1)

    transitive_closure_pane.set_from_node("from")
    transitive_closure_pane.set_to_node("to")
    flow.screenshot_self("data")
    flow.run(False)
    flow.screenshot_after_run()




@pytest.mark.level1_step
def test_02_trans_cls_lev1(page, init):
    """
    Level 1 Scenarios (for Transitive Closure)
    """

    # Create a sas program and run
    sas_program_code = """
data 'LinkSetInTC''générer ='n;
input 'from''从'n $ 'to''到'n $ @@;
datalines;
'B''乙'n 'C''丙'n  'B''乙'n 'D''丁'n  'C''丙'n 'B''乙'n  'D''丁'n 'A''甲'n  'D''丁'n 'C''丙'n
;

libname mycas cas;

proc casutil;
load data=WORK.'LINKSETINTC''GÉNÉRER ='n casout="linksetintc''GÉNÉRER=";
run;
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.format_program()
    sas_program.run(True)
    sas_program.wait_toast_disappear()
    sas_program.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + " (1)")

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)

    # Add Transitive Closure node
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_TRANSITIVE_CLOSURE]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Add a table
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)

    # Set lib and table
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETINTC''GÉNÉRER=")
    table_pane.refresh_table()

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.link_two_nodes_in_flow("LINKSETINTC''GÉNÉRER=", Helper.data_locale.STEP_TRANSITIVE_CLOSURE)
    flow.arrange_nodes()

    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas("LINKSETINTC''GÉNÉRER=")

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TRANSITIVE_CLOSURE)

    # Set process variable
    transitive_closure_pane = TransitiveClosurePane(page)
    transitive_closure_pane.set_select_a_server_for_this_step(item_index=1)

    transitive_closure_pane.set_from_node("from'从")
    transitive_closure_pane.set_to_node("to'到")
    transitive_closure_pane.set_log_details(item_index=1)
    transitive_closure_pane.set_log_details(item_value=Helper.data_locale.NO_SUMMARY)

    transitive_closure_pane.set_code_generation(item_index=1)
    transitive_closure_pane.set_code_generation(item_value=Helper.data_locale.USE_CAS_PROCEDURE)
    flow.screenshot_without_toast("data")
    # Run the flow
    flow.run(False)
    flow.screenshot_after_run()

