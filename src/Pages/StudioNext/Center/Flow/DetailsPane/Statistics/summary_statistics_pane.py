"""
@author: Liu Jia
@date: 2024/09/05
@description: Define summary statistics pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class SummaryStatisticsPane(BasicStepPane)
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_column_for_analysis_variables(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ANALYSIS_VARIABLES, column_name=column_name)
    def add_column_for_classification_variable(self, column_name: str):
       self.add_column(parent_label=Helper.data_locale.CLASSIFICATION_VARIABLE, column_name=column_name)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_copy_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.COPY_VARIABLES, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)
    def add_column_for_weight_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT_VARIABLE, column_name=column_name)

    """Methods in Option tab"""
    def expand_windowshade_basic_statistics(self):
        self.expand_windowshade(parent_label=Helper.data_locale.BASIC_STATISTICS)