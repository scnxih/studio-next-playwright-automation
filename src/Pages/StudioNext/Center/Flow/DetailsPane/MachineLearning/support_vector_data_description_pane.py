"""
@File: support_vector_data_description
@Author: Allison
@Date: 6/17/2025 3:36 AM
@Description:

"""
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class SupportVectorDataDescription(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

        """Data tab"""

    def add_columns_for_interval_inputs(self, check_column_name_list: list = None,
                                        uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INTERVAL_INPUTS,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_norminal_inputs(self, check_column_name_list: list = None,
                                        uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.NORMINAL_INPUTS,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_weight_variables(self, column_name : str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT_VARIABLE, column_name=column_name)

        """Options tab"""

    def set_text_for_rbf_bandwidth_parameter(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.RBF_BANDWIDTH_PARAMETER, input_text=input_text)

    def set_text_for_expected_outlier_fraction(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.EXPECTED_OUTLIER_FRACTION, input_text=input_text)

    def set_text_for_solver_tolerance(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.SOLVER_TOLERANCE, input_text=input_text)

    def set_maximum_iterations(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_ITERATIONS, value=input_value)

    def set_optimization_solver(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.OPTIMIZATION_SOLVER, item_index=item_index, item_value=item_value)

    def set_stochastic_parameters(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STOCHASTIC_PARAMETERS, item_index=item_index, item_value=item_value)

    def set_maximum_support_vectors(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.MAXIMUM_SUPPORT_VECTORS, value=input_value)

    def set_observations_sampled(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.OBSERVATIONS_SAMPLED, value=input_value)

    def set_text_for_threshold_tolerance(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.THRESHOLD_TOLERANCE, input_text=input_text)

    def set_text_for_center_tolerance(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.CENTER_TOLERANCE, input_text=input_text)

    def set_convergence_criterion(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.CONVERGENCE_CRITERION, value=input_value)

        """Options tab"""

    def set_check_create_support_vectors_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_SUPPORT_VECTORS_DATA)

    def set_uncheck_create_support_vectors_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_SUPPORT_VECTORS_DATA)

    def set_check_save_scoring_model(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SCORING_MODEL)

    def set_uncheck_save_scoring_model(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_SCORING_MODEL)

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_include_variables_from_the_input_data_set(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INCLUDE_VARIABLES_FROM_THE_INPUT_DATA_SET,
                                        item_index=item_index,
                                        item_value=item_value)

    def add_columns_for_include_these_variables(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INCLUDE_THESE_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)