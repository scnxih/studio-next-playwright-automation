"""This is test case file for step Line Chart"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.line_chart_pane import LineChartPane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


@pytest.mark.level0_step
def test_01_line_chart_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    line_chart_pane = LineChartPane(page)
    line_chart_pane.add_column_for_category("Team'中文")
    flow.run(True)


@pytest.mark.level1_step
def test_02_line_chart_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    line_chart_pane = LineChartPane(page)
    line_chart_pane.set_filter_input_data("UPPER('Division''中'n) = '东部'")
    line_chart_pane.add_column_for_category("Team'中文")
    line_chart_pane.add_column_for_subcategory("姓名1")
    line_chart_pane.set_display_subcategory_legend(item_index=1)
    line_chart_pane.set_measure(item_index=2)
    line_chart_pane.add_column_for_column("nHits'中")
    line_chart_pane.set_statistics(item_index=1)
    line_chart_pane.set_error_bars(item_index=2)
    line_chart_pane.set_type(item_index=1)
    line_chart_pane.set_check_specify_statistic_multiplier()
    line_chart_pane.set_multiplier("2")
    line_chart_pane.expand_windowshade_additional_roles()
    line_chart_pane.add_column_for_group_analysis_by("League'中")
    line_chart_pane.add_column_for_weight("nHome'中")
    flow.run(True)


@pytest.mark.level1_step
def test_03_line_chart_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;    
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("BASEBALL'中文测试")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_LINE_CHART)
    line_chart_pane = LineChartPane(page)
    line_chart_pane.add_column_for_category("Team'中文")
    line_chart_pane.set_measure(item_index=2)
    line_chart_pane.add_column_for_column("nHits'中")
    line_chart_pane.expand_windowshade_additional_roles()
    line_chart_pane.add_column_for_group_analysis_by("League'中")

    line_chart_pane.click_options_tab()
    line_chart_pane.expand_windowshade_lines()
    line_chart_pane.set_check_show_data_labels()
    line_chart_pane.set_check_show_line_label()
    line_chart_pane.set_label("中文'测试")
    line_chart_pane.set_check_set_color()
    line_chart_pane.set_color_transparency(item_index=2)
    line_chart_pane.set_line_style(item_index=5)
    line_chart_pane.add_column_for_url_variable("Div'中")

    line_chart_pane.expand_windowshade_x_axis()
    line_chart_pane.set_check_reverse_tick_values()
    line_chart_pane.set_check_show_tick_values_in_data_order()
    line_chart_pane.set_option_for_display_label_for_x_axis(item_index=2)
    line_chart_pane.set_text_for_first_label_for_x_axis("x轴标签")
    line_chart_pane.set_check_rotate_values_in_case_of_tick_collisions()
    line_chart_pane.set_rotate_degree(item_index=1)
    line_chart_pane.set_check_for_create_reference_line_for_x_axis()
    line_chart_pane.set_reference_values_x(item_index=15)
    line_chart_pane.set_line_offset(item_index=3)

    line_chart_pane.expand_windowshade_y_axis()
    line_chart_pane.set_check_specify_minimum_value()
    line_chart_pane.set_minimum_value("1200")
    line_chart_pane.set_check_specify_maximum_value()
    line_chart_pane.set_maximum_value("2000")
    line_chart_pane.set_option_for_display_label_for_y_axis(item_index=4)
    line_chart_pane.set_text_for_first_label_for_y_axis("y轴标签")
    line_chart_pane.set_check_use_logarithmic_scale()
    line_chart_pane.set_base_value(item_index=1)
    line_chart_pane.set_check_for_create_reference_line_for_y_axis()
    line_chart_pane.set_reference_values_y("1500")

    line_chart_pane.expand_windowshade_title_footnote()
    line_chart_pane.set_title("线图中文标题")
    line_chart_pane.set_footnote("线图中文脚注")

    flow.run(True)
