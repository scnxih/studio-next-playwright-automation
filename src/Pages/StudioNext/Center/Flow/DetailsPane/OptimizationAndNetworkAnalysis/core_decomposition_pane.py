"""
@author: Frank (Feng) Jiang
@date: 2024/09/12
@description: define panes of Core Decomposition step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class CoreDecompositionPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_links(self):
        self.expand_windowshade(Helper.data_locale.LINKS)

    def collapse_windowshade_links(self):
        self.collapse_windowshade(Helper.data_locale.LINKS)

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def set_link_direction(self, direction: str):
        self.set_option_for_radio_group(Helper.data_locale.LINK_DIRECTION, direction)

    def add_column_for_from_node(self, col_name: str):
        self.add_column(Helper.data_locale.FROM_NODE, col_name)

    def delete_column_for_from_node(self):
        self.delete_column(Helper.data_locale.FROM_NODE)

    def add_column_for_to_node(self, col_name: str):
        self.add_column(Helper.data_locale.TO_NODE, col_name)

    def delete_column_for_to_node(self):
        self.delete_column(Helper.data_locale.TO_NODE)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_group_analysis_by(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_group_analysis_by(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def set_check_include_nodes_data(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)

    def set_uncheck_include_nodes_data(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_NODES_DATA)

    def expand_windowshade_nodes(self):
        self.expand_windowshade(Helper.data_locale.NODES)

    def collapse_windowshade_nodes(self):
        self.collapse_windowshade(Helper.data_locale.NODES)

    def input_filter_nodes_data(self, filter_expression: str):
        self.set_text_for_text_control(Helper.data_locale.FILTER_NODES_DATA, input_text=filter_expression)

    def empty_filter_nodes_data(self):
        self.set_text_for_text_control(Helper.data_locale.FILTER_NODES_DATA, input_text="")

    def add_column_for_node(self, col_name: str):
        self.add_column_exact_label(Helper.data_locale.NODE_WITH_COLON, col_name)

    def delete_column_for_node(self):
        self.delete_column_exact_label(Helper.data_locale.NODE_WITH_COLON)

    """Methods in Options tab"""

    def set_max_time(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.MAXIMUM_TIME_TIME, item_value=radio_btn_label)

    def input_time_in_seconds(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.TIME_IN_SECONDS, input_text=input_value)

    def empty_time_in_seconds(self):
        self.set_text_for_text_control(Helper.data_locale.TIME_IN_SECONDS, input_text="")

    def select_log_details(self, combo_option_value: str):
        self.set_option_for_combobox(Helper.data_locale.LOG_DETAILS, item_value=combo_option_value)

    def select_procedure(self, proc: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_value=proc)

    """Methods in Output tab"""

    def set_check_create_nodes_table(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_NODES_TABLE)

    def set_uncheck_create_nodes_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_NODES_TABLE)

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
