"""This is test case file for step Characterize Data"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.characterize_data_pane import CharacterizeDataPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_characterize_date_level0(page, init):
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
    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_CHARACTERIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CHARACTERIZE_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CHARACTERIZE_DATA)
    Characterize_Data_Pane =CharacterizeDataPane(page)
    Characterize_Data_Pane.click_data_tab()
    Characterize_Data_Pane.set_filter_input_data("'nAtBat''中'n > 200")
    Characterize_Data_Pane.expand_windowshade_automatic_characterization()
    Characterize_Data_Pane.add_columns_for_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    Characterize_Data_Pane.add_column_for_grouping_variable(column_name="nRBI'中")
    time.sleep(1)
    flow.screenshot_self("data")
    flow.arrange_nodes()
    flow.run(False)
    flow.screenshot_without_toast("run")

@pytest.mark.level1_step
def test_02_characterize_date_level1(page, init):
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
    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_CHARACTERIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CHARACTERIZE_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CHARACTERIZE_DATA)
    Characterize_Data_Pane =CharacterizeDataPane(page)
    Characterize_Data_Pane.click_data_tab()
    Characterize_Data_Pane.set_filter_input_data("'nAtBat''中'n > 200")
    Characterize_Data_Pane.expand_windowshade_automatic_characterization()
    Characterize_Data_Pane.add_columns_for_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    Characterize_Data_Pane.expand_windowshade_custom_characterization()
    Characterize_Data_Pane.add_column_for_grouping_variable(column_name="nRBI'中")
    flow.screenshot_self("data")
    Characterize_Data_Pane.click_options_tab()
    Characterize_Data_Pane.expand_windowshade_categorical_variables()
    Characterize_Data_Pane.set_check_frequency_table()
    Characterize_Data_Pane.set_check_frequency_chart()
    Characterize_Data_Pane.set_check_treat_missing_values_valid_level()
    Characterize_Data_Pane.set_check_limit_categorical_values()
    Characterize_Data_Pane.expand_windowshade_numeric_variables()
    Characterize_Data_Pane.set_check_descriptive_statistics()
    Characterize_Data_Pane.set_check_histogram()
    Characterize_Data_Pane.expand_windowshade_date_variables()
    Characterize_Data_Pane.set_check_display_minimum_maximum_date()
    Characterize_Data_Pane.set_check_frequency_plot()
    flow.screenshot_self("options")
    flow.arrange_nodes()
    flow.run(False)
    flow.screenshot_without_toast("run")
    flow.click_results_tab()
    flow.screenshot_without_toast("results")
