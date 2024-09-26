import pytest

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Utilities.enums import FlowNodeType, TopMenuItem

from src.Pages.StudioNext.Center.Flow.DetailsPane.TextAnalytics.text_parsing_and_topic_analysis_pane import \
    TextParsingAndTopicAnalysisPane

"""This is test case file for step Text Scoring"""


def test_init(page, init):
    PageHelper.init_environments(page)


@pytest.mark.level0_step
def test_01_txt_and_topic_lev0(page, init):
    """
    Level 0 Scenarios (for topic model = SVD)
    """
    # Create a sas program and run
    sas_program_code = """
libname mycas cas caslib="CASUSER";

data mycas.getstart;
infile datalines delimiter='|' missover;
length text $150;
input text$ apple_fruit did$;
datalines;
Delicious and crunchy apple is one of the popular fruits | 1 |d01
Apple was the king of all fruits. | 1 |d02
Custard apple or Sitaphal is a sweet pulpy fruit | 1 |d03
apples are a common tree throughout the tropics | 1 |d04
apple is round in shape, and tasts sweet | 1 |d05
Tropical apple trees produce sweet apple| 1| d06
Fans of sweet apple adore Fuji because it is the sweetest of| 1 |d07
this apple tree is small | 1 |d08
Apple Store shop iPhone x and iPhone x Plus.| 0 |d09
See a list of Apple phone numbers around the world.| 0 |d10
Find links to user guides and contact Apple Support, | 0 |d11
Apple counters Samsung Galaxy launch with iPhone gallery | 0 |d12
Apple Smartphones - Verizon Wireless.| 0 |d13
Apple mercurial chief executive, was furious.| 0 |d14
Apple has upgraded the phone.| 0 |d15
the great features of the new Apple iPhone x.| 0 |d16
Apple sweet apple iphone.| 0 |d17
Apple apple will make cars | 0 |d18
Apple apple also makes watches| 0 |d19
Apple apple makes computers too| 0 |d20
;
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
    table_pane.set_library("mycas")
    table_pane.set_table("getstart")
    table_pane.refresh_table()

    # Add Text Parsing and Topic Discovery node
    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.link_two_nodes_in_flow("getstart", Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.arrange_nodes()

    # Fow overflow menu changed
    # flow.apply_detail_layout_vertical()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_vertical()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    # TextParsingAndTopicAnalysisPane
    tp_ta_pane = TextParsingAndTopicAnalysisPane(page)
    tp_ta_pane.set_input_table_contains(1)
    tp_ta_pane.set_input_table_contains(0)

    tp_ta_pane.set_language(item_value="英语")

    flow.select_node_in_flow_canvas("getstart")
    table_pane = TablePane(page)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.PREVIEW_DATA)
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.NOTES)
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.TABLE_PROPERTIES)
    table_pane.refresh_table()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    tp_ta_pane.set_text_variable("text")

    tp_ta_pane.set_scree_plot_of_singular_values()

    tp_ta_pane.set_save_term_by_document_matrix()

    # Incomplete function (Studio Next on daily.pgc)
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY,
                                            "添加输出端口",
                                            "{sasstudio-steps-gui-icu.textparsingandtopicdiscovery.outputports.topicDistOutputDSName.displayname.title}")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "添加输出端口", "父表")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("casuser")
    table_pane.set_table("tbd")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "tbd")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    tp_ta_pane.set_save_term_information()

    # Incomplete function (Studio Next on daily.pgc)
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY,
                                            "添加输出端口",
                                            "{sasstudio-steps-gui-icu.genericText.outputport.termInformationTable.title}")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "添加输出端口", "词条信息表")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("casuser")
    table_pane.set_table("terms")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "terms")
    flow.arrange_nodes()


@pytest.mark.level0_step
def test_02_txt_and_topic_lev0(page, init):
    """
    Level 0 Scenarios (for topic model = LDA)
    """

    # Create a sas program and run
    sas_program_code = """
libname mycas cas caslib="CASUSER";

data mycas.getstart;
    infile datalines delimiter='|' missover;
    length text $150;
    input text$ apple_fruit did$;
    datalines;
Delicious and crunchy apple is one of the popular fruits | 1 |d01
Apple was the king of all fruits. | 1 |d02
Custard apple or Sitaphal is a sweet pulpy fruit | 1 |d03
apples are a common tree throughout the tropics | 1 |d04
apple is round in shape, and tasts sweet | 1 |d05
Tropical apple trees produce sweet apple| 1| d06
Fans of sweet apple adore Fuji because it is the sweetest of| 1 |d07
this apple tree is small | 1 |d08
Apple Store shop iPhone x and iPhone x Plus.| 0 |d09
See a list of Apple phone numbers around the world.| 0 |d10
Find links to user guides and contact Apple Support, | 0 |d11
Apple counters Samsung Galaxy launch with iPhone gallery | 0 |d12
Apple Smartphones - Verizon Wireless.| 0 |d13
Apple mercurial chief executive, was furious.| 0 |d14
Apple has upgraded the phone.| 0 |d15
the great features of the new Apple iPhone x.| 0 |d16
Apple sweet apple iphone.| 0 |d17
Apple apple will make cars | 0 |d18
Apple apple also makes watches| 0 |d19
Apple apple makes computers too| 0 |d20
;
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
    table_pane.set_library("mycas")
    table_pane.set_table("getstart")
    table_pane.refresh_table()

    # Add Text Parsing and Topic Discovery node
    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY]

    flow.add_step_from_stepspane_to_flow(step_path)

    # Link two nodes
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.link_two_nodes_in_flow("getstart", Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)
    flow.arrange_nodes()
    flow.apply_detail_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    # TextParsingAndTopicAnalysisPane
    tp_ta_pane = TextParsingAndTopicAnalysisPane(page)
    tp_ta_pane.set_input_table_contains(1)
    tp_ta_pane.set_input_table_contains(0)

    tp_ta_pane.set_language(0)
    tp_ta_pane.set_language(item_value="英语")

    flow.select_node_in_flow_canvas("getstart")
    table_pane = TablePane(page)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.PREVIEW_DATA)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.NOTES)
    table_pane.refresh_table()
    table_pane.tab_group.click_tab_by_text(Helper.data_locale.TABLE_PROPERTIES)
    table_pane.refresh_table()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY)

    tp_ta_pane.set_text_variable("text")
    tp_ta_pane.set_topic_model(item_index=1)
    tp_ta_pane.set_topic_model(item_index=0)
    tp_ta_pane.set_topic_model(item_index=1)

    tp_ta_pane.set_number_of_topics_to("3")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY,
                                            "添加输出端口",
                                            "{sasstudio-steps-gui-icu.textparsingandtopicdiscovery.outputports.topicDistOutputDSName.displayname.title}")

    # flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "添加输出端口", "父表")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("casuser")
    table_pane.set_table("topicsWords")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_PARSING_AND_TOPIC_DISCOVERY, "topicsWords")
    flow.arrange_nodes()
