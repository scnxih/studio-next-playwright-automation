from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class Textarea(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//textarea[contains(@class, 'sas_components-TextArea')]"

    # If the page contains more than one textarea, data_test_id or aria-label is required.
    def __init__(self, container_base_xpath, page, data_test_id="", aria_label="", supplement_base_xpath="", textarea_label=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 aria_label=aria_label,supplement_base_xpath=supplement_base_xpath)
        if textarea_label != "":
            self.base_xpath += "[../../../descendant::label[contains(text(),'{0}')]]".format(textarea_label)

    def fill_text(self, text):
        self.scroll_if_needed(self.base_locator)
        self.fill(self.base_locator, text)
        self.key_press("Enter")

    def clear_text(self):
        self.scroll_if_needed(self.base_locator)
        self.clear(self.base_locator)

    def get_value(self):
        self.scroll_if_needed(self.base_locator)
        return self.get_attribute(self.base_locator, "text()")
