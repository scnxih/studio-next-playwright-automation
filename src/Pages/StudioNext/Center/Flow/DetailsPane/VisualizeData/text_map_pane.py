"""
@author: Dommy (Fuying) Chen
@date: 2024/09/11
@description: define panes of Text Map step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class TextMapPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_plot_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PLOT_DATA)

    def collapse_windowshade_plot_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PLOT_DATA)

    def add_column_for_latitude(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LATITUDE, column_name=column_name)

    def add_column_for_longitude(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LONGITUDE, column_name=column_name)

    def add_column_for_text(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.TEXT, column_name=column_name)

    def set_check_include_choropleth_map_layer(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_CHOROPLETH_MAP_LAYER)

    def set_uncheck_include_choropleth_map_layer(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.INCLUDE_CHOROPLETH_MAP_LAYER)

    def expand_windowshade_choropleth_map(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CHOROPLETH_MAP)

    def collapse_windowshade_choropleth_map(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.CHOROPLETH_MAP)

    def expand_windowshade_map_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.MAP_DATA)

    def collapse_windowshade_map_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.MAP_DATA)

    def set_filter_map_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_MAP_DATA, input_text=filter_text)

    def add_column_for_id_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, column_name=column_name)

    def set_check_include_response_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_RESPONSE_DATA)

    def set_uncheck_include_response_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.INCLUDE_RESPONSE_DATA)

    def expand_windowshade_map_response_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.MAP_RESPONSE_DATA)

    def collapse_windowshade_map_response_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.MAP_RESPONSE_DATA)

    def set_filter_map_response_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_MAP_RESPONSE_DATA, input_text=filter_text)

    def add_column_for_response_id_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, section_label=Helper.data_locale.MAP_RESPONSE_DATA,
                        column_name=column_name)

    def set_check_id_variable(self):
        get_checkbox(self.base_xpath, self.page, supplement_base_xpath="[.//label[contains(text(), '{0}')]]"
                     .format(Helper.data_locale.ID_VARIABLE)).set_check()

    def set_uncheck_id_variable(self):
        get_checkbox(self.base_xpath, self.page, supplement_base_xpath="[.//label[contains(text(), '{0}')]]"
                     .format(Helper.data_locale.ID_VARIABLE)).set_uncheck()

    def set_base_map(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.BASE_MAP, item_index=item_index,
                                        item_value=item_value)

    def input_esri_base_map_URL(self, esri_url: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.SPECIFY_ESRI_BASE_MAP_URL, input_text=esri_url)

    """Below methods are in Options tab"""

    def expand_windowshade_text(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TEXT)

    def set_check_specify_predefined_style(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_PREDEFINED_STYLE)

    def set_uncheck_specify_predefined_style(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_PREDEFINED_STYLE)

    def set_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STYLE, item_index=item_index,
                                     item_value=item_value)

    def set_check_specify_text_options(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_TEXT_OPTIONS)

    def set_uncheck_specify__text_options(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_TEXT_OPTIONS)

    def set_check_set_font_color(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SET_FONT_COLOR)

    def set_uncheck_set_font_color(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SET_FONT_COLOR)

    def set_font_family(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FONT_FAMILY, item_index=item_index,
                                     item_value=item_value)

    def set_font_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FONT_STYLE, item_index=item_index,
                                     item_value=item_value)

    def set_font_weight(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FONT_WEIGHT, item_index=item_index,
                                     item_value=item_value)

    def set_label_position(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LABEL_POSITION, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_choromap(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CHOROMAP)

    def expand_windowshade_line_attributes(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LINE_ATTRIBUTES)

    def set_check_set_color(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SET_COLOR)

    def set_uncheck_set_color(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SET_COLOR)

    def set_line_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_title_footnote(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TITLE_AND_FOOTNOTE)

    def collapse_windowshade_title_footnote(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TITLE_AND_FOOTNOTE)

    def set_title(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TITLE, input_text=input_text)

    def set_footnote(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FOOTNOTE, input_text=input_text)

    def expand_windowshade_graph_size(self):
        self.expand_windowshade(parent_label=Helper.data_locale.GRAPH_SIZE)

    def collapse_windowshade_graph_size(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.GRAPH_SIZE)

    def set_units(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.UNITS, item_index=item_index,
                                 item_value=item_value)
