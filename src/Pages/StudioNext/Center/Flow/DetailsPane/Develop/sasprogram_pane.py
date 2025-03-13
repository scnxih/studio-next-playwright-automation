"""
Author: Alice
Date: Mar 05, 2024
Description: This is SASProgram pane in flow Details pane.

"""
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.text import *
from src.Pages.Common.textarea import *
from src.Pages.Common.widget import Widget
from src.Utilities.enums import *


class SASProgramPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)
        self.widget = Widget(self.base_xpath, page)

    def type_into_text_area(self, user_input):
        self.editor.type_into_text_area(user_input)

    def fold_all_regions(self):
        self.click_context_menu(self.base_xpath, Helper.data_locale.FOLD_ALL_REGIONS)

    def unfold_all_regions(self):
        self.click_context_menu(self.base_xpath, Helper.data_locale.UNFOLD_ALL_REGIONS)

    def pop_find_widget(self):
        self.click_context_menu(self.base_xpath, Helper.data_locale.FIND)

    def find(self, find_str, if_match_case, if_match_whole_word):
        self.__switch_to_find_or_replace(FindOrReplace.find)
        self.__match_case(if_match_case)
        time.sleep(0.5)
        self.__match_whole_word(if_match_whole_word)
        time.sleep(0.5)
        self.widget.fill_textarea_by_placeholder(Helper.data_locale.FIND, find_str)
        time.sleep(0.5)

    def find_next(self):
        self.widget.click_btn_by_aria_label(Helper.data_locale.NEXT_MATCH)

    def find_previous(self):
        self.widget.click_btn_by_aria_label(Helper.data_locale.PREVIOUS_MATCH)

    def close_widget(self):
        self.widget.click_btn_by_aria_label(Helper.data_locale.CLOSE_ESCAPE)

    def __match_case(self, if_match_case: bool):
        if if_match_case:

            # Original
            # self.widget.toggle_on_checkbox_by_title(Helper.data_locale.MATCH_CASE)

            # Thursday, March 13, 2025, #2
            # Element in xpath changed to aria-lable from title for buttons
            # (Match Case, Match Whole Word and Use Regular Expression) in Code Editor Find widget.
            self.widget.toggle_on_checkbox_by_aria_label(Helper.data_locale.MATCH_CASE)
        else:
            # Original
            # self.widget.toggle_off_checkbox_by_title(Helper.data_locale.MATCH_CASE)

            # Thursday, March 13, 2025, #2
            # Element in xpath changed to aria-lable from title for buttons
            # (Match Case, Match Whole Word and Use Regular Expression) in Code Editor Find widget.
            self.widget.toggle_on_checkbox_by_aria_label(Helper.data_locale.MATCH_CASE)

    def __match_whole_word(self, if_match_whole_word: bool):
        if if_match_whole_word:
            # Original
            # self.widget.toggle_on_checkbox_by_title(Helper.data_locale.MATCH_WHOLE_WORD)

            # Changed on Thursday, Mar 13, 2025
            self.widget.toggle_on_checkbox_by_aria_label(Helper.data_locale.MATCH_WHOLE_WORD)

        else:
            # Original
            # self.widget.toggle_off_checkbox_by_title(Helper.data_locale.MATCH_WHOLE_WORD)

            # Changed on Thursday, Mar 13, 2025
            self.widget.toggle_on_checkbox_by_aria_label(Helper.data_locale.MATCH_WHOLE_WORD)

    def __preserve_case(self, if_preserve_case: bool):
        if if_preserve_case:
            # Original
            # self.widget.toggle_on_checkbox_by_title(Helper.data_locale.PRESERVE_CASE)

            # Changed on Thursday, Mar 13, 2025
            self.widget.toggle_on_checkbox_by_aria_label(Helper.data_locale.PRESERVE_CASE)
        else:
            # Original
            # self.widget.toggle_off_checkbox_by_title(Helper.data_locale.PRESERVE_CASE)
            # Changed on Thursday, Mar 13, 2025
            self.widget.toggle_off_checkbox_by_aria_label(Helper.data_locale.PRESERVE_CASE)

    def __replace_visible(self):
        if self.is_visible(self.widget.textarea_by_placeholder(Helper.data_locale.REPLACE)):
            return True
        return False

    def __switch_to_find_or_replace(self, find_or_replace: FindOrReplace):
        if find_or_replace == FindOrReplace.find:
            if self.__replace_visible():
                self.widget.click_btn_by_aria_label(Helper.data_locale.TOGGLE_REPLACE)
        else:
            if not self.__replace_visible():
                self.widget.click_btn_by_aria_label(Helper.data_locale.TOGGLE_REPLACE)

    def __internal_replace(self, find_str, replace_str, if_match_case, if_match_whole_word, if_preserve_case):
        self.__switch_to_find_or_replace(FindOrReplace.replace)
        self.widget.fill_textarea_by_placeholder(Helper.data_locale.FIND, find_str)
        time.sleep(0.3)
        self.widget.fill_textarea_by_placeholder(Helper.data_locale.REPLACE, replace_str)
        time.sleep(0.3)
        self.__match_case(if_match_case)
        time.sleep(0.3)
        self.__match_whole_word(if_match_whole_word)
        time.sleep(0.3)
        self.__preserve_case(if_preserve_case)
        time.sleep(0.3)

    def replace(self, find_str, replace_str, if_match_case, if_match_whole_word, if_preserve_case):
        self.__internal_replace(find_str, replace_str, if_match_case, if_match_whole_word, if_preserve_case)
        self.widget.click_btn_by_title(Helper.data_locale.REPLACE_ENTER)

    def replace_all(self, find_str, replace_str, if_match_case, if_match_whole_word, if_preserve_case):
        self.__internal_replace(find_str, replace_str, if_match_case, if_match_whole_word, if_preserve_case)

        # Original
        # self.widget.click_btn_by_title(Helper.data_locale.REPLACE_ALL_ENTER)

        # Changed on Thursday, March 13, 2025
        # Element in xpath changed to aria-lable from title for buttons
        # (Match Case, Match Whole Word and Use Regular Expression) in Code Editor Find widget.
        self.widget.click_btn_by_aria_label(Helper.data_locale.REPLACE_ALL_ENTER)
