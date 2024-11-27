"""
@author: Alice
@date: 2024/11/22
@description: Define Aggregate Loss Models pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class AggregateLossModelsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_server(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_severity(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SEVERITY)

    def collapse_windowshade_severity(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.SEVERITY)

    def set_loss_severity_model(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SPECIFY_LOSS_SEVERITY_MODEL,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_count(self):
        self.expand_windowshade(parent_label=Helper.data_locale.COUNT)

    def collapse_windowshade_count(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.COUNT)

    def set_loss_count_model(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SPECIFY_LOSS_COUNT_MODEL,
                                        item_index=item_index, item_value=item_value)

    def set_count_model_type(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.COUNT_MODEL_TYPE,
                                        item_index=item_index, item_value=item_value)
    def set_filter_input_data(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_INPUT_DATA, input_text=input_text)

    """Methods in Severity tab"""
