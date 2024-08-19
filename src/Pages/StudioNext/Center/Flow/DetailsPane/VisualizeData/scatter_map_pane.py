"""
@author: Frank (Feng) Jiang
@date: 2024/08/19
@description: define panes of Scatter Map step
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class ScatterMapPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def expand_windowshade_plot_data(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PLOT_DATA)

    def collapse_windowshade_plot_data(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PLOT_DATA)

    def add_column_for_latitude(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LATITUDE, column_name=column_name)

    def add_column_for_longitude(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LONGITUDE, column_name=column_name)

    def add_column_for_group(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.GROUP, column_name=column_name)

    """Methods in Options tab"""
