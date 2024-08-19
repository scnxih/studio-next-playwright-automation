"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 19th, 2024
"""
# -*- coding: UTF-8 -*-
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class TextParsingAndTopicAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_input_table_contains(self, item_index: int = None, item_value: str = None):
        """
        The input table contains:
        0  Unparsed Text
        1  Term-by-document matrix

        """
        self.click_Tab(Helper.data_locale.DATA)

        self.set_option_for_radio_group(parent_label="",
                                        item_index=item_index,
                                        item_value=item_value)

        self.screenshot_self("set_plot_orientation")
