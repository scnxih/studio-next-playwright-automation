"""
Author: Alice
Date: Apr 09, 2024
Description: This is window shade.
"""


from src.Pages.Common.common_component import *


class WindowShade(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@class='sas_components-WindowShade-WindowShade_header'][@role='button']"

    # If the page contains more than one checkbox, data_test_id or label is required.
    def __init__(self,container_base_xpath, page, supplement_base_xpath="",parent_label=""):
        if parent_label != "":
            supplement_base_xpath = "[descendant::span[text()='{0}']]".format(parent_label)
        CommonComponent.__init__(self,container_base_xpath=container_base_xpath,page=page,supplement_base_xpath=supplement_base_xpath)

    def is_expanded(self):
        if self.get_attribute(self.base_xpath,"aria-expanded").lower() == "true":
            return True
        return False

    def expand(self):
        if self.is_expanded():
            return
        self.click_self()

    def collapse(self):
        if self.is_expanded():
            self.click_self()




