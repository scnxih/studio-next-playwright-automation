"""This is test case file for step Coin Toss Simulation"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.coin_toss_simulation_pane import CoinTossSimulationPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


@pytest.mark.level0_step
def test_01_coin_toss_simulation_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_COIN_TOSS_SIMULATION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.run(False)


@pytest.mark.level1_step
def test_02_coin_toss_simulation_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_COIN_TOSS_SIMULATION]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_COIN_TOSS_SIMULATION)
    coin_toss_simulation_pane = CoinTossSimulationPane(page)
    coin_toss_simulation_pane.set_check_show_graph_table()
    coin_toss_simulation_pane.set_check_grid_lines()
    coin_toss_simulation_pane.set_check_gradient_fill()
    coin_toss_simulation_pane.set_check_data_skin()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("输出'cointest")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_COIN_TOSS_SIMULATION, "输出'cointest")
    flow.arrange_nodes()
    flow.run(False)
    flow.screenshot_after_run_slow()
