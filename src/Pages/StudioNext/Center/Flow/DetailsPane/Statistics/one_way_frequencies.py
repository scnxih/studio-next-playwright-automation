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

    def expand_windowshade_additonal_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.Frequency_Count, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    """Options tab"""

