"""
@author: Liu Jia
@date: 2024/09/03
@description: Define maximal cliques pane
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
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_LINKS_DATA, input_text=filter_text)
    def add_column_for_from_node(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FROM_NODE, column_name=column_name)
    def add_column_for_to_node(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.TO_NODE, column_name=column_name)

    """Methods in Options tab"""
    def set_check_maximum_number_of_cliques(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_MAXIMUM_NUMBER_OF_CLIQUES)
    def set_maximum_number_of_cliques(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_CLIQUES, input_text=input_text)
    def set_select_maximum_time(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.MAXIMUM_TIME_TIME, item_index=item_index, item_value=item_value)
    def set_maximum_time(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TIME_IN_SECONDS, input_text=input_text)
    def set_log_details(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LOG_DETAILS, item_index=item_index, item_value=item_value)
    def set_select_code_generation(self, item_index=None, item_value=None):
            self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_index=item_index, item_value=item_value)

    """Methods in Output tab"""
    def set_check_save_maximal_cliques_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_MAXIMAL_CLIQUES_DATA)
    def set_check_replace_existing_output_table(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_uncheck_replace_existing_output_table(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)



