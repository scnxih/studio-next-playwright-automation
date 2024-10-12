"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: October 11th, 2024
"""

# -*- coding: UTF-8 -*-
import time
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class MinimumCutPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_select_a_server_for_this_step(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def set_from_node(self, column_name: str):
        """
        Data/From node
        """
        self.click_tab(Helper.data_locale.DATA)

        self.add_column(parent_label=Helper.data_locale.FROM_NODE,
                        column_name=column_name)

        self.screenshot_self("set_from_node")

    def set_to_node(self, column_name: str):
        """
        Data/To node
        """
        self.click_tab(Helper.data_locale.DATA)

        self.add_column(parent_label=Helper.data_locale.TO_NODE,
                        column_name=column_name)

        self.screenshot_self("set_to_node")
