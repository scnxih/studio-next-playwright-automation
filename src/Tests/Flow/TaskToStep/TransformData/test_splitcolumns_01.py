"""This is test case file for step Split Columndef test_Split_Columns_level0(page, init):"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.split_columns_pane import SplitColumnsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


@pytest.mark.level0_step
def test_01_Split_Columns_level0(page, init):
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

    step_path = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA, Helper.data_locale.STEP_SPLIT_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SPLIT_COLUMNS)
    flow.click_on_canvas_in_flow()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SPLIT_COLUMNS)
    Split_Columns_pane = SplitColumnsPane(page)
    Split_Columns_pane.set_filter_input_data("'nAtBat''中'n> 100")
    Split_Columns_pane.add_column_for_Column_to_split(column_name="Team'中文")
    Split_Columns_pane.add_column_for_Formatted_identifier_values(column_name="nRuns'中")
    Split_Columns_pane.add_column_for_Labels_for_new_columns(column_name="nRBI'中")
    Split_Columns_pane.expand_windowshade_additional_roles()
    Split_Columns_pane.add_columns_for_group_analysis_by(check_column_name_list=["nHits'中", "CrHits'中"])

    Split_Columns_pane.click_output_tab()
    Split_Columns_pane.set_check_for_replace_existing_output_table()
    Split_Columns_pane.set_check_for_use_column_name_prefix()
    Split_Columns_pane.set_text_for_prefix("行'列")
    Split_Columns_pane.set_specify_data_to_show(item_index=1)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("OUTPUT'中文测试")

    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SPLIT_COLUMNS,"OUTPUT'中文测试")
    flow.run(True)