from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class Combobox(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@role='combobox']"

    # When the page contains more than one combobox, data_test_id is required.
    # If items count > 20, items_count is required.
    def __init__(self, container_base_xpath, page, data_test_id="", items_count=20):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id)
        self.items_count = items_count

    def selected_item_value(self):
        return self.get_inner_text(self.locate_xpath("//span[contains(@class,'Select-Select_label')]"))

    def _select_item_by_press_key(self, item_value):
        i = 0
        while self.selected_item_value() != item_value and i < self.items_count:
            self.key_press("ArrowDown")
            i += 1
        if self.selected_item_value() == item_value:
            self.key_press("Enter")
            Helper.logger.debug("find item in combobox:" + item_value)
            return True
        return False

    def select_item(self, item_value):
        """
        Description: select combobox item by keyboard ArrowUp or ArrowDown. Used for most of combobox out of treegrid.
        """
        self.scroll_if_needed(self.base_locator)
        if self.get_attribute(self.base_locator, "aria-expanded").lower() == "false":
            if self.selected_item_value() == item_value:
                return
            self.click(self.base_locator)
        for i in range(self.items_count):
            self.key_press("ArrowUp")
        return self._select_item_by_press_key(item_value)


    def choose_item(self, combo_item_text: str):
        """
        Description: select combobox item by mouse click. Used for combobox in treegrid.
        """
        self.click_self()
        self.scroll_if_needed(BasePage.combo_item_locator(self, combo_item_text))
        BasePage.click_combo_item(self, combo_item_text)

