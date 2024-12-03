"""
@author: Dommy (Fuying) Chen
@date: 2024/11/27
@description: define panes of Transform Columns step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class TransformColumnsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_select_a_server_for_this_step(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_note_about_server_selection(self):
        self.expand_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def collapse_windowshade_note_about_server_selection(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)

    def set_filter_input_data(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_INPUT_DATA, input_text=filter_text)

    def expand_windowshade_transform1(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TRANSFORM_1)

    def collapse_windowshade_transform1(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TRANSFORM_1)

    def add_column_for_variable1(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.VARIABLE_1, column_name=column_name)

    def set_transform_for_transform1(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.TRANSFORM,
                                     section_label=Helper.data_locale.TRANSFORM_1, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_transform2(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TRANSFORM_2)

    def collapse_windowshade_transform2(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TRANSFORM_2)

    def add_column_for_variable2(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.VARIABLE_2, column_name=column_name)

    def set_transform_for_transform2(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.TRANSFORM,
                                     section_label=Helper.data_locale.TRANSFORM_2, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_transform3(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TRANSFORM_3)

    def collapse_windowshade_transform3(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TRANSFORM_3)

    def add_column_for_variable3(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.VARIABLE_3, column_name=column_name)

    def set_transform_for_transform3(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.TRANSFORM,
                                     section_label=Helper.data_locale.TRANSFORM_3, item_index=item_index,
                                     item_value=item_value)

    def set_custom_transform(self, filter_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.CUSTOM_TRANSFORM, input_text=filter_text)


    """Below methods are in Output tab"""

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_specify_data_to_show(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPECIFY_DATA_TO_SHOW,
                                     item_index=item_index,
                                     item_value=item_value)

    def set_number_of_observations_default(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_OBSERVATIONS, value=input_value)

    def set_number_of_observations_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_OBSERVATIONS,
                                                       times=increment_number)

    def set_number_of_observations_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.NUMBER_OF_OBSERVATIONS,
                                                       times=decrement_number)
