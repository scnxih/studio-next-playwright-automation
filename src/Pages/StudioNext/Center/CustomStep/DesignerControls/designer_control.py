"""
Author: Alice
Date: Jan 29, 2024
Description: This is base class of all designer controls in Custom Step.
"""

from src.Pages.Common.base_page import *


class DesignerControl(BasePage):
    _data_testid_prefix = ""

    def __init__(self, page, control_number: int = 1):
        BasePage.__init__(self, page)
        # self.base_xpath += "//div[starts-with(@data-testid,'{0}-{1}')]".format(self._data_testid_prefix,control_number)
        self.base_xpath += "//div[@data-testid='{0}-{1}']".format(self._data_testid_prefix, control_number)

    def move_up(self):
        # Original
        self.click_context_menu_by_right_click(self.base_locator,Helper.data_locale.MOVE_UP)

        # Test control of the screenshot
        # self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.MOVE_UP, take_screenshot=True)

    def move_down(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.MOVE_DOWN)

    def move_to_top(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.MOVE_TO_TOP)

    def move_to_end(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.MOVE_TO_END)

    def move_to_section(self, section_text):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.MOVE_TO_SECTION, section_text)

    def move_to_page(self, page_text):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.MOVE_TO_PAGE, page_text)

    def duplicate(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.DUPLICATE)

    def delete(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.DELETE)

    def cut(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.CUT)

    def copy(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.COPY)

    def paste(self):
        self.click_context_menu_by_right_click(self.base_locator, Helper.data_locale.PASTE)
