"""
@author: Dommy (Fuying) Chen
@date: 2024/08/21
@description: define panes of Line Chart step
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class CoinTossSimulationPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Options tab"""

    def set_number_of_coins(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_COINS, input_text=input_text)

    def set_number_of_tosses(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_COINS, input_text=input_text)

    def expand_windowshade_output(self):
        self.expand_windowshade(parent_label=Helper.data_locale.OUTPUT)

    def collapse_windowshade_output(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.OUTPUT)

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_check_show_graph_table(self):
        self.set_check_for_checkbox(Helper.data_locale.SHOW_GRAPH_TABLE)

    def set_uncheck_show_graph_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SHOW_GRAPH_TABLE)

    def expand_windowshade_graph_options(self):
        self.expand_windowshade(parent_label=Helper.data_locale.OUTPUT)

    def collapse_windowshade_graph_options(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.OUTPUT)

    def set_check_grid_lines(self):
        self.set_check_for_checkbox(label=Helper.data_locale.GRID_LINES)

    def set_uncheck_grid_lines(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.GRID_LINES)

    def set_check_gradient_fill(self):
        self.set_check_for_checkbox(label=Helper.data_locale.GRADIENT_FILL)

    def set_uncheck_gradient_fill(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.GRADIENT_FILL)

    def set_check_data_skin(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DATA_SKIN)

    def set_uncheck_data_skin(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DATA_SKIN)