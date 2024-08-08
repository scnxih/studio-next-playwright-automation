"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: July 26th, 2024
"""
from src.Data.elements_ids import TestID
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.text import *
from src.Pages.Common.button import *
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.combobox import Combobox
from src.Pages.Common.radio_group import RadioGroup
from src.Pages.StudioNext.Dialog.select_key_column_dialog import SelectKeyColumnDialog
from playwright.sync_api import expect

class LoadTablePane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)
        self.load_table_technique_radio_group = RadioGroup(self.base_xpath, page, data_test_id="loadTableLoadTechnique")
        self.preprocess_actions_radio_group = RadioGroup(self.base_xpath, page, data_test_id="loadTableInsertPreprocessActions")
        self.select_key_column_dialog = SelectKeyColumnDialog(page)

    @property
    def button_add_columns(self):
        """
        'Add columns' button in 'Options' tab page
        """
        return Button(self.base_xpath, self.page, data_test_id='columnSelectorToolbarAddButton')

    @property
    def checkbox_if_not_exist_create_one(self):
        # data-testid="loadTableAllowCreate-checkbox"
        return Checkbox(self.base_xpath, self.page, data_test_id='loadTableAllowCreate-checkbox')

    @property
    def combobox_filter_column_mapping(self):
        """
        Combobox 'Filter Column Mapping' in Column Resolution tab page
        """
        return Combobox(self.base_xpath, self.page, data_test_id='columnResolutionContainer-filter')

    @property
    def dialog_select_key_column(self):
        """
        'Select Key Column' dialog (data-testid="selectColumnDialog-dialog"
        """
        return self.page.get_by_test_id('selectColumnDialog-dialog')

    def set_target_library(self, target_library_name):
        # Click 'Target Table' tab page
        self.click_Tab(Helper.data_locale.TARGET_TABLE)
        Text(self.base_xpath, self.page, supplement_base_xpath="[contains(@aria-label, '"
                                                               + Helper.data_locale.LIBRARY + "')]").fill_text(
            target_library_name)
        time.sleep(1)

        # Method-1: Explicitly pic name
        self.screenshot(self.base_xpath, "set_target_library")

    def set_target_table(self, target_table_name):
        self.click_Tab(Helper.data_locale.TARGET_TABLE)
        Text(self.base_xpath, self.page, aria_label=Helper.data_locale.TABLE_NAME_INPUT).fill_text(target_table_name)

        # Wait 1 sec
        time.sleep(1)

        # Method-1: Explicitly pic name
        self.screenshot(self.base_xpath, "set_target_table")

    def refresh_target_table(self):
        """
        Click 'Target Table' tab page, then click 'Refresh' button.
        """
        self.click_Tab(Helper.data_locale.TARGET_TABLE)
        Button(self.base_xpath, self.page, aria_label=Helper.data_locale.REFRESH).click_self()

    def set_update_rows_for_load_technique(self):
        """
        Set load technique in 'Options' tab page
        """
        # Click 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)
        if not self.load_table_technique_radio_group.is_checked(Helper.data_locale.UPDATE_ROWS):
            self.load_table_technique_radio_group.set_check(Helper.data_locale.UPDATE_ROWS)

        self.screenshot_self('update_rows')

    def set_truncate_table_option_for_preprocessing_actions(self):
        """
        data-testid=loadTableInsertPreprocessActions
        """
        # Click 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        if not self.preprocess_actions_radio_group.is_checked(Helper.data_locale.TRUNCATE_TABLE):
            self.preprocess_actions_radio_group.set_check(Helper.data_locale.TRUNCATE_TABLE)
            self.screenshot_self('truncate_table')

    def check_options(self):
        """
        Go to 'Options' tab page
        """
        # Click 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

    def check_column_resolution(self):
        """
        Switch to Column Resolution tab page
        """
        self.click_Tab(Helper.data_locale.COLUMN_RESOLUTION)

    def check_column_structure(self):
        """
        Switch to Column Resolution tab page
        """
        self.click_Tab(Helper.data_locale.COLUMN_STRUCTURE)

    def filter_successful_mapping(self):
        """
        Switch to Column Resolution tab page
        Then Click Filter Combobox, select 'Successful'
        """
        self.click_Tab(Helper.data_locale.COLUMN_RESOLUTION)
        # self.combobox_filter_column_mapping.select_item('成功')
        self.combobox_filter_column_mapping.select_item(Helper.data_locale.FILTER_COLUMN_MAPPING_SUCCESSFUL)

    def filter_ignored_mapping(self):
        """
        Switch to Column Resolution tab page
        Then Click Filter Combobox, select 'Ignored'
        """
        self.click_Tab(Helper.data_locale.COLUMN_RESOLUTION)
        # self.combobox_filter_column_mapping.select_item('忽略')
        self.combobox_filter_column_mapping.select_item(Helper.data_locale.FILTER_COLUMN_MAPPING_IGNORED)

    def filter_informational_mapping(self):
        """
        Switch to Column Resolution tab page
        Then Click Filter Combobox, select 'Informational'
        """
        self.click_Tab(Helper.data_locale.COLUMN_RESOLUTION)
        # self.combobox_filter_column_mapping.select_item('信息')
        self.combobox_filter_column_mapping.select_item(Helper.data_locale.FILTER_COLUMN_MAPPING_INFORMATIONAL)

    def select_key_column(self, col_name: str):
        """
        'Add columns' button in 'Options' tab page
        """

        # Switch to 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        # First, click the 'Add columns' button
        # Button(self.base_xpath, self.page, data_test_id='columnSelectorToolbarAddButton').click_self()
        self.button_add_columns.click_self()

        # Check if the dialog is opened
        if self.dialog_select_key_column.is_visible():

            if self.page.locator("//div[@role='row'][.//span[text()='" + col_name + "']]").is_visible():
                # self.click(self.page.locator("//div[@role='row'][.//span[text()='姓名1']]"))
                self.click(self.page.locator("//div[@role='row'][.//span[text()='" + col_name + "']]"))

                # Click OK
                # //button[@type='button'][.//span[text()='确定']]
                self.click(
                    self.page.locator("//button[@type='button'][.//span[text()='" + Helper.data_locale.OK + "']]"))

                self.screenshot_self("selected_key_column")
        else:
            self.click(self.page.locator("//button[@type='button'][.//span[text()='" + Helper.data_locale.CANCEL + "']]"))
