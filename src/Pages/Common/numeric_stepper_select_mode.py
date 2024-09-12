from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


class NumericStepperSelectMode(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@class='sas_components-NumericStepper-NumericStepper_container']"

    # If the page contains more than one radio group, data_test_id is required.
    def __init__(self, container_base_xpath, page, data_test_id="",supplement_base_xpath="",parent_label =""):
        if parent_label!="":
            supplement_base_xpath = "[../../descendant::label[contains(text(), '{0}')]]".format(parent_label)
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)

    @property
    def btn_decrement_value(self):
        return self.locate_xpath("//button[@aria-label='{0}']".format(Helper.data_locale.DECREMENT_VALUE))

    @property
    def btn_increment_value(self):
        return self.locate_xpath("//button[@aria-label='{0}']".format(Helper.data_locale.INCREMENT_VALUE))

    @property
    def div_value(self):
        return self.locate_xpath(
            "//div[@class='sas_components-NumericStepper-NumericStepper_select-mode']")

    def click_decrement_value(self, times:int=None):
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

    def click_increment_value(self, times:int =None):
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

    def get_value(self)->str:
        self.scroll_if_needed(self.base_locator)
        value = self.get_attribute(self.div_value, "aria-valuenow")
        return value
