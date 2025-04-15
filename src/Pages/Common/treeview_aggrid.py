import time

from src.Helper.helper import Helper
from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent


# This class is ag-grid tree view. The folder tree in SAS Server/SAS Content/Library/Steps pane can use it.
class TreeViewAGGrid(CommonComponent):

    def set_base_xpath(self):
        # self.base_xpath += "//div[@class='ag-body ag-layout-normal']"
        self.base_xpath += "//div[@class='ag-root-wrapper ag-ltr ag-layout-normal']"

    def __init__(self, container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 supplement_base_xpath=supplement_base_xpath)

    def grid_item(self, text: str):
        """
        Return gridcell item in AG-Grid
        //div[@role='gridcell']/descendant::span[text()='{0}}']
        """
        if Helper.if_contain_quotation(text):
            escaped_text = Helper.escape_quotation_for_xpath(text)
            return self.locate_xpath(f"//div[@role='gridcell']"
                                     f"[descendant::span[text()={escaped_text}]]")
        else:
            return self.locate_xpath(f"//div[@role='gridcell']"
                                     f"[descendant::span[text()='{text}']]")

    def click_grid_item(self, item_text: str):
        """
        Click AG-Grid item obtained from grid_item()
        """
        self.grid_item(item_text).click()

    def click_context_menu_on_grid_item(self, item_text: str, *context_menu_text):
        self.click_context_menu_by_right_click(self.grid_item(item_text), *context_menu_text)

    def label_element_name(self, label):
        return self.locate_xpath("//span[text()='{0}']".format(label))

    def icon_expand_element_org(self, label):
        return self.locate_xpath("//span[text()='{0}']/../../../../../../descendant::span[@class='ag-group-expanded "
                                 "']/span[1]".format(label))

    def icon_collapse_element_org(self, label):
        return self.locate_xpath("//span[text()='{0}']/../../../../../../descendant::span[@class='ag-group-contracted "
                                 "']/span[1]".format(label))

    def icon_expand_element(self, label):
        return self.locate_xpath("//span[text()='{0}']/../../../../descendant::span[@class='ag-group-expanded "
                                 "']/span[1]".format(label))

    def icon_collapse_element(self, label):
        return self.locate_xpath("//span[text()='{0}']/../../../../descendant::span[@class='ag-group-contracted "
                                 "']/span[1]".format(label))

    def navigate_to_element(self, element_path: list):
        for i in range(len(element_path)):
            label = element_path[i]
            if i == len(element_path) - 1:
                Helper.logger.debug(" i == len(element_path) - 1")
                element = self.label_element_name(label)
                time.sleep(0.5)
                self.scroll_vertical_if_needed(element)
                if self.is_visible(element):
                    Helper.logger.debug("see last element:" + label)
                    self.click(element)
                    return element
                else:
                    Helper.logger.debug("not last element even after scroll:" + label)
                    return None
            icon_expand = self.icon_expand_element(label)
            time.sleep(0.5)
            if self.is_visible(icon_expand):
                continue
            icon_collapse = self.icon_collapse_element(label)
            self.scroll_vertical_if_needed(icon_collapse)
            time.sleep(0.5)
            if self.is_visible(icon_collapse):
                self.click(icon_collapse)
                time.sleep(0.5)
                self.wait_for(icon_expand)
                time.sleep(0.5)
                continue
        Helper.logger.debug("failed to navigate to element:{0}".format("/".join(map(str, element_path))))
        return None

    def navigate_to_element_and_click_context_menu(self, element_path: list, *context_menu_text):
        element = self.navigate_to_element(element_path)
        self.click_context_menu_by_right_click(element, *context_menu_text)

    def navigate_to_element_and_dblclick(self, element_path: list):
        element = self.navigate_to_element(element_path)
        self.dblclick(element)
