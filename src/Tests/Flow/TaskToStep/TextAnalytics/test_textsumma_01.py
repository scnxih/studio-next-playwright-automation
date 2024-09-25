"""This is test case file for step Text Summarization"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.TextAnalytics.text_summarization_pane import TextSummarization
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *

@pytest.mark.level0_step
def test_01_text_summarization_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    flow.run(True)

@pytest.mark.level1_step
def test_02_text_summarization_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_check_use_entities_and_noun_groups()
    flow.run(True)

@pytest.mark.level1_step
def test_03_text_summarization_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.corpusSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Corpus'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Corpus'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_check_entire_corpus()
    text_summarization_pane.set_check_use_entities_and_noun_groups()

    flow.run(True)

@pytest.mark.level1_step
def test_04_text_summarization_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.docSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Document'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Document'中文")
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.corpusSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Corpus'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Corpus'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_check_entire_corpus()
    text_summarization_pane.set_check_use_entities_and_noun_groups()

    text_summarization_pane.click_output_tab()
    text_summarization_pane.set_include_variables_from_input_CAS_table(item_index=3)
    text_summarization_pane.add_columns_for_include_these_variables(check_column_name_list=["text'中文"])
    text_summarization_pane.expand_windowshade_corpus_summary()
    text_summarization_pane.set_check_show_output_data()
    flow.run(True)

@pytest.mark.level1_step
def test_05_text_summarization_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
cas;
caslib _all_ assign;
data casuser.'TEXTSUMMARY''中文'n;
set AUTOLIB.'TEXTSUMMARY''中文'n;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    table_pane.set_table("TEXTSUMMARY'中文")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "TEXTSUMMARY'中文")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_TEXT_ANALYTICS,
                 Helper.data_locale.STEP_TEXT_SUMMARIZATION]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("TEXTSUMMARY'中文", Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    flow.arrange_nodes()

    flow.click_add_output_port_in_context_menu_on_node(Helper.data_locale.STEP_TEXT_SUMMARIZATION,
                                                       "{sasstudio-steps-gui-icu.textsummarization.outputports.corpusSumOutTbl.title}")
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Corpus'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_TEXT_SUMMARIZATION, "Corpus'中文")
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_TEXT_SUMMARIZATION)
    text_summarization_pane = TextSummarization(page)
    text_summarization_pane.set_language(item_index=1)

    text_summarization_pane.add_column_for_text_variable("text'中文")
    text_summarization_pane.set_key_variable(item_index=1)
    text_summarization_pane.add_column_for_key_variable("key'中文")

    text_summarization_pane.click_options_tab()
    text_summarization_pane.set_uncheck_each_document()
    text_summarization_pane.set_check_entire_corpus()
    text_summarization_pane.set_check_use_entities_and_noun_groups()

    text_summarization_pane.click_output_tab()
    text_summarization_pane.expand_windowshade_corpus_summary()
    text_summarization_pane.set_check_show_output_data()
    flow.run(True)
