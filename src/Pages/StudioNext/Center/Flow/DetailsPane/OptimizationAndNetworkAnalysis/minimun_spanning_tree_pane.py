"""
@author: Dommy (Fuying) Chen
@date: 2024/09/12
@description: define panes of Minimum Spanning Tree step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class MinimunSpanningTree(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_note_about_server_selection(self):
        self.expand_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def collapse_windowshade_note_about_server_selection(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def set_select_server_for_step(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def set_filter_links_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_LINKS_DATA, input_text=filter_text)

    def add_column_for_from_node(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FROM_NODE, column_name=column_name)

    def add_column_for_to_node(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.TO_NODE, column_name=column_name)

    def add_column_for_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT,column_name=column_name)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    """Below methods are in Options tab"""
    def set_log_details(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LOG_DETAILS, item_index=item_index,
                                     item_value=item_value)

    def set_code_generation(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_index=item_index,
                                        item_value=item_value)

    """Below methods are in Output tab"""

    def set_check_save_minimum_spanning_tree_information_date(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_MINIMUM_SPANNING_TREE_INFORMATION_DATA)

    def set_uncheck_save_minimum_spanning_tree_information_date(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_MINIMUM_SPANNING_TREE_INFORMATION_DATA)

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)