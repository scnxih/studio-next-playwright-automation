"""
@author: Frank (Feng) Jiang
@date: 2024/09/26
@description: define panes of Segmentation step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class SegmentationPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def input_filter_input_data(self, filter_expression: str):
        self.set_text_for_text_control(Helper.data_locale.FILTER_INPUT_DATA, input_text=filter_expression)

    def empty_filter_input_data(self):
        self.set_text_for_text_control(Helper.data_locale.FILTER_INPUT_DATA, input_text="")

    def select_language(self, lang: str):
        self.set_option_for_combobox(Helper.data_locale.LANGUAGE, item_value=lang)

    def add_column_for_text_var(self, col_name: str):
        self.add_column(Helper.data_locale.TEXT_VARIABLE, col_name)

    def delete_column_for_text_var(self):
        self.delete_column(Helper.data_locale.TEXT_VARIABLE)

    def set_key_var(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.KEY_VARIABLE, item_value=radio_btn_label)

    def add_column_for_key_var(self, col_name: str):
        self.add_column(Helper.data_locale.KEY_VARIABLE, col_name)

    def delete_column_for_key_var(self):
        self.delete_column(Helper.data_locale.KEY_VARIABLE)

    """Methods in Options tab"""

    def expand_windowshade_parse_text(self):
        self.expand_windowshade(Helper.data_locale.PARSE_TEXT)

    def collapse_windowshade_parse_text(self):
        self.collapse_windowshade(Helper.data_locale.PARSE_TEXT)

    def set_check_extract_noun_groups(self):
        self.set_check_for_checkbox(Helper.data_locale.EXTRACT_NOUN_GROUPS)

    def set_uncheck_extract_noun_groups(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.EXTRACT_NOUN_GROUPS)

    def set_check_extract_entities(self):
        self.set_check_for_checkbox(Helper.data_locale.EXTRACT_ENTITIES)

    def set_uncheck_extract_entities(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.EXTRACT_ENTITIES)

    def set_check_stem_terms(self):
        self.set_check_for_checkbox(Helper.data_locale.STEM_TERMS)

    def set_uncheck_stem_terms(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.STEM_TERMS)

    def set_check_specify_a_start_list(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_A_START_LIST)

    def set_uncheck_specify_a_start_list(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_A_START_LIST)

    def expand_windowshade_segmentation(self):
        self.expand_windowshade(Helper.data_locale.STEP_SEGMENTATION)

    def collapse_windowshade_segmentation(self):
        self.collapse_windowshade(Helper.data_locale.STEP_SEGMENTATION)

    def set_num_of_segments(self, num_of_segments: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.NUM_OF_SEGMENTS, num_of_segments)

    def increase_num_of_segments(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.NUM_OF_SEGMENTS, times)

    def decrease_num_of_segments(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.NUM_OF_SEGMENTS, times)

    def expand_windowshade_details(self):
        self.expand_windowshade(Helper.data_locale.DETAILS)

    def collapse_windowshade_details(self):
        self.collapse_windowshade(Helper.data_locale.DETAILS)

    def set_check_random_number_seed(self):
        self.set_check_for_checkbox(Helper.data_locale.RANDOM_NUMBER_SEED)

    def set_uncheck_random_number_seed(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.RANDOM_NUMBER_SEED)

    def input_random_seed(self, random_seed: str):
        self.set_text_for_text_control(Helper.data_locale.RANDOM_SEED, input_text=random_seed)

    def empty_random_seed(self):
        self.set_text_for_text_control(Helper.data_locale.RANDOM_SEED, input_text="")

    def set_check_max_num_of_iterations(self):
        self.set_check_for_checkbox(Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS)

    def set_uncheck_max_num_of_iterations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS)

    def input_num_of_iterations(self, iter_num: str):
        self.set_text_for_text_control(Helper.data_locale.NUMBER_OF_ITERATIONS, input_text=iter_num)

    def empty_num_of_iterations(self):
        self.set_text_for_text_control(Helper.data_locale.NUMBER_OF_ITERATIONS, input_text="")

    """Methods in Output tab"""

    def set_check_replace_existing_output_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../following-sibling::div[1]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_SEGMENTATION_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../following-sibling::div[1]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_SEGMENTATION_RESULTS)).set_uncheck()

    def set_check_save_segmentation_results(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_SEGMENTATION_RESULTS)

    def set_uncheck_save_segmentation_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_SEGMENTATION_RESULTS)

    def set_check_replace_existing_output_table_for_save_segmentation_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_SEGMENTATION_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_segmentation_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_SEGMENTATION_RESULTS)).set_uncheck()

    def set_check_save_segment_stat(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_SEGMENT_STAT)

    def set_uncheck_save_segment_stat(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_SEGMENT_STAT)

    def set_check_replace_existing_output_table_for_save_segment_stat(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_SEGMENT_STAT)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_segment_stat(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_SEGMENT_STAT)).set_uncheck()

    def set_check_save_doc_term_segmentation_results(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_DOC_TERM_SEGMENTATION_RESULTS)

    def set_uncheck_save_doc_term_segmentation_results(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_DOC_TERM_SEGMENTATION_RESULTS)

    def set_check_replace_existing_output_table_for_save_doc_term_segmentation_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_DOC_TERM_SEGMENTATION_RESULTS)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_doc_term_segmentation_results(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_DOC_TERM_SEGMENTATION_RESULTS)).set_uncheck()

    def set_check_save_term_info(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_TERM_INFO)

    def set_uncheck_save_term_info(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_TERM_INFO)

    def set_check_replace_existing_output_table_for_save_term_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TERM_INFO)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_term_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TERM_INFO)).set_uncheck()
