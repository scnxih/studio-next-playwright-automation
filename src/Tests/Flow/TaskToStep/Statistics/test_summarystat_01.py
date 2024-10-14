"""This is test case file for step Summary Statistics"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.summary_statistics_pane import SummaryStatisticsPane
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_summary_statistics_level0(page, init):
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
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SUMMARY_STATISTICS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUMMARY_STATISTICS)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUMMARY_STATISTICS)
    Summary_Statistics_Pane = SummaryStatisticsPane(page)
    Summary_Statistics_Pane.click_data_tab()
    Summary_Statistics_Pane.add_columns_for_analysis_variables(check_column_name_list=["nHits'中", "CrHits'中"])
    Summary_Statistics_Pane.add_columns_for_classification_variable(check_column_name_list=["Team'中文", "nRBI'中"])
    Summary_Statistics_Pane.expand_windowshade_additional_roles()
    Summary_Statistics_Pane.add_columns_for_group_analysis_by(check_column_name_list=["nAtBat'中", "nHits'中"])
    Summary_Statistics_Pane.add_columns_for_copy_variables(check_column_name_list=["nBB'中", "YrMajor'中"])
    flow.screenshot_self("data")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Result'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUMMARY_STATISTICS, "Result'中文")
    flow.arrange_nodes()
    flow.run(False)
    flow.screenshot_after_run()
@pytest.mark.level1_step
def test_02_Summary_Statistics_level1(page, init):
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
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SUMMARY_STATISTICS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUMMARY_STATISTICS)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUMMARY_STATISTICS)

    Summary_Statistics_Pane = SummaryStatisticsPane(page)
    Summary_Statistics_Pane.click_data_tab()
    Summary_Statistics_Pane.add_columns_for_analysis_variables(check_column_name_list=["nHits'中", "CrHits'中"])
    Summary_Statistics_Pane.add_columns_for_classification_variable(check_column_name_list=["Team'中文", "nRBI'中"])
    Summary_Statistics_Pane.set_combinations_of_classification_variables(item_index=1)
    Summary_Statistics_Pane.expand_windowshade_additional_roles()
    Summary_Statistics_Pane.add_columns_for_group_analysis_by(check_column_name_list=["nAtBat'中", "nHits'中"])
    Summary_Statistics_Pane.add_columns_for_copy_variables(check_column_name_list=["nBB'中", "YrMajor'中"])
    Summary_Statistics_Pane.set_value_to_copy(item_index=1)
    Summary_Statistics_Pane.add_column_for_frequency_count(column_name="CrAtBat'中")
    Summary_Statistics_Pane.add_column_for_weight_variable(column_name="Salary'中")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUMMARY_STATISTICS, "Result'中文")
    flow.arrange_nodes()

    flow.run(False)
    flow.screenshot_after_run()