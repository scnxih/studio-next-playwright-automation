"""
@author: Liu Jia
@date: 2024/09/03
@description: Define Maximal Cliques pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *
class MaximalCliquesPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_select_server_for_step(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,item_index=item_index,item_value=item_value)

    def set_filter_link_data(self,filter_text:str):
        self.click_Tab(Helper.data_locale.DATA)
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_, input_text=filter_text)
