"""
@author: Liu Jia
@date: 2024/09/29
@description: Define Factor Analysis pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class FactorAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_columns_for_analysis_variables(self, check_column_name_list: list = None,
                                           uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ANALYSIS_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def unexpand_windowshade_additional_roles(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_variables_partial_out(self, check_column_name_list: list = None,
                                              uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)

    def add_column_frequency_count(self, parent_label: str, column_name: str, section_label: str = None):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)

    def add_column_weight(self, parent_label: str, column_name: str, section_label: str = None):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,check_column_name_list=check_column_name_list, uncheck_column_name_list=uncheck_column_name_list)

    """Methods in Option tab"""
    def expand_windowshade_factor_extraction(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.FACTOR_EXTRACTION)
    def unexpand_windowshade_factor_extraction(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.FACTOR_EXTRACTION)
    def set_check_show_only_common_extraction_methods(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_ONLY_COMMON_EXTRACTION_METHODS)
    def set_uncheck_show_only_common_extraction_methods(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_ONLY_COMMON_EXTRACTION_METHODS)
    def set_select_factor_extraction_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FACTOR_EXTRACTION_METHOD, item_index=item_index,item_value=item_value)
    def set_select_number_of_factors(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.NUMBER_OF_FACTORS, item_index=item_index,item_value=item_value)
    def set_value_for_custom_number_of_factors(self, value:str = None):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.CUSTOM_NUMBER_OF_FACTORS,value=value)


