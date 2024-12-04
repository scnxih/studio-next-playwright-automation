"""This is test case file for step Rank Data"""

from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.rank_data_pane import RankDataPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
@pytest.mark.level0_step
def test_01_rank_data_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA, Helper.data_locale.STEP_RANK_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_RANK_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_RANK_DATA)
    Rank_data_pane = RankDataPane(page)
    Rank_data_pane.click_data_tab()
    Rank_data_pane.set_filter_input_data("'nAtBat''中'n > 200")
    Rank_data_pane.add_columns_for_columns_to_rank(check_column_name_list=["Team'中文", "nRBI'中"])
    Rank_data_pane.expand_windowshade_additional_roles()
    Rank_data_pane.add_columns_for_rank_by(check_column_name_list=["nHits'中", "nHome'中"])
    flow.screenshot_self("data")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_RANK_DATA, "Result'中文")
    flow.arrange_nodes()

    flow.run(False)
    flow.screenshot_after_run_slow()