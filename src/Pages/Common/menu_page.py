"""
Author: Alice
Date: Mar 22, 2024
Description: This is the MenuPage which is used to screenshot menus.
"""
from src.Pages.Common.base_page import *


class MenuPage(BasePage):
    """When there is more than one menus, data_test_id is required, this data_test_id defines the child element
    of the div[@role='region'], when there is only one menu, this data_test_id is NOT required."""

    def __init__(self, page, data_test_id=''):
        BasePage.__init__(self, page)
        self.base_xpath += "//div[contains(@class,'sas_components-Popover-Popover_popover-inner')]"
        if data_test_id != '':
            self.base_xpath += "[child::div[@data-testid='{0}']]".format(data_test_id)
