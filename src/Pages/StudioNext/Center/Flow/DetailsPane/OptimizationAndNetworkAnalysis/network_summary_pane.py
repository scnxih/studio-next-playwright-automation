"""
@author: Frank (Feng) Jiang
@date: 2024/09/18
@description: define panes of Network Summary step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class NetworkSummaryPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_links(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LINKS)

    def collapse_windowshade_links(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LINKS)

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def set_link_direction(self, direction: str):
        self.set_option_for_radio_group(Helper.data_locale.LINK_DIRECTION, direction)

    def add_column_for_from_node(self, column_name: str):
        self.add_column(Helper.data_locale.FROM_NODE, column_name)

    def delete_column_for_from_node(self):
        self.delete_column(Helper.data_locale.FROM_NODE)

    def add_column_for_to_node(self, column_name: str):
        self.add_column(Helper.data_locale.TO_NODE, column_name)

    def delete_column_for_to_node(self):
        self.delete_column(Helper.data_locale.TO_NODE)

    def add_column_for_weight_in_links(self, column_name: str):
        self.add_column(Helper.data_locale.WEIGHT, column_name, section_label=Helper.data_locale.LINKS)

    def delete_column_for_weight_in_links(self):
        self.delete_column(Helper.data_locale.WEIGHT, section_label=Helper.data_locale.LINKS)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

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
        self.expand_windowshade(parent_label=Helper.data_locale.NODES)

    def collapse_windowshade_nodes(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NODES)

    def input_filter_nodes_data(self, filter_expression: str):
        self.set_text_for_text_control(Helper.data_locale.FILTER_NODES_DATA, input_text=filter_expression)

    def empty_filter_nodes_data(self):
        self.set_text_for_text_control(Helper.data_locale.FILTER_NODES_DATA, input_text="")

    def add_column_for_node(self, column_name: str):
        self.add_column_exact_label(Helper.data_locale.NODE_WITH_COLON, column_name)

    def delete_column_for_node(self):
        self.delete_column_exact_label(Helper.data_locale.NODE_WITH_COLON)

    def add_column_for_weight_in_nodes(self, column_name: str):
        self.add_column(Helper.data_locale.WEIGHT, column_name, section_label=Helper.data_locale.NODES)

    def delete_column_for_weight_in_nodes(self):
        self.delete_column(Helper.data_locale.WEIGHT, section_label=Helper.data_locale.NODES)

    """Methods in Options tab"""

    def expand_windowshade_statistics(self):
        self.expand_windowshade(Helper.data_locale.STATISTICS)

    def collapse_windowshade_statistics(self):
        self.collapse_windowshade(Helper.data_locale.STATISTICS)

    def set_check_biconnected_components(self):
        self.set_check_for_checkbox(Helper.data_locale.BICONNECTED_COMPONENTS)

    def set_uncheck_biconnected_components(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.BICONNECTED_COMPONENTS)

    def set_check_connected_components(self):
        self.set_check_for_checkbox(Helper.data_locale.CONNECTED_COMPONENTS)

    def set_uncheck_connected_components(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CONNECTED_COMPONENTS)

    def set_check_approximate_diameter(self):
        self.set_check_for_checkbox(Helper.data_locale.APPROXIMATE_DIAMETER)

    def set_uncheck_approximate_diameter(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.APPROXIMATE_DIAMETER)

    def set_check_shortest_paths(self):
        self.set_check_for_checkbox(Helper.data_locale.SHORTEST_PATHS)

    def set_uncheck_shortest_paths(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SHORTEST_PATHS)

    def select_metric_type_for_approximate_diameter(self, opt_type: str):
        get_combobox(self.base_xpath, self.page,
                     supplement_base_xpath="[./../../../../../../../preceding-sibling::div[1]"
                                           "//label[contains(text(),'{0}')]]"
                     .format(Helper.data_locale.APPROXIMATE_DIAMETER)).select_item(opt_type)

    def select_metric_type_for_shortest_paths(self, opt_type: str):
        get_combobox(self.base_xpath, self.page,
                     supplement_base_xpath="[./../../../../../../../preceding-sibling::div[1]"
                                           "//label[contains(text(),'{0}')]]"
                     .format(Helper.data_locale.SHORTEST_PATHS)).select_item(opt_type)

    def select_log_details(self, log_opt: str):
        self.set_option_for_combobox(Helper.data_locale.LOG_DETAILS, item_value=log_opt)

    def select_procedure(self, proc_type: str):
        self.set_option_for_radio_group(Helper.data_locale.CODE_GENERATION, proc_type)

    """Methods in Output tab"""

    def set_check_create_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_OUTPUT_TABLE)

    def set_uncheck_create_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_OUTPUT_TABLE)

    def set_check_replace_existing_output_table_for_output_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_OUTPUT_TABLE)).set_check()

    def set_uncheck_replace_existing_output_table_for_output_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_OUTPUT_TABLE)).set_uncheck()

    def set_check_create_nodes_table(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_NODES_TABLE)

    def set_uncheck_create_nodes_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_NODES_TABLE)

    def set_check_replace_existing_output_table_for_nodes_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_NODES_TABLE)).set_check()

    def set_uncheck_replace_existing_output_table_for_nodes_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_NODES_TABLE)).set_uncheck()

    def set_check_create_links_table(self):
        self.set_check_for_checkbox(Helper.data_locale.CREATE_LINKS_TABLE)

    def set_uncheck_create_links_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_LINKS_TABLE)

    def set_check_replace_existing_output_table_for_links_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_LINKS_TABLE)).set_check()

    def set_uncheck_replace_existing_output_table_for_links_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.CREATE_LINKS_TABLE)).set_uncheck()
