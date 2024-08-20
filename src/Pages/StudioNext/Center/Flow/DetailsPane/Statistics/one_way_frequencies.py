"""
@File: one-way_frequencies
@Author: Allison
@Date: 8/19/2024 3:14 AM 
@Description: 

"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class OneWayFrequencies(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

        """Data tab"""

    def add_columns_for_analysis_variables(self, check_column_name_list: list = None,
                                           uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ANALYSIS_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    """Options tab"""

    def set_check_frequency_table(self):
        self.set_check_for_checkbox(Helper.data_locale.FREQUENCY_TABLE)

    def set_uncheck_frequency_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.FREQUENCY_TABLE)

    def set_check_include_percentages(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_PERCENTAGES)

    def set_uncheck_include_percentages(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_PERCENTAGES)

    def set_check_include_cumulative_frequencies_and_percentages(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_CUMULATIVE_FREQUENCIES_AND_PERCENTAGES)

    def set_uncheck_include_cumulative_frequencies_and_percentages(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_CUMULATIVE_FREQUENCIES_AND_PERCENTAGES)

    def set_row_value_order(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.ROW_VALUE_ORDER, item_index=item_index, item_value=item_value)

    def expand_windowshade_statistics(self):
        self.expand_windowshade(parent_label=Helper.data_locale.STATISTICS)

    def collapse_windowshade_statistics(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.STATISTICS)

    def set_null_hypothesis_proportion(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NULL_HYPOTHESIS_PROPORTION, input_text=input_text)

    def set_confidence_level(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.CONFIDENCE_LEVEL, item_index=item_index, item_value=item_value)

    def set_custom_confidence_level(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.CUSTOM_CONFIDENCE_LEVEL, input_text=input_text)

    def set_check_asymptotic_test_for_binomial_proportion(self):
        self.set_check_for_checkbox(Helper.data_locale.ASYMPTOTIC_TEST)

    def set_uncheck_asymptotic_test_for_binomial_proportion(self):
        self.set_check_for_checkbox(Helper.data_locale.ASYMPTOTIC_TEST)

    def set_check_use_monte_carlo_estimation(self):
        self.set_check_for_checkbox(Helper.data_locale.USE_MONTE_CARLO_ESTIMATION)

    def set_uncheck_use_monte_carlo_estimation(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.USE_MONTE_CARLO_ESTIMATION)

    def expand_windowshade_plots_and_missing_values(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PLOTS_AND_MISSING_VALUES)

    def collapse_windowshade_plots_and_missing_values(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PLOTS_AND_MISSING_VALUES)

    def set_check_suppress_plots(self):
        self.set_check_for_checkbox(Helper.data_locale.SUPPRESS_PLOTS)

    def set_uncheck_suppress_plots(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SUPPRESS_PLOTS)

    def set_check_include_in_frequency_table(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_IN_FREQUENCY_TABLE)

    def set_uncheck_include_in_frequency_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_IN_FREQUENCY_TABLE)

    def set_check_include_in_percentages_and_statistics(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_IN_PERCENTAGES_AND_STATISTICS)

    def set_uncheck_include_in_percentages_and_statistics(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_IN_PERCENTAGES_AND_STATISTICS)