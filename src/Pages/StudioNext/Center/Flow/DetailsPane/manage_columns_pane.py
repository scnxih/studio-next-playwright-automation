"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: July 9th, 2024
"""
# -*- coding: UTF-8 -*-
from playwright.sync_api import expect
from src.Pages.Common.button import *
from src.Pages.Common.treegrid import TreeGrid
from src.Pages.Common.treeview_flow import TreeViewFlow

from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane


class ManageColumnsPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)
        self.tree = TreeViewFlow(self.base_xpath, page)
        self.treegrid = TreeGrid(self.base_xpath, page)

    @property
    def button_add_all_columns(self):
        """
        Button 'Add all' underneath tab pages
        """
        return "//button[@data-testid='addAllColumnsButton']"

    @property
    def button_add_columns(self):
        """
        Button 'Add all' underneath tab pages
        """
        return "//button[@data-testid='addColumnsButton']"

    @property
    def button_remove_selected_columns(self):
        """
        Button 'Remove selected columns' underneath tab pages
        """
        return "//button[@data-testid='manageColumns-removeButton']"

    @property
    def button_remove_all_columns(self):
        """
        Button 'Add all' underneath tab pages
        """
        return "//button[@data-testid='manageColumns-removeAllButton']"

    def add_all_columns(self):
        """
        Click the 'Add all' button in 'Options' tab page
        """
        # Click 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        # expect the 'Add columns' button to be disabled
        expect(self.transform_to_locator(self.button_add_columns)).to_be_disabled()

        # Click 'Add All' button
        # Button(self.base_xpath, self.page, data_test_id='addAllColumnsButton').click_self()
        self.click(self.button_add_all_columns)

        # Determine if all columns have been added
        self.wait_until_enabled(self.button_remove_all_columns)

        # The Button 'Add all' should be disabled
        # expect(self.transform_to_locator("//button[@data-testid='addAllColumnsButton']")).to_be_disabled()
        expect(self.transform_to_locator(self.button_add_all_columns)).to_be_disabled()

        # Take screenshot
        self.screenshot(self.base_xpath, "add_all_columns")

    def remove_all_columns(self):
        """
        Remove all columns button: data-testid="manageColumns-removeAllButton"
        """
        # Click 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        # Click 'Remove all columns' button
        # Button(self.base_xpath, self.page, data_test_id='manageColumns-removeAllButton').click_self()
        self.click(self.button_remove_all_columns)

        # Wait 3 sec to counteract delay owing to performance issue
        # time.sleep(3)

        # Determine if all columns have been added
        self.wait_until_enabled(self.button_add_all_columns)

        # The Button 'Add all' should be disabled
        # expect(self.transform_to_locator("//button[@data-testid='addAllColumnsButton']")).to_be_disabled()
        expect(self.transform_to_locator(self.button_remove_all_columns)).to_be_disabled()

        # Take screenshot
        self.screenshot(self.base_xpath, "remove_all_columns")

    def add_columns_by_double_click(self, element_path: list):
        """
        First navigate to the item,
        then double-click tree-item (column) to add it to the RHS pane.
        """
        self.tree.navigate_to_element_and_dblclick(element_path)

    # def add_columns_by_context_menu(self, element_path: list, *context_menu_text):
    def add_columns_by_context_menu(self, element_path: list):
        """
        First navigate to the item,
        then add tree-item (column) to the RHS pane from context menu
        """
        self.tree.navigate_to_element_and_click_context_menu(element_path, Helper.data_locale.ADD_COLUMN)

        # Determine if columns have been added
        self.wait_until_enabled(self.button_remove_selected_columns)

        # Take screenshot
        self.screenshot(self.base_xpath, "add_columns_by_context_menu")

    def add_columns_by_toolbar_button(self, element_path: list):
        """
        First navigate to the item,
        then click 'Add columns' button to add tree-item (column) to the RHS pane from context menu
        """
        self.tree.navigate_to_element(element_path)
        self.click(self.button_add_columns)

        # Determine if columns have been added
        self.wait_until_enabled(self.button_remove_all_columns)

        # Take screenshot
        self.screenshot(self.base_xpath, "add_columns_by_toolbar_button")



