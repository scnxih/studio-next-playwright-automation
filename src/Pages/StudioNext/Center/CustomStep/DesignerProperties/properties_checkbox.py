"""
Author: Alice
Date: Apr 03, 2024
Description: This is properties of checkbox in custom step designer.
"""
from src.Pages.Common.base_page import BasePage
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.numeric_stepper import NumericStepper
from src.Pages.Common.text import Text
from src.Pages.StudioNext.Center.CustomStep.DesignerProperties.properties import Properties


class PropertiesCheckbox(Properties):
    def __init__(self, page):
        Properties.__init__(self, page)
        self.check_box = Checkbox(self.base_xpath, self.page, data_test_id="checkbox1_checkedByDefault-checkbox")
        self.numeric_stepper = NumericStepper(self.base_xpath, self.page,
                                              supplement_base_xpath="[ancestor::div[@data-testid='datePickerAttributesIndent']]")

    def set_check_by_default(self):
        self.check_box.set_check()

    def set_uncheck_by_default(self):
        self.check_box.set_uncheck()

    def set_indent(self, indent: str):
        self.numeric_stepper.set_value(indent)
