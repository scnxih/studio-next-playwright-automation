"""
@author: Frank (Feng) Jiang
@date: 2024/08/19
@description: define panes of Scatter Map step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class ScatterMapPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_plot_data(self):
        self.expand_windowshade(Helper.data_locale.PLOT_DATA)

    def collapse_windowshade_plot_data(self):
        self.collapse_windowshade(Helper.data_locale.PLOT_DATA)

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def add_column_for_latitude(self, col_name: str):
        self.add_column(Helper.data_locale.LATITUDE, col_name)

    def add_column_for_longitude(self, col_name: str):
        self.add_column(Helper.data_locale.LONGITUDE, col_name)

    def add_column_for_group(self, col_name: str):
        self.add_column(Helper.data_locale.GROUP, col_name)

    def delete_column_for_latitude(self):
        self.delete_column(Helper.data_locale.LATITUDE)

    def delete_column_for_longitude(self):
        self.delete_column(Helper.data_locale.LONGITUDE)

    def delete_column_for_group(self):
        self.delete_column(Helper.data_locale.GROUP)

    def set_check_include_choropleth_map_layer(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_CHOROPLETH_MAP_LAYER)

    def set_uncheck_include_choropleth_map_layer(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_CHOROPLETH_MAP_LAYER)

    def expand_windowshade_choropleth_map(self):
        self.expand_windowshade(Helper.data_locale.CHOROPLETH_MAP)

    def collapse_windowshade_choropleth_map(self):
        self.collapse_windowshade(Helper.data_locale.CHOROPLETH_MAP)

    def expand_windowshade_map_data(self):
        self.expand_windowshade(Helper.data_locale.MAP_DATA)

    def collapse_windowshade_map_data(self):
        self.collapse_windowshade(Helper.data_locale.MAP_DATA)

    def input_filter_map_data(self, filter_expression: str):
        self.set_text_for_text_control(Helper.data_locale.FILTER_MAP_DATA, input_text=filter_expression)

    def empty_filter_map_data(self):
        self.set_text_for_text_control(Helper.data_locale.FILTER_MAP_DATA, input_text="")

    def add_column_for_ID_in_map_data(self, col_name: str):
        self.add_column(Helper.data_locale.ID_VARIABLE, col_name, section_label=Helper.data_locale.MAP_DATA)

    def delete_column_for_ID_in_map_data(self):
        self.delete_column(Helper.data_locale.ID_VARIABLE, section_label=Helper.data_locale.MAP_DATA)

    def set_check_include_response_data(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_RESPONSE_DATA)

    def set_uncheck_include_response_data(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_RESPONSE_DATA)

    def expand_windowshade_map_response_data(self):
        self.expand_windowshade(Helper.data_locale.MAP_RESPONSE_DATA)

    def collapse_windowshade_map_response_data(self):
        self.collapse_windowshade(Helper.data_locale.MAP_RESPONSE_DATA)

    def input_filter_map_response_data(self, filter_expression: str):
        self.set_text_for_text_control(Helper.data_locale.FILTER_MAP_RESPONSE_DATA, input_text=filter_expression)

    def empty_filter_map_response_data(self):
        self.set_text_for_text_control(Helper.data_locale.FILTER_MAP_RESPONSE_DATA, input_text="")

    def add_column_for_response_variable(self, col_name: str):
        self.add_column(Helper.data_locale.RESPONSE_VARIABLE, col_name)

    def delete_column_for_response_variable(self):
        self.delete_column(Helper.data_locale.RESPONSE_VARIABLE)

    def add_column_for_ID_in_map_response_data(self, col_name: str):
        self.add_column(Helper.data_locale.ID_VARIABLE, col_name, section_label=Helper.data_locale.MAP_RESPONSE_DATA)

    def delete_column_for_ID_in_map_response_data(self):
        self.delete_column(Helper.data_locale.ID_VARIABLE, section_label=Helper.data_locale.MAP_RESPONSE_DATA)

    def set_check_ID_variable(self):
        get_checkbox(self.base_xpath, self.page, supplement_base_xpath="[.//label[contains(text(), '{0}')]]"
                     .format(Helper.data_locale.ID_VARIABLE)).set_check()

    def set_uncheck_ID_variable(self):
        get_checkbox(self.base_xpath, self.page, supplement_base_xpath="[.//label[contains(text(), '{0}')]]"
                     .format(Helper.data_locale.ID_VARIABLE)).set_uncheck()

    def select_radio_base_map(self, item_value: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.BASE_MAP, item_value=item_value)

    def input_Esri_URL(self, esri_url: str):
        self.set_text_for_text_control(Helper.data_locale.SPECIFY_ESRI_BASE_MAP_URL, input_text=esri_url)

    def empty_Esri_URL(self):
        self.set_text_for_text_control(Helper.data_locale.SPECIFY_ESRI_BASE_MAP_URL, input_text="")

    """Methods in Options tab"""

    def expand_windowshade_data_labels(self):
        self.expand_windowshade(Helper.data_locale.DATA_LABELS)

    def collapse_windowshade_data_labels(self):
        self.collapse_windowshade(Helper.data_locale.DATA_LABELS)

    def add_column_for_label_variable(self, col_name: str):
        self.add_column(Helper.data_locale.LABEL_VARIABLE, col_name)

    def delete_column_for_label_variable(self):
        self.delete_column(Helper.data_locale.LABEL_VARIABLE)

    def expand_windowshade_label_options(self):
        self.expand_windowshade(Helper.data_locale.LABEL_OPTIONS)

    def collapse_windowshade_label_options(self):
        self.collapse_windowshade(Helper.data_locale.LABEL_OPTIONS)

    def set_check_set_font_color(self):
        self.set_check_for_checkbox(Helper.data_locale.SET_FONT_COLOR)

    def set_uncheck_set_font_color(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SET_FONT_COLOR)

    def select_font_family(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.FONT_FAMILY, item_value=item_value)

    def input_family(self, family: str):
        self.set_text_for_text_control(Helper.data_locale.FAMILY, input_text=family)

    def empty_family(self):
        self.set_text_for_text_control(Helper.data_locale.FAMILY, input_text="")

    def set_font_size_for_label(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_7_PT, size)

    def increase_font_size_for_label(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_7_PT, times)

    def decrease_font_size_for_label(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_7_PT, times)

    def select_font_style(self, style: str):
        self.set_option_for_combobox(Helper.data_locale.FONT_STYLE, item_value=style)

    def select_font_weight(self, weight: str):
        self.set_option_for_combobox(Helper.data_locale.FONT_WEIGHT, item_value=weight)

    def select_label_position(self, position: str):
        self.set_option_for_combobox(Helper.data_locale.LABEL_POSITION, item_value=position)

    def expand_windowshade_legend(self):
        self.expand_windowshade(Helper.data_locale.LEGEND)

    def collapse_windowshade_legend(self):
        self.collapse_windowshade(Helper.data_locale.LEGEND)

    def set_check_generate_choromap_legend(self):
        self.set_check_for_checkbox(Helper.data_locale.GENERATE_CHOROMAP_LEGEND)

    def set_uncheck_generate_choromap_legend(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.GENERATE_CHOROMAP_LEGEND)

    def input_choromap_legend_label(self, legend_label: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../../../preceding-sibling::div[1]//label[text()='{0}']]"
                 .format(Helper.data_locale.GENERATE_CHOROMAP_LEGEND)).fill_text(legend_label)

    def empty_choromap_legend_label(self):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../../../preceding-sibling::div[1]//label[text()='{0}']]"
                 .format(Helper.data_locale.GENERATE_CHOROMAP_LEGEND)).clear_text()

    def set_check_generate_plot_legend(self):
        self.set_check_for_checkbox(Helper.data_locale.GENERATE_PLOT_LEGEND)

    def set_uncheck_generate_plot_legend(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.GENERATE_PLOT_LEGEND)

    def input_plot_legend_label(self, legend_label: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../../../preceding-sibling::div[1]//label[text()='{0}']]"
                 .format(Helper.data_locale.GENERATE_PLOT_LEGEND)).fill_text(legend_label)

    def empty_plot_legend_label(self):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../../../preceding-sibling::div[1]//label[text()='{0}']]"
                 .format(Helper.data_locale.GENERATE_PLOT_LEGEND)).clear_text()

    def expand_windowshade_markers(self):
        self.expand_windowshade(Helper.data_locale.MARKERS)

    def collapse_windowshade_markers(self):
        self.collapse_windowshade(Helper.data_locale.MARKERS)

    def set_check_for_set_color_in_markers(self):
        self.set_check_for_checkbox(Helper.data_locale.SET_COLOR, section_label=Helper.data_locale.MARKERS)
        """Added by Alice on 2024-09-19 end"""

    def set_uncheck_for_set_color_in_markers(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SET_COLOR, section_label=Helper.data_locale.MARKERS)

    def set_color_for_markers(self, red_value: int, green_value: int, blue_value: int):
        self.set_rgb_for_color_picker(red_value, green_value, blue_value, parent_label=Helper.data_locale.COLOR,
                                      section_label=Helper.data_locale.MARKERS)

    def select_symbol_type(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.SYMBOL, item_value=item_value)

    def set_markers_size(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.SIZE_DEFAULT_7_PIXEL, size)

    def increase_markers_size(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.SIZE_DEFAULT_7_PIXEL, times)

    def decrease_markers_size(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.SIZE_DEFAULT_7_PIXEL, times)

    def expand_windowshade_plot(self):
        self.expand_windowshade(Helper.data_locale.PLOT)

    def collapse_windowshade_plot(self):
        self.collapse_windowshade(Helper.data_locale.PLOT)

    def input_transparency_in_plot(self, transparency: str):
        """
        :param transparency: should be an integer and between 0 and 100.
        :return:
        """
        # get_text(self.base_xpath, self.page, supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]"
        #                                                            "/../../../../../../../..//span[text()='{1}']]".
        #          format(Helper.data_locale.TRANSPARENCY_PERCENT, Helper.data_locale.PLOT)).fill_text(transparency)
        self.set_text_for_text_control(Helper.data_locale.TRANSPARENCY_PERCENT, transparency,
                                       section_label=Helper.data_locale.PLOT)

    def empty_transparency_in_plot(self):
        # get_text(self.base_xpath, self.page, supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]"
        #                                                            "/../../../../../../../..//span[text()='{1}']]".
        #          format(Helper.data_locale.TRANSPARENCY_PERCENT, Helper.data_locale.PLOT)).fill_text("")
        self.set_text_for_text_control(Helper.data_locale.TRANSPARENCY_PERCENT, "",
                                       section_label=Helper.data_locale.PLOT)

    def expand_windowshade_choromap(self):
        self.expand_windowshade(Helper.data_locale.CHOROMAP)

    def collapse_windowshade_choromap(self):
        self.collapse_windowshade(Helper.data_locale.CHOROMAP)

    def expand_windowshade_line_attr(self):
        self.expand_windowshade(Helper.data_locale.LINE_ATTRIBUTES)

    def collapse_windowshade_line_attr(self):
        self.collapse_windowshade(Helper.data_locale.LINE_ATTRIBUTES)

    def set_check_for_set_color_in_line_attr(self):
        # get_checkbox(self.base_xpath, self.page,
        #              supplement_base_xpath="[.//label[text()='{0}']/../../../../../../../..//span[text()='{1}']]"
        #              .format(Helper.data_locale.SET_COLOR, Helper.data_locale.LINE_ATTRIBUTES)).set_check()
        self.set_check_for_checkbox(Helper.data_locale.SET_COLOR, section_label=Helper.data_locale.LINE_ATTRIBUTES)

    def set_uncheck_for_set_color_in_line_attr(self):
        # get_checkbox(self.base_xpath, self.page,
        #              supplement_base_xpath="[.//label[text()='{0}']/../../../../../../../..//span[text()='{1}']]"
        #              .format(Helper.data_locale.SET_COLOR, Helper.data_locale.LINE_ATTRIBUTES)).set_uncheck()
        self.set_uncheck_for_checkbox(Helper.data_locale.SET_COLOR, section_label=Helper.data_locale.LINE_ATTRIBUTES)

    def set_color_for_line_attr(self, red_value, green_value, blue_value):
        self.set_rgb_for_color_picker(red_value, green_value, blue_value, parent_label=Helper.data_locale.COLOR,
                                      section_label=Helper.data_locale.LINE_ATTRIBUTES)

    def set_line_thickness(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.LINE_THICKNESS, size)

    def increase_line_thickness(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.LINE_THICKNESS, times)

    def decrease_line_thickness(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.LINE_THICKNESS, times)

    def select_line_style(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.LINE_STYLE, item_value=item_value)

    def input_transparency_in_choromap(self, transparency: str):
        """
        :param transparency: should be an integer and between 0 and 100.
        :return:
        """
        # get_text(self.base_xpath, self.page, supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]"
        #                                                            "/../../../../../../../..//span[text()='{1}']]".
        #          format(Helper.data_locale.TRANSPARENCY_PERCENT, Helper.data_locale.CHOROMAP)).fill_text(transparency)
        self.set_text_for_text_control(Helper.data_locale.TRANSPARENCY_PERCENT, transparency,
                                       section_label=Helper.data_locale.CHOROMAP)

    def empty_transparency_in_choromap(self):
        # get_text(self.base_xpath, self.page, supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]"
        #                                                            "/../../../../../../../..//span[text()='{1}']]".
        #          format(Helper.data_locale.TRANSPARENCY_PERCENT, Helper.data_locale.CHOROMAP)).fill_text("")
        self.set_text_for_text_control(Helper.data_locale.TRANSPARENCY_PERCENT, "",
                                       section_label=Helper.data_locale.CHOROMAP)

    def expand_windowshade_title_and_footnote(self):
        self.expand_windowshade(Helper.data_locale.TITLE_AND_FOOTNOTE)

    def collapse_windowshade_title_and_footnote(self):
        self.collapse_windowshade(Helper.data_locale.TITLE_AND_FOOTNOTE)

    def input_title(self, title: str):
        self.set_text_for_text_control(Helper.data_locale.TITLE, title)

    def empty_title(self):
        self.set_text_for_text_control(Helper.data_locale.TITLE, "")

    def set_font_size_for_title(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_14_PT, size)

    def increase_font_size_for_title(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_14_PT, times)

    def decrease_font_size_for_title(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_14_PT, times)

    def input_footnote(self, footnote: str):
        self.set_text_for_text_control(Helper.data_locale.FOOTNOTE, footnote)

    def empty_footnote(self):
        self.set_text_for_text_control(Helper.data_locale.FOOTNOTE, "")

    def set_font_size_for_footnote(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_12_PT, size)

    def increase_font_size_for_footnote(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_12_PT, times)

    def decrease_font_size_for_footnote(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.FONT_SIZE_DEFAULT_12_PT, times)

    def expand_windowshade_graph_size(self):
        self.expand_windowshade(Helper.data_locale.GRAPH_SIZE)

    def collapse_windowshade_graph_size(self):
        self.collapse_windowshade(Helper.data_locale.GRAPH_SIZE)

    def select_units(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.UNITS, item_value=item_value)

    def set_plot_width(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.WIDTH, size)

    def increase_plot_width(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.WIDTH, times)

    def decrease_plot_width(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.WIDTH, times)

    def set_plot_height(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.HEIGHT, size)

    def increase_plot_height(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.HEIGHT, times)

    def decrease_plot_height(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.HEIGHT, times)

    """Added by Alice on 2024-09-19 start"""
    def set_rgb_for_color_in_marker(self, red_value: int, green_value: int, blue_value: int):
        self.set_rgb_for_color_picker(red_value=red_value,green_value=green_value,blue_value=blue_value,parent_label="颜色",section_label="标记")

    """Added by Alice on 2024-09-19 end"""