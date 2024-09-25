"""
@author: Liu Jia
@date: 2024/09/20
@description: Define Causal Models pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class CausalModelsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def set_filter_link_data(self,filter_text:str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_LINKS_DATA, input_text=filter_text)
    def set_select_method(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(item_index=item_index,item_value=item_value)
    def add_column_for_dependent_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.DEPENDENT_VARS, column_name=column_name)
    def add_columns_for_exogenous_explanatory_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.EXOGENOUS_EXPLANATORY_VARIABLES, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_endogenous_explanatory_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ENDOGENOUS_EXPLANATORY_VARIABLES,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_excluded_instrumental_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.EXCLUDED_INSTRUMENTAL_VARIABLES,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_outcome_equation(self):
        self.expand_windowshade(parent_label=Helper.data_locale.OUTCOME_EQUATION)
    def collapse_windowshade_outcome_equation(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.OUTCOME_EQUATION)
    def add_column_for_dependent_variable_outcome_equation(self, column_name: str):
        self.add_column(section_label=Helper.data_locale.OUTCOME_EQUATION,parent_label=Helper.data_locale.DEPENDENT_VARS, column_name=column_name)
    def add_columns_for_continuous_variable_outcome_equation(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(section_label=Helper.data_locale.OUTCOME_EQUATION,parent_label=Helper.data_locale.CONTINUOUS_VARIABLES,
                         check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def set_check_intercept_outcome_equation(self):
        self.set_check_for_checkbox(section_label=Helper.data_locale.OUTCOME_EQUATION,label=Helper.data_locale.INCLUDE_THE_INTERCEPT)
    def expand_windowshade_selection_equation(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SELECTION_EQUATION)
    def collapse_windowshade_selection_equation(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.SELECTION_EQUATION)
    def add_column_for_dependent_variable_selection_equationn(self, column_name: str):
        self.add_column(section_label=Helper.data_locale.SELECTION_EQUATION,parent_label=Helper.data_locale.DEPENDENT_VARS, column_name=column_name)
    def set_select_distinct_value_dependent_variable(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DISTINCT_VALUE_DEPENDENT_VARIABLE, item_index=item_index,item_value=item_value)
    def add_columns_for_continuous_variable_selection_equation(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(section_label=Helper.data_locale.SELECTION_EQUATION,parent_label=Helper.data_locale.CONTINUOUS_VARIABLES,
                         check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def set_check_intercept_selection_equation(self):
        self.set_check_for_checkbox(section_label=Helper.data_locale.SELECTION_EQUATION,label=Helper.data_locale.INCLUDE_THE_INTERCEPT)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None, uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)

    """Methods in Options tab"""
    def set_select_optimization_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.OPTIMIZATION_METHOD, item_index=item_index,item_value=item_value)
    def set_select_maximum_number_of_iterations(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS, item_index=item_index, item_value=item_value)
    def set_maximum_number_of_iterations_text(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS, input_text=input_text)
    def set_select_variance_estimation_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.VARIANCE_ESTIMATION_METHOD, item_index=item_index, item_value=item_value)
    def set_select_Type_covariances_parameter_estimates(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COVARIANCE_OF_THE_PARAMETER_ESTIMATES, item_index=item_index,item_value=item_value)
    def set_select_statistics_to_display(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SELECT_STATISTICS_TO_DISPLAY, item_index=item_index,item_value=item_value)
    def set_check_correlations_parameter_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CORRELATIONS_OF_PARAMETER_ESTIMATES)
    def set_uncheck_correlations_parameter_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CORRELATIONS_OF_PARAMETER_ESTIMATES)
    def set_check_covariances_parameter_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.COVARIANCE_OF_THE_PARAMETER_ESTIMATES)
    def set_uncheck_covariances_parameter_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.COVARIANCE_OF_THE_PARAMETER_ESTIMATES)
    def set_check_iteration_history_objective_function(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ITERATION_HISTORY_OF_OBJECTIVE_FUCTION)
    def set_uncheck_iteration_history_objective_function(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ITERATION_HISTORY_OF_OBJECTIVE_FUCTION)

    """Methods in Output tab"""
    def set_check_create_parameter_estimates_data_set(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_PARAMETER_ESTIMATES_DATASET)
    def set_uncheck_create_parameter_estimates_data_set(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_PARAMETER_ESTIMATES_DATASET)
    def set_check_covariance_matrix_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ADD_COVARIANCE_MATRIX_ESTIMATES)
    def set_uncheck_covariance_matrix_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ADD_COVARIANCE_MATRIX_ESTIMATES)
    def set_check_correlation_matrix_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ADD_CORRELATION_MATRIX_ESTIMATES)
    def set_uncheck_correlation_matrix_estimates(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ADD_CORRELATION_MATRIX_ESTIMATES)


