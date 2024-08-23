"""
@File: support_vector_data_description
@Author: Allison
@Date: 8/22/2024 3:36 AM 
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

    def add_colum_for_weight_variables(self, column_name : str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT_VARIABLE, column_name=column_name)