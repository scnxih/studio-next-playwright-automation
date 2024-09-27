import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import FlowNodeType
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.same_birthday_pane import SameBirthdayProbabilityPane

"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: September 11th, 2024
"""

"""This is test case file for step Same Birthday Probability"""




@pytest.mark.level0_step
def test_01_same_birthday_lev0(page, init):
    """
    Level-0 testcase for Statistics/Same Birthday Probability
    Reference: https://sww2.sas.com/saspedia/SAS_Studio_Same_Birthday_Probability_task#Level_0_Scenario
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add STEP_SAME_BIRTHDAY_PROBABILITY
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY]
    flow.add_step_from_stepspane_to_flow(step_path)

    # Connect output port with same birthday node
    # flow.apply_detail_layout_vertical()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY)

    same_birthday_probability_pane = SameBirthdayProbabilityPane(page)
    same_birthday_probability_pane.set_number_of_people_in_a_room("145")
    same_birthday_probability_pane.screenshot_self("options")

    flow.run(True)
    time.sleep(1)
    flow.screenshot_self("run")
    # flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.click_log_tab()
    time.sleep(0.5)
    flow.screenshot_self("log")
    # flow.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + "(1)")
    # flow.tab_group.click_tab_by_text("输出数据 (1)")
    flow.click_output_data_tab()
    time.sleep(0.5)
    flow.screenshot_self("output_data")
    # time.sleep(3)

    # flow.screenshot_self(pic_name="flow_results_same_birthday")
    # Mask table name
    # //h5[@data-testid="dataPane-toolbar-nameHeading"]
    # flow.screenshot_self(pic_name="flow_results_same_birthday",
    #                      mask=['//h5[@data-testid="dataPane-toolbar-nameHeading"]'],
    #                      mask_color="#000000")
    # WholePage(page).screenshot_self(pic_name="flow_results_same_birthday")


@pytest.mark.level1_step
def test_02_same_birthday_lev1(page, init):
    """
    Level-1 testcase for Statistics/Same Birthday Probability
    Reference: https://sww2.sas.com/saspedia/SAS_Studio_Same_Birthday_Probability_task#Level_0_Scenario
    """

    # Create a flow
    flow: FlowPage = PageHelper.new_flow(page)

    # Add a table node
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    # Set output table
    table_pane = TablePane(page)
    table_pane.set_library("work")
    table_pane.set_table("prob_same_birthday")

    # Add STEP_SAME_BIRTHDAY_PROBABILITY
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY]
    flow.add_step_from_stepspane_to_flow(step_path)

    # Connect output port with same birthday node
    flow.select_output_port_node_in_flow(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY)
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY, "prob_same_birthday")
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY)

    same_birthday_probability_pane = SameBirthdayProbabilityPane(page)
    same_birthday_probability_pane.set_number_of_people_in_a_room("2")

    flow.run(True)
    time.sleep(3)
    flow.screenshot_self("run")
    flow.click_log_tab()
    time.sleep(0.5)
    flow.screenshot_self("log")
    flow.click_output_data_tab()
    time.sleep(0.5)
    flow.screenshot_self("output_data")
    # flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    # flow.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + "(1)")
    # flow.tab_group.click_tab_by_text("输出数据 (1)")
    # time.sleep(3)

    # flow.screenshot_self(pic_name="flow_results_same_birthday")
    # Mask table name
    # //h5[@data-testid="dataPane-toolbar-nameHeading"]
    # flow.screenshot_self(pic_name="flow_results_same_birthday",
    #                      mask=['//h5[@data-testid="dataPane-toolbar-nameHeading"]'],
    #                      mask_color="#000000")
    # WholePage(page).screenshot_self(pic_name="flow_results_same_birthday")
