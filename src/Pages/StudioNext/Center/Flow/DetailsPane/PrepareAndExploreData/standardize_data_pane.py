"""
@File: standardize_data
@Author: Allison
@Date: 8/21/2024 3:27 AM 
@Description: 

"""
from src.Helper.helper import Helper
from src.Pages.Common.common_component_factory import get_radio_group
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class StandardizeData(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

        """Data tab"""

    def add_columns_for_variables_to_standardize(self, check_column_name_list: list = None,
                                                 uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.VARIABLES_TO_STANDARDIZE,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)

    def add_column_for_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

        """Options tab"""

    def set_check_center_data_only(self):
        self.set_check_for_checkbox(Helper.data_locale.CENTER_DATA_ONLY)

    def set_uncheck_center_data_only(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.CENTER_DATA_ONLY)

    def set_centering_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.CENTERING_METHOD, item_index=item_index,
                                     item_value=item_value)

    def set_standardization_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STANDARDIZATION_METHOD, item_index=item_index,
                                     item_value=item_value)

    def set_tuning_constant(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TUNING_CONSTANT, input_text=input_text)

    def set_lambda(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LAMBDA, input_text=input_text)

    def set_proportion_of_pairs(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PROPORTION_OF_PAIRS, input_text=input_text)

    def set_proportion_of_data(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PROPORTION_OF_DATA, input_text=input_text)

    def set_missing_values_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MISSING_VALUES_METHODS, item_index=item_index,
                                     item_value=item_value)

    def set_replace_missing_values_with(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.REPLACE_MISSING_VALUES_WITH, item_index=item_index,
                                     item_value=item_value)

    def set_custom_value(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.CUSTOM_VALUE, input_text=input_text)

    def set_check_for_display_location_and_scale_measures(self):
        self.set_check_for_checkbox(Helper.data_locale.DISPLAY_LOCATION_AND_SCALE_MEASURES)

    def set_uncheck_for_display_location_and_scale_measures(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.DISPLAY_LOCATION_AND_SCALE_MEASURES)

        """Output tab"""

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_variables_to_include(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.VARIABLES_TO_INCLUDE, item_index=item_index,
                                     item_value=item_value)

    def set_specify_prefix_radiobutton(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label='', item_index=item_index, item_value=item_value)

    def set_prefix_for_standardized_variables(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PREFIX_FOR_STANDARDIZED_VARIABLES,
                                       input_text=input_text)

    def set_prefix_for_original_variables(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PREFIX_FOR_ORIGINAL_VARIABLES,
                                       input_text=input_text)

    def set_specify_data_to_show(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPECIFY_DATA_TO_SHOW, item_index=item_index,
                                     item_value=item_value)

    # Added by Alice on Jun 19, 2025
    def set_specify_prefix_radiobutton_new(self, item_index: int = None, item_value: str = None):

        if item_index != None:
            get_radio_group(self.base_xpath, self.page,
                            supplement_base_xpath="[../../../preceding-sibling::div[1][.//label[contains(text(),'" + Helper.data_locale.VARIABLES_TO_INCLUDE + "')]]]").set_check_for_index(
                index=item_index)

        if item_value != None:
            get_radio_group(self.base_xpath, self.page,
                            supplement_base_xpath="[../../../preceding-sibling::div[1][.//label[contains(text(),'" + Helper.data_locale.VARIABLES_TO_INCLUDE + "')]]]").set_check(
                text=item_value)

    # Select CAS
    def set_select_a_server_radiobutton(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP, item_index=item_index, item_value=item_value)

    def expand_windowshade_center_and_scale(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CENTER_AND_SCALE)

    def collapse_windowshade_center_and_scale(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.CENTER_AND_SCALE)

    def add_column_for_select_column(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.SELECT_COLUMN, column_name=column_name)

    def set_select_column_options_radiobutton(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.COLUMN_OPTIONS, item_index=item_index, item_value=item_value)

    def set_new_column(self, input_text: str, section_label: str = None):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NEW_COLUMN, input_text=input_text, section_label=section_label)

    def expand_windowshade_additional_center_and_scale(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_CENTER_AND_SCALE)

    def collapse_windowshade_additional_center_and_scale(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_CENTER_AND_SCALE)