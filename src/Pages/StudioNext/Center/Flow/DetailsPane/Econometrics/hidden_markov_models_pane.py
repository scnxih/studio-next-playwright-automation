"""
@author: Frank (Feng) Jiang
@date: 2024/09/12
@description: define panes of Hidden Markov Models step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class HiddenMarkovModelsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def add_columns_for_dependent_vars(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.DEPENDENT_VARS, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_dependent_vars(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.DEPENDENT_VARS, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def add_column_for_time_ID(self, col_name: str):
        self.add_column(Helper.data_locale.TIME_ID, col_name)

    def delete_column_for_time_ID(self):
        self.delete_column(Helper.data_locale.TIME_ID)

    def add_column_for_cross_sectional_ID(self, col_name: str):
        self.add_column(Helper.data_locale.CROSS_SECTIONAL_ID, col_name)

    def delete_column_for_cross_sectional_ID(self):
        self.delete_column(Helper.data_locale.CROSS_SECTIONAL_ID)

    """Methods in Model tab"""

    def select_model_type(self, option: str):
        self.set_option_for_combobox(Helper.data_locale.MODEL_TYPE, option)

    def set_num_of_hidden_states(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_HIDDEN_STATES, size)

    def increase_num_of_hidden_states(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_HIDDEN_STATES, times)

    def decrease_num_of_hidden_states(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_HIDDEN_STATES, times)

    def expand_windowshade_regressors(self):
        self.expand_windowshade(Helper.data_locale.REGRESSORS)

    def collapse_windowshade_regressors(self):
        self.collapse_windowshade(Helper.data_locale.REGRESSORS)

    def add_columns_for_independent_vars(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.INDEPENDENT_VARS, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_independent_vars(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.INDEPENDENT_VARS, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def set_check_add_lags_of_the_dependent_vars(self):
        self.set_check_for_checkbox(Helper.data_locale.ADD_LAGS_OF_THE_INDEPENDENT_VARS)

    def set_uncheck_add_lags_of_the_dependent_vars(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.ADD_LAGS_OF_THE_INDEPENDENT_VARS)

    def set_num_of_lags(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_LAGS, size)

    def increase_num_of_lags(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_LAGS, times)

    def decrease_num_of_lags(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_LAGS, times)

    def set_check_include_intercept_in_model(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_INTERCEPT_IN_MODEL)

    def set_uncheck_include_intercept_in_model(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_INTERCEPT_IN_MODEL)

    def set_check_add_seasonal_dummies_as_regressors(self):
        self.set_check_for_checkbox(Helper.data_locale.ADD_SEASONAL_DUMMIES_AS_REGRESSORS)

    def set_uncheck_add_seasonal_dummies_as_regressors(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.ADD_SEASONAL_DUMMIES_AS_REGRESSORS)

    def set_num_of_seasonal_periods(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_SEASONAL_PERIODS, size)

    def increase_num_of_seasonal_periods(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_SEASONAL_PERIODS, times)

    def decrease_num_of_seasonal_periods(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_SEASONAL_PERIODS, times)

    def set_check_center_seasonal_dummies(self):
        self.set_check_for_checkbox(Helper.data_locale.CENTER_SEASONAL_DUMMIES)

    def set_uncheck_center_seasonal_dummies(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CENTER_SEASONAL_DUMMIES)

    def set_check_add_time_trends_as_regressors(self):
        self.set_check_for_checkbox(Helper.data_locale.ADD_TIME_TRENDS_AS_REGRESSORS)

    def set_uncheck_add_time_trends_as_regressors(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.ADD_TIME_TRENDS_AS_REGRESSORS)

    def select_radio_btn_for_add_time_trends_as_regressors(self, radio_btm_label: str):
        self.click(self.locate_xpath("//div[@role='radiogroup']//label[text()='{0}']".format(radio_btm_label)))

    def set_check_add_lags_of_the_independent_vars(self):
        self.set_check_for_checkbox(Helper.data_locale.ADD_LAGS_OF_THE_INDEPENDENT_VARS)

    def set_uncheck_add_lags_of_the_independent_vars(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.ADD_LAGS_OF_THE_INDEPENDENT_VARS)

    def set_check_include_only_the_lagged_values_of_the_independent_vars(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_ONLY_THE_LAGGED_VALUES_OF_THE_INDEPENDENT_VARS)

    def set_uncheck_include_only_the_lagged_values_of_the_independent_vars(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_ONLY_THE_LAGGED_VALUES_OF_THE_INDEPENDENT_VARS)

    """Methods in Options tab"""

    def expand_windowshade_methods(self):
        self.expand_windowshade(Helper.data_locale.METHODS)

    def collapse_windowshade_methods(self):
        self.collapse_windowshade(Helper.data_locale.METHODS)

    def select_parameter_estimation_method(self, radio_option: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.PARAMETER_EXTIMATION_METHOD,
                                        item_value=radio_option)

    def set_check_estimate_the_nonstationary_markov_chain(self):
        self.set_check_for_checkbox(Helper.data_locale.ESTIMATE_THE_NONSTATIONARY_MARKOV_CHAIN)

    def set_uncheck_estimate_the_nonstationary_markov_chain(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.ESTIMATE_THE_NONSTATIONARY_MARKOV_CHAIN)

    def set_check_random_number_seed(self):
        self.set_check_for_checkbox(Helper.data_locale.RANDOM_NUMBER_SEED)

    def set_uncheck_random_number_seed(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.RANDOM_NUMBER_SEED)

    def input_random_seed(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.RANDOM_SEED, input_text=input_value)

    def empty_random_seed(self):
        self.set_text_for_text_control(Helper.data_locale.RANDOM_SEED, input_text="")

    def expand_windowshade_nonlinear_optimization(self):
        self.expand_windowshade(Helper.data_locale.NONLINEAR_OPTIMIZATION)

    def collapse_windowshade_nonlinear_optimization(self):
        self.collapse_windowshade(Helper.data_locale.NONLINEAR_OPTIMIZATION)

    def select_algorithm(self, radio_option: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.ALGORITHM, item_value=radio_option)

    def set_check_enable_multistart_mode(self):
        self.set_check_for_checkbox(Helper.data_locale.ENABLE_MULTISTART_MODE)

    def set_uncheck_enable_multistart_mode(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.ENABLE_MULTISTART_MODE)

    def input_max_num_of_iterations(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS, input_text=input_value)

    def empty_max_num_of_iterations(self):
        self.set_text_for_text_control(Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS, input_text="")

    def expand_windowshade_initial_values(self):
        self.expand_windowshade(Helper.data_locale.INITIAL_VALUES)

    def collapse_windowshade_initial_values(self):
        self.collapse_windowshade(Helper.data_locale.INITIAL_VALUES)

    def set_check_set_the_initial_values_to_the_param(self):
        self.set_check_for_checkbox(Helper.data_locale.SET_THE_INIT_VALUES_TO_THE_PARAM_ESTIMATES_OF_A_MATCHED_MODEL)

    def set_uncheck_set_the_initial_values_to_the_param(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SET_THE_INIT_VALUES_TO_THE_PARAM_ESTIMATES_OF_A_MATCHED_MODEL)

    def select_procedure(self, radio_option: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_value=radio_option)

    """Methods in Output tab"""

    def set_check_create_scoring_model(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_SCORING_MODEL)

    def set_uncheck_create_scoring_model(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_SCORING_MODEL)

    def set_check_replace_existing_output_table_for_scoring_model(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_SCORING_MODEL)).set_check()

    def set_uncheck_replace_existing_output_table_for_scoring_model(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_SCORING_MODEL)).set_uncheck()

    def set_check_create_parameter_estimates(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_PARAMETER_ESTIMATES)

    def set_uncheck_create_parameter_estimates(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_PARAMETER_ESTIMATES)

    def set_check_replace_existing_output_table_for_parameter_estimates(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_PARAMETER_ESTIMATES)).set_check()

    def set_uncheck_replace_existing_output_table_for_parameter_estimates(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_PARAMETER_ESTIMATES)).set_uncheck()

    def set_check_create_the_covariance_matrix_of_param_estimates_CAS_only(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_THE_COVARIANCE_MATRIX_OF_PARAM_ESTIMATES_CAS_ONLY)

    def set_uncheck_create_the_covariance_matrix_of_param_estimates_CAS_only(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_THE_COVARIANCE_MATRIX_OF_PARAM_ESTIMATES_CAS_ONLY)

    def set_check_create_fit_statistics(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_FIT_STAT)

    def set_uncheck_create_fit_statistics(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_FIT_STAT)

    def set_check_replace_existing_output_table_for_fit_statistics(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_FIT_STAT)).set_check()

    def set_uncheck_replace_existing_output_table_for_fit_statistics(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_FIT_STAT)).set_uncheck()

    def set_check_create_forecasting_results(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_FORECASTING_RESULTS)

    def set_uncheck_create_forecasting_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_FORECASTING_RESULTS)

    def set_check_replace_existing_output_table_for_forecasting_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_FORECASTING_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_forecasting_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_FORECASTING_RESULTS)).set_uncheck()

    def expand_windowshade_forecast_settings(self):
        self.expand_windowshade(Helper.data_locale.FORECAST_SETTINGS)

    def collapse_windowshade_forecast_settings(self):
        self.collapse_windowshade(Helper.data_locale.FORECAST_SETTINGS)

    def set_num_of_periods_to_forecast(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PERIODS_FORECAST, size)

    def increase_num_of_periods_to_forecast(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PERIODS_FORECAST, times)

    def decrease_num_of_periods_to_forecast(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PERIODS_FORECAST, times)

    def select_forecast_confidence_level(self, option: str):
        self.set_option_for_combobox(Helper.data_locale.FORECAST_CONFIDENCE_LEVEL, option)

    def input_custom_confidence_level(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.CUSTOM_CONFIDENCE_LEVEL, input_text=input_value)

    def empty_custom_confidence_level(self):
        self.set_text_for_text_control(Helper.data_locale.CUSTOM_CONFIDENCE_LEVEL, input_text="")

    def set_check_perform_forecasting_after_each_observation(self):
        self.set_check_for_checkbox(Helper.data_locale.PERFORM_FORECASTING_AFTER_EACH_OBSERVATION)

    def set_uncheck_perform_forecasting_after_each_observation(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.PERFORM_FORECASTING_AFTER_EACH_OBSERVATION)

    def set_num_of_periods_to_hold_back(self, size: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PERIODS_TO_HOLD_BACK, size)

    def increase_num_of_periods_to_hold_back(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PERIODS_TO_HOLD_BACK, times)

    def decrease_num_of_periods_to_hold_back(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_PERIODS_TO_HOLD_BACK, times)

    def set_check_create_decoding_results(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_DECODING_RESULTS)

    def set_uncheck_create_decoding_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_DECODING_RESULTS)

    def set_check_replace_existing_output_table_for_decoding_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_DECODING_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_decoding_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_DECODING_RESULTS)).set_uncheck()

    def set_check_create_evaluation_results(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_EVALUATION_RESULTS)

    def set_uncheck_create_evaluation_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_EVALUATION_RESULTS)

    def set_check_replace_existing_output_table_for_evaluation_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_EVALUATION_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_evaluation_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_EVALUATION_RESULTS)).set_uncheck()

    def set_check_create_filtering_results(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_FILTERING_RESULTS)

    def set_uncheck_create_filtering_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_FILTERING_RESULTS)

    def set_check_replace_existing_output_table_for_filtering_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_FILTERING_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_filtering_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_FILTERING_RESULTS)).set_uncheck()

    def set_check_create_smoothing_results(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_SMOOTHING_RESULTS)

    def set_uncheck_create_smoothing_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_SMOOTHING_RESULTS)

    def set_check_replace_existing_output_table_for_smoothing_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_SMOOTHING_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_smoothing_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_SMOOTHING_RESULTS)).set_uncheck()
