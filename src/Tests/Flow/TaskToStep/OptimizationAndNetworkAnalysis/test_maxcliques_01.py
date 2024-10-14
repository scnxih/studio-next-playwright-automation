"""This is test case file for step Maximal Cliques"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.maximal_cliques_pane import MaximalCliquesPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_Maximal_Cliques_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("linksetincharnode'中文")
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_MAXIMAL_CLIQUES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("linksetincharnode'中文", Helper.data_locale.STEP_MAXIMAL_CLIQUES)
    flow.click_on_canvas_in_flow()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MAXIMAL_CLIQUES)
    Maximal_Cliques_Pane = MaximalCliquesPane(page)
    Maximal_Cliques_Pane.set_select_server_for_step(item_index=0)
    Maximal_Cliques_Pane.set_filter_link_data("'weight''中文'n <> 15")
    Maximal_Cliques_Pane.add_column_for_from_node("from'中文")
    Maximal_Cliques_Pane.add_column_for_to_node("to'中文")

    Maximal_Cliques_Pane.click_options_tab()
    Maximal_Cliques_Pane.set_check_maximum_number_of_cliques()
    Maximal_Cliques_Pane.set_maximum_number_of_cliques("5")
    Maximal_Cliques_Pane.set_select_maximum_time(item_index=1)
    Maximal_Cliques_Pane.set_maximum_time("600")
    Maximal_Cliques_Pane.set_log_details(item_index=0)
    Maximal_Cliques_Pane.set_select_code_generation(item_index=0)
    time.sleep(1)
    flow.screenshot_self("options")
    Maximal_Cliques_Pane.click_output_tab()
    Maximal_Cliques_Pane.set_check_save_maximal_cliques_data()

    flow.run(False)
    flow.screenshot_without_toast("run")
    flow.click_results_tab()
    flow.screenshot_without_toast("results")
    flow.click_output_data_tab()
    flow.screenshot_without_toast("output_data")
@pytest.mark.level1_step
def test_02_Maximal_Cliques_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("linksetincharnode'中文")
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_MAXIMAL_CLIQUES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("linksetincharnode'中文", Helper.data_locale.STEP_MAXIMAL_CLIQUES)
    flow.click_on_canvas_in_flow()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MAXIMAL_CLIQUES)
    Maximal_Cliques_Pane = MaximalCliquesPane(page)
    Maximal_Cliques_Pane.set_select_server_for_step(item_index=0)
    Maximal_Cliques_Pane.set_filter_link_data("'weight''中文'n <> 15")
    Maximal_Cliques_Pane.add_column_for_from_node("from'中文")
    Maximal_Cliques_Pane.add_column_for_to_node("to'中文")

    Maximal_Cliques_Pane.click_options_tab()
    Maximal_Cliques_Pane.set_check_maximum_number_of_cliques()
    Maximal_Cliques_Pane.set_maximum_number_of_cliques("5")
    Maximal_Cliques_Pane.set_select_maximum_time(item_index=1)
    Maximal_Cliques_Pane.set_maximum_time("600")
    Maximal_Cliques_Pane.set_log_details(item_index=1)
    Maximal_Cliques_Pane.set_select_code_generation(item_index=1)

    Maximal_Cliques_Pane.click_output_tab()
    Maximal_Cliques_Pane.set_check_save_maximal_cliques_data()
    flow.screenshot_self("output")
    flow.run(False)
    flow.screenshot_after_run()