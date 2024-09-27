"""
@author: Dommy (Fuying) Chen
@date: 2024/09/26
@description: define panes of Line Chart step
"""
from src.Pages.Common.common_component_factory import get_text, get_radio_group, get_windowshade
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class BarLineChartPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def expand_windowshade_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.DATA)

    def collapse_windowshade_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.DATA)

    def expand_windowshade_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ROLES)

    def collapse_windowshade_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ROLES)

    def add_column_for_category(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.CATEGORY_WITH_COLON, column_name=column_name)

    def add_column_for_subcategory(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.SUBCATEGORY_WITH_COLON, column_name=column_name)

    def add_column_for_bar_variable(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.BAR_VARIABLE, column_name=column_name)

    def set_statistics_bar(self, item_index: int = None, item_value: str = None):
        get_radio_group(self.base_xpath, self.page,
                        supplement_base_xpath="[../../../../descendant::label[contains(text(),'" + Helper.data_locale.BAR_VARIABLE + "')]]").set_check_for_index(
            index=item_index)

    def add_column_for_line_variable(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.LINE_VARIABLE, column_name=column_name)

    def set_statistics_line(self, item_index: int = None, item_value: str = None):
        get_radio_group(self.base_xpath, self.page,
                        supplement_base_xpath="[../../../../descendant::label[contains(text(),'" + Helper.data_locale.LINE_VARIABLE + "')]]").set_check_for_index(
            index=item_index)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_group_analysis_by(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, column_name=column_name)

    def add_column_for_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    """Below methods are in Options tab"""

    def click_appearance_tab(self):
        """
        Description: click Appearance tab.
        """
        self.click_tab(Helper.data_locale.APPEARANCE)

    def expand_windowshade_bars(self):
        self.expand_windowshade(parent_label=Helper.data_locale.BARS)

    def collapse_windowshade_bars(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.BARS)

    def set_check_show_labels_bar(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_LABELS, section_label=Helper.data_locale.BARS)

    def set_uncheck_show_labels_bar(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_LABELS, section_label=Helper.data_locale.BARS)

    def set_color_transparency_bar(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COLOR_TRANSPARENCY,
                                     section_label=Helper.data_locale.BARS, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_details_bar(self):
        get_windowshade(self.base_xpath, self.page,
                        supplement_base_xpath="[descendant::span[text()='" + Helper.data_locale.DETAILS + "']][../../../../../../../../../descendant::span[text()='" + Helper.data_locale.BARS + "']]").expand()

    def collapse_windowshade_details_bar(self):
        get_windowshade(self.base_xpath, self.page,
                        supplement_base_xpath="[descendant::span[text()='" + Helper.data_locale.DETAILS + "']][../../../../../../../../../descendant::span[text()='" + Helper.data_locale.BARS + "']]").collapse()

    def set_check_apply_color_gradient(self):
        self.set_check_for_checkbox(label=Helper.data_locale.APPLY_COLOR_GRADIENT)

    def set_uncheck_apply_color_gradient(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.APPLY_COLOR_GRADIENT)

    def set_effect(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.EFFECT, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_url_variable_bar(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.URL_VARIABLE, section_label=Helper.data_locale.BARS,
                        column_name=column_name)

    def expand_windowshade_lines(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LINES)

    def collapse_windowshade_lines(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LINES)

    def set_check_show_labels_line(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_LABELS, section_label=Helper.data_locale.LINES)

    def set_uncheck_show_labels_line(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_LABELS, section_label=Helper.data_locale.LINES)

    def set_thickness_default(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.THICKNESS_DEFAULT_1_PIXEL, value=input_value)

    def set_thickness_increment(self, increment_number: int):
        self.click_increment_value_for_numeric_stepper(parent_label=Helper.data_locale.THICKNESS_DEFAULT_1_PIXEL,
                                                       times=increment_number)

    def set_thickness_decrement(self, decrement_number: int):
        self.click_decrement_value_for_numeric_stepper(parent_label=Helper.data_locale.THICKNESS_DEFAULT_1_PIXEL,
                                                       times=decrement_number)

    def set_color_transparency_line(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COLOR_TRANSPARENCY,
                                     section_label=Helper.data_locale.LINES, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_details_line(self):
        get_windowshade(self.base_xpath, self.page,
                        supplement_base_xpath="[descendant::span[text()='" + Helper.data_locale.DETAILS + "']][../../../../../../../../../descendant::span[text()='" + Helper.data_locale.LINES + "']]").expand()

    def collapse_windowshade_details_line(self):
        get_windowshade(self.base_xpath, self.page,
                        supplement_base_xpath="[descendant::span[text()='" + Helper.data_locale.DETAILS + "']][../../../../../../../../../descendant::span[text()='" + Helper.data_locale.LINES + "']]").collapse()

    def set_line_style(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_STYLE, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_url_variable_line(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.URL_VARIABLE, section_label=Helper.data_locale.LINES,
                        column_name=column_name)

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

    def set_option_for_display_label_for_x_axis(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DISPLAY_LABEL,
                                     section_label=Helper.data_locale.X_AXIS, item_index=item_index,
                                     item_value=item_value)

    def set_text_for_first_label_for_x_axis(self, input_text: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(), '" + Helper.data_locale.LABEL + "')]][../../../../following-sibling::div[1][.//label[text()=  '" + Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS + "']]][../../../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()= '" + Helper.data_locale.X_AXIS + "']]]").fill_text(
            input_text)

    def set_check_rotate_values_in_case_of_tick_collisions(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS)

    def set_uncheck_rotate_values_in_case_of_tick_collisions(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS)

    def set_rotate_degree(self, item_index=None, item_value=None):
        get_radio_group(self.base_xpath, self.page,
                        supplement_base_xpath="[../../../../descendant::label[contains(text(),'" + Helper.data_locale.ROTATE_VALUES_IN_CASE_OF_TICK_COLLISIONS + "')]]").set_check_for_index(
            index=item_index)

    def set_check_for_create_reference_line_for_x_axis(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                    section_label=Helper.data_locale.X_AXIS)

    def set_uncheck_for_create_reference_line_for_x_axis(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                      section_label=Helper.data_locale.X_AXIS)

    def set_reference_values_x_axis(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.REFERENCE_VALUE, item_index=item_index,
                                     item_value=item_value)

    def set_line_offset(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LINE_OFFSET, item_index=item_index,
                                     item_value=item_value)

    def set_reference_label_x(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                        item_index=item_index, item_value=item_value)

    def set_radio_reference_label_x_axis(self, item_index: int = None, item_value: str = None):
        get_radio_group(self.base_xpath, self.page,
                        supplement_base_xpath="[../../../../descendant::label[contains(text(),'" + Helper.data_locale.LINE_OFFSET + "')]]").set_check_for_index(
            index=item_index)

    def set_text_for_second_label_for_x_axis(self, input_text: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(), '" + Helper.data_locale.LABEL + "')]][../../../../preceding-sibling::div[1][.//label[text() = '" + Helper.data_locale.REFERENCE_VALUE_AS_LABEL + "']]][../../../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()= '" + Helper.data_locale.X_AXIS + "']]]").fill_text(
            input_text)

    def expand_windowshade_y_axis(self):
        self.expand_windowshade(parent_label=Helper.data_locale.Y_AXIS)

    def collapse_windowshade_y_axis(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.Y_AXIS)

    def set_check_use_zero_baseline(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_ZERO_BASELINE)

    def set_uncheck_use_zero_baseline(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_ZERO_BASELINE)

    def set_check_use_uniform_scale(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_UNIFORM_SCALE)

    def set_uncheck_use_uniform_scale(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_UNIFORM_SCALE)

    def set_check_show_grid_lines(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_GRID_LINES)

    def set_uncheck_show_grid_lines(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_GRID_LINES)

    def expand_windowshade_bar_axis(self):
        self.expand_windowshade(parent_label=Helper.data_locale.BAR_AXIS)

    def collapse_windowshade_bar_axis(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.BAR_AXIS)

    def set_option_for_display_label_for_bar_axis(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DISPLAY_LABEL,
                                     section_label=Helper.data_locale.BAR_AXIS, item_index=item_index,
                                     item_value=item_value)

    def set_text_for_first_label_for_bar_axis(self, input_text: str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(), '" + Helper.data_locale.LABEL + "')]][.. /../../../../../../ descendant::span[text() = '" + Helper.data_locale.BAR_AXIS + "']]").fill_text(
            input_text)

    def set_check_for_create_reference_line_for_bar_axis(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                    section_label=Helper.data_locale.BAR_AXIS)

    def set_uncheck_for_create_reference_line_for_bar_axis(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                      section_label=Helper.data_locale.BAR_AXIS)

    def set_radio_reference_label_bar_axis(self, item_index: int = None, item_value: str = None):
        get_radio_group(self.base_xpath, self.page,
                        supplement_base_xpath="[.. /../../../../../../ descendant::span[text() = '" + Helper.data_locale.BAR_AXIS + "']]").set_check_for_index(
            index=item_index)

    def expand_windowshade_line_axis(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LINE_AXIS)

    def collapse_windowshade_line_axis(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LINE_AXIS)

    def set_option_for_display_label_for_line_axis(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DISPLAY_LABEL,
                                     section_label=Helper.data_locale.LINE_AXIS, item_index=item_index,
                                     item_value=item_value)

    def set_check_for_create_reference_line_for_line_axis(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                    section_label=Helper.data_locale.LINE_AXIS)

    def set_uncheck_for_create_reference_line_for_line_axis(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_REFERENCE_LINE,
                                      section_label=Helper.data_locale.LINE_AXIS)

    def set_radio_reference_label_line_axis(self, item_index: int = None, item_value: str = None):
        get_radio_group(self.base_xpath, self.page,
                        supplement_base_xpath="[.. /../../../../../../ descendant::span[text() = '" + Helper.data_locale.LINE_AXIS + "']]").set_check_for_index(
            index=item_index)

    def expand_windowshade_legend(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LEGEND)

    def collapse_windowshade_legend(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LEGEND)

    def set_legend_location(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LEGEND_LOCATION, item_index=item_index,
                                     item_value=item_value)

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

    def set_width(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.WIDTH, value=input_value)

    def set_height(self, input_value: str):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.HEIGHT, value=input_value)
