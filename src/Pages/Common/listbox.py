"""
Author: Alice
Date: November 14, 2023
Description: This is listbox common component, it will be used in Custom Step pane.
"""
from src.Pages.Common.common_component import *


class Listbox(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//ul[@role='listbox']"

    # If the page contains more than one listbox, data_test_id or aria_label or aria_labelledby is required.
    def __init__(self,container_base_xpath, page,data_test_id ="", aria_label="",aria_labelledby=""):
        CommonComponent.__init__(self,container_base_xpath=container_base_xpath,page=page,data_test_id= data_test_id,aria_label=aria_label,aria_labelledby=aria_labelledby)



    def span_list_item(self,text:str):
        """
        Description: get list item by text.
        param item_text: text of list item.
        return: Locator
        """
        return self.locate_xpath(f"//li[@role='option']//span[contains(@class,'sas_components-ListBox-List_item-text')][text()='{text}']")


    def dblclick_list_item(self,item_text:str):
        """
        Description: double click a list item.
        param item_text: text of list item.
        return: None
        """
        self.dblclick(self.span_list_item(item_text))

    def right_click_list_item(self,item_text:str):
        """
        Description: right click on a list item.
        param item_text: text of list item.
        return: None
        """
        self.right_click(self.span_list_item(item_text))

    def click_list_item(self,item_text:str):
        """
        Description: click on a list item.
        param item_text: text of list item.
        return: None
        """
        self.click(self.span_list_item(item_text))

    def click_context_menu_on_list_item(self, item_text:str, *context_menu_text):
        """
        Description: click context menu on a list item.
        param item_text: text of list item.
        param context_menu_text: cascaded context menu items
        return: None
        """
        self.click_context_menu_by_right_click(self.span_list_item(item_text),*context_menu_text)


