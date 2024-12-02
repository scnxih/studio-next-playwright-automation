"""
Author: Alice
Date: November 14, 2023
Description: This is listbox common component, it will be used in Custom Step pane.
"""
from src.Pages.Common.common_component import *


class Listbox(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//ul[@role='listbox']"
        # self.base_xpath += "//div[@role='row']"

    # If the page contains more than one listbox, data_test_id or aria_label or aria_labelledby is required.
    def __init__(self, container_base_xpath, page, data_test_id="", aria_label="", aria_labelledby="",
                 supplement_base_xpath="", parent_label=""):
        if parent_label != "":
            supplement_base_xpath = "[../../descendant::label[contains(text(),'{0}')]]".format(parent_label)
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 aria_label=aria_label, aria_labelledby=aria_labelledby,
                                 supplement_base_xpath=supplement_base_xpath)

    def span_list_item(self, text: str):
        """
        Description: get list item by text.
        @param text: text of list item.
        return: Locator
        """
        if Helper.if_contain_quotation(text):
            escaped_text = Helper.escape_quotation_for_xpath(text)
            return self.locate_xpath(
                # Component in custom step changed on Nov.14th 2024
                f"//li[@role='option']//span[contains(@class,'sas_components-ListBox-List_item-text')][text()={escaped_text}]")

            # WRONG
            # f"//div[@role='gridcell']//span[contains(@class,'sas_components-List-Item-Item_item-text')][text()={escaped_text}]")
        else:
            # Component in custom step changed on Nov.14th 2024
            return self.locate_xpath(f"//li[@role='option']//span[contains(@class,'sas_components-ListBox-List_item-text')][text()='{text}']")

            # WRONG
            # return self.locate_xpath(
            #     f"//div[@role='gridcell']//span[contains(@class,'sas_components-List-Item-Item_item-text')][text()='{text}']")

    def li_item(self, text: str):
        """
        Description: get li locator by text.
        @param text: text of list item.
        return: Locator
        """
        if Helper.if_contain_quotation(text):
            escaped_text = Helper.escape_quotation_for_xpath(text)
            return self.locate_xpath(
                "//li[@role='option'][.//span[contains(@class,'sas_components-ListBox-List_item-text')][text()={0}]]".format(
                    escaped_text))
        else:
            return self.locate_xpath(
                "//li[@role='option'][.//span[contains(@class,'sas_components-ListBox-List_item-text')][text()='{0}']]".format(
                    text))

    def is_checked_li_item(self, text: str):
        if self.get_attribute(self.li_item(text), "aria-selected").lower() == "true":
            return True
        else:
            return False

    def set_check_li_item(self, text: str):
        if self.is_checked_li_item(text):
            return
        else:
            self.click_list_item(text)

    def set_uncheck_li_item(self, text: str):
        if self.is_checked_li_item(text):
            self.click_list_item(text)
            return
        else:
            return

    def dblclick_list_item(self, item_text: str):
        """
        Description: double click a list item.
        param item_text: text of list item.
        return: None
        """
        self.dblclick(self.span_list_item(item_text))

    def right_click_list_item(self, item_text: str):
        """
        Description: right click on a list item.
        param item_text: text of list item.
        return: None
        """
        self.right_click(self.span_list_item(item_text))

    def click_list_item(self, item_text: str):
        """
        Description: click on a list item.
        param item_text: text of list item.
        return: None
        """
        self.click(self.span_list_item(item_text))

    def click_context_menu_on_list_item(self, item_text: str, *context_menu_text):
        """
        Description: click context menu on a list item.
        param item_text: text of list item.
        param context_menu_text: cascaded context menu items
        return: None
        """
        self.click_context_menu_by_right_click(self.span_list_item(item_text), *context_menu_text)
