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
        self.set_check_for_checkbox(label=Helper.data_locale.Choropleth_MAP_LAYER)
    def set_filter_map_data(self,filter_text:str):
        self.click_Tab(Helper.data_locale.DATA)
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_MAP_DATA, input_text=filter_text)
    def add_column_for_ID_variable_Map_data(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, column_name=column_name,section_label=Helper.data_locale.MAP_DATA)
    def add_column_for_ID_variable_Map_response_data(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, column_name=column_name,section_label=Helper.data_locale.MAP_RESPONSE_DATA)
    def set_Base_map_(self,item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.BASE_MAP,item_index=item_index, item_value=item_value)



