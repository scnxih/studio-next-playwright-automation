"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 21st, 2024
"""

# -*- coding: UTF-8 -*-
import time
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class CapabilityAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_process_variable(self, column_name: str):
        """
        Data/Process variable
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.add_column(parent_label=Helper.data_locale.PROCESS_VARIABLE,
                        column_name=column_name)

        self.screenshot_self("set_process_variable")

    def set_target_value_to(self, target_value: str):
        """
        Switch to Data tab page, expand and set target value
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.expand_windowshade(Helper.data_locale.SPECIFICATION_LIMITS)

        self.set_text_for_text_control(parent_label=Helper.data_locale.TARGET_VALUE,
                                       input_text=target_value)

        self.screenshot_self("set_target_value_to")

        self.collapse_windowshade(Helper.data_locale.SPECIFICATION_LIMITS)

    def set_lower_limit_to(self, lower_limit: str):
        """
        Switch to Data tab page, expand and set lower limit value
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.expand_windowshade(Helper.data_locale.SPECIFICATION_LIMITS)

        self.set_text_for_text_control(parent_label=Helper.data_locale.LOWER_LIMIT,
                                       input_text=lower_limit)

        self.screenshot_self("set_lower_limit_to")

        self.collapse_windowshade(Helper.data_locale.SPECIFICATION_LIMITS)

    def set_upper_limit_to(self, upper_limit: str):
        """
        Switch to Data tab page, expand and set lower limit value
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.expand_windowshade(Helper.data_locale.SPECIFICATION_LIMITS)

        self.set_text_for_text_control(parent_label=Helper.data_locale.UPPER_LIMIT,
                                       input_text=upper_limit)

        self.screenshot_self("set_upper_limit_to")

        self.collapse_windowshade(Helper.data_locale.SPECIFICATION_LIMITS)

    def set_classification_variable(self, column_name: str):
        """
        Data/Classification variable
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

        self.add_column(parent_label=Helper.data_locale.CLASSIFICATION_VARIABLE,
                        column_name=column_name)

        self.screenshot_self("set_classification_variable")

        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def set_group_analysis_by(self, column_name: str):
        """
        Data/Classification variable
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

        self.add_column(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                        column_name=column_name)

        self.screenshot_self("set_group_analysis_by")

        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)
