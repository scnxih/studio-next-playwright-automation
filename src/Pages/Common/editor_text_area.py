"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: September 9th, 2023
"""
import time

from src.Helper.helper import Helper
from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class EditorTextArea(CommonComponent):
    """
    Text Area for Editors
    """
    def set_base_xpath(self):
        # DOES NOT WORK
        # Would cause trouble in click() screenshot() and fill()
        # self.base_xpath += "//div[@class='monaco-editor no-user-select  showUnused showDeprecated vs']"

        # DOES NOT WORK
        # unavailable for *.xml *.json *.txt and *.workspace
        # self.base_xpath += "//div[@data-testid='programView-editorPane-editor']"

        self.base_xpath += "//div[contains(@data-testid, 'container')][contains(@class, 'EditorPane')]"

    def __init__(self, container_base_xpath, page):
        """
        Initialize Editor Text Area
        """
        # BasePage.__init__(self, page)
        # self.base_xpath = "//div[@class='monaco-editor no-user-select  showUnused showDeprecated vs']"

        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page)

    def get_text_area(self):
        """
        Get text area by xpath
        :return: Text area xpath
        """
        return self.locate_xpath(f"//textarea[@aria-label='" + Helper.data_locale.EDITOR_CONTENT + "']")

    def type_into_text_area(self, user_input):
        """
        :param user_input: content will be put into text area
        :return:
        """
        self.force_click(self.get_text_area())
        self.fill(self.get_text_area(), user_input)
        self.wait_for_page_load()
        # time.sleep(2)

        self.click_dialog_title_or_studionext_header()
        self.wait_for_page_load()

        # time.sleep(1)

        self.screenshot(self.base_xpath, "text_area")
        # time.sleep(1)

    def human_mimic_typing(self, user_input):
        """
        //div[contains(@data-testid, 'container')][contains(@class, 'EditorPane')]//div[contains(@data-testid,'editor' )]

        """
        self.force_click(self.get_text_area())

        # Jan 15 2025
        # self.page.get_by_test_id("programView-editorPane-editor").press_sequentially(user_input, delay=30)

        # Jan 15 2025
        self.get_text_area().press_sequentially(user_input, delay=30)

    def format_code_via_context_menu(self):
        """
        :param user_input: content will be put into text area
        :return:
        """
        self.force_click(self.get_text_area())
        self.wait_for_page_load(time_out=3000)

        # self.right_click(self.get_text_area())
        # self.right_click(self.get_text_area())
        self.key_press('Shift+F10')
        # self.wait_for_page_load(time_out=3000)
        self.get_by_test_id('editorPane-format').click()
        self.wait_for_page_load(time_out=3000)