"""This is test case file for step Community Detection"""
import pytest

from src.Data.input_data_zh import INPUTDATAZH
from src.Helper.page_helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.community_detection_pane import \
    CommunityDetectionPane
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage
from src.Pages.StudioNext.Center.start_page import StartPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem, FlowNodeType


@pytest.mark.level0_step
def test_00_community_detection_in_flow(page, init):
    """
    Example: Community Detection Task
    link: https://go.documentation.sas.com/doc/en/sasstudiocdc/v_055/webeditorcdc/webeditorref/p12ahk8igzw3bjn1qr1czjkjxnbd.htm

    """

    # Create a new flow from new start page
    top = TopMenuPage(page)
    top.check_view_item(TopMenuItem.view_start_page)
    StartPage(page).wait_for_timeout(time_out=3000)
    StartPage(page).build_a_flow()

    # Wait for a while
    MainCenterPage(page).wait_for_timeout(time_out=3000)

    flow: FlowPage = FlowPage(page)
    flow.wait_for_page_load()

    flow.add_node(FlowNodeType.sas_program)
    flow.wait_for_page_load()

    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)

    sas_program_pane = SASProgramPane(page)

    flow.wait_for_page_load()

    sas_program_pane.type_into_text_area(INPUTDATAZH.CORE_DECOMPOSITION)
    sas_program_pane.editor.format_code_via_context_menu()

    flow.prt_scn("sas_program")

    sas_program_pane.set_node_name("创建表")
    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    flow.wait_for_page_load()
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    flow.wait_for_page_load()
    table_pane.set_table("LINKSETIN'链接")
    flow.wait_for_page_load()
    table_pane.set_node_name("LINKSETIN'链接")
    flow.wait_for_page_load()
    table_pane.set_node_description("Table on CAS")
    flow.wait_for_page_load()

    flow.link_two_nodes_in_flow("创建表", "LINKSETIN'链接")
    flow.wait_for_page_load()
    flow.arrange_nodes()
    flow.prt_scn("after_link_two_nodes")

    flow.saveas(Helper.public_folder_path, 'community_detection', True, True)
    flow.run(False)

    flow.select_node_in_flow_canvas("LINKSETIN'链接")

    table_pane.preview_data()

    flow.wait_for_page_load()
    flow.prt_scn("after_file_saving")

    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                 Helper.data_locale.STEP_COMMUNITY_DETECTION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_COMMUNITY_DETECTION)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.link_two_nodes_in_flow("LINKSETIN'链接", Helper.data_locale.STEP_COMMUNITY_DETECTION)
    community_detection_pane = CommunityDetectionPane(page)
    community_detection_pane.add_column_for_from_node("from'始")
    community_detection_pane.add_column_for_to_node("to'终")
    community_detection_pane.add_column_for_weight_in_nodes("weight'中")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_COMMUNITY_DETECTION, Helper.data_locale.ADD_OUTPUT_PORT)
    flow.save(True)
    flow.run(True)
    flow.click_results_tab()
    flow.wait_for_page_load(time_out=5000)
    flow.screenshot_self('results')

    flow.click_output_data_tab()
    flow.wait_for_page_load(time_out=5000)
    flow.screenshot_self('output')

