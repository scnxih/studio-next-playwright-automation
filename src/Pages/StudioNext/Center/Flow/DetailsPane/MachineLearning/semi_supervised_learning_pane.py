"""
@author: Dommy (Fuying) Chen
@date: 2024/09/13
@description: define panes of Semi-supervised Learning step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class SemiSupervisedLearning(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_labeled(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LABELED)

    def collapse_windowshade_labeled(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LABELED)

    def set_filter_labeled_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_LABELED_DATA, input_text=filter_text)

    def add_column_for_target_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.TARGET_VARIABLE, column_name=column_name)

    def add_columns_for_input_variables(self, check_column_name_list: list = None,
                                        uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INPUT_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_unlabeled(self):
        self.expand_windowshade(parent_label=Helper.data_locale.UNLABELED)

    def collapse_windowshade_unlabeled(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.UNLABELED)

    def set_filter_unlabeled_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_UNLABELED_DATA, input_text=filter_text)

    """Methods in Options tab"""

    def set_kernel(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.KERNEL, item_index=item_index,
                                        item_value=item_value)

    def set_number_of_neighbors(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_NEIGHBORS, input_text=filter_text)

    def set_number_of_iterations(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_ITERATIONS, input_text=filter_text)

    def set_rbf_kernel_width(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.RBF_KERNEL_WIDTH, input_text=filter_text)

    def set_code_generation(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_index=item_index,
                                        item_value=item_value)

    """Methods in Output tab"""

    def set_check_create_output_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_OUTPUT_DATA)

    def set_uncheck_create_output_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_OUTPUT_DATA)

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_include_variables_from_input_CAS_table(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INCLUDE_VARIABLES_FROM_THE_INPUT_CAS_TABLE,
                                        item_index=item_index,
                                        item_value=item_value)

    def add_columns_for_include_these_variables(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INCLUDE_THESE_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
