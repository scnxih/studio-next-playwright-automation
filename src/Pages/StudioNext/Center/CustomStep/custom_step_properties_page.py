"""
Author: Alice
Date: Apr 03, 2024
Description: This is properties of checkbox in custom step designer.
"""
import time

from src.Pages.Common.base_page import BasePage
from src.Pages.Common.text import Text
from src.Pages.Common.window_shade import WindowShade
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.numeric_stepper import NumericStepper
from src.Helper.helper import *
from src.Pages.Common.textarea import Textarea
from src.Pages.Common.button import Button
from src.Pages.Common.color_picker import ColorPicker


class CustomStepPropertiesPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = ".//div[@class='sas_components-Layouts-Flow-Flow_flow_vertical sas_designer-components-Properties-Properties_properties-flow']"
        self.text_id = Text(self.base_xpath, self.page, data_test_id="idInput-input")
        self.text_label = Text(self.base_xpath, self.page, data_test_id="labelInput-input")
        self.check_box_by_default = Checkbox(self.base_xpath, self.page,
                                             data_test_id="checkbox1_checkedByDefault-checkbox")
        self.numeric_stepper = NumericStepper(self.base_xpath, self.page,
                                              supplement_base_xpath="[ancestor::div[@data-testid='datePickerAttributesIndent']]")
        self.window_shade_dependencies = WindowShade(self.base_xpath, self.page,
                                                     supplement_base_xpath="[descendant::span[text()='{0}']]".format(
                                                         Helper.data_locale.DEPENDENCIES))

        self.text_area_visibility = Textarea(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(Helper.data_locale.VISIBILITY))
        self.text_area_enablement = Textarea(self.base_xpath, self.page,
                                             supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                                 Helper.data_locale.ENABLEMENT))
        self.btn_color = Button(self.base_xpath,self.page,supplement_base_xpath="[contains(@aria-label,'{0}')]".format(Helper.data_locale.CHOOSE_COLOR))
        self.color_picker = ColorPicker(self.base_xpath,self.page)

    # def set_id(self,text:str):
    #     self.text_id.fill_text(text)

    def set_label(self, label: str):
        self.text_label.fill_text(label)

    def set_check_by_default(self):
        self.check_box_by_default.set_check()

    def set_uncheck_by_default(self):
        self.check_box_by_default.set_uncheck()

    def set_indent(self, indent: str):
        self.numeric_stepper.set_value(indent)

    def expand_dependencies(self):
        self.window_shade_dependencies.expand()

    def collapse_dependencies(self):
        self.window_shade_dependencies.collapse()

    def set_visibility(self,text:str):
        self.expand_dependencies()
        self.text_area_visibility.fill_text(text)

    def set_enablement(self,text:str):
        self.expand_dependencies()
        self.text_area_enablement.fill_text(text)

    def click_select_color(self):
        self.btn_color.click_self()

    def set_RGB(self,red_value:int,green_value:int, blue_value:int):
        time.sleep(0.5)
        self.color_picker.click_custom()
        time.sleep(1)
        self.color_picker.set_red_value(red_value)
        time.sleep(0.5)
        self.color_picker.set_green_value(green_value)
        time.sleep(0.5)
        self.color_picker.set_blue_value(blue_value)
        time.sleep(0.5)
        self.color_picker.click_ok()
        time.sleep(0.5)