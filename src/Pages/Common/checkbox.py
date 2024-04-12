from abc import ABC

from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import *


class Checkbox(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@role='checkbox']"

    # If the page contains more than one checkbox, data_test_id or label is required.
    def __init__(self,container_base_xpath, page, data_test_id="", label=""):
        CommonComponent.__init__(self,container_base_xpath=container_base_xpath,page=page,data_test_id=data_test_id,label=label)

    def is_checked(self):
        self.scroll_if_needed(self.base_locator)
        is_checked = self.base_locator.get_attribute("aria-checked")
        if is_checked == None:
            return False
        if is_checked.lower() == "false":
            return False
        return True

    def set_check(self):
        self.scroll_if_needed(self.base_locator)
        if not self.is_checked():
            if self.is_enabled(self.base_locator):
                self.click(self.base_locator)
            else:
                Helper.logger.debug("failed to click the checkbox {0} since it is disabled now!".format(self.label))

    def set_uncheck(self):
        self.scroll_if_needed(self.base_locator)
        if self.is_checked():
            if self.is_enabled(self.base_locator):
                self.click(self.base_locator)
            else:
                Helper.logger.debug("failed to click the checkbox {0} since it is disabled now!".format(self.label))