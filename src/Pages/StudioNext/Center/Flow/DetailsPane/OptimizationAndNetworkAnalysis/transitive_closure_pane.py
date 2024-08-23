"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 23rd, 2024
"""

# -*- coding: UTF-8 -*-
import time
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class TransitiveClosurePane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)
