"""This is test case file for step Mosaic Plot"""
import pytest
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.mosaic_plot_pane import MosaicPlotPane
from src.Data.input_data_zh import *
from src.Helper.page_factory import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


@pytest.mark.level0_step
def test_00_mosaic_plot_in_flow(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CARS")
    time.sleep(0.5)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_MOSAIC_PLOT]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("CARS", Helper.data_locale.STEP_MOSAIC_PLOT)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    time.sleep(0.5)

    mosaic_plot_pane = MosaicPlotPane(page)
    mosaic_plot_pane.add_column_for_y_axis("气缸")
    time.sleep(0.5)
    mosaic_plot_pane.add_column_for_X_axis("原产地")
    time.sleep(0.5)
    flow.run(True)


@pytest.mark.level1_step
def test_01_mosaic_plot_in_flow(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area(INPUTDATAZH.AUTOLIB)
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CARS")
    time.sleep(0.3)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_MOSAIC_PLOT]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("CARS", Helper.data_locale.STEP_MOSAIC_PLOT)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    time.sleep(0.3)

    mosaic_plot_pane = MosaicPlotPane(page)
    mosaic_plot_pane.add_column_for_y_axis("气缸")
    time.sleep(0.3)
    mosaic_plot_pane.add_column_for_X_axis("原产地")
    time.sleep(0.3)
    mosaic_plot_pane.add_columns_for_stratify_by(["类型", "驱动类型"])
    time.sleep(0.3)
    mosaic_plot_pane.expand_windowshade_additional_roles()
    mosaic_plot_pane.add_column_for_group_analysis_by("型号")
    time.sleep(0.3)
    mosaic_plot_pane.click_options_tab()
    mosaic_plot_pane.set_check_square_plot()
    time.sleep(0.3)
    mosaic_plot_pane.select_color_tiles_by(Helper.data_locale.STANDARDIZED_RESIDUALS)
    time.sleep(0.3)
    flow.run(True)
