"""
@author: Liu Jia
@date: 2024/09/05
@description: Define summary statistics pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class SummaryStatisticsPane(BasicStepPane)
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def