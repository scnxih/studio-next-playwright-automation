import time

from src.Helper.helper import Helper
from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class Toolbar(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@role='group']"

    # When the page contains more than one toolbar, developer needs to specify any parameter of class_attribute,
    # data_test_id or supplement_base_xpath to discriminate the toolbar.
    def __init__(self, container_base_xpath, page, class_attribute="", data_test_id="", supplement_base_xpath=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 class_attribute=class_attribute, supplement_base_xpath=supplement_base_xpath)

    def btn_by_title_contains(self, title):
        return self.locate_xpath(f"//button[contains(@title,'{title}')]")

    def btn_by_title(self, title):
        return self.locate_xpath(f"//button[@title='{title}']")

    def div_by_title(self, title):
        return self.locate_xpath(f"//div[@title='{title}']")

    """Added by Alice on 09/25/2023 Start"""

    def btn_by_test_id_contains(self, data_test_id):
        return self.locate_xpath(f"//button[contains(@data-testid,'{data_test_id}')]")

    """Added by Alice on 09/25/2023 End"""

    def btn_by_test_id(self, data_test_id):
        return self.get_by_test_id(data_test_id)

    def click_btn_by_title_contains(self, title):
        if self.is_enabled(self.btn_by_title_contains(title)):
            self.click(self.btn_by_title_contains(title))
            return True
        else:
            Helper.logger.debug("This btn is disabled now:" + title)
            return False

    def click_div_by_title(self, title):
        if self.is_enabled(self.div_by_title(title)):
            self.click(self.div_by_title(title))
            return True
        else:
            Helper.logger.debug("This btn is disabled now:" + title)
            return False

    def click_btn_by_title(self, title):
        if self.is_enabled(self.btn_by_title(title)):
            self.click(self.btn_by_title(title))
            return True
        else:
            Helper.logger.debug("This btn is disabled now:" + title)
            return False

    """Added by Alice on 09/25/2023 Start"""

    def click_btn_by_test_id_contains(self, data_test_id):
        if self.is_enabled(self.btn_by_test_id_contains(data_test_id)):
            self.click(self.btn_by_test_id_contains(data_test_id))
            return True
        else:
            Helper.logger.debug("This btn is disabled now:" + data_test_id)
            return False

    """Added by Alice on 09/25/2023 End"""

    def click_btn_by_test_id(self, data_test_id):
        if self.is_enabled(self.btn_by_test_id(data_test_id)):
            self.click(self.btn_by_test_id(data_test_id))
            return True
        else:
            Helper.logger.debug("This btn is disabled now:" + data_test_id)
            return False

    def click_btn_menu_by_title(self, btn_title, *menu_item_text):
        enabled = self.click_btn_by_title(btn_title)
        if not enabled:
            return False
        time.sleep(0.3)
        return self.click_menu_item(*menu_item_text)

    def check_btn_menu_by_title(self, btn_title, *menu_item_text):
        enabled = self.click_btn_by_title(btn_title)
        if not enabled:
            return False
        time.sleep(0.3)
        self.check_menu_item(*menu_item_text)

    def uncheck_btn_menu_by_title(self, btn_title, *menu_item_text):
        enabled = self.click_btn_by_title(btn_title)
        if not enabled:
            return False
        time.sleep(0.3)
        self.uncheck_menu_item(*menu_item_text)

    def click_div_menu_by_title(self, btn_title, *menu_item_text):
        enabled = self.click_div_by_title(btn_title)
        if not enabled:
            return False
        time.sleep(0.3)
        return self.click_menu_item(*menu_item_text)

    def check_div_menu_by_title(self, btn_title, *menu_item_text):
        enabled = self.click_div_by_title(btn_title)
        if not enabled:
            return False
        time.sleep(0.3)
        self.check_menu_item(*menu_item_text)

    def uncheck_div_menu_by_title(self, btn_title, *menu_item_text):
        enabled = self.click_div_by_title(btn_title)
        if not enabled:
            return False
        time.sleep(0.3)
        self.uncheck_menu_item(*menu_item_text)

    def click_btn_menu_by_test_id_wait_until_enabled(self, data_test_id, *menu_item_text):
        enabled = self.wait_until_enabled(self.btn_by_test_id(data_test_id))
        if enabled:
            enabled = self.click_btn_by_test_id(data_test_id)
        if not enabled:
            return False
        time.sleep(0.3)
        return self.click_menu_item_wait_until_enabled(*menu_item_text)

    def click_btn_menu_by_test_id(self, data_test_id, *menu_item_text):
        enabled = self.click_btn_by_test_id(data_test_id)
        if not enabled:
            return False
        time.sleep(0.3)
        return self.click_menu_item(*menu_item_text)

    def check_btn_menu_by_test_id(self, data_test_id, *menu_item_text):
        enabled = self.click_btn_by_test_id(data_test_id)
        if not enabled:
            return False
        time.sleep(0.3)
        self.check_menu_item(*menu_item_text)

    def uncheck_btn_menu_by_test_id(self, data_test_id, *menu_item_text):
        enabled = self.click_btn_by_test_id(data_test_id)
        if not enabled:
            return False
        time.sleep(0.3)
        self.uncheck_menu_item(*menu_item_text)

    def click_menu_in_more_options(self, *menu_item_text):
        enabled = self.click_btn_by_title(Helper.data_locale.MORE_OPTIONS)
        if not enabled:
            return False
        time.sleep(0.3)
        return self.click_menu_item(*menu_item_text)

    def check_menu_in_more_options(self, *menu_item_text):
        enabled = self.click_btn_by_title(Helper.data_locale.MORE_OPTIONS)
        if not enabled:
            return False
        time.sleep(0.3)
        self.check_menu_item(*menu_item_text)
        time.sleep(0.3)

    def uncheck_menu_in_more_options(self, *menu_item_text):
        enabled = self.click_btn_by_title(Helper.data_locale.MORE_OPTIONS)
        if not enabled:
            return False
        time.sleep(0.3)
        self.uncheck_menu_item(*menu_item_text)
        time.sleep(0.3)

    def press_btn_by_test_id(self, data_test_id):
        is_pressed = self.is_button_pressed(self.btn_by_test_id(data_test_id))
        if is_pressed:
            return
        self.click(self.btn_by_test_id(data_test_id))

    def unpress_btn_by_test_id(self, data_test_id):
        is_pressed = self.is_button_pressed(self.btn_by_test_id(data_test_id))
        if is_pressed:
            self.click(self.btn_by_test_id(data_test_id))
