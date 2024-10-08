"""
@author: Liu Jia
@date: 2024/09/28
@description: Define Describe Missing data pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class DescribeMissingDataPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_columns_for_analysis_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ANALYSIS_VARIABLES,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def expand_windowshade_additional_roles(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
