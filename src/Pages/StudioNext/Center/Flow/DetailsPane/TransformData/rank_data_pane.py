"""
@author: Liu Jia
@date: 2024/09/18
@description: Define Rank data pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class RankDataPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_columns_for_columns_to_rank(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.COLUMN_TO_RANK,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_rank_by(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.RANK_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
    """Methods in Options tab"""
    def expand_windowshade_methods(self):
        self.expand_windowshade(parent_label=Helper.data_locale.METHODS)
    def collapse_windowshade_methods(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.METHODS)
    def set_ranking_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.RANKING_METHOD, item_index=item_index, item_value=item_value)
    def set_quantile(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_QUANTILE, item_index=item_index,item_value=item_value)
    def set_denominator(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_DENOMINATOR, item_index=item_index,item_value=item_value)
    def set_normal_score_formula(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_NORMAL_SCORE_FORMULA, item_index=item_index,item_value=item_value)
    def set_values_tied(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.IF_VALUES_TIED, item_index=item_index, item_value=item_value)
    def set_Rank_Order(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.RANK_ORDER, item_index=item_index, item_value=item_value)

    """Methods in OUTPUT tab"""
    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_check_create_new_variables_for_ranked_variables(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_NEW_VARIABLES_FOR_THE_RANKED_VARIABLES)
    def set_uncheck_create_new_variables_for_ranked_variablee(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_NEW_VARIABLES_FOR_THE_RANKED_VARIABLES)
    def set_specify_data_to_show(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPECIFY_DATA_TO_SHOW, item_index=item_index, item_value=item_value)

    """there should be a numeric stepper"""