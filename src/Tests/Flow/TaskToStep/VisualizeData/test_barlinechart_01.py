"""This is test case file for step Bar-Line Chart"""
"""Added by Dommy 2024-10-14"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.bar_line_chart_pane import BarLineChartPane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
@pytest.mark.level0_step
def test_01_bar_line_chart_in_flow(page, init):
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
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BAR_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_BAR_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BAR_LINE_CHART)
    bar_line_chart_pane = BarLineChartPane(page)

    bar_line_chart_pane.add_column_for_category("Team'中文")
    bar_line_chart_pane.add_column_for_bar_variable("nAtBat'中")
    bar_line_chart_pane.add_column_for_line_variable("nHits'中")
    flow.run(True)

@pytest.mark.level1_step
def test_02_bar_line_chart_in_flow(page, init):
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
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BAR_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_BAR_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BAR_LINE_CHART)
    bar_line_chart_pane = BarLineChartPane(page)
    bar_line_chart_pane.expand_windowshade_data()
    time.sleep(1)

    bar_line_chart_pane.set_filter("UPPER('Division''中'n) = '东部'")
    bar_line_chart_pane.expand_windowshade_roles()
    bar_line_chart_pane.add_column_for_category("Team'中文")
    bar_line_chart_pane.add_column_for_bar_variable("nAtBat'中")
    bar_line_chart_pane.set_statistics_bar(item_index=1)
    bar_line_chart_pane.add_column_for_line_variable("nHits'中")
    bar_line_chart_pane.set_statistics_line(item_index=1)

    bar_line_chart_pane.expand_windowshade_additional_roles()
    bar_line_chart_pane.add_column_for_group_analysis_by("League'中")
    bar_line_chart_pane.add_column_for_weight("nHome'中")
    flow.run(True)


def test_03_bar_line_chart_in_flow(page, init):
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
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BAR_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_BAR_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BAR_LINE_CHART)
    bar_line_chart_pane = BarLineChartPane(page)
    bar_line_chart_pane.expand_windowshade_data()
    time.sleep(1)

    bar_line_chart_pane.set_filter("UPPER('Division''中'n) = '东部'")
    bar_line_chart_pane.expand_windowshade_roles()
    bar_line_chart_pane.add_column_for_category("Team'中文")
    bar_line_chart_pane.add_column_for_bar_variable("nAtBat'中")
    bar_line_chart_pane.set_statistics_bar(item_index=1)
    bar_line_chart_pane.add_column_for_line_variable("nHits'中")
    bar_line_chart_pane.set_statistics_line(item_index=1)

    bar_line_chart_pane.expand_windowshade_additional_roles()
    bar_line_chart_pane.add_column_for_group_analysis_by("League'中")
    bar_line_chart_pane.add_column_for_weight("nHome'中")

    bar_line_chart_pane.click_appearance_tab()
    bar_line_chart_pane.expand_windowshade_bars()
    bar_line_chart_pane.set_check_show_labels_bar()
    bar_line_chart_pane.set_check_set_color_bar()
    bar_line_chart_pane.set_color_transparency_bar(item_index=2)
    bar_line_chart_pane.expand_windowshade_details_bar()
    bar_line_chart_pane.set_check_apply_color_gradient()
    bar_line_chart_pane.set_effect(item_index=3)
    bar_line_chart_pane.add_column_for_url_variable_bar("Position'中")

    bar_line_chart_pane.expand_windowshade_lines()
    bar_line_chart_pane.set_check_show_labels_line()
    bar_line_chart_pane.set_check_set_color_line()
    bar_line_chart_pane.set_thickness_default("3")
    bar_line_chart_pane.set_color_transparency_line(item_index=3)
    bar_line_chart_pane.expand_windowshade_details_line()
    bar_line_chart_pane.set_line_style(item_index=5)
    bar_line_chart_pane.add_column_for_url_variable_line("Team'中文")

    flow.run(True)


def test_04_bar_line_chart_in_flow(page, init):
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
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BAR_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_BAR_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BAR_LINE_CHART)
    bar_line_chart_pane = BarLineChartPane(page)
    bar_line_chart_pane.expand_windowshade_data()
    time.sleep(1)

    bar_line_chart_pane.expand_windowshade_roles()
    bar_line_chart_pane.add_column_for_category("Team'中文")
    bar_line_chart_pane.add_column_for_bar_variable("nAtBat'中")
    bar_line_chart_pane.add_column_for_line_variable("nHits'中")

    bar_line_chart_pane.expand_windowshade_additional_roles()
    bar_line_chart_pane.add_column_for_group_analysis_by("League'中")
    bar_line_chart_pane.add_column_for_weight("nHome'中")

    bar_line_chart_pane.click_appearance_tab()

    bar_line_chart_pane.expand_windowshade_x_axis()
    bar_line_chart_pane.set_check_reverse_tick_values()
    bar_line_chart_pane.set_check_show_tick_values_in_data_order()
    bar_line_chart_pane.set_option_for_display_label_for_x_axis(item_index=2)
    bar_line_chart_pane.set_text_for_first_label_for_x_axis("x轴标签")
    bar_line_chart_pane.set_check_rotate_values_in_case_of_tick_collisions()
    bar_line_chart_pane.set_rotate_degree(item_index=1)
    bar_line_chart_pane.set_check_for_create_reference_line_for_x_axis()
    bar_line_chart_pane.set_reference_values_x_axis(item_index=6)
    bar_line_chart_pane.set_line_offset(item_index=4)
    bar_line_chart_pane.set_radio_reference_label_x_axis(item_index=1)
    bar_line_chart_pane.set_text_for_second_label_for_x_axis("x轴参考线标签")

    bar_line_chart_pane.expand_windowshade_y_axis()
    bar_line_chart_pane.set_uncheck_use_zero_baseline()
    bar_line_chart_pane.set_check_use_uniform_scale()
    bar_line_chart_pane.expand_windowshade_bar_axis()
    bar_line_chart_pane.set_option_for_display_label_for_bar_axis(item_index=4)
    bar_line_chart_pane.set_text_for_first_label_for_bar_axis("条标签")
    bar_line_chart_pane.set_check_for_create_reference_line_for_bar_axis()
    bar_line_chart_pane.set_reference_value_bar_axis("1000")
    bar_line_chart_pane.set_radio_reference_label_bar_axis(item_index=1)
    bar_line_chart_pane.set_text_for_second_label_for_bar_axis("条参考线标签")
    bar_line_chart_pane.expand_windowshade_line_axis()
    bar_line_chart_pane.set_option_for_display_label_for_line_axis(item_index=5)
    bar_line_chart_pane.set_text_for_first_label_for_line_axis("线条标签")
    bar_line_chart_pane.set_check_for_create_reference_line_for_line_axis()
    bar_line_chart_pane.set_reference_value_Line_axis("500")
    bar_line_chart_pane.set_radio_reference_label_line_axis(item_index=1)
    bar_line_chart_pane.set_text_for_second_label_for_line_axis("线条参考线标签")

    bar_line_chart_pane.expand_windowshade_legend()
    bar_line_chart_pane.set_legend_location(item_index=1)
    bar_line_chart_pane.expand_windowshade_title_footnote()
    bar_line_chart_pane.set_title("标题")
    bar_line_chart_pane.set_footnote("注脚")
    bar_line_chart_pane.expand_windowshade_graph_size()
    bar_line_chart_pane.set_units(item_index=2)
    bar_line_chart_pane.set_width("800")
    bar_line_chart_pane.set_height("600")

    flow.run(True)

def test_05_bar_line_chart_in_flow(page, init):
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
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "BASEBALL'中文测试")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_BAR_LINE_CHART]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("BASEBALL'中文测试", Helper.data_locale.STEP_BAR_LINE_CHART)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BAR_LINE_CHART)
    bar_line_chart_pane = BarLineChartPane(page)
    bar_line_chart_pane.expand_windowshade_data()
    time.sleep(1)

    bar_line_chart_pane.expand_windowshade_roles()
    bar_line_chart_pane.set_filter("UPPER('Division''中'n) = '东部'")
    bar_line_chart_pane.expand_windowshade_roles()
    bar_line_chart_pane.add_column_for_category("Team'中文")
    bar_line_chart_pane.add_column_for_bar_variable("nAtBat'中")
    bar_line_chart_pane.set_statistics_bar(item_index=1)
    bar_line_chart_pane.add_column_for_line_variable("nHits'中")
    bar_line_chart_pane.set_statistics_line(item_index=1)

    bar_line_chart_pane.expand_windowshade_additional_roles()
    bar_line_chart_pane.add_column_for_group_analysis_by("League'中")
    bar_line_chart_pane.add_column_for_weight("nHome'中")

    bar_line_chart_pane.click_appearance_tab()
    bar_line_chart_pane.expand_windowshade_bars()
    bar_line_chart_pane.set_check_show_labels_bar()
    bar_line_chart_pane.set_check_set_color_bar()
    bar_line_chart_pane.set_color_transparency_bar(item_index=2)
    bar_line_chart_pane.expand_windowshade_details_bar()
    bar_line_chart_pane.set_check_apply_color_gradient()
    bar_line_chart_pane.set_effect(item_index=4)
    bar_line_chart_pane.add_column_for_url_variable_bar("Position'中")

    bar_line_chart_pane.expand_windowshade_lines()
    bar_line_chart_pane.set_check_show_labels_line()
    bar_line_chart_pane.set_check_set_color_line()
    bar_line_chart_pane.set_thickness_default("3")
    bar_line_chart_pane.set_color_transparency_line(item_index=3)
    bar_line_chart_pane.expand_windowshade_details_line()
    bar_line_chart_pane.set_line_style(item_index=3)
    bar_line_chart_pane.add_column_for_url_variable_line("Team'中文")

    bar_line_chart_pane.expand_windowshade_x_axis()
    bar_line_chart_pane.set_check_reverse_tick_values()
    bar_line_chart_pane.set_check_show_tick_values_in_data_order()
    bar_line_chart_pane.set_option_for_display_label_for_x_axis(item_index=1)
    bar_line_chart_pane.set_check_rotate_values_in_case_of_tick_collisions()
    bar_line_chart_pane.set_check_for_create_reference_line_for_x_axis()
    bar_line_chart_pane.set_reference_values_x_axis(item_index=6)
    bar_line_chart_pane.set_line_offset(item_index=4)
    bar_line_chart_pane.set_radio_reference_label_x_axis(item_index=0)

    bar_line_chart_pane.expand_windowshade_y_axis()
    bar_line_chart_pane.set_check_use_uniform_scale()
    bar_line_chart_pane.expand_windowshade_bar_axis()
    bar_line_chart_pane.set_option_for_display_label_for_bar_axis(item_index=2)
    bar_line_chart_pane.set_check_for_create_reference_line_for_bar_axis()
    bar_line_chart_pane.set_reference_value_bar_axis("1000")
    bar_line_chart_pane.set_radio_reference_label_bar_axis(item_index=0)

    bar_line_chart_pane.expand_windowshade_line_axis()
    bar_line_chart_pane.set_option_for_display_label_for_line_axis(item_index=4)
    bar_line_chart_pane.set_check_for_create_reference_line_for_line_axis()
    bar_line_chart_pane.set_reference_value_Line_axis("500")
    bar_line_chart_pane.set_radio_reference_label_line_axis(item_index=0)

    flow.run(True)
