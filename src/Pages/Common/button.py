from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class Button(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//button[@type='button']"

    # When the page contains more than one combobox, data_test_id is required.
    # If items count > 20, items_count is required.
    def __init__(self, container_base_xpath, page, data_test_id="", aria_label="", title=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 aria_label=aria_label, title=title)

