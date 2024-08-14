"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 13th, 2024
"""
# -*- coding: UTF-8 -*-
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class BoxPlotPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_analysis_variable(self, column_name: str):
        """
        Analysis variable
        """
        self.set_column(parent_label="分析变量", column_name=column_name)
