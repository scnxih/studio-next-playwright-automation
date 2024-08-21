"""
@File: standardize_data
@Author: Allison
@Date: 8/21/2024 3:27 AM 
@Description: 

"""
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class StandardizeData(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

        """Data tab"""

    def add_columns_for_variables_to_standardize(self, check_column_name_list: list = None,
                                                 uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.VARIABLES_TO_STANDARDIZE,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)

    def add_column_for_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

        """Options tab"""

    def set_check_center_data_only(self):
        self.set_check_for_checkbox(Helper.data_locale.CENTER_DATA_ONLY)

    def set_uncheck_center_data_only(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CENTER_DATA_ONLY)

    def set_centering_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.CENTERING_METHOD, item_index=item_index,
                                     item_value=item_value)

    def set_standardization_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STANDARDIZATION_METHOD, item_index=item_index,
                                     item_value=item_value)

    def set_tuning_constant(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TUNING_CONSTANT, input_text=input_text)

    def set_lambda(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LAMBDA, input_text=input_text)

    def set_proportion_of_paris(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PROPORTION_OF_PAIRS, input_text=input_text)

    def set_proportion_of_data(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PROPORTION_OF_DATA, input_text=input_text)

    def set_missing_values_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MISSING_VALUES_METHODS, item_index=item_index,
                                     item_value=item_value)
