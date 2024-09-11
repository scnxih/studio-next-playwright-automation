"""
@author: Dommy (Fuying) Chen
@date: 2024/08/23
@description: define panes of Line Chart step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class ClusterVariablesPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def add_columns_for_variables_to_cluster(self, check_column_name_list: list = None,
                                             uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.VARIABLES_TO_CLUSTER,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def delete_columns_for_variables_to_cluster(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.VARIABLES_TO_CLUSTER,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_variables_to_cluster(self, check_column_name_list: list = None,
                                                 uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.VARIABLES_TO_CLUSTER,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_variables_to_cluster(self, check_column_name_list: list = None,
                                                   uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.VARIABLES_TO_CLUSTER,
                                           check_column_name_list=check_column_name_list,
                                           uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_variables_to_partial_out(self, check_column_name_list: list = None,
                                                 uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def delete_columns_for_variables_to_partial_out(self, check_column_name_list: list = None,
                                                    uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_variables_to_partial_out(self, check_column_name_list: list = None,
                                                     uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_variables_to_cluster(self, check_column_name_list: list = None,
                                                   uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,
                                           check_column_name_list=check_column_name_list,
                                           uncheck_column_name_list=uncheck_column_name_list)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)

    def add_column_for_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def delete_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                             uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                              uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                                           check_column_name_list=check_column_name_list,
                                           uncheck_column_name_list=uncheck_column_name_list)

    """Below methods are in Options tab"""

    def set_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METHOD, item_index=item_index,
                                     item_value=item_value)

    def set_maximum_number_of_clusters(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_CLUSTERS, item_index=item_index,
                                     item_value=item_value)

    def set_check_maximum_second_eigenvalue(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MAXIMUM_SECOND_EIGENVALUE)

    def set_uncheck_maximum_second_eigenvalue(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MAXIMUM_SECOND_EIGENVALUE)

    def set_eigenvalue(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.EIGENVALUE, input_text=input_text)

    def set_check_minimum_proportion_of_variation(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MINIMUM_PROPORTION_OF_VARIATION)

    def set_uncheck_minimum_proportion_of_variation(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MINIMUM_PROPORTION_OF_VARIATION)

    def set_proportion(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PROPORTION, input_text=input_text)

    def expand_windowshade_deatails(self):
        self.expand_windowshade(parent_label=Helper.data_locale.DETAILS)

    def collapse_windowshade_deatail(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.DETAILS)

    def set_analyze(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.ANALYZE, item_index=item_index,
                                     item_value=item_value)

    def set_check_correct_the_covariances_or_correlations_for_the_means(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CORRECT_THE_COVARIANCES_OR_CORRELATIONS_FOR_THE_MEANS)

    def set_uncheck_correct_the_covariances_or_correlations_for_the_means(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CORRECT_THE_COVARIANCES_OR_CORRELATIONS_FOR_THE_MEANS)

    def set_check_maximum_number_of_iterations(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS)

    def set_uncheck_maximum_number_of_iterations(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS)

    def set_iterations(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.ITERATIONS, input_text=input_text)

    def set_select_plots_to_display(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SELECT_PLOTS_TO_DISPLAY, item_index=item_index,
                                     item_value=item_value)

    """Below methods are in Output tab"""

    def set_check_create_statistics_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_STATISTICS_DATA)

    def set_uncheck_create_statistics_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_STATISTICS_DATA)

    def set_check_create_tree_information_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_TREE_INFORMATION_DATA)

    def set_uncheck_create_tree_information_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_TREE_INFORMATION_DATA)

    def set_check_replace_existing_output_table_for_statistics(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label["
                                           "contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                         Helper.data_locale.CREATE_STATISTICS_DATA)).set_check()

    def set_uncheck_replace_existing_output_table_for_statistics(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label["
                                           "contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                         Helper.data_locale.CREATE_STATISTICS_DATA)).set_uncheck()

    def set_check_replace_existing_output_table_for_tree_information(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label["
                                           "contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                         Helper.data_locale.CREATE_TREE_INFORMATION_DATA)).set_check()

    def set_uncheck_replace_existing_output_table_for_tree_information(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label["
                                           "contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                         Helper.data_locale.CREATE_TREE_INFORMATION_DATA)).set_uncheck()
