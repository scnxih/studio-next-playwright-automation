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
        self.add_column_exact_label(parent_label=Helper.data_locale.CATEGORY_WITH_COLON, column_name=column_name)

    def add_column_for_subcategory(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.SUBCATEGORY_WITH_COLON, column_name=column_name)

    def set_display_subcategory_legend(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.DISPLAY_SUBCATEGORY_LEGEND,
                                        item_index=item_index, item_value=item_value)

    def set_legend_location(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LEGEND_LOCATION, item_index=item_index,
                                     item_value=item_value)

    def set_measure(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MEASURE, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_column(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.COLUMN, column_name=column_name)

    def set_statistics(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STATISTICS, item_index=item_index,
                                     item_value=item_value)

    def set_error_bars(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.ERROR_BARS, item_index=item_index,
                                     item_value=item_value)

    def set_type(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.TYPE, item_index=item_index,
                                     item_value=item_value)

    def set_confidence_level(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.CONFIDENCE_LEVEL, item_index=item_index,
                                     item_value=item_value)

    def set_check_specify_statistic_multiplier(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_A_STATISTIC_MULTIPLIER)

    def set_uncheck_specify_statistic_multiplier(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_A_STATISTIC_MULTIPLIER)

    def set_multiplier(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MULTIPLIER, input_text=input_text)

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
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_LINE_LABEL)

    def set_uncheck_show_line_label(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_LINE_LABEL)

    def set_label(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LABEL, input_text=input_text)

    def set_check_set_color(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SET_COLOR)

    def set_uncheck_set_color(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SET_COLOR)

    def set_color_transparency(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COLOR_TRANSPARENCY, item_index=item_index,
                                     item_value=item_value)

    def set_line_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_url_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.URL_VARIABLE, column_name=column_name)

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

    def set_display_label_x(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DISPLAY_LABEL,
                                     preceding_label=Helper.data_locale.X_AXIS, item_index=item_index,
                                     item_value=item_value)

    def set_label_x(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LABEL, input_text=input_text)

    def set_check_rotate_values_in_case_of_tick_collisions(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS)

    def set_uncheck_rotate_values_in_case_of_tick_collisions(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS)

    def set_rotate_degree(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS,
                                        item_index=item_index, item_value=item_value)

    def set_check_create_reference_line_x(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE)

    def set_uncheck_create_reference_lines_x(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE)

    def set_reference_values_x(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def set_line_offset(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_OFFSET, item_index=item_index,
                                     item_value=item_value)

    def set_reference_label_x(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                        item_index=item_index, item_value=item_value)

    def set_label_for_reference_x(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LABEL, input_text=input_text)

    def expand_windowshade_y_axis(self):
        self.expand_windowshade(parent_label=Helper.data_locale.Y_AXIS)

    def collapse_windowshade_y_axis(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.Y_AXIS)

    def set_check_specify_minimum_value(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_MINIMUM_VALUE)

    def set_uncheck_specify_minimum_value(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_MINIMUM_VALUE)

    def set_minimum_value(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MINIMUM_VALUE, input_text=input_text)

    def set_check_specify_maximum_value(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_MAXIMUM_VALUE)

    def set_uncheck_specify_maximum_value(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_MAXIMUM_VALUE)

    def set_maximum_value(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MAXIMUM_VALUE, input_text=input_text)

    def set_check_show_grid_lines(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_GRID_LINES)

    def set_uncheck_show_grid_lines(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_GRID_LINES)

    def set_display_label_for_y_axis(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DISPLAY_LABEL, item_index=item_index,
                                     item_value=item_value)

    def set_check_use_logarithmic_scale(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_LOGARITHMIC_SCALE)

    def set_uncheck_use_logarithmic_scale(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_LOGARITHMIC_SCALE)

    def set_base_value(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.BASE_VALUE, item_index=item_index,
                                     item_value=item_value)

    def set_check_create_reference_line_y(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE)

    def set_uncheck_create_reference_lines_y(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE)

    def set_reference_values_y(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.REFERENCE_VALUE, input_text=input_text)

    def set_reference_label_y(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                        item_index=item_index, item_value=item_value)

    def set_label_for_reference_y(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LABEL, input_text=input_text)

    def expand_windowshade_title_footnote(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TITLE_AND_FOOTNOTE)

    def collapse_windowshade_title_footnote(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TITLE_AND_FOOTNOTE)

    def set_title(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TITLE, input_text=input_text)

    def set_footnote(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FOOTNOTE, input_text=input_text)

    def expand_windowshade_graph_size(self):
        self.expand_windowshade(parent_label=Helper.data_locale.GRAPH_SIZE)

    def collapse_windowshade_graph_size(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.GRAPH_SIZE)

    def set_units(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.UNITS, item_index=item_index,
                                     item_value=item_value)
