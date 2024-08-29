"""
@author: Liu Jia
@date: 2024/08/22
@description: Define bubble map pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class SplitColumnsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_column_for_Column_to_split(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.COLUMN_TO_SPLIT, column_name=column_name)
    def add_column_for_Formatted_identifier_values(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FORMATTED_IDENTIFIER_VALUES, column_name=column_name)
    def add_column_for_Labels_for_new_columns(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LABELS_FOR_NEW_COLUMNS, column_name=column_name)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    """Methods in Output tab"""
    def set_check_for_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_check_for_use_column_name_prefix(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_COLUMN_NAME_PREFIX)
    def set_text_for_prefix(self,input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PREFIX, input_text=input_text)
    def set_specify_data_to_show(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPECIFY_DATA_TO_SHOW,
                                     preceding_label=None, item_index=item_index,
                                     item_value=item_value)
