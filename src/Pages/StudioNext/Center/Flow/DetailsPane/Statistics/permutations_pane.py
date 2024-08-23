"""
@File: permutations
@Author: Allison
@Date: 8/21/2024 2:54 AM 
@Description: 

"""
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class Permutations(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

        """Options tab"""
    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)