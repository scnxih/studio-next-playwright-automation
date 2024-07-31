from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


def _is_div_class_contains_selected(div_class):
    if div_class.lower().find("radiobutton_selected") >= 0:
        return True
    return False


class RadioGroup(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@role='radiogroup']"

    # If the page contains more than one radio group, data_test_id is required.
    def __init__(self, container_base_xpath, page, data_test_id="",supplement_base_xpath="",parent_label=""):
        if parent_label != "":
            supplement_base_xpath = "[../../descendant::label[contains(text(),'{0}')]]".format(parent_label)
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)

    def div_radio_item(self, text):
        return self.locate_xpath(f"//label[text()='{text}']/../../..")

    # index starts from 0.
    def div_radio_item_for_index(self, index: int):
        index = index+1
        return self.locate_xpath(f"//child::div[{index}]")

    def is_checked(self, text):
        self.scroll_if_needed(self.base_locator)
        div_class = self.div_radio_item(text).get_attribute("class")
        return _is_div_class_contains_selected(div_class)

    # index starts from 0.
    def is_checked_for_index(self, index):
        self.scroll_if_needed(self.base_locator)
        div_class = self.div_radio_item_for_index(index).get_attribute("class")
        return _is_div_class_contains_selected(div_class)

    def set_check(self, text):
        if self.is_checked(text):
            return
        self.click(self.div_radio_item(text))

    # index starts from 0.
    def set_check_for_index(self, index: int):
        if self.is_checked_for_index(index):
            return
        self.click(self.div_radio_item_for_index(index))

    def get_radio_items_count(self):
        return self.locator_count("/child::div")

