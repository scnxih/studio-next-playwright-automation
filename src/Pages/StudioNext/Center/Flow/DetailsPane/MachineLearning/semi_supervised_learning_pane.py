"""
@author: Dommy (Fuying) Chen
@date: 2024/09/13
@description: define panes of Semi-supervised Learning step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class SemiSupervisedLearning(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def expand_windowshade_labeled(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LABELED)

    def collapse_windowshade_labeled(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NOTE_ABOUT_SERVER_SELECTION)