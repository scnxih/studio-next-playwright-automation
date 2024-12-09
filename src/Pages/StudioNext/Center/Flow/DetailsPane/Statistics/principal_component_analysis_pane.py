"""
@author: Frank (Feng) Jiang
@date: 2024/10/16
@description: define panes of Principal Component Analysis step
"""

from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class PrincipalComponentAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def select_server(self, server: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP, item_value=server)

    def expand_windowshade_note_about_server_selection(self):
        self.expand_windowshade(Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def collapse_windowshade_note_about_server_selection(self):
        self.collapse_windowshade(Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def add_columns_for_interval_inputs(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.INTERVAL_INPUTS, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_interval_inputs(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.INTERVAL_INPUTS, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_inputs_to_partial_out(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.INPUTS_TO_PARTIAL_OUT, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_inputs_to_partial_out(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.INPUTS_TO_PARTIAL_OUT, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def add_column_for_freq_count(self, col_name: str):
        self.add_column(Helper.data_locale.FREQUENCY_COUNT, col_name)

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

    def select_num_of_components(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.NUM_OF_COMPONENTS, item_value=item_value)

    def set_custom_value(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.CUSTOM_VALUE, size)

    def increase_custom_value(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.CUSTOM_VALUE, times)

    def decrease_custom_value(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.CUSTOM_VALUE, times)

    def select_method(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.METHOD, item_value=item_value)

    def select_analyze(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.ANALYZE, item_value=item_value)

    def set_check_correct_the_covariances_or_correlations_for_the_means(self):
        self.set_check_for_checkbox(Helper.data_locale.CORRECT_THE_COVARIANCES_OR_CORRELATIONS_FOR_THE_MEANS)

    def set_uncheck_correct_the_covariances_or_correlations_for_the_means(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CORRECT_THE_COVARIANCES_OR_CORRELATIONS_FOR_THE_MEANS)

    def select_standardize_variance_of_scores(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.STANDARDIZE_VARIANCE_OF_SCORES, item_value=item_value)

    def set_check_specify_the_max_num_of_iterations(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_THE_MAX_NUM_OF_ITERATIONS)

    def set_uncheck_specify_the_max_num_of_iterations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_THE_MAX_NUM_OF_ITERATIONS)

    def input_iterations(self, iterations: str):
        self.set_text_for_text_control(Helper.data_locale.ITERATIONS, iterations)

    def empty_iterations(self):
        self.set_text_for_text_control(Helper.data_locale.ITERATIONS, "")

    def set_check_specify_a_prefix_to_label_the_components(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_A_PREFIX_TO_LABEL_THE_COMPONENTS)

    def set_uncheck_specify_a_prefix_to_label_the_components(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_A_PREFIX_TO_LABEL_THE_COMPONENTS)

    def input_component_prefix(self, prefix: str):
        self.set_text_for_text_control(Helper.data_locale.COMPONENT_PREFIX, prefix)

    def empty_component_prefix(self):
        self.set_text_for_text_control(Helper.data_locale.COMPONENT_PREFIX, "")

    def select_plot_to_display(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.SELECT_PLOTS_TO_DISPLAY, item_value=item_value)

    def set_check_eigenvalue_by_component(self):
        self.set_check_for_checkbox(Helper.data_locale.EIGENVALUE_BY_COMPONENT)

    def set_uncheck_eigenvalue_by_component(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.EIGENVALUE_BY_COMPONENT)

    def set_check_component_pattern_profiles(self):
        self.set_check_for_checkbox(Helper.data_locale.COMPONENT_PATTERN_PROFILES)

    def set_uncheck_component_pattern_profiles(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.COMPONENT_PATTERN_PROFILES)

    """Methods in Output tab"""

    def set_check_save_component_scores(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_COMPONENT_SCORES)

    def set_uncheck_save_component_scores(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_COMPONENT_SCORES)

    def set_check_replace_existing_output_table_for_save_component_scores(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_COMPONENT_SCORES)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_component_scores(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_COMPONENT_SCORES)).set_uncheck()

    def set_check_save_statistics(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_STATISTICS)

    def set_uncheck_save_statistics(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_STATISTICS)

    def set_check_replace_existing_output_table_for_save_statistics(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_STATISTICS)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_statistics(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_STATISTICS)).set_uncheck()

    def set_include_vars_from_the_input_CAS_table(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INCLUDE_VARIABLES_FROM_THE_INPUT_CAS_TABLE,
                                        item_value=radio_btn_label)

    def add_columns_for_include_these_vars(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.INCLUDE_THESE_VARIABLES, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_include_these_vars(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.INCLUDE_THESE_VARIABLES, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)
