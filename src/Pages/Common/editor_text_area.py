"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: September 9th, 2023
"""
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
        self.fill(self.get_text_area(), user_input)
        self.screenshot_trivial(self.base_xpath, "text_area")


