"""
Author: Alice
Date: Apr 03, 2024
Description: This is properties of checkbox in custom step designer.
"""
from src.Pages.Common.base_page import BasePage
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.numeric_stepper import NumericStepper
from src.Pages.Common.text import Text
from src.Pages.StudioNext.Center.CustomStep.DesignerProperties.properties_designer import PropertiesDesigner


class PropertiesCheckbox(PropertiesDesigner):
    def __init__(self, page):
        PropertiesDesigner(self.page)
        self.check_box= Checkbox(self.base_xpath,self.page,data_test_id="checkbox1_checkedByDefault-checkbox")
        self.numeric_stepper = NumericStepper(self.base_xpath,self.page)

    def set_check_by_default(self):
        self.check_box.set_check()

    def set_uncheck_by_default(self):
        self.check_box.set_uncheck()





    





