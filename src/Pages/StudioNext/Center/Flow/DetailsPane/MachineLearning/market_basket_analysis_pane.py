"""
@author: Alice
@date: 2025/06/18
@description: Define Market Basket Analysis pane
"""
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane



class MarketBasketAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_server(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_severity(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SEVERITY)