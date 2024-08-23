"""
@author: Dommy (Fuying) Chen
@date: 2024/08/23
@description: define panes of Line Chart step
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class PokerHandProbabilityPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Options tab"""

    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
