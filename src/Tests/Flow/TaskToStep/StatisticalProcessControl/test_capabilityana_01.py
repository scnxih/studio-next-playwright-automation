import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.StatisticalProcessControl.capability_analysis_pane import \
    CapabilityAnalysisPane
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Utilities.enums import FlowNodeType, TopMenuItem

"""This is test case file for step Capability Analysis"""


def test_init(page, init):
    PageHelper.init_environments(page)


@pytest.mark.level0_step
def test_01_cap_anlys_lev0_(page, init):
    """
    Level-0 testcase for Capability Analysis
    """
    # Create a sas program and run
    sas_program_code = """
data trans;
input thick @@;
label thick='Plating Thickness (mils)';
datalines;
3.468 3.428 3.509 3.516 3.461 3.492 3.478 3.556 3.482 3.512
3.490 3.467 3.498 3.519 3.504 3.469 3.497 3.495 3.518 3.523
3.458 3.478 3.443 3.500 3.449 3.525 3.461 3.489 3.514 3.470
3.561 3.506 3.444 3.479 3.524 3.531 3.501 3.495 3.443 3.458
3.481 3.497 3.461 3.513 3.528 3.496 3.533 3.450 3.516 3.476
3.512 3.550 3.441 3.541 3.569 3.531 3.468 3.564 3.522 3.520
3.505 3.523 3.475 3.470 3.457 3.536 3.528 3.477 3.536 3.491
3.510 3.461 3.431 3.502 3.491 3.506 3.439 3.513 3.496 3.539
3.469 3.481 3.515 3.535 3.460 3.575 3.488 3.515 3.484 3.482
3.517 3.483 3.467 3.467 3.502 3.471 3.516 3.474 3.500 3.466
run;
    """

    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area(sas_program_code)
    sas_program.format_program()
    sas_program.run(True)

    sas_program.wait_toast_disappear()

    sas_program.tab_group.click_tab_by_text(Helper.data_locale.OUTPUT_DATA + " (1)")

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("work")
    table_pane.set_table("trans")
    table_pane.refresh_table()

    # Add Capability Analysis node
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                 Helper.data_locale.STEP_CAPABILITY_ANALYSIS]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.link_two_nodes_in_flow("trans", Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)

    # NOTE: Extra Refresh Operations Are Added Owing to CAS Server Instability
    flow.select_node_in_flow_canvas("trans")
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.NOTES)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.PREVIEW_DATA)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.TABLE_PROPERTIES)
    table_pane.refresh_table()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)

    # Set process variable
    capability_analysis = CapabilityAnalysisPane(page)
    capability_analysis.set_process_variable("thick")

    # Set upper and lower limits
    capability_analysis.set_lower_limit_to("3.45")
    capability_analysis.set_upper_limit_to("3.55")

    # Run the flow
    flow.run(True)

    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    time.sleep(3)
    flow.screenshot_self("results")


@pytest.mark.level1_step
def test_02_cap_anlys_lev1_(page, init):
    """
    Level-1 testcase for Capability Analysis
    """

    # Create a sas program and run

    # Set I18N library
    set_autolib_code = """
    libname AUTOLIB '/segatest/I18N/Autolib' ;
        """

    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    PageHelper.set_autoexec(page, set_autolib_code)

    # Create a flow and add table node
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("Autolib")
    table_pane.set_table("BASEBALL'中文测试")
    table_pane.refresh_table()

    # Add Capability Analysis node
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                 Helper.data_locale.STEP_CAPABILITY_ANALYSIS]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CAPABILITY_ANALYSIS)
    flow.arrange_nodes()
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)

    # NOTE: Extra Refresh Operations Are Added Owing to CAS Server Instability
    flow.select_node_in_flow_canvas("BASEBALL'中文测试")
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.NOTES)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.PREVIEW_DATA)
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.NOTES)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.TABLE_PROPERTIES)
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.PREVIEW_DATA)
    table_pane.refresh_table()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAPABILITY_ANALYSIS)

    # Set process variable
    capability_analysis = CapabilityAnalysisPane(page)
    capability_analysis.set_process_variable("logSalary'中")

    # Set upper and lower limits
    capability_analysis.set_target_value_to("3.50")
    capability_analysis.set_lower_limit_to("3.45")
    capability_analysis.set_upper_limit_to("3.55")

    capability_analysis.set_classification_variable("Team'中文")
    capability_analysis.set_group_analysis_by("League'中")

    capability_analysis.set_histogram()
    capability_analysis.set_check_option_for_histogram_distribution("Beta")
    capability_analysis.set_check_option_for_histogram_distribution("Gamma")
    capability_analysis.set_check_option_for_histogram_distribution("指数")
    capability_analysis.set_include_inset_table()

    # Run the flow
    flow.run(True)
    flow.wait_toast_disappear()
    flow.tab_group.click_tab_by_text(Helper.data_locale.SUBMITTED_CODE_AND_RESULTS)
    flow.tab_group.click_tab_by_text(Helper.data_locale.RESULTS)

    # time.sleep(10)
    flow.screenshot_self("results")
