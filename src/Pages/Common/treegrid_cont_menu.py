"""
File: treegrid_cont_menu.py
Author: Frank (Feng) Jiang
Contact: frank.jiang@sas.com
Date: 2023/11/29
"""
from src.Pages.Common.common_component import *


class TreegridContextMenu(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[contains(@class, 'ag-menu-list')][@role='tree']"

    def __init__(self, container_base_xpath, page):
        """
        Initialization
        :param page:
        """
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page)

    def menu_item_by_text(self, item_text):
        """
        Get xpath of context menu item from text input
        :param item_text: context menu item text
        :return: xpath of context menu item
        """
        return self.locate_xpath(f"//span[text()='{item_text}']")

    def click_menu_item_by_text(self, item_text):
        """
        Click specific context menu item from text input
        :param item_text: context menu item text
        :return: None
        """
        if self.is_enabled(f"//span[text()='{item_text}']//.."):
            self.menu_item_by_text(item_text).click()
