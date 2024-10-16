"""
@author: Frank (Feng) Jiang
@date: 2024/09/29
@description: define panes of Boolean Rules step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *
from src.Pages.StudioNext.Dialog.select_a_value_dialog import *


class BooleanRulesPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)
        self.sv_dialog = SelectAValueDialog(page)

    """Methods in Data tab"""

    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def set_input_table_contains(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.INPUT_TABLE_CONTAINS, item_value=radio_btn_label)

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

    def expand_windowshade_target(self):
        self.expand_windowshade(Helper.data_locale.TARGET)

    def collapse_windowshade_target(self):
        self.collapse_windowshade(Helper.data_locale.TARGET)

    def set_type_of_target(self, radio_btn_label: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.TYPE_OF_TARGET, item_value=radio_btn_label)

    def add_column_for_nominal_target(self, col_name: str):
        self.add_column(Helper.data_locale.NOMINAL_TARGET, col_name)

    def delete_column_for_nominal_target(self):
        self.delete_column(Helper.data_locale.NOMINAL_TARGET)

    def add_column_for_primary_binary_target(self, col_name: str):
        self.add_column(Helper.data_locale.PRIMARY_BINARY_TARGET, col_name)

    def delete_column_for_primary_binary_target(self):
        self.delete_column(Helper.data_locale.PRIMARY_BINARY_TARGET)

    def add_columns_for_additional_binary_targets(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.add_columns(Helper.data_locale.ADDITIONAL_BINARY_TARGETS, check_column_name_list=check_columns_list,
                         uncheck_column_name_list=uncheck_columns_list)

    def delete_columns_for_additional_binary_targets(self, check_columns_list: list, uncheck_columns_list: list = None):
        self.delete_columns_for_listbox(Helper.data_locale.ADDITIONAL_BINARY_TARGETS, check_column_name_list=check_columns_list,
                                        uncheck_column_name_list=uncheck_columns_list)

    def select_level_of_interest(self, item_value: str):
        self.set_option_for_combobox(Helper.data_locale.LEVEL_OF_INTEREST, item_value=item_value)

    def click_select_a_value_btn(self):
        get_button(self.base_xpath, self.page, aria_label=Helper.data_locale.SELECT_A_VALUE).click_self()

    def select_value_from_select_a_value_dialog(self, value: str):
        self.click_select_a_value_btn()
        self.sv_dialog.select_a_value_and_OK(value)

    """Methods in Options tab"""

    def expand_windowshade_parse_text_in_options_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[text()='{1}']]").format(Helper.data_locale.PARSE_TEXT, Helper.data_locale.STEM_TERMS)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            return
        self.click(self.base_xpath)

    def collapse_windowshade_parse_text_in_options_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[text()='{1}']]").format(Helper.data_locale.PARSE_TEXT, Helper.data_locale.STEM_TERMS)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            self.click(self.base_xpath)

    def set_check_include_parts_of_speech(self):
        self.set_check_for_checkbox(Helper.data_locale.INCLUDE_PARTS_OF_SPEECH)

    def set_uncheck_include_parts_of_speech(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.INCLUDE_PARTS_OF_SPEECH)

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

    def set_min_num_of_occu_to_keep_a_term(self, num_of_occu: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.MIN_NUM_OF_OCCURRENCES_TO_KEEP_A_TERM, num_of_occu)

    def increase_min_num_of_occu_to_keep_a_term(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.MIN_NUM_OF_OCCURRENCES_TO_KEEP_A_TERM, times)

    def decrease_min_num_of_occu_to_keep_a_term(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.MIN_NUM_OF_OCCURRENCES_TO_KEEP_A_TERM, times)

    def set_check_use_the_log_to_weight_the_cellls_of_the_term_by_doc_matrix(self):
        self.set_check_for_checkbox(Helper.data_locale.USE_THE_LOG_TO_WEIGHT_THE_CELLS_OF_THE_TERM_BY_DOC_MATRIX)

    def set_uncheck_use_the_log_to_weight_the_cellls_of_the_term_by_doc_matrix(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.USE_THE_LOG_TO_WEIGHT_THE_CELLS_OF_THE_TERM_BY_DOC_MATRIX)

    def select_weight_terms_by(self, combo_option: str):
        self.set_option_for_combobox(Helper.data_locale.WEIGHT_TERMS_BY, item_value=combo_option)

    def set_check_specify_a_start_or_stop_list(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_A_START_OR_STOP_LIST)

    def set_uncheck_specify_a_start_or_stop_list(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_A_START_OR_STOP_LIST)

    def select_list_type(self, list_type: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.LIST_TYPE, item_value=list_type)

    def select_stop_list_type(self, stop_list_type: str):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.STOP_LIST_TYPE, item_value=stop_list_type)

    def set_check_specify_a_synonym_list(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_A_SYNONYM_LIST)

    def set_uncheck_specify_a_synonym_list(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_A_SYNONYM_LIST)

    def set_check_specify_a_multi_word_terms_list(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_A_MULTI_WORD_TERMS_LIST)

    def set_uncheck_specify_a_multi_word_terms_list(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_A_MULTI_WORD_TERMS_LIST)

    def expand_windowshade_rules_extraction_in_options_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[contains(text(), '{1}')]]").format(Helper.data_locale.RULES_EXTRACTION, Helper.data_locale.MIN_G_SCORE)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            return
        self.click(self.base_xpath)

    def collapse_windowshade_rules_extraction_in_options_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[contains(text(), '{1}')]]").format(Helper.data_locale.RULES_EXTRACTION, Helper.data_locale.MIN_G_SCORE)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            self.click(self.base_xpath)

    def set_min_num_of_docs_in_which_a_term_must_appear_to_be_used_in_a_rule(self, num_of_doc: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.MIN_NUM_OF_DOCS_IN_WHICH_A_TERM_MUST_APPEAR_TO_BE_USED_IN_A_RULE, num_of_doc)

    def increase_min_num_of_docs_in_which_a_term_must_appear_to_be_used_in_a_rule(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.MIN_NUM_OF_DOCS_IN_WHICH_A_TERM_MUST_APPEAR_TO_BE_USED_IN_A_RULE, times)

    def decrease_min_num_of_docs_in_which_a_term_must_appear_to_be_used_in_a_rule(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.MIN_NUM_OF_DOCS_IN_WHICH_A_TERM_MUST_APPEAR_TO_BE_USED_IN_A_RULE, times)

    def set_min_g_score(self, g_score: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.MIN_G_SCORE, g_score)

    def increase_min_g_score(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.MIN_G_SCORE, times)

    def decrease_min_g_score(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.MIN_G_SCORE, times)

    def set_check_specify_separate_min_g_score_for_neg_terms(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_SEPARATE_MIN_G_SCORE_FOR_NEGATIVE_TERMS)

    def set_uncheck_specify_separate_min_g_score_for_neg_terms(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_SEPARATE_MIN_G_SCORE_FOR_NEGATIVE_TERMS)

    def set_min_g_score_for_neg_terms(self, g_score_neg_term: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.MIN_G_SCORE_FOR_NEGATIVE_TERMS, g_score_neg_term)

    def increase_min_g_score_for_neg_terms(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.MIN_G_SCORE_FOR_NEGATIVE_TERMS, times)

    def decrease_min_g_score_for_neg_terms(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.MIN_G_SCORE_FOR_NEGATIVE_TERMS, times)

    def set_min_m_value_for_computing_estimated_precision(self, min_m_value: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.MIN_M_VALUE_FOR_COMPUTING_ESTIMATED_PRECISION, min_m_value)

    def increase_min_m_value_for_computing_estimated_precision(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.MIN_M_VALUE_FOR_COMPUTING_ESTIMATED_PRECISION, times)

    def decrease_min_m_value_for_computing_estimated_precision(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.MIN_M_VALUE_FOR_COMPUTING_ESTIMATED_PRECISION, times)

    def set_check_specify_separate_min_m_value_for_neg_terms(self):
        self.set_check_for_checkbox(Helper.data_locale.SPECIFY_SEPARATE_MIN_M_VALUE_FOR_NEGATIVE_TERMS)

    def set_uncheck_specify_separate_min_m_value_for_neg_terms(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SPECIFY_SEPARATE_MIN_M_VALUE_FOR_NEGATIVE_TERMS)

    def set_min_m_value_for_neg_terms(self, min_m_value: str):
        self.set_value_for_numeric_stepper(Helper.data_locale.MIN_M_VALUE_FOR_NEGATIVE_TERMS, min_m_value)

    def increase_min_m_value_for_neg_terms(self, times: int):
        self.click_increment_value_for_numeric_stepper(Helper.data_locale.MIN_M_VALUE_FOR_NEGATIVE_TERMS, times)

    def decrease_min_m_value_for_neg_terms(self, times: int):
        self.click_decrement_value_for_numeric_stepper(Helper.data_locale.MIN_M_VALUE_FOR_NEGATIVE_TERMS, times)

    """Methods in Output tab"""

    def expand_windowshade_parse_text_in_output_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[text()='{1}']]").format(Helper.data_locale.PARSE_TEXT, Helper.data_locale.SAVE_PARSED_TERM_INFO)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            return
        self.click(self.base_xpath)

    def collapse_windowshade_parse_text_in_output_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[text()='{1}']]").format(Helper.data_locale.PARSE_TEXT, Helper.data_locale.SAVE_PARSED_TERM_INFO)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            self.click(self.base_xpath)

    def set_check_save_term_by_doc_matrix(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_TERM_BY_DOCUMENT_MATRIX)

    def set_uncheck_save_term_by_doc_matrix(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_TERM_BY_DOCUMENT_MATRIX)

    def set_check_replace_existing_output_table_for_save_term_by_doc_matrix(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TERM_BY_DOCUMENT_MATRIX)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_term_by_doc_matrix(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_TERM_BY_DOCUMENT_MATRIX)).set_uncheck()

    def set_check_save_parsed_term_info(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_PARSED_TERM_INFO)

    def set_uncheck_save_parsed_term_info(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_PARSED_TERM_INFO)

    def set_check_replace_existing_output_table_for_save_parsed_term_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_PARSED_TERM_INFO)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_parsed_term_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_PARSED_TERM_INFO)).set_uncheck()

    def set_check_save_parsing_config(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_PARSING_CONFIG_FOR_BOOLEAN_RULES_SCORING)

    def set_uncheck_save_parsing_config(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_PARSING_CONFIG_FOR_BOOLEAN_RULES_SCORING)

    def set_check_replace_existing_output_table_for_save_parsing_config(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_PARSING_CONFIG_FOR_BOOLEAN_RULES_SCORING)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_parsing_config(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_PARSING_CONFIG_FOR_BOOLEAN_RULES_SCORING)).set_uncheck()

    def expand_windowshade_rules_extraction_in_output_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[text()='{1}']]").format(Helper.data_locale.RULES_EXTRACTION, Helper.data_locale.SAVE_RULES)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            return
        self.click(self.base_xpath)

    def collapse_windowshade_rules_extraction_in_output_tab(self):
        self.base_xpath = ("//div[contains(@class,'sas_components-WindowShade-WindowShade_header')][@role='button']"
                           "[descendant::span[text()='{0}']][./../../../following-sibling::section[1]//label"
                           "[text()='{1}']]").format(Helper.data_locale.RULES_EXTRACTION, Helper.data_locale.SAVE_RULES)
        if self.get_attribute(self.base_xpath, "aria-expanded").lower() == "true":
            self.click(self.base_xpath)

    def set_check_save_rules(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_RULES)

    def set_uncheck_save_rules(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_RULES)

    def set_check_replace_existing_output_table_for_save_rules(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_RULES)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_rules(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_RULES)).set_uncheck()

    def set_check_save_rule_term_info(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_RULE_TERM_INFO)

    def set_uncheck_save_rule_term_info(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_RULE_TERM_INFO)

    def set_check_replace_existing_output_table_for_save_rule_term_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_RULE_TERM_INFO)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_rule_term_info(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_RULE_TERM_INFO)).set_uncheck()

    def set_check_save_candidate_terms(self):
        self.set_check_for_checkbox(Helper.data_locale.SAVE_CANDIDATE_TERMS)

    def set_uncheck_save_candidate_terms(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SAVE_CANDIDATE_TERMS)

    def set_check_replace_existing_output_table_for_save_candidate_terms(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_CANDIDATE_TERMS)).set_check()

    def set_uncheck_replace_existing_output_table_for_save_candidate_terms(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']/../../../../../../preceding-sibling::div[3]"
                                           "//label[contains(text(),'{1}')]]"
                     .format(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,
                             Helper.data_locale.SAVE_CANDIDATE_TERMS)).set_uncheck()
