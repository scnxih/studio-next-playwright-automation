"""
@author: Frank (Feng) Jiang
@date: 2024/09/27
@description: define panes of Mosaic Plot step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class MosaicPlotPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def add_column_for_y_axis(self, col_name: str):
        self.add_column(Helper.data_locale.Y_AXIS_LOWER, col_name)

    def delete_column_for_y_axis(self):
        self.delete_column(Helper.data_locale.Y_AXIS_LOWER)

    def add_column_for_X_axis(self, col_name: str):
        self.add_column(Helper.data_locale.X_AXIS_LOWER, col_name)

    def delete_column_for_x_axis(self):
        self.delete_column(Helper.data_locale.X_AXIS_LOWER)

    def add_columns_for_stratify_by(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.STRATIFY_BY, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_stratify_by(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.STRATIFY_BY, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_group_analysis_by(self, col_name: str):
        self.add_column(Helper.data_locale.GROUP_ANALYSIS_BY, col_name)

    def delete_column_for_group_analysis_by(self):
        self.delete_column(Helper.data_locale.GROUP_ANALYSIS_BY)

    def add_column_for_freq_count(self, col_name: str):
        self.add_column(Helper.data_locale.FREQUENCY_COUNT, col_name)

    def delete_column_for_freq_count(self):
        self.delete_column(Helper.data_locale.FREQUENCY_COUNT)

    """Methods in Options tab"""

    def set_check_square_plot(self):
        self.set_check_for_checkbox(Helper.data_locale.SQUARE_PLOT)

    def set_uncheck_square_plot(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SQUARE_PLOT)

    def select_color_tiles_by(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.COLOR_TILES_BY, item_value=item_value)
