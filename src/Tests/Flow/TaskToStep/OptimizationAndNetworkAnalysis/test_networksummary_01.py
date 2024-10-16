"""This is test case file for step Network Summary"""
import pytest
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.network_summary_pane import NetworkSummaryPane
from src.Data.input_data_zh import *
from src.Helper.page_factory import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


@pytest.mark.level0_step
def test_00_network_summary_in_flow(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CORE_DECOMPOSITION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETIN'链接")
    time.sleep(0.5)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("NODESETIN'节点")
    time.sleep(0.5)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_NETWORK_SUMMARY]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_NETWORK_SUMMARY)
    flow.click_on_canvas_in_flow()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_NETWORK_SUMMARY, "添加输入端口",
                                            "{sasstudio-steps-gui-icu.genericText.inputport.nodesData.title}")
    flow.link_two_nodes_in_flow("NODESETIN'节点", Helper.data_locale.STEP_NETWORK_SUMMARY)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_NETWORK_SUMMARY)

    network_summary_pane = NetworkSummaryPane(page)
    network_summary_pane.add_column_for_from_node("from'始")
    network_summary_pane.add_column_for_to_node("to'终")
    time.sleep(0.5)
    network_summary_pane.set_check_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)
    network_summary_pane.expand_windowshade(Helper.data_locale.NODES)
    network_summary_pane.add_column_for_node("node'中")
    time.sleep(0.5)

    network_summary_pane.click_options_tab()
    network_summary_pane.set_check_for_checkbox(Helper.data_locale.CONNECTED_COMPONENTS)
    time.sleep(0.5)
    flow.run(False)


@pytest.mark.level1_step
def test_01_network_summary_in_flow(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.CORE_DECOMPOSITION)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("LINKSETIN'链接")
    time.sleep(0.8)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("NODESETIN'节点")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_NETWORK_SUMMARY]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_NETWORK_SUMMARY)
    flow.click_on_canvas_in_flow()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_NETWORK_SUMMARY, "添加输入端口",
                                            "{sasstudio-steps-gui-icu.genericText.inputport.nodesData.title}")
    flow.link_two_nodes_in_flow("NODESETIN'节点", Helper.data_locale.STEP_NETWORK_SUMMARY)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_NETWORK_SUMMARY)

    network_summary_pane = NetworkSummaryPane(page)
    network_summary_pane.add_column_for_from_node("from'始")
    network_summary_pane.add_column_for_to_node("to'终")
    time.sleep(0.5)
    network_summary_pane.set_check_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)
    network_summary_pane.expand_windowshade(Helper.data_locale.NODES)
    network_summary_pane.add_column_for_node("node'中")
    time.sleep(0.5)

    network_summary_pane.click_options_tab()
    network_summary_pane.set_check_for_checkbox(Helper.data_locale.BICONNECTED_COMPONENTS)
    time.sleep(0.5)

    network_summary_pane.click_output_tab()
    network_summary_pane.set_check_for_checkbox(Helper.data_locale.CREATE_NODES_TABLE)

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_NETWORK_SUMMARY, "添加输出端口",
                                            "{sasstudio-steps-gui-icu.genericText.outputport.nodesTable.title}")
    flow.add_node(FlowNodeType.table)
    time.sleep(0.5)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("输出节点表")
    time.sleep(0.5)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_NETWORK_SUMMARY, "输出节点表")
    flow.run(False)
