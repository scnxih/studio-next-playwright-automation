from src.Pages.Common.common_component import *


class SwitchButton(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//button[@role='switch']"

    # If the page contains more than one checkbox, data_test_id or label is required.
    def __init__(self, container_base_xpath, page, data_test_id=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id)

    def is_on(self):
        self.scroll_if_needed(self.base_locator)
        is_checked = self.base_locator.get_attribute("aria-checked")
        if is_checked == None:
            return False
        if is_checked.lower() == "false":
            return False
        return True

    def turn_on(self):
        if not self.is_on():
            self.click(self.base_locator)

    def turn_off(self):
        if self.is_on():
            self.click(self.base_locator)
