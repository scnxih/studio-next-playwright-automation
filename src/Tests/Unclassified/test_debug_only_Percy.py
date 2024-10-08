from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.bubble_map_pane import BubbleMapPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.split_columns_pane import SplitColumnsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.maximal_cliques_pane import MaximalCliquesPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.summary_statistics_pane import SummaryStatisticsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.rank_data_pane import RankDataPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Econometrics.causal_models_pane import CausalModelsPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.characterize_data_pane import CharacterizeDataPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.ExamineData.describe_missing_data_pane import DescribeMissingDataPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


def test_01_custom_step_columnselector(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.check_show_single_page_as_tab()
    properties.set_label("Data")

    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.select_control(DesignerControlType.input_table, 1)
    properties.set_indent(1)
    properties.set_label("Select the source table:")
    properties.set_default_library("SASHELP")
    properties.set_default_table("CLASS")


def test_Bubble_Map_in_flow_level0(page,init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CITY_POP_LOC'中文")


    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,Helper.data_locale.STEP_BUBBLE_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CITY_POP_LOC'中文",Helper.data_locale.STEP_BUBBLE_MAP)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BUBBLE_MAP)
    bubble_map_pane=BubbleMapPane(page)
    bubble_map_pane.set_filter_input_data("population_city''中文'n > 1000")
    bubble_map_pane.add_column(Helper.data_locale.LATITUDE,"LAT'中文",None)
    bubble_map_pane.add_column(Helper.data_locale.LONGITUDE,"LONG'中文",None)
    bubble_map_pane.add_column(Helper.data_locale.BUBBLE_SIZE,"population_city'中文",None)
    bubble_map_pane.add_column(Helper.data_locale.GROUP, "COUNTY_NAME'中文", None)

    flow.run(True)
def test_Bubble_Map_in_flow_level1_01(page,init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("CITY_POP_LOC'中文")


    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,Helper.data_locale.STEP_BUBBLE_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("CITY_POP_LOC'中文",Helper.data_locale.STEP_BUBBLE_MAP)
    flow.arrange_nodes()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("NEVADA'中文")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_BUBBLE_MAP, "添加输入端口", "{sasstudio-steps-gui-icu.bubblemap.inputports.cmMapDataset.displayname.title}")
    flow.link_two_nodes_in_flow("NEVADA'中文", Helper.data_locale.STEP_BUBBLE_MAP)
    flow.arrange_nodes()

    #flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_BUBBLE_MAP, "添加输入端口","{sasstudio-steps-gui-icu.genericText.inputport.mapResponseData.title}")
    #flow.link_two_nodes_in_flow("COUNTY_POP'中文", Helper.data_locale.STEP_BUBBLE_MAP)
    #flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BUBBLE_MAP)
    bubble_map_pane=BubbleMapPane(page)
    bubble_map_pane.set_filter_input_data("population_city''中文'n > 1000")
    bubble_map_pane.add_column(Helper.data_locale.LATITUDE,"LAT'中文",None)
    bubble_map_pane.add_column(Helper.data_locale.LONGITUDE,"LONG'中文",None)
    bubble_map_pane.add_column(Helper.data_locale.BUBBLE_SIZE,"population_city'中文",None)
    bubble_map_pane.add_column(Helper.data_locale.GROUP, "COUNTY_NAME'中文", None)

    bubble_map_pane.set_choropleth_map_layer()
    bubble_map_pane.set_filter_map_data("'STATE''中文'n>30")
    bubble_map_pane.add_column_for_ID_variable_Map_data(column_name="ID'中文")

    #bubble_map_pane.set_response_data()
    #bubble_map_pane.set_filter_map_resopnse_data("county>2")
    #bubble_map_pane.add_column_for_response_variable(column_name='county_name')
    #bubble_map_pane.add_column_for_ID_variable_Map_response_data(column_name='county')

    bubble_map_pane.set_Base_map(item_index=1)

    """Options tab"""
    bubble_map_pane.click_options_tab()
    bubble_map_pane.expand_windowshade_Data_labels()
    bubble_map_pane.add_column_for_bubble_label(column_name="city'中文")

    bubble_map_pane.expand_windowshade_label_options()
    bubble_map_pane.set_font_color()
    bubble_map_pane.set_font_family(item_index=1)
    bubble_map_pane.set_font_style(item_index=1)
    bubble_map_pane.set_font_weight(item_index=1)
    bubble_map_pane.set_label_position(item_index=2)

    bubble_map_pane.expand_windowshade_bubbles()
    #bubble_map_pane.set_bubbles_color()
    bubble_map_pane.expand_windowshade_plot()
    bubble_map_pane.set_number_of_transparency("20")

    bubble_map_pane.expand_windowshade_title_and_footnote()
    bubble_map_pane.set_title("This is title")
    bubble_map_pane.set_footnote("This is footnote")

    bubble_map_pane.expand_windowshade_graph_size()
    bubble_map_pane.set_units(item_index=1)

    flow.run(True)

def test_Split_Columns_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")

    step_path = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA, Helper.data_locale.STEP_SPLIT_COLUMNS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SPLIT_COLUMNS)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SPLIT_COLUMNS)
    Split_Columns_pane = SplitColumnsPane(page)
    Split_Columns_pane.set_filter_input_data("'nAtBat''中'n> 100")
    Split_Columns_pane.add_column_for_Column_to_split(column_name="Team'中文")
    Split_Columns_pane.add_column_for_Formatted_identifier_values(column_name="nRuns'中")
    Split_Columns_pane.add_column_for_Labels_for_new_columns(column_name="nRBI'中")
    Split_Columns_pane.expand_windowshade_additional_roles()
    Split_Columns_pane.add_columns_for_group_analysis_by(check_column_name_list=["nHits'中", "CrHits'中"])

    Split_Columns_pane.click_output_tab()
    Split_Columns_pane.set_check_for_replace_existing_output_table()
    Split_Columns_pane.set_check_for_use_column_name_prefix()
    Split_Columns_pane.set_text_for_prefix("行'列")
    Split_Columns_pane.set_specify_data_to_show(item_index=1)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    table_pane.set_table("OUTPUT'中文测试")

    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SPLIT_COLUMNS,"OUTPUT'中文测试")

    flow.run(True)

def test_Maximal_Cliques_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("linksetincharnode'中文")
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_MAXIMAL_CLIQUES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("linksetincharnode'中文", Helper.data_locale.STEP_MAXIMAL_CLIQUES)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MAXIMAL_CLIQUES)
    Maximal_Cliques_Pane = MaximalCliquesPane(page)
    Maximal_Cliques_Pane.set_select_server_for_step(item_index=0)
    Maximal_Cliques_Pane.set_filter_link_data("'weight''中文'n <> 15")
    Maximal_Cliques_Pane.add_column_for_from_node("from'中文")
    Maximal_Cliques_Pane.add_column_for_to_node("to'中文")

    Maximal_Cliques_Pane.click_options_tab()
    Maximal_Cliques_Pane.set_check_maximum_number_of_cliques()
    Maximal_Cliques_Pane.set_maximum_number_of_cliques("5")
    Maximal_Cliques_Pane.set_select_maximum_time(item_index=1)
    Maximal_Cliques_Pane.set_maximum_time("600")
    Maximal_Cliques_Pane.set_log_details(item_index=0)
    Maximal_Cliques_Pane.set_select_code_generation(item_index=0)

    Maximal_Cliques_Pane.click_output_tab()
    Maximal_Cliques_Pane.set_check_save_maximal_cliques_data()

    flow.run(True)
def test_Maximal_Cliques_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("linksetincharnode'中文")
    step_path = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_MAXIMAL_CLIQUES]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("linksetincharnode'中文", Helper.data_locale.STEP_MAXIMAL_CLIQUES)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MAXIMAL_CLIQUES)
    Maximal_Cliques_Pane = MaximalCliquesPane(page)
    Maximal_Cliques_Pane.set_select_server_for_step(item_index=0)
    Maximal_Cliques_Pane.set_filter_link_data("'weight''中文'n <> 15")
    Maximal_Cliques_Pane.add_column_for_from_node("from'中文")
    Maximal_Cliques_Pane.add_column_for_to_node("to'中文")

    Maximal_Cliques_Pane.click_options_tab()
    Maximal_Cliques_Pane.set_check_maximum_number_of_cliques()
    Maximal_Cliques_Pane.set_maximum_number_of_cliques("5")
    Maximal_Cliques_Pane.set_select_maximum_time(item_index=1)
    Maximal_Cliques_Pane.set_maximum_time("600")
    Maximal_Cliques_Pane.set_log_details(item_index=1)
    Maximal_Cliques_Pane.set_select_code_generation(item_index=1)

    Maximal_Cliques_Pane.click_output_tab()
    Maximal_Cliques_Pane.set_check_save_maximal_cliques_data()

    flow.run(True)
def test_summary_statistics_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SUMMARY_STATISTICS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUMMARY_STATISTICS)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUMMARY_STATISTICS)
    Summary_Statistics_Pane = SummaryStatisticsPane(page)
    Summary_Statistics_Pane.click_data_tab()
    Summary_Statistics_Pane.add_columns_for_analysis_variables(check_column_name_list=["nHits'中", "CrHits'中"])
    Summary_Statistics_Pane.add_columns_for_classification_variable(check_column_name_list=["Team'中文", "nRBI'中"])
    Summary_Statistics_Pane.expand_windowshade_additional_roles()
    Summary_Statistics_Pane.add_columns_for_group_analysis_by(check_column_name_list=["nAtBat'中", "nHits'中"])
    Summary_Statistics_Pane.add_columns_for_copy_variables(check_column_name_list=["nBB'中", "YrMajor'中"])

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("CASUSER")
    table_pane.set_table("Result'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUMMARY_STATISTICS, "Result'中文")
    flow.arrange_nodes()
    flow.run(True)

def test_Summary_Statistics_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SUMMARY_STATISTICS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_SUMMARY_STATISTICS)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_SUMMARY_STATISTICS)

    Summary_Statistics_Pane = SummaryStatisticsPane(page)
    Summary_Statistics_Pane.click_data_tab()
    Summary_Statistics_Pane.add_columns_for_analysis_variables(check_column_name_list=["nHits'中", "CrHits'中"])
    Summary_Statistics_Pane.add_columns_for_classification_variable(check_column_name_list=["Team'中文", "nRBI'中"])
    Summary_Statistics_Pane.set_combinations_of_classification_variables(item_index=1)
    Summary_Statistics_Pane.expand_windowshade_additional_roles()
    Summary_Statistics_Pane.add_columns_for_group_analysis_by(check_column_name_list=["nAtBat'中", "nHits'中"])
    Summary_Statistics_Pane.add_columns_for_copy_variables(check_column_name_list=["nBB'中", "YrMajor'中"])
    Summary_Statistics_Pane.set_value_to_copy(item_index=1)
    Summary_Statistics_Pane.add_column_for_frequency_count(column_name="CrAtBat'中")
    Summary_Statistics_Pane.add_column_for_weight_variable(column_name="Salary'中")

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_SUMMARY_STATISTICS, "Result'中文")
    flow.arrange_nodes()

    flow.run(True)
def test_rank_data_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA, Helper.data_locale.STEP_RANK_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_RANK_DATA)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_RANK_DATA)
    Rank_data_pane = RankDataPane(page)
    Rank_data_pane.click_data_tab()
    Rank_data_pane.set_filter_input_data("'nAtBat''中'n > 200")
    Rank_data_pane.add_columns_for_columns_to_rank(check_column_name_list=["Team'中文", "nRBI'中"])
    Rank_data_pane.expand_windowshade_additional_roles()
    Rank_data_pane.add_columns_for_rank_by(check_column_name_list=["nHits'中", "nHome'中"])

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_RANK_DATA, "Result'中文")
    flow.arrange_nodes()

    flow.run(True)
