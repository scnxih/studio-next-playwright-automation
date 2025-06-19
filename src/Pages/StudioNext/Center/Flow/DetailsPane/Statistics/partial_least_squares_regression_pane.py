"""
@author: Dommy (Fuying) Chen
@date: 2025/06/19
@description: define panes of Partial Least Squares Regression step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class PartialLeastSquaresRegressionPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_select_a_server_for_this_step(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_note_about_server_selection(self):
        self.expand_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def collapse_windowshade_note_about_server_selection(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def set_filter_input_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_INPUT_DATA, input_text=filter_text)

    def add_columns_for_dependent_variables(self, check_column_name_list: list = None,
                                            uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.DEPENDENT_VARS,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_explanatory_variables(self):
        self.expand_windowshade(parent_label=Helper.data_locale.EXPLANATORY_VARIABLES)

    def collapse_windowshade_explanatory_variables(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.EXPLANATORY_VARIABLES)

    def add_columns_for_continuous_variables(self, check_column_name_list: list = None,
                                             uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.CONTINUOUS_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_Classification_variables(self, check_column_name_list: list = None,
                                                 uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.CLASSIFICATION_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_treament_of_missing_values(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TREATMENT_OF_MISSING_VALUES)

    def collapse_windowshade_explanatory_variables(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TREATMENT_OF_MISSING_VALUES)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_partition_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PARTITION_DATA)

    def collapse_windowshade_partition_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PARTITION_DATA)

    def expand_windowshade_input_data_contains_training_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.INPUT_DATA_CONTAINS_TRAINING_DATA)

    def collapse_windowshade_input_data_contains_training_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.INPUT_DATA_CONTAINS_TRAINING_DATA)

    def set_check_include_test_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_TEST_DATA)

    def set_uncheck_include_test_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.INCLUDE_TEST_DATA)

    def set_indentify_partitions(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.IDENTIFY_PARTITIONS,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_proportion_of_testing_cases(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.PROPORTION_OF_TESTING_DATA,
                                           value=input_value)

    def set_check_random_number_seed(self):
        self.set_check_for_checkbox(label=Helper.data_locale.RANDOM_NUMBER_SEED)

    def set_uncheck_random_number_seed(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.RANDOM_NUMBER_SEED)

    def set_random_seed(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.RANDOM_SEED, value=input_value)

    """Methods in Model tab"""

    def set_model_type(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.MODEL_TYPE,
                                        item_index=item_index, item_value=item_value)

    def set_n(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.N, value=input_value)

    def set_n_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.N,
                                                       times=increment_number)

    def set_n_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.N,
                                                       times=decrement_number)

    def set_model_effects(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MODEL_EFFECTS, input_text=filter_text)

    """Methods in Options tab"""

    def expand_windowshade_methods(self):
        self.expand_windowshade(parent_label=Helper.data_locale.METHODS)

    def collapse_windowshade_methods(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.METHODS)

    def set_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METHOD,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_check_center_the_responses_and_predictors(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CENTER_THE_RESPONSE_AND_PREDICTORS)

    def set_uncheck_center_the_responses_and_predictors(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CENTER_THE_RESPONSE_AND_PREDICTORS)

    def set_check_scale_the_responses_and_predictors(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SCALE_THE_RESPONSE_AND_PREDICTORS)

    def set_uncheck_scale_the_responses_and_predictors(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SCALE_THE_RESPONSE_AND_PREDICTORS)

    def set_check_specify_the_number_of_factors(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_THE_NUMBER_OF_FACTORS)

    def set_uncheck_specify_the_number_of_factors(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_THE_NUMBER_OF_FACTORS)

    def set_number_of_factors(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_FACTORS, value=input_value)

    def set_number_of_factors_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_FACTORS,
                                                       times=increment_number)

    def set_number_of_factors_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_FACTORS,
                                                       times=decrement_number)

    def expand_windowshade_cross_validation(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CROSS_VALIDATION)

    def collapse_windowshade_cross_validation(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.CROSS_VALIDATION)

    def set_cross_validation_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.CROSS_VALIDATION_METHOD,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_algorithm(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.ALGORITHM,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_check_specify_the_maximum_number_of_iterations(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_THE_MAX_NUM_OF_ITERATIONS)

    def set_uncheck_specify_the_maximum_number_of_iterations(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_THE_MAX_NUM_OF_ITERATIONS)

    def set_maximum_number_of_iterations(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS,
                                           value=input_value)

    def expand_windowshade_statistics(self):
        self.expand_windowshade(parent_label=Helper.data_locale.STATISTICS)

    def collapse_windowshade_statistics(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.STATISTICS)

    def set_statistics_to_display(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STATISTICS_TO_DISPLAY,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_check_coefficients_of_final_predictive_model(self):
        self.set_check_for_checkbox(label=Helper.data_locale.COEFFICIENT_OF_FINAL_PREDICTIVE_MODE)

    def set_uncheck_coefficients_of_final_predictive_model(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.COEFFICIENT_OF_FINAL_PREDICTIVE_MODE)

    def set_check_variation_accounted_for_in_responses_and_predictors(self):
        self.set_check_for_checkbox(label=Helper.data_locale.VALIDATION_ACCOUNTED_FOR_IN_RESPONSE_AND_PREDICTORS)

    def set_uncheck_variation_accounted_for_in_responses_and_predictors(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.VALIDATION_ACCOUNTED_FOR_IN_RESPONSE_AND_PREDICTORS)

    def set_check_details_of_the_fitted_model(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DETAILS_OF_THE_FITTED_MODEL)

    def set_uncheck_details_of_the_fitted_model(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DETAILS_OF_THE_FITTED_MODEL)

    def expand_windowshade_plots(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PLOTS)

    def collapse_windowshade_plots(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PLOTS)

    def set_select_plots_to_display(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SELECT_PLOTS_TO_DISPLAY,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_check_correlation_loading_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CORRELATION_LOADING_PLOT)

    def set_uncheck_correlation_loading_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CORRELATION_LOADING_PLOT)

    def set_check_specify_the_number_of_factors_to_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_THE_NUMBER_OF_FACTORS_TO_PLOT)

    def set_uncheck_specify_the_number_of_factors_to_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_THE_NUMBER_OF_FACTORS_TO_PLOT)

    def set_number_of_factors_to_plot(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_FACTORS_TO_PLOT,
                                           value=input_value)
