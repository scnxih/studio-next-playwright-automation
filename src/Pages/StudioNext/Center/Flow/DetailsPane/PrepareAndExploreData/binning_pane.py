"""
@author: Liu Jia
@date: 2025/06/17
@description: Define binning pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class BinningPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def set_filter_link_data(self,filter_text:str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_LINKS_DATA, input_text=filter_text)
    def add_columns_for_interval_inputs_to_bin(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns_exact_label(parent_label=Helper.data_locale.INTERVAL_INPUTS,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_frequency_count(self, check_column_name_list: list = None,
                                               uncheck_column_name_list: list = None):
        self.add_columns_exact_label(parent_label=Helper.data_locale.FREQUENCY_COUNT,
                                     check_column_name_list=check_column_name_list,
                                     uncheck_column_name_list=uncheck_column_name_list)
    """Methods in Options tab"""
    def set_number_of_bins(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_BINS, input_text=input_text)
    def set_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METHOD, item_index=item_index, item_value=item_value)
    def set_winsor_rate(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.WINSOR_RATE, input_text=input_text)

    """Methods in output tab"""
    def set_check_save_binned_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_BINNED_DATA)

    def set_check_save_Scoring_code(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SCORING_CODE)
