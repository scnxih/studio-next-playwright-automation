"""This is test case file for step Core Decomposition"""
import pytest
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.core_decomposition_pane import CoreDecompositionPane
from src.Data.input_data_zh import *
from src.Helper.page_factory import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


@pytest.mark.level0_step
def test_00_core_decomposition_in_flow(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_CORE_DECOMPOSITION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("NODESETIN'节点")
    time.sleep(0.5)

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "添加输入端口",
                                            "{sasstudio-steps-gui-icu.coredecomposition.inputports.nodesdataset.displayname.title}")
    flow.link_two_nodes_in_flow("NODESETIN'节点", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.click_on_canvas_in_flow()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CORE_DECOMPOSITION)

    core_decomposition_pane = CoreDecompositionPane(page)
    core_decomposition_pane.add_column_for_from_node("from'始")
    core_decomposition_pane.add_column_for_to_node("to'终")
    time.sleep(0.5)
    core_decomposition_pane.set_check_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)
    core_decomposition_pane.expand_windowshade(Helper.data_locale.NODES)
    core_decomposition_pane.add_column_for_node("node'中")
    time.sleep(0.5)
    flow.run(True)


@pytest.mark.level1_step
def test_01_core_decomposition_in_flow(page, init):
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
                 Helper.data_locale.STEP_CORE_DECOMPOSITION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.click_on_canvas_in_flow()
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "添加输入端口",
                                            "{sasstudio-steps-gui-icu.coredecomposition.inputports.nodesdataset.displayname.title}")
    flow.link_two_nodes_in_flow("NODESETIN'节点", Helper.data_locale.STEP_CORE_DECOMPOSITION)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CORE_DECOMPOSITION)

    core_decomposition_pane = CoreDecompositionPane(page)
    core_decomposition_pane.add_column_for_from_node("from'始")
    core_decomposition_pane.add_column_for_to_node("to'终")

    core_decomposition_pane.set_check_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)
    core_decomposition_pane.expand_windowshade(Helper.data_locale.NODES)
    core_decomposition_pane.add_column_for_node("node'中")
    time.sleep(0.5)

    core_decomposition_pane.click_options_tab()
    core_decomposition_pane.select_procedure(Helper.data_locale.USE_CAS_PROCEDURE)
    time.sleep(0.5)
    core_decomposition_pane.click_output_tab()
    core_decomposition_pane.set_check_create_nodes_table()
    time.sleep(0.2)

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "添加输出端口")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("输出节点表")
    time.sleep(0.5)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CORE_DECOMPOSITION, "输出节点表")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    time.sleep(0.5)
    flow.run(True)
