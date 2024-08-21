from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *
from src.Pages.StudioNext.Dialog.select_column_dialog import SelectColumnDialog


class ListDataPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Below methods are in Data tab"""

    def add_columns_for_list_variables(self, check_column_name_list: list = None,
                                       uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.LIST_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_total_of(self, check_column_name_list: list = None,
                                 uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.TOTAL_OF,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_identifying_label(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.IDENTIFYING_LABEL,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def delete_columns_for_list_variables(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.LIST_VARIABLES,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_list_variables(self, check_column_name_list: list = None,
                                           uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.LIST_VARIABLES,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_list_variables(self, check_column_name_list: list = None,
                                             uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.LIST_VARIABLES,
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

    def delete_columns_for_total_of(self, check_column_name_list: list = None,
                                    uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.TOTAL_OF,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_total_of(self, check_column_name_list: list = None,
                                     uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.TOTAL_OF,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_total_of(self, check_column_name_list: list = None,
                                       uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.TOTAL_OF,
                                           check_column_name_list=check_column_name_list,
                                           uncheck_column_name_list=uncheck_column_name_list)

    def delete_columns_for_identifying_label(self, check_column_name_list: list = None,
                                             uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.IDENTIFYING_LABEL,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_identifying_label(self, check_column_name_list: list = None,
                                              uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.IDENTIFYING_LABEL,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_identifying_label(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.IDENTIFYING_LABEL,
                                           check_column_name_list=check_column_name_list,
                                           uncheck_column_name_list=uncheck_column_name_list)

    """Below methods are in Options tab"""

    def set_check_display_row_numbers(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DISPLAY_ROW_NUMBERS)

    def set_uncheck_display_row_numbers(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DISPLAY_ROW_NUMBERS)

    def set_column_label(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.COLUMN_LABEL, input_text=input_text)

    def set_check_use_labels_as_column_headings(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_COLUMN_LABELS_AS_COLUMN_HEADINGS)

    def set_uncheck_use_labels_as_column_headings(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_COLUMN_LABELS_AS_COLUMN_HEADINGS)

    def set_check_display_number_of_rows(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DISPLAY_NUMBER_OF_ROWS)

    def set_uncheck_display_number_of_rows(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DISPLAY_NUMBER_OF_ROWS)

    def set_check_round_values(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ROUND_VALUES_BEFORE_SUMMING_THE_VARIABLE)

    def set_uncheck_round_values(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ROUND_VALUES_BEFORE_SUMMING_THE_VARIABLE)

    def set_heading_direction(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.HEADING_DIRECTION, item_index=item_index,
                                     item_value=item_value)

    def set_column_width(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COLUMN_WIDTH, item_index=item_index,
                                     item_value=item_value)

    def set_check_split_labels(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPLIT_LABELS)

    def set_uncheck_split_labels(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPLIT_LABELS)

    def set_split_character(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPLIT_CHARACTER, item_index=item_index,
                                     item_value=item_value)

    def set_rows_to_list(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.ROWS_TO_LIST, item_index=item_index,
                                     item_value=item_value)