def test_causal_models_2sls_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("PRICEDATA")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("PRICEDATA", Helper.data_locale.STEP_CAUSAL_MODELS)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)
    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("('价格'n >= 30)")
    Causal_models_pane.set_select_method(item_index=0)
    Causal_models_pane.add_column_for_dependent_variable("销售")
    Causal_models_pane.add_columns_for_endogenous_explanatory_variables(check_column_name_list=["价格1", "价格2"])
    Causal_models_pane.add_columns_for_exogenous_explanatory_variables(check_column_name_list=["价格3", "价格4"])
    Causal_models_pane.add_columns_for_excluded_instrumental_variables(check_column_name_list=["价格5", "价格6"])

    flow.run(True)


def test_causal_models_heckman_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("JUNKMAIL_中'文")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("JUNKMAIL_中'文", Helper.data_locale.STEP_CAUSAL_MODELS)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)
    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("'All_中''文'n > 0")
    Causal_models_pane.set_select_method(item_index=1)

    Causal_models_pane.expand_windowshade_outcome_equation()
    Causal_models_pane.add_column_for_dependent_variable_outcome_equation("Make_中'文")
    Causal_models_pane.add_columns_for_continuous_variable_outcome_equation(check_column_name_list=["Address_中'文"])
    Causal_models_pane.set_check_intercept_outcome_equation()

    Causal_models_pane.expand_windowshade_selection_equation()
    Causal_models_pane.add_column_for_dependent_variable_selection_equationn("Test_中'文")
    Causal_models_pane.set_select_distinct_value_dependent_variable(item_index=1)
    Causal_models_pane.add_columns_for_continuous_variable_selection_equation(check_column_name_list=["All_中'文","_3D_中'文"])
    Causal_models_pane.set_check_intercept_selection_equation()

    Causal_models_pane.click_options_tab()
    Causal_models_pane.set_select_optimization_method(item_index=1)
    Causal_models_pane.set_select_maximum_number_of_iterations(item_index=1)
    Causal_models_pane.set_maximum_number_of_iterations_text("200")
    Causal_models_pane.set_select_variance_estimation_method(item_index=1)
    Causal_models_pane.set_select_Type_covariances_parameter_estimates(item_index=1)
    Causal_models_pane.set_select_statistics_to_display(item_index=1)
    Causal_models_pane.set_check_correlations_parameter_estimates()
    Causal_models_pane.set_check_covariances_parameter_estimates()
    Causal_models_pane.set_check_iteration_history_objective_function()

    Causal_models_pane.click_output_tab()
    Causal_models_pane.set_check_create_parameter_estimates_data_set()
    Causal_models_pane.set_check_covariance_matrix_estimates()
    Causal_models_pane.set_check_correlation_matrix_estimates()

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane.set_library("WORK")
    table_pane.set_table("Result'中文")
    flow.click_context_menu_on_node_in_flow(Helper.data_locale.STEP_CAUSAL_MODELS, "添加输出端口")
    flow.link_two_nodes_in_flow(Helper.data_locale.STEP_CAUSAL_MODELS, "Result'中文")
    flow.arrange_nodes()

    flow.run(True)

def test_causal_models_2sls_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("PRICEDATA")
    step_path = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("PRICEDATA", Helper.data_locale.STEP_CAUSAL_MODELS)
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CAUSAL_MODELS)
    Causal_models_pane = CausalModelsPane(page)

    Causal_models_pane.click_data_tab()
    Causal_models_pane.set_filter_input_data("('价格'n >= 30)")
    Causal_models_pane.set_select_method(item_index=0)
    Causal_models_pane.add_column_for_dependent_variable("销售")
    Causal_models_pane.add_columns_for_endogenous_explanatory_variables(check_column_name_list=["价格1", "价格2"])
    Causal_models_pane.add_columns_for_exogenous_explanatory_variables(check_column_name_list=["价格3", "价格4"])
    Causal_models_pane.add_columns_for_excluded_instrumental_variables(check_column_name_list=["价格5", "价格6"])
    Causal_models_pane.expand_windowshade_additional_roles()
    Causal_models_pane.add_columns_for_group_analysis_by(check_column_name_list=["日期"])

    Causal_models_pane.click_options_tab()
    Causal_models_pane.set_select_optimization_method(item_index=1)
    Causal_models_pane.set_select_maximum_number_of_iterations(item_index=1)
    Causal_models_pane.set_maximum_number_of_iterations_text(input_text="200")
    Causal_models_pane.set_select_statistics_to_display(item_index=2)
    Causal_models_pane.set_select_pots_display(item_index=2)

    flow.run(True)

def test_characterize_date_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_CHARACTERIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CHARACTERIZE_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CHARACTERIZE_DATA)
    Characterize_Data_Pane =CharacterizeDataPane(page)
    Characterize_Data_Pane.click_data_tab()
    Characterize_Data_Pane.set_filter_input_data("'nAtBat''中'n > 200")
    Characterize_Data_Pane.expand_windowshade_automatic_characterization()
    Characterize_Data_Pane.add_columns_for_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    Characterize_Data_Pane.add_column_for_grouping_variable(column_name="nRBI'中")
    flow.arrange_nodes()
    flow.run(True)

def test_characterize_date_level1(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_CHARACTERIZE_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_CHARACTERIZE_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_CHARACTERIZE_DATA)
    Characterize_Data_Pane =CharacterizeDataPane(page)
    Characterize_Data_Pane.click_data_tab()
    Characterize_Data_Pane.set_filter_input_data("'nAtBat''中'n > 200")
    Characterize_Data_Pane.expand_windowshade_automatic_characterization()
    Characterize_Data_Pane.add_columns_for_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    Characterize_Data_Pane.expand_windowshade_custom_characterization()
    Characterize_Data_Pane.add_column_for_grouping_variable(column_name="nRBI'中")

    Characterize_Data_Pane.click_options_tab()
    Characterize_Data_Pane.expand_windowshade_categorical_variables()
    Characterize_Data_Pane.set_check_frequency_table()
    Characterize_Data_Pane.set_check_frequency_chart()
    Characterize_Data_Pane.set_check_treat_missing_values_valid_level()
    Characterize_Data_Pane.set_check_limit_categorical_values()
    Characterize_Data_Pane.expand_windowshade_numeric_variables()
    Characterize_Data_Pane.set_check_descriptive_statistics()
    Characterize_Data_Pane.set_check_histogram()
    Characterize_Data_Pane.expand_windowshade_date_variables()
    Characterize_Data_Pane.set_check_display_minimum_maximum_date()
    Characterize_Data_Pane.set_check_frequency_plot()
    flow.arrange_nodes()
    flow.run(True)

def test_describe_missing_data_level0(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area('libname autolib "/segatest/I18N/Autolib/";')
    editor.run(True)

    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    step_path = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_DESCRIBE_MISSING_DATA]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_DESCRIBE_MISSING_DATA)
    flow.click_on_canvas_in_flow()
    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_DESCRIBE_MISSING_DATA)
    Discribe_Missing_Data_Pane =DescribeMissingDataPane(page)
    Discribe_Missing_Data_Pane.click_data_tab()
    Discribe_Missing_Data_Pane.set_filter_input_data("'nAtBat''中'n > 200")
    Discribe_Missing_Data_Pane.add_columns_for_analysis_variables(check_column_name_list=["Team'中文", "nAtBat'中"])
    Discribe_Missing_Data_Pane.expand_windowshade_additional_roles()
    Discribe_Missing_Data_Pane.add_columns_for_group_analysis_by(check_column_name_list=["nRuns'中", "nRBI'中"])