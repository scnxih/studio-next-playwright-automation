"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: July 24th, 2024
"""
# -*- coding: UTF-8 -*-

from playwright.sync_api import expect
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.button import *
from src.Pages.Common.dialog import Dialog
from src.Pages.StudioNext.Dialog.add_filter_dialog import AddFilterDialog


class FilterRowsPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)
        # self.add_filter_dialog = AddFilterDialog()

    @property
    def button_filter_value(self):
        """
        Return the Lookup value button
        """
        return self.get_by_test_id("filterView-filterValue0-button")

    @property
    def select_a_column_dialog(self):
        # if self.is_visible(Dialog(self.page, title=Helper.data_locale.SELECT_A_COLUMN)):
        return Dialog(self.page, title=Helper.data_locale.SELECT_A_COLUMN)

    @property
    def quick_filter_dialog(self):
        return "//div[@data-testid='quickFilterDialog-dialog']"

    def add_a_row(self):
        Button(self.base_xpath, self.page, data_test_id="filterView-addRowButton").click_self()

    def select_a_column(self, col_name: str):
        Button(self.base_xpath, self.page,
               data_test_id="filterView-filterColumn0-columnCompositeInputCompositeInput-button").click_self()

        # Dialog(self.page, title=Helper.data_locale.SELECT_A_COLUMN).screenshot_self('select_a_col')
        self.select_a_column_dialog.screenshot_self('select_a_col')

        # //div[@role='row'][@row-id='Sex']
        self.is_visible(self.locator("//div[@role='row'][@row-id='" + col_name + "']"))

        self.click(self.locator("//div[@role='row'][@row-id='" + col_name + "']"))
        self.select_a_column_dialog.screenshot_self('selected_a_col')

        self.click(self.page.get_by_test_id("selectColumnDialog-firstButton"))

        # self.select_a_column_dialog.close_dialog()

        # Dialog(self.page, title=Helper.data_locale.SELECT_A_COLUMN).close_dialog()

    def set_filter_value(self):
        """
        First click 'Filter Value' button
        """
        Button(self.base_xpath, self.page, data_test_id="filterView-filterValue0-button").click_self()

        self.is_visible(self.locator(self.quick_filter_dialog))

        # self.click(self.page.get_by_test_id("quickFilterDialog-dismissButton"))

    def cancel_and_close_add_filter_dialog(self):
        """
        Click the Cancel button and close dialog.
        """
        add_filter_dialog = AddFilterDialog(self.page)
        add_filter_dialog.cancel_and_close()

    def set_condition_to(self, condition: str, value: str):
        """
        Set filter condition to given value
        """
        self.click(self.button_filter_value)

        add_filter_dialog = AddFilterDialog(self.page)

        add_filter_dialog.condition_combo_box.click_self()
        add_filter_dialog.condition_combo_box.select_item(condition)

        add_filter_dialog.condition_value_input.fill_text(value)

        # self.click(add_filter_dialog.button_filter)
