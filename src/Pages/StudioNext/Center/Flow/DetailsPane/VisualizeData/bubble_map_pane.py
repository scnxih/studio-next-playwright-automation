"""
@author: Liu Jia
@date: 2024/08/20
@description: Define bubble map pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class BubbleMapPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def set_choropleth_map_layer(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_CHOROPLETH_MAP_LAYER)
    def set_filter_map_data(self,filter_text:str):
        self.click_Tab(Helper.data_locale.DATA)
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_MAP_DATA, input_text=filter_text)
    def add_column_for_ID_variable_Map_data(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, column_name=column_name,section_label=Helper.data_locale.MAP_DATA)

    def set_response_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_RESPONSE_DATA)

    def set_filter_map_resopnse_data(self,filter_text:str):
        self.click_Tab(Helper.data_locale.DATA)
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_MAP_RESPONSE_DATA, input_text=filter_text)

    def add_column_for_response_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.RESPONSE_VARIABLE, column_name=column_name,section_label=Helper.data_locale.MAP_RESPONSE_DATA)
    def add_column_for_ID_variable_Map_response_data(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, column_name=column_name,section_label=Helper.data_locale.MAP_RESPONSE_DATA)

    def set_Base_map(self,item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.BASE_MAP,item_index=item_index, item_value=item_value)

    """Methods in Options tab"""

    def expand_windowshade_Data_labels(self):
        self.expand_windowshade(parent_label=Helper.data_locale.DATA_LABELS)
    def add_column_for_bubble_label(self):
        self.add_column(parent_label=Helper.data_locale.BUBBLE_LABEL,column_name=column_name,section_label=Helper.data_locale.DATA_LABELS)
    def expand_windowshade_label_options(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LABEL_OPTIONS)
    def set_font_color(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SET_FONT_COLOR)
    def set_font_family(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FONT_FAMILY,
                                     section_label=Helper.data_locale.LABEL_OPTIONS,
                                     item_index=item_index, item_value=item_value)
    def set_font_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FONT_STYLE,
                                     section_label=Helper.data_locale.LABEL_OPTIONS,
                                     item_index=item_index, item_value=item_value)
    def set_font_weight(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FONT_WEIGHT,
                                     section_label=Helper.data_locale.LABEL_OPTIONS,
                                     item_index=item_index, item_value=item_value)
    def set_label_position(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LABEL_POSITION,
                                     section_label=Helper.data_locale.LABEL_OPTIONS,
                                     item_index=item_index, item_value=item_value)
    def set_bubbles_color(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SET_BUBBLES_COLOR)
    def set_number_of_transparency(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TRANSPARENCY_PERCENT, input_text=input_text)
    def expand_windowshade_(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TITLE_AND_FOOTNOTE)