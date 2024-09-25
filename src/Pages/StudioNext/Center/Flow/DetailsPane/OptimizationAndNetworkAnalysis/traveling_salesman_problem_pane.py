"""
@author: Frank (Feng) Jiang
@date: 2024/09/12
@description: define panes of Core Decomposition step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class TravelingSalesmanProblemPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def select_server(self, server: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP, item_value=server)

    def expand_windowshade_note_about_server_selection(self):
        self.expand_windowshade(Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def collapse_windowshade_note_about_server_selection(self):
        self.collapse_windowshade(Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def input_filter_links_data(self, filter_expression: str):
        self.set_text_for_text_control(Helper.data_locale.FILTER_LINKS_DATA, input_text=filter_expression)

    def empty_filter_links_data(self):
        self.set_text_for_text_control(Helper.data_locale.FILTER_LINKS_DATA, input_text="")

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

    def add_column_for_weight(self, col_name: str):
        self.add_column(Helper.data_locale.WEIGHT, col_name)

    def delete_column_for_weight(self):
        self.delete_column(Helper.data_locale.WEIGHT)

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

    """Methods in Options tab"""

    def set_max_time(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.MAXIMUM_TIME_TIME, item_value=radio_btn_label)

    def input_time_in_seconds(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.TIME_IN_SECONDS, input_text=input_value)

    def empty_time_in_seconds(self):
        self.set_text_for_text_control(Helper.data_locale.TIME_IN_SECONDS, input_text="")

    def select_log_details(self, combo_option_value: str):
        self.set_option_for_combobox(Helper.data_locale.LOG_DETAILS, item_value=combo_option_value)

    def set_solution_strategy(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SOLUTION_STRATEGY, item_value=radio_btn_label)

    def expand_windowshade_MILP_solver_options(self):
        self.expand_windowshade(Helper.data_locale.MILP_SOLVER_OPTIONS)

    def collapse_windowshade_MILP_solver_options(self):
        self.collapse_windowshade(Helper.data_locale.MILP_SOLVER_OPTIONS)

    def set_target_objective_value(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.TARGET_OBJECTIVE_VALUE,
                                        item_value=radio_btn_label)

    def input_target_value(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.TARGET_VALUE, input_text=input_value)

    def empty_target_value(self):
        self.set_text_for_text_control(Helper.data_locale.TARGET_VALUE, input_text="")

    def set_absolute_gap_between_current_and_best_remaining_objective_value(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.ABSOLUTE_GAP_BETWEEN_CURRENT_AND_BEST_REMAINING_OBJECTIVE_VALUE,
                                        item_value=radio_btn_label)

    def input_absolute_gap_value(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.ABSOLUTE_GAP_VALUE, input_text=input_value)

    def empty_absolute_gap_value(self):
        self.set_text_for_text_control(Helper.data_locale.ABSOLUTE_GAP_VALUE, input_text="")

    def set_relative_gap_between_current_and_best_remaining_objective_value(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.RELATIVE_GAP_BETWEEN_CURRENT_AND_BEST_REMAINING_OBJECTIVE_VALUE,
                                        item_value=radio_btn_label)

    def input_relative_gap_value(self, input_value: str):
        self.set_text_for_text_control(Helper.data_locale.ABSOLUTE_GAP_VALUE, input_text=input_value)

    def empty_relative_gap_value(self):
        self.set_text_for_text_control(Helper.data_locale.ABSOLUTE_GAP_VALUE, input_text="")

    def select_procedure(self, proc: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_value=proc)

    """Methods in Output tab"""

    def set_check_save_tour_info(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_TOUR_INFO)

    def set_uncheck_save_tour_info(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_TOUR_INFO)

    def set_check_replace_existing_output_table_for_save_tour_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TOUR_INFO)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_tour_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TOUR_INFO)).set_uncheck()

    def set_check_save_tour_nodes_info(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_TOUR_NODES_INFO)

    def set_uncheck_save_tour_nodes_info(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_TOUR_NODES_INFO)

    def set_check_replace_existing_output_table_for_save_tour_nodes_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TOUR_NODES_INFO)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_tour_nodes_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TOUR_NODES_INFO)).set_uncheck()
