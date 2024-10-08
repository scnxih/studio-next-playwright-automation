"""
@author: Liu Jia
@date: 2024/09/29
@description: Define Correspondence Analysis pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class CorrespondenceAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
