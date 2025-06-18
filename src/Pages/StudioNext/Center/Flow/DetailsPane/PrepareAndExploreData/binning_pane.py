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

    def add_columns_for_interval_inputs_to_bin(self, check_column_name_list: list = None,
                                              uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INTERVAL_INPUTS,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.FREQUENCY_COUNT,column_name=column_name)
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
    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_include_variables_from_input(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INCLUDE_VARIABLES_FROM_THE_INPUT_CAS_TABLE,item_index=item_index,item_value=item_value)

    def add_columns_for_include_these_variables(self, check_column_name_list: list = None,
                                               uncheck_column_name_list: list = None):
        self.add_columns_exact_label(parent_label=Helper.data_locale.INCLUDE_THESE_VARIABLES,
                                     check_column_name_list=check_column_name_list,
                                     uncheck_column_name_list=uncheck_column_name_list)
    def set_check_save_Scoring_code(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SCORING_CODE)
    def set_specify_data_to_show(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPECIFY_DATA_TO_SHOW,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_number_of_observations_default(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_OBSERVATIONS, value=input_value)

    def set_number_of_observations_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_OBSERVATIONS,
                                                       times=increment_number)