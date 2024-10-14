"""This is test case file for step Describe missing Data"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.describe_missing_data_pane import DescribeMissingDataPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_describe_missing_data_level0(page, init):
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
    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_DESCRIBE_MISSING_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_DESCRIBE_MISSING_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_DESCRIBE_MISSING_DATA)
    Discribe_Missing_Data_Pane =DescribeMissingDataPane(page)
    Discribe_Missing_Data_Pane.click_data_tab()
    Discribe_Missing_Data_Pane.set_filter_input_data("'nAtBat''中'n > 200")
    Discribe_Missing_Data_Pane.add_columns_for_analysis_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    Discribe_Missing_Data_Pane.expand_windowshade_additional_roles()
    Discribe_Missing_Data_Pane.add_columns_for_group_analysis_by(check_column_name_list=["nRuns'中", "nRBI'中"])
    flow.screenshot_self("data")
    flow.arrange_nodes()
    flow.run(False)
    flow.screenshot_without_toast("run")
    flow.click_results_tab()
    time.sleep(1)
    flow.screenshot_without_toast("results")
