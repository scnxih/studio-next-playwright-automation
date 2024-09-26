"""
@author: Liu Jia
@date: 2024/09/26
@description: Define Characterize data pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class CharacterizeDataPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def expand_windowshade_automatic_characterization(self):
        self.expand_windowshade(parent_label=Helper.data_locale.AUTOMATIC_CHARACTERIZATION)
    def collapse_windowshade_automatic_characterization(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.AUTOMATIC_CHARACTERIZATION)
    def expand_windowshade_custom_characterization(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CUSTOM_CHARACTERIZATION)
    def collapse_windowshade_custom_characterization(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.CUSTOM_CHARACTERIZATION)
    def add_columns_for_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns_exact_label(parent_label=Helper.data_locale.VARIABLES_COLON,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_categorical_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.CATEGORICAL_VARIABLES,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_date_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.DATE_VARIABLES,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_column_for_grouping_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.GROUPING_VARIABLE, column_name=column_name)

    """Methods in Option tab"""
    def expand_windowshade_categorical_variables(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CATEGORICAL_VARIABLES)
    def collapse_windowshade_categorical_variables(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.CATEGORICAL_VARIABLES)
    def set_check_frequency_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.FREQUENCY_TABLE)
    def set_uncheck_frequency_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.FREQUENCY_TABLE)
    def set_check_frequency_chart(self):
        self.set_check_for_checkbox(label=Helper.data_locale.FREQUENCY_CHART)
    def set_uncheck_frequency_chart(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.FREQUENCY_CHART)
    def set_check_treat_missing_values_valid_level(self):
        self.set_check_for_checkbox(label=Helper.data_locale.TREAT_MISSING_VALUES_VALID_LEVEL)
    def set_uncheck_treat_missing_values_valid_level(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.TREAT_MISSING_VALUES_VALID_LEVEL)
    def set_check_limit_categorical_values(self):
        self.set_check_for_checkbox(label=Helper.data_locale.LIMIT_CATEGORICAL_VALUES)
    def set_uncheck_limit_categorical_values(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.LIMIT_CATEGORICAL_VALUES)
    def expand_windowshade_numeric_variables(self):
        self.expand_windowshade(parent_label=Helper.data_locale.NUMERIC_VARIABLES)
    def collapse_windowshade_numeric_variabless(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NUMERIC_VARIABLES)
    def set_check_descriptive_statistics(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DESCRIPTIVE_STATISTICS)
    def set_uncheck_descriptive_statistics(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DESCRIPTIVE_STATISTICS)
    def set_check_histogram(self):
        self.set_check_for_checkbox(label=Helper.data_locale.HISTOGRAM)
    def set_uncheck_histogram(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.HISTOGRAM)
    def expand_windowshade_date_variables(self):
        self.expand_windowshade(parent_label=Helper.data_locale.DATE_VARIABLES)
    def collapse_windowshade_date_variabless(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.DATE_VARIABLES)
    def set_check_display_minimum_maximum_date(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DISPLAY_MINIMUM_AND_MAXIMUM_DATE)
    def set_uncheck_display_minimum_maximum_date(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DISPLAY_MINIMUM_AND_MAXIMUM_DATE)
    def set_check_frequency_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.FREQUENCY_PLOT)
    def set_uncheck_frequency_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.FREQUENCY_PLOT)