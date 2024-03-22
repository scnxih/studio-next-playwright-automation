"""
Author: Alice
Date: Mar 07, 2024
Description: This is tree in flow details pane.
"""

from src.Helper.helper import *
from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent

"""This treeview will be used in Sort step in details pane in flow."""


class TreeViewFlow(CommonComponent):

    def set_base_xpath(self):
        self.base_xpath += "//ul[@role='tree'][@class='sas_components-Tree-Tree_nodes']"

    def __init__(self, container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 supplement_base_xpath=supplement_base_xpath)

    def label_element_name(self, label):
        return self.locate_xpath("//label[text()='" + label + "']")

    def icon_expand_element(self, label):
        return self.locate_xpath("//label[text()='{0}']/../../../../../descendant::div[@aria-expanded='true']".format(label))

    def icon_collapse_element(self, label):
        return self.locate_xpath("//label[text()='{0}']/../../../../../descendant::div[@aria-expanded='false']".format(label))

    def navigate_to_element(self, element_path: list):
        for i in range(len(element_path)):
            label = element_path[i]
            Helper.logger.debug(" i =" + str(i))
            time.sleep(0.5)
            if i == len(element_path) - 1:
                Helper.logger.debug(" i =" + str(i))
                element = self.label_element_name(label)
                self.scroll_vertical_if_needed(element)
                if self.is_visible(element):
                    Helper.logger.debug("see last element:" + label)
                    self.click(element)
                    return element
                else:
                    Helper.logger.debug("not last element even after scroll:" + label)
                    return None
            icon_expand = self.icon_expand_element(label)
            if self.is_visible(icon_expand):
                Helper.logger.debug("icon_expand is visible:" + label)
                continue
            icon_collapse = self.icon_collapse_element(label)
            self.scroll_vertical_if_needed(icon_collapse)
            if self.is_visible(icon_collapse):
                Helper.logger.debug("icon_collapse is visible:" + label)
                self.click(icon_collapse)
                self.wait_for(icon_expand)
                continue
        Helper.logger.debug("failed to navigate to element:{0}".format("/".join(map(str, element_path))))
        return None

    def navigate_to_element_and_click_context_menu(self, element_path: list, *context_menu_text):
        element = self.navigate_to_element(element_path)
        self.click_context_menu(element, *context_menu_text)

    def navigate_to_element_and_dblclick(self,element_path: list):
        element = self.navigate_to_element(element_path)
        self.dblclick(element)


