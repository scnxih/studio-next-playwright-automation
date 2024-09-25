"""
@author: Frank (Feng) Jiang
@date: 2024/09/10
@description: define panes of Canonical Correlation step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class CanonicalCorrelationPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def add_columns_for_var_set1(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.VARIABLE_SET_1, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_var_set1(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.VARIABLE_SET_1, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def add_columns_for_var_set2(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.VARIABLE_SET_2, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_var_set2(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.VARIABLE_SET_2, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def set_check_prefix_label_for_var_set1(self):
        self.set_check_for_checkbox(Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_1)

    def set_uncheck_prefix_label_for_var_set1(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_1)

    def set_check_prefix_label_for_var_set2(self):
        self.set_check_for_checkbox(Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_2)

    def set_uncheck_prefix_label_for_var_set2(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_2)

    def input_prefix_for_var_set1(self, prefix: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[1]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.PREFIX, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_1)).fill_text(prefix)

    def empty_prefix_for_var_set1(self):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[1]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.PREFIX, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_1)).clear_text()

    def input_label_for_var_set1(self, label: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[2]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.LABEL, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_1)).fill_text(label)

    def empty_label_for_var_set1(self):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[2]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.LABEL, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_1)).clear_text()

    def input_prefix_for_var_set2(self, prefix: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[1]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.PREFIX, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_2)).fill_text(prefix)

    def empty_prefix_for_var_set2(self):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[1]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.PREFIX, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_2)).clear_text()

    def input_label_for_var_set2(self, label: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[2]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.LABEL, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_2)).fill_text(label)

    def empty_label_for_var_set2(self):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[./../../..//label[contains(text(),'{0}')]/../../../../../"
                                       "preceding-sibling::div[2]//label[contains(text(), '{1}')]]"
                 .format(Helper.data_locale.LABEL, Helper.data_locale.PREFIX_LABEL_FOR_VAR_SET_2)).clear_text()

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_var_to_partial_out(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.VARIABLES_TO_PARTIAL_OUT, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_var_to_partial_out(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,
                                        check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def add_column_for_freq_count(self, col_name: str):
        self.add_column(Helper.data_locale.FREQUENCY_COUNT, column_name=col_name)

    def delete_column_for_freq_count(self):
        self.delete_column(Helper.data_locale.FREQUENCY_COUNT)

    def add_column_for_weight(self, col_name: str):
        self.add_column(Helper.data_locale.WEIGHT, col_name)

    def delete_column_for_weight(self):
        self.delete_column(Helper.data_locale.WEIGHT)

    def add_columns_for_group_analysis_by(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_group_analysis_by(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    """Methods in Options tab"""

    def set_check_canonical_redundancy_stat(self):
        self.set_check_for_checkbox(Helper.data_locale.CANONICAL_REDUNDANCY_STAT)

    def set_uncheck_canonical_redundancy_stat(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CANONICAL_REDUNDANCY_STAT)

    def set_check_specify_num_of_canonical_variates(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_NUM_OF_CANONICAL_VARIATES)

    def set_uncheck_specify_num_of_canonical_variates(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_NUM_OF_CANONICAL_VARIATES)

    def set_check_perform_regression(self):
        self.set_check_for_checkbox(Helper.data_locale.PERFORM_REGRESSION)

    def set_uncheck_perform_regression(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.PERFORM_REGRESSION)

    def set_check_canonical_var_score_plots(self):
        self.set_check_for_checkbox(Helper.data_locale.CANONICAL_VAR_SCORE_PLOTS)

    def set_uncheck_canonical_var_score_plots(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CANONICAL_VAR_SCORE_PLOTS)

    def set_num_of_variates(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_VARIATES, size)

    def increase_num_of_variates(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_VARIATES, times)

    def decrease_num_of_variates(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_VARIATES, times)

    def select_regression_type(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.REGRESSION_TYPE, item_value=item_value)

    def expand_windowshade_regression_stat(self):
        self.expand_windowshade(Helper.data_locale.REGRESSION_STAT)

    def collapse_windowshade_regression_stat(self):
        self.collapse_windowshade(Helper.data_locale.REGRESSION_STAT)

    def set_check_regression_coefficients(self):
        self.set_check_for_checkbox(Helper.data_locale.REGRESSION_COEFFICIENTS)

    def set_uncheck_regression_coefficients(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REGRESSION_COEFFICIENTS)

    def set_check_standardized_regression_coefficients(self):
        self.set_check_for_checkbox(Helper.data_locale.STANDARDIZED_REGRESSION_COEFFICIENTS)

    def set_uncheck_standardized_regression_coefficients(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.STANDARDIZED_REGRESSION_COEFFICIENTS)

    def set_check_standard_error_of_coefficients(self):
        self.set_check_for_checkbox(Helper.data_locale.STANDARD_ERROR_OF_COEFFICIENTS)

    def set_uncheck_standard_error_of_coefficients(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.STANDARD_ERROR_OF_COEFFICIENTS)

    def set_check_t_stat_for_coefficients(self):
        self.set_check_for_checkbox(Helper.data_locale.T_STAT_FOR_COEFFICIENTS)

    def set_uncheck_t_stat_for_coefficients(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.T_STAT_FOR_COEFFICIENTS)

    def set_check_squared_multiple_correlation(self):
        self.set_check_for_checkbox(Helper.data_locale.SQUARED_MULTIPLE_CORRELATION)

    def set_uncheck_squared_multiple_correlation(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SQUARED_MULTIPLE_CORRELATION)

    def expand_windowshade_correlations(self):
        self.expand_windowshade(Helper.data_locale.CORRELATIONS)

    def collapse_windowshade_correlations(self):
        self.collapse_windowshade(Helper.data_locale.CORRELATIONS)

    def set_check_correlations_of_regression_coefficients(self):
        self.set_check_for_checkbox(Helper.data_locale.CORRELATIONS_OF_REGRESSION_COEFFICIENTS)

    def set_uncheck_correlations_of_regression_coefficients(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CORRELATIONS_OF_REGRESSION_COEFFICIENTS)

    def set_check_partial_correlations(self):
        self.set_check_for_checkbox(Helper.data_locale.PARTIAL_CORRELATIONS)

    def set_uncheck_partial_correlations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.PARTIAL_CORRELATIONS)

    def set_check_squared_partial_correlations(self):
        self.set_check_for_checkbox(Helper.data_locale.SQUARED_PARTIAL_CORRELATIONS)

    def set_uncheck_squared_partial_correlations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SQUARED_PARTIAL_CORRELATIONS)

    def set_check_semipartial_correlations(self):
        self.set_check_for_checkbox(Helper.data_locale.SEMIPARTIAL_CORRELATIONS)

    def set_uncheck_semipartial_correlations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SEMIPARTIAL_CORRELATIONS)

    def set_check_squared_semipartial_correlations(self):
        self.set_check_for_checkbox(Helper.data_locale.SQUARED_SEMIPARTIAL_CORRELATIONS)

    def set_uncheck_squared_semipartial_correlations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SQUARED_SEMIPARTIAL_CORRELATIONS)

    def set_num_of_pairwise_plots(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PAIRWISE_PLOTS, size)

    def increase_num_of_pairwise_plots(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PAIRWISE_PLOTS, times)

    def decrease_num_of_pairwise_plots(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PAIRWISE_PLOTS, times)

    """Methods in Output tab"""

    def set_check_create_score_dataset(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_SCORE_DATASET)

    def set_uncheck_create_score_dataset(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_SCORE_DATASET)

    def set_check_create_stat_dataset(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_STAT_DATASET)

    def set_uncheck_create_stat_dataset(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_STAT_DATASET)

    def set_check_replace_existing_output_table_for_score_data(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_SCORE_DATASET)).set_check()

    def set_uncheck_replace_existing_output_table_for_score_data(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_SCORE_DATASET)).set_uncheck()

    def set_check_replace_existing_output_table_for_stat_data(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_STAT_DATASET)).set_check()

    def set_uncheck_replace_existing_output_table_for_stat_data(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_STAT_DATASET)).set_uncheck()
