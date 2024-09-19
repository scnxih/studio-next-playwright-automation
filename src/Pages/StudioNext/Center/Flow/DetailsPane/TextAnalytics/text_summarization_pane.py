"""
@author: Dommy (Fuying) Chen
@date: 2024/09/19
@description: define panes of Text Summarization step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class TextSummarization(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_language(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LANGUAGE, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_text_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.TEXT_VARIABLE, column_name=column_name)

    def set_key_variable(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.KEY_VARIABLE, item_index=item_index,
                                        item_value=item_value)

    def add_column_for_key_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.KEY_VARIABLE, column_name=column_name)

    """Methods in Options tab"""

    def set_check_each_document(self):
        self.set_check_for_checkbox(label=Helper.data_locale.EACH_DOCUMENT)

    def set_uncheck_each_document(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.EACH_DOCUMENT)

    def set_check_entire_corpus(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ENTIRE_CORPUS)

    def set_uncheck_entire_corpus(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ENTIRE_CORPUS)

    def set_check_use_terms(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_TERMS)

    def set_uncheck_use_terms(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_TERMS)

    def set_check_use_entities_and_noun_groups(self):
        self.set_check_for_checkbox(label=Helper.data_locale.USE_ENTITIES_AND_NOUN_GROUPS)

    def set_uncheck_use_entities_and_noun_groups(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.USE_ENTITIES_AND_NOUN_GROUPS)

    """Methods in Output tab"""

    def expand_windowshade_document_summaries(self):
        self.expand_windowshade(parent_label=Helper.data_locale.DOCUMENT_SUMMARIES)

    def collapse_windowshade_document_summaries(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.DOCUMENT_SUMMARIES)

    def set_check_replace_existing_output_table_for_document(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table_for_document(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_include_variables_from_input_CAS_table(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INCLUDE_VARIABLES_FROM_THE_INPUT_CAS_TABLE,
                                        item_index=item_index,
                                        item_value=item_value)

    def add_columns_for_include_these_variables(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.INCLUDE_THESE_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def set_specify_data_to_show(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SPECIFY_DATA_TO_SHOW, item_index=item_index,
                                     item_value=item_value)

    def expand_windowshade_corpus_summary(self):
        self.expand_windowshade(parent_label=Helper.data_locale.CORPUS_SUMMARY)

    def collapse_windowshade_corpus_summary(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.CORPUS_SUMMARY)

    def set_check_replace_existing_output_table_for_corpus(self):
        self.set_check_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_uncheck_replace_existing_output_table_for_corpus(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)

    def set_check_show_output_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_OUTPUT_DATA)

    def set_uncheck_show_output_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)