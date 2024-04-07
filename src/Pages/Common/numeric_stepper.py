from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class NumericStepper(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@class='sas_components-NumericStepper-NumericStepper_container']"

    # If the page contains more than one radio group, data_test_id is required.
    def __init__(self, container_base_xpath, page, data_test_id="",supplement_base_xpath=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)

    @property
    def btn_decrement_value(self):
        return self.locate_xpath("//button[@aria-label='{0}']".format(Helper.data_locale.DECREMENT_VALUE))

    @property
    def btn_increment_value(self):
        return self.locate_xpath("//button[@aria-label='{0}']".format(Helper.data_locale.INCREMENT_VALUE))

    @property
    def input(self):
        return self.locate_xpath(
            "//input[contains(@class, 'sas_components-Input-Input_input')]")

    def click_decrement_value(self, times=None):
        """
        Description: click decrement button to increase value of number stepper.
        :param times: int value, great than 0, optional. If not set this param, click decrement button once.
        """
        self.scroll_if_needed(self.base_locator)
        if times is None:
            if self.get_attribute(self.btn_decrement_value, "aria-disabled").lower() == "false":
                self.click(self.btn_decrement_value)
                return True
            else:
                Helper.logger.debug("the decrement_value button is disabled, so failed to click it")
                return False
        else:
            i = 0
            while i < times:
                if self.get_attribute(self.btn_decrement_value, "aria-disabled").lower() == "false":
                    self.click(self.btn_decrement_value)
                    i += 1
                    if i == times:
                        return True
                else:
                    Helper.logger.debug("the decrement_value button is disabled, so failed to click it")
                    return False

    def click_increment_value(self, times=None):
        """
        Description: click increment button to increase value of number stepper.
        :param times: int value, great than 0, optional. If not set this param, click increment button once.
        """
        self.scroll_if_needed(self.base_locator)
        if times is None:
            if self.get_attribute(self.btn_increment_value, "aria-disabled").lower() == "false":
                self.click(self.btn_increment_value)
                return True
            else:
                Helper.logger.debug("the decrement_value button is disabled, so failed to click it")
                return False
        else:
            i = 0
            while i < times:
                if self.get_attribute(self.btn_increment_value, "aria-disabled").lower() == "false":
                    self.click(self.btn_increment_value)
                    i += 1
                    if i == times:
                        return True
                else:
                    Helper.logger.debug("the decrement_value button is disabled, so failed to click it")
                    return False

    def get_value(self):
        self.scroll_if_needed(self.base_locator)
        return self.get_attribute(self.input,"value")

    def set_value(self, input_text):
        self.scroll_if_needed(self.base_locator)
        if self.is_read_only(self.input):
            Helper.logger.debug("input text is read only, so cannot input text")
            return
        self.fill(self.input, input_text)

    def clear_value(self):
        self.scroll_if_needed(self.base_locator)
        if self.is_read_only(self.input):
            Helper.logger.debug("input text is read only, so cannot input text")
            return
        self.clear(self.input)
