from time import sleep

from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.multiple_regression_statistical_power_pane import \
    MultipleRegressionStatisticalPowerPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.bar_line_chart_pane import BarLineChartPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.text_map_pane import TextMapPane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

def test_02_text_map_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Dommy新文件夹ÀÁÂÌÍÎ/CS' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CITY_POP_LOC'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "CITY_POP_LOC'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_TEXT_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("CITY_POP_LOC'中文", Helper.data_locale.STEP_TEXT_MAP)
    flow.arrange_nodes()

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_MAP, Helper.data_locale.ADD_INPUT_PORT,
                                            Helper.data_locale.MAP_INPUT_DATA)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("NEVADA'中文")
    flow.link_two_nodes_in_flow("NEVADA'中文", Helper.data_locale.STEP_TEXT_MAP)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_MAP)
    text_map_pane = TextMapPane(page)
    text_map_pane.expand_windowshade_plot_data()
    text_map_pane.add_column_for_latitude("LAT'中文")
    text_map_pane.add_column_for_longitude("LONG'中文")
    text_map_pane.add_column_for_text("COUNTY_NAME'中文")

    text_map_pane.set_check_include_choropleth_map_layer()
    text_map_pane.add_column_for_id_variable("ID'中文")

    text_map_pane.click_options_tab()
    text_map_pane.expand_windowshade_text()
    text_map_pane.set_check_specify_predefined_style()
    text_map_pane.set_style(item_index=5)
    text_map_pane.set_check_specify_text_options()
    text_map_pane.set_check_set_font_color()
    text_map_pane.set_font_family(item_index=2)
    text_map_pane.set_font_style(item_index=1)
    text_map_pane.set_font_weight(item_index=1)
    text_map_pane.set_label_position(item_index=5)

    text_map_pane.expand_windowshade_choromap()
    text_map_pane.expand_windowshade_line_attributes()
    text_map_pane.set_check_set_color()
    text_map_pane.set_line_style(item_index=5)
    text_map_pane.click_options_tab()

    flow.run(True)
    flow.screenshot_without_toast("run")


def test_01_multiple_regression_statistical_power_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS,
                 Helper.data_locale.STEP_MULTIPLE_REGRESSION_STATISTICAL_POWER]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MULTIPLE_REGRESSION_STATISTICAL_POWER)
    multiple_regression_statistical_power_pane = MultipleRegressionStatisticalPowerPane(page)
    multiple_regression_statistical_power_pane.expand_windowshade_number_of_predictors()
    multiple_regression_statistical_power_pane.set_number_of_full_model_predictors("4")
    multiple_regression_statistical_power_pane.set_number_of_reduced_model_predictors("2")
    multiple_regression_statistical_power_pane.expand_windowshade_variance_accounted_for()
    multiple_regression_statistical_power_pane.set_full_model_rsquare_value("0.4")
    multiple_regression_statistical_power_pane.set_reduced_model_rsquare_value("0.3")

    multiple_regression_statistical_power_pane.expand_windowshade_sample_size()
    multiple_regression_statistical_power_pane.set_sample_size_value("9")

    flow.run(True)
