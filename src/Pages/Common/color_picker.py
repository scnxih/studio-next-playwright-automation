"""
Author: Alice
Date: November 14, 2023
Description: This is listbox common component, it will be used in Custom Step pane.
"""

from src.Pages.Common.common_component import CommonComponent
from src.Pages.Common.text import Text
from src.Helper.helper import Helper
from src.Pages.Common.button import Button


class ColorPicker(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[contains(@class,'color-picker-container')]"

    # If the page contains more than one checkbox, data_test_id or label is required.
    def __init__(self, container_base_xpath, page, data_test_id="", label=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page)
        self.input_red = Text(self.base_xpath, self.page,
                              supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                  Helper.data_locale.RED))
        self.input_green = Text(self.base_xpath, self.page,
                                supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                    Helper.data_locale.GREEN))
        self.input_blue = Text(self.base_xpath, self.page,
                               supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                   Helper.data_locale.BLUE))
        self.btn_ok = Button(self.base_xpath, self.page,
                             supplement_base_xpath="[./span[text()='{0}']]".format(Helper.data_locale.OK))
        self.btn_cancel = Button(self.base_xpath, self.page,
                                 supplement_base_xpath="[./span[text()='{0}']]".format(Helper.data_locale.CANCEL))

    @property
    def span_basic(self):
        return self.locate_xpath("//span[text()='{0}']".format(Helper.data_locale.BASIC))

    @property
    def span_custom(self):
        return self.locate_xpath("//span[text()='{0}']".format(Helper.data_locale.CUSTOM))

    def click_basic(self):
        self.click(self.span_basic)

    def click_custom(self):
        self.click(self.span_custom)

    def set_red_value(self, value: int):
        self.input_red.fill_text(str(value))

    def set_green_value(self, value: int):
        self.input_green.fill_text(str(value))

    def set_blue_value(self, value: int):
        self.input_blue.fill_text(str(value))

    def click_ok(self):
        self.click(self.btn_ok)

    def click_cancel(self):
        self.click(self.btn_cancel)
