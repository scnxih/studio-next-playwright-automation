"""
File: context_menu.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/9/15 15:10
"""
from abc import ABC

from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import *


class ContextMenu(CommonComponent):
    """
    ContextMenu

    Might be integrated with Menu in the future
    """
    def set_base_xpath(self):
        self.base_xpath += "//ul[contains(@class, 'MenuList')][@role='presentation']"

    def __init__(self, container_base_xpath, page):
        """
        Initialization
        :param page:
        """
        # BasePage.__init__(self, page)

        # Example:
        # //ul[contains(@class, "MenuList")][@role="presentation"]
        # self.base_xpath = "//ul[contains(@class, 'MenuList')][@role='presentation']"

        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page)

    def menu_item_by_text(self, item_text):
        """
        Get xpath of context menu item from text input
        :param item_text: context menu item text
        :return: xpath of context menu item
        """

        # Example:
        # //ul[contains(@class, 'MenuList')][@role='presentation']/descendant::li/descendant::span[text()='Run']
        return self.locate_xpath(f"/descendant::li/descendant::span[text()='{item_text}']")

    def menu_item_by_test_id(self, data_test_id):
        """
        get xpath of context menu item from data-testid
        :param data_test_id:
        :return:
        """
        return self.locate_xpath(f"/descendant::li/descendant::span[@data-testid='{data_test_id}']")

    def click_menu_item_by_text(self, item_text):
        """
        Click specific context menu item from text input
        :param item_text: context menu item text
        :return: None
        """
        self.menu_item_by_text(item_text).click()

    def click_menu_item_by_test_id(self, data_test_id):
        """
        Click specific context menu item from data-testid
        :param data_test_id: data-testid
        :return: None
        """
        self.menu_item_by_test_id(data_test_id).click()
