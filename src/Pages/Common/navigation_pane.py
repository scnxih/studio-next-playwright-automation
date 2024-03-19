"""
File: navigation_pane.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/11/10 10:44 
"""
import time

from src.Pages.Common.common_component import CommonComponent
from src.Helper.helper import Helper


class NavigationPane(CommonComponent):
    """
    Encapsulate the navigation pane in Settings dialog
    """

    def set_base_xpath(self):
        self.base_xpath += '//div[@role="navigation"][@class="sas_components-Tree-Tree_nodes-container"]'

    def __init__(self, container_base_xpath, page, data_test_id=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id)

    @property
    def collapsed_icon_global_treeitem(self):
        """
        Hard-coded collapsed Global tree-item
        :return:
        """
        return self.locate_xpath('//div[@role="treeitem"][@aria-expanded="false"]//span[@data-testid="G-0-expandIcon"]')

    @property
    def collapsed_icon_sas_studio_treeitem(self):
        """
        Hard-coded collapsed SAS Studio tree-item
        :return:
        """
        return self.locate_xpath(
            '//div[@role="treeitem"][@aria-expanded="false"]//span[@data-testid="Custom-0-expandIcon"]')

    @property
    def collapsed_icon_sas_program_treeitem(self):
        """
        Hard-coded collapsed SAS Studio tree-item
        :return:
        """
        return self.locate_xpath(
            '//div[@role="treeitem"][@aria-expanded="false"]//span[@data-testid="Custom-0-Child-2-expandIcon"]')

    @property
    def expanded_icon_global_treeitem(self):
        """
        Hard-coded collapsed Global tree-item
        :return:
        """
        return self.locate_xpath('//div[@role="treeitem"][@aria-expanded="true"]//span[@data-testid="G-0-expandIcon"]')

    @property
    def expanded_icon_sas_studio_treeitem(self):
        """
        Hard-coded collapsed SAS Studio tree-item
        :return:
        """
        return self.locate_xpath(
            '//div[@role="treeitem"][@aria-expanded="true"]//span[@data-testid="Custom-0-expandIcon"]')

    @property
    def expanded_icon_sas_program_treeitem(self):
        """
        Hard-coded collapsed SAS Studio tree-item
        :return:
        """
        return self.locate_xpath(
            '//div[@role="treeitem"][@aria-expanded="true"]//span[@data-testid="Custom-0-Child-2-expandIcon"]')

    def expand_all_treeitems(self):
        """
        Expand all tree items
        :return:
        """
        if self.is_visible(self.collapsed_icon_global_treeitem):
            self.click(self.collapsed_icon_global_treeitem)

        time.sleep(2)

        if self.is_visible(self.collapsed_icon_sas_studio_treeitem):
            self.click(self.collapsed_icon_sas_studio_treeitem)

        time.sleep(2)

        if self.is_visible(self.collapsed_icon_sas_program_treeitem):
            self.click(self.collapsed_icon_sas_program_treeitem)

        time.sleep(2)

    def debug_collapse_all_tree_items(self):
        """
        Collapse all tree items after Settings dialog is open.
        :return:
        """
        if self.is_visible(self.expanded_icon_global_treeitem):
            self.click(self.expanded_icon_global_treeitem)

        time.sleep(2)

        if self.is_visible(self.expanded_icon_sas_studio_treeitem):
            self.click(self.expanded_icon_sas_studio_treeitem)

        time.sleep(2)

        if self.is_visible(self.expanded_icon_sas_program_treeitem):
            self.click(self.expanded_icon_sas_program_treeitem)

        time.sleep(2)

    def tree_item_testid(self, data_testid):
        """
        Generate xpath based on data-testid for tree-item in navigation pane

        :param data_testid:
        :return:
        """
        # //div[@data-testid="settings-layout-tree-Custom-0-Child-1"]
        return self.locate_xpath('//div[@data-testid="' + data_testid + '"]')

    def click_tree_item_testid(self, data_testid):
        """
        Click tree-item based on data-testid for tree-item in navigation pane
        :param data_testid:
        :return:
        """
        self.click(self.tree_item_testid(data_testid))

    def number_of_expanded_icons(self):
        """
        
        :return:
        """
        Helper.logger.debug("Step1: Determine the number of collapse icons")
        Helper.logger.debug(
            "Number of expand icons: " + str(self.locator_count('//span[contains(@data-testid, "expandIcon")]')))

    def icon_expanded(self):
        """
        Return xpath of the expanded icon
        :return:
        """
        # return self.locate_xpath()
        pass

    def check_collapsed_icons(self):
        """
        Count the number of collapsed tree-item.
        If all tree-items are closed,
        :return:
        """
        # Determine if there is any collapsed icon by counting
        if self.locator_count('//div[@role="treeitem"][@aria-expanded="false"]') is not 0:
            Helper.logger.debug("Collapsed icon exist!")

        pass

    def iterate_thru_treeitems(self):
        """
        Iterate through tree-items.
        NOTE: Locator object is not iterable.
        :return:
        """
        # Step-1: Get the total number of tree-items
        i = 1
        while i <= self.locator_count('//div[@role="treeitem"]'):
            Helper.logger.debug("Going through # " + str(i) + "tree-item")

            # Step-2: Iterate thru iteration
            # Formula: (xpath)[Number]
            # Exmaple: (//div[@role="treeitem"])[15]
            self.click(self.locator('(//div[@role="treeitem"])[' + str(i) +']'))
            time.sleep(2)

            i = i+1
