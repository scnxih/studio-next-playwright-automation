import time

import pytest

from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.PrepareAndExploreData.standardize_data_pane import StandardizeData
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.permutations_pane import Permutations
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Utilities.enums import AccordionType, TopMenuItem, DesignerControlType, FlowNodeType
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.one_way_frequencies_pane import OneWayFrequencies
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
"""This is test case file for step Permutations"""
@pytest.mark.level0_step
def test_01_permutations_level0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_PERMUTATIONS]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("OUT'中文测试")
    time.sleep(0.8)

    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_PERMUTATIONS, "OUT'中文测试")
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_PERMUTATIONS)
    permutations = Permutations(page)
    permutations.set_uncheck_replace_existing_output_table()
    flow.run(False)

    permutations.set_check_replace_existing_output_table()
    flow.run(False)
    flow.screenshot_after_run()