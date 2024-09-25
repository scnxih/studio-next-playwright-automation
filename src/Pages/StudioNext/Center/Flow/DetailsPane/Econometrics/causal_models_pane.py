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





    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None, uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)

    """Methods in Options tab"""