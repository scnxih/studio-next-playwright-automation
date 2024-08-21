"""
@author: Dommy (Fuying) Chen
@date: 2024/08/21
@description: define panes of Line Chart step
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class LineChartPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def add_column_for_category(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.CATEGORY, column_name=column_name)

    def add_column_for_subcategory(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.SUBCATEGORY, column_name=column_name)

    def set_measure(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MEASURE, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_group_analysis_by(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, column_name=column_name)

    def add_column_for_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    """Below methods are in Options tab"""

    def expand_windowshade_lines(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LINES)

    def collapse_windowshade_lines(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LINES)

    def set_check_show_data_labels(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_DATA_LABELS)

    def set_uncheck_show_data_labels(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_DATA_LABELS)

    def set_check_show_line_label(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_LINE_LABEL_DOES_NOT_APPLY)

    def set_uncheck_show_line_label(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_LINE_LABEL_DOES_NOT_APPLY)

    def set_label(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LABEL, input_text=input_text)

    def set_color_transparency(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COLOR_TRANSPARENCY, item_index=item_index,
                                     item_value=item_value)

    def set_line_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_url_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.URL, column_name=column_name)

    def expand_windowshade_x_axis(self):
        self.expand_windowshade(parent_label=Helper.data_locale.X_AXIS)

    def collapse_windowshade_x_axis(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.X_AXIS)

    def set_check_reverse_tick_values(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REVERSE_TICK_VALUES)

    def set_uncheck_reverse_tick_values(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REVERSE_TICK_VALUES)

    def set_check_show_tick_values_in_data_order(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_TICK_VALUES_IN_DATA_ORDER)

    def set_uncheck_show_tick_values_in_data_order(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_TICK_VALUES_IN_DATA_ORDER)

    def set_display_label(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def set_check_rotate_values_in_case_of_tick_collisions(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS)

    def set_uncheck_rotate_values_in_case_of_tick_collisions(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS)

    def set_rotate_degree(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS,
                                        item_index=item_index, item_value=item_value)

    def set_check_create_reference_line(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE)

    def set_uncheck_create_reference_lines(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE)

    def set_reference_values(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def set_line_offset(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_OFFSET, item_index=item_index,
                                     item_value=item_value)

    def set_reference_label(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                        item_index=item_index, item_value=item_value)

    def set_label_for_reference(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LABEL, input_text=input_text)

    def expand_windowshade_y_axis(self):
        self.expand_windowshade(parent_label=Helper.data_locale.Y_AXIS)

    def collapse_windowshade_y_axis(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.Y_AXIS)

    def set_check_specify_minimum_value(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_MINIMUM_VALUE)

    def set_uncheck_specify_minimum_value(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_MINIMUM_VALUE)