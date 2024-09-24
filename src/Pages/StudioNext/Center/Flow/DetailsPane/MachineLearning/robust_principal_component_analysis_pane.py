"""
@author: Dommy (Fuying) Chen
@date: 2024/09/19
@description: define panes of Robust Principal Component Analysis step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class RobustPrincipalComponentAnalysis(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_input_variables(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INPUT_VARIABLES, item_index=item_index,
                                        item_value=item_value)

    def add_columns_for_interval_inputs(self, check_column_name_list: list = None,
                                        uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INTERVAL_INPUTS,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_column_for_id_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ID_VARIABLE, column_name=column_name)

    """Methods in Options tab"""

    def set_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox_exact_label(parent_label=Helper.data_locale.METHOD_WITH_COLON, item_index=item_index,
                                     item_value=item_value)

    def set_lambda(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox_exact_label(parent_label=Helper.data_locale.LAMBDA_WITH_COLON, item_index=item_index,
                                     item_value=item_value)

    def set_custom_lambda_value(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.CUSTOM_LAMBDA_VALUE, input_text=filter_text)

    def set_lambda_weight(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox_exact_label(parent_label=Helper.data_locale.LAMBDA_WEIGHT_WITH_COLON, item_index=item_index,
                                     item_value=item_value)

    def set_custom_lambda_weight_value(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.CUSTOM_LAMBDA_WEIGHT_VALUE,
                                       input_text=filter_text)

    def set_maximum_iterations(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_ITERATIONS, value=input_value)

    def set_maximum_iterations_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_ITERATIONS,
                                                       times=increment_number)

    def set_maximum_iterations_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_ITERATIONS,
                                                       times=decrement_number)

    def set_tolerance(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TOLERANCE, input_text=filter_text)

    def set_check_scale_observations(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SCALE_OBSERVATIONS)

    def set_uncheck_scale_observations(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.EACH_DOCUMENT)

    def set_check_center_observations(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CENTER_OBSERVATIONS)

    def set_uncheck_center_observations(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CENTER_OBSERVATIONS)

    def set_initial_mu(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.INITIAL_MU,
                                       input_text=input_value)

    def set_check_use_fixed_value_for_mu(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_FIXED_VALUE_FOR_MU)

    def set_uncheck_use_fixed_value_for_mu(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_FIXED_VALUE_FOR_MU)

    def expand_windowshade_singular_value_decomposition_options(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SINGULAR_VALUE_DECOMPOSITION_OPTIONS)

    def collapse_windowshade_singular_value_decomposition_options(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.SINGULAR_VALUE_DECOMPOSITION_OPTIONS)

    def set_svd_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox_exact_label(parent_label=Helper.data_locale.SVD_METHOD_WITH_COLON, item_index=item_index,
                                     item_value=item_value)

    def set_maximum_rank(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_RANK, value=input_value)

    def set_maximum_rank_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_RANK,
                                                       times=increment_number)

    def set_maximum_rank_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_RANK,
                                                       times=decrement_number)

    def set_power(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.POWER, value=input_value)

    def set_power_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.POWER,
                                                       times=increment_number)

    def set_power_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.POWER,
                                                       times=decrement_number)

    """Methods in Output tab"""

    def set_check_save_low_rank_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_LOW_RANK_DATA)

    def set_uncheck_save_low_rank_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_LOW_RANK_DATA)

    def set_check_save_sparse_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SPARSE_DATA)

    def set_uncheck_save_sparse_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_SPARSE_DATA)

    def set_check_save_error_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_ERROR_DATA)

    def set_uncheck_save_error_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_ERROR_DATA)

    def set_check_save_scoring_code(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SCORING_CODE)

    def set_uncheck_save_scoring_code(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_SCORING_CODE)

    def set_decomposition_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DECOMPOSITION_METHOD, item_index=item_index,
                                     item_value=item_value)

    def set_check_save_left_singular_vectors_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_LEFT_SINGULAR_VECTORS_DATA)

    def set_uncheck_save_left_singular_vectors_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_LEFT_SINGULAR_VECTORS_DATA)

    def set_check_save_singular_values_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SINGULAR_VALUES_DATA)

    def set_uncheck_save_singular_values_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_SINGULAR_VALUES_DATA)

    def set_check_save_right_singular_vectors_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_RIGHT_SINGULAR_VECTORS_DATA)

    def set_uncheck_save_right_singular_vectors_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_RIGHT_SINGULAR_VECTORS_DATA)

    def set_check_save_component_loadings_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_COMPONENT_LOADINGS_DATA)

    def set_uncheck_save_component_loadings_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_COMPONENT_LOADINGS_DATA)

    def set_check_save_pc_scores_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_PC_SCORES_DATA)

    def set_uncheck_save_pc_scores_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_PC_SCORES_DATA)
