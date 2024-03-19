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

    def find(self, find_str, if_match_case, if_match_whole_word):
        self.click_context_menu(self.base_xpath, Helper.data_locale.FIND)
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
            self.widget.toggle_on_checkbox_by_title(Helper.data_locale.MATCH_CASE)
        else:
            self.widget.toggle_off_checkbox_by_title(Helper.data_locale.MATCH_CASE)

    def __match_whole_word(self, if_match_whole_word: bool):
        if if_match_whole_word:
            self.widget.toggle_on_checkbox_by_title(Helper.data_locale.MATCH_WHOLE_WORD)
        else:
            self.widget.toggle_off_checkbox_by_title(Helper.data_locale.MATCH_WHOLE_WORD)
