from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.centrality_metrics_pane import \
    CentralityMetricsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane

from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.list_data_pane import ListDataPane


def test_01_list_data_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("SASHELP")
    table_pane.set_table("BASEBALL")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL", Helper.data_locale.STEP_LIST_DATA)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LIST_DATA)
    list_data_pane = ListDataPane(page)
    list_data_pane.set_filter_input_data("nAtBat>400")
    list_data_pane.add_columns_for_list_variables(check_column_name_list=["Name", "Team"])
    time.sleep(0.5)

    list_data_pane.click_options_tab()
    list_data_pane.set_uncheck_display_row_numbers()
    list_data_pane.set_column_label("中文")
    list_data_pane.set_check_display_number_of_rows()

    flow.run(True)
