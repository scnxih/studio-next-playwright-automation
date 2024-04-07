"""
Author: Alice
Date: Apr 03, 2024
Description: This is properties of checkbox in custom step designer.
"""
from src.Pages.Common.base_page import BasePage
from src.Pages.Common.text import Text


class PropertiesDesigner(BasePage):
    def __init__(self, page):
        BasePage(page)
        self.base_xpath = ".//div[@class='sas_components-Layouts-Flow-Flow_flow_vertical sas_designer-components-Properties-Properties_properties-flow']"
        self.text_id = Text(self.base_xpath, self.page, data_test_id="idInput-input")
        self.text_label = Text(self.base_xpath, self.page, data_test_id="labelInput-input")
