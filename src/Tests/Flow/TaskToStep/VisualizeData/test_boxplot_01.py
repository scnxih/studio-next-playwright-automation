import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.box_plot_pane import BoxPlotPane
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import FlowNodeType
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.same_birthday_pane import SameBirthdayProbabilityPane

"""This is testcase file for step Box Plot"""
"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: September 11th, 2024
"""


def test_init(page, init):
    PageHelper.init_environments(page)


@pytest.mark.level0_step
def test_01_box_plot_lev0(page, init):
    """
    Level-0 testcase for Visualization/Box Plot
    Data Input: SASHELP.BASEBALL
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table node
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    # Set input table
    table_pane = TablePane(page)
    table_pane.set_library("sashelp")
    table_pane.set_table("baseball")

    # Add STEP_CATEGORY_VISUALIZE_DATA/STEP_BOX_PLOT
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BOX_PLOT]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)
    flow.link_two_nodes_in_flow("baseball", Helper.data_locale.STEP_BOX_PLOT)
    flow.arrange_nodes()
    # Fow overflow menu changed
    # flow.apply_detail_layout_vertical()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)

    box_plot_pane = BoxPlotPane(page)
    box_plot_pane.set_filter_input_data("Team IS NOT MISSING")
    box_plot_pane.set_analysis_variable("nHome")

    flow.run(True)

    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)
    time.sleep(3)

    flow.screenshot_self(pic_name="baseball_box_plot")


@pytest.mark.level1_step
def test_02_box_plot_lev1(page, init):
    """
    Level-1 testcase for Visualization/Box Plot
    Data Input: SASHELP.CLASS
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table node
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    # Set input table
    table_pane = TablePane(page)
    table_pane.set_library("sashelp")
    table_pane.set_table("class")

    # Add STEP_CATEGORY_VISUALIZE_DATA/STEP_BOX_PLOT
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BOX_PLOT]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)
    flow.link_two_nodes_in_flow("class", Helper.data_locale.STEP_BOX_PLOT)
    flow.arrange_nodes()
    # Fow overflow menu changed
    # flow.apply_detail_layout_vertical()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)

    box_plot_pane = BoxPlotPane(page)
    box_plot_pane.set_filter_input_data("Weight IS NOT MISSING")
    box_plot_pane.set_analysis_variable("Weight")
    box_plot_pane.set_subcategory("Sex")
    # box_plot_pane.set_group_analysis_by("Age")
    box_plot_pane.set_category("Age")

    box_plot_pane.set_plot_orientation(item_index=1)
    time.sleep(0.5)
    box_plot_pane.set_plot_orientation(item_index=0)
    time.sleep(0.5)
    box_plot_pane.set_check_notches()

    box_plot_pane.set_color_transparency_percentage(item_index=2)
    box_plot_pane.set_color_transparency_percentage(item_index=1)
    box_plot_pane.set_color_transparency_percentage(item_index=0)

    box_plot_pane.set_effect(item_index=2)
    box_plot_pane.set_effect(item_index=1)
    box_plot_pane.set_effect(item_index=0)

    box_plot_pane.set_graph_size_unit(item_index=1)
    box_plot_pane.set_graph_size_width_to("7")

    box_plot_pane.set_title_as("MyTitle")
    box_plot_pane.set_footnote_as("MyFootNote")

    flow.run(True)

    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)
    time.sleep(3)

    flow.screenshot_self(pic_name="cars_box_plot",
                         mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                         mask_color="#000000")


@pytest.mark.level1_step
def test_03_box_plot_lev1(page, init):
    """
    Level-1 testcase for Visualization/Box Plot
    Data Input: SASHELP.CARS
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table node
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    # Set input table
    table_pane = TablePane(page)
    table_pane.set_library("sashelp")
    table_pane.set_table("cars")

    # Add STEP_CATEGORY_VISUALIZE_DATA/STEP_BOX_PLOT
    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BOX_PLOT]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)
    flow.link_two_nodes_in_flow("cars", Helper.data_locale.STEP_BOX_PLOT)
    flow.arrange_nodes()
    # Fow overflow menu changed
    # flow.apply_detail_layout_vertical()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BOX_PLOT)

    box_plot_pane = BoxPlotPane(page)
    box_plot_pane.set_filter_input_data("Weight IS NOT MISSING")
    box_plot_pane.set_analysis_variable("MPG_City")
    box_plot_pane.set_subcategory("Type")
    box_plot_pane.set_group_analysis_by("Origin")

    box_plot_pane.set_plot_orientation(item_index=1)
    time.sleep(0.5)
    box_plot_pane.set_plot_orientation(item_index=0)
    time.sleep(0.5)
    box_plot_pane.set_check_notches()

    box_plot_pane.set_color_transparency_percentage(item_index=2)
    box_plot_pane.set_color_transparency_percentage(item_index=1)
    box_plot_pane.set_color_transparency_percentage(item_index=0)

    box_plot_pane.set_effect(item_index=2)
    box_plot_pane.set_effect(item_index=1)
    box_plot_pane.set_effect(item_index=0)

    box_plot_pane.set_graph_size_unit(item_index=1)
    box_plot_pane.set_graph_size_width_to("7")

    box_plot_pane.set_title_as("MyTitle")
    box_plot_pane.set_footnote_as("MyFootNote")

    flow.run(True)

    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    # flow.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + "(1)")
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)
    time.sleep(3)

    flow.screenshot_self(pic_name="cars_box_plot",
                         mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                         mask_color="#000000")
