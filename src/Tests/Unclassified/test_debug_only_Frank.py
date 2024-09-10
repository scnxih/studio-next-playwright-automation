"""
@author: Frank (Feng) Jiang
@date: 2024/08/22
@description:
"""

from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.scatter_map_pane import ScatterMapPane
from src.Data.input_data_zh import *
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


def test_scatter_map_controls_in_data_pane(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.apply_detail_layout_vertical()
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_SCATTER_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    time.sleep(0.5)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SCATTER_MAP)
    scatter_map_pane = ScatterMapPane(page)
    scatter_map_pane.collapse_windowshade_plot_data()
    time.sleep(0.5)
    scatter_map_pane.expand_windowshade_plot_data()
    time.sleep(0.5)
    scatter_map_pane.input_filter_input_data("This is expression.")
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_plot_data()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_choropleth_map_layer()
    time.sleep(0.5)
    scatter_map_pane.set_uncheck_include_choropleth_map_layer()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_choropleth_map_layer()
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_data()
    time.sleep(0.5)
    scatter_map_pane.expand_windowshade_map_data()
    time.sleep(0.5)
    scatter_map_pane.input_filter_map_data("This is expression.")
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_data()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_response_data()
    time.sleep(0.5)
    scatter_map_pane.set_uncheck_include_response_data()
    time.sleep(0.5)
    scatter_map_pane.set_check_include_response_data()
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_response_data()
    time.sleep(0.5)
    scatter_map_pane.expand_windowshade_map_response_data()
    time.sleep(0.5)
    scatter_map_pane.input_filter_map_response_data("This is expression.")
    time.sleep(0.5)
    scatter_map_pane.collapse_windowshade_map_response_data()
    time.sleep(0.5)
    scatter_map_pane.set_uncheck_ID_variable()
    time.sleep(0.5)
    scatter_map_pane.set_check_ID_variable()
    time.sleep(0.5)
    scatter_map_pane.select_radio_base_map(item_value=Helper.data_locale.ESRI_MAP)
    time.sleep(0.5)
    scatter_map_pane.input_Esri_URL("http://www.google.com")
    time.sleep(0.5)
    scatter_map_pane.select_radio_base_map(item_value=Helper.data_locale.OPEN_STREET_MAP)


def test_scatter_map_l0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.SCATTER_MAP)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("CITY_POP_LOC'中")
    time.sleep(0.8)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_SCATTER_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CITY_POP_LOC'中", Helper.data_locale.STEP_SCATTER_MAP)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SCATTER_MAP)

    scatter_map_pane = ScatterMapPane(page)
    scatter_map_pane.add_column(parent_label=Helper.data_locale.LATITUDE, column_name="lat'纬度")
    time.sleep(0.5)
    scatter_map_pane.add_column(parent_label=Helper.data_locale.LONGITUDE, column_name="long'经度")
    time.sleep(0.5)
    flow.run(True)
