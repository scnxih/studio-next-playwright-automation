"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: July 26th, 2024
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.text import *
from src.Pages.Common.button import *
from src.Pages.Common.checkbox import Checkbox



class LoadTablePane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    @property
    def checkbox_if_not_exist_create_one(self):
        # data-testid="loadTableAllowCreate-checkbox"
        Checkbox(self.base_xpath, self.page, data_test_id='loadTableAllowCreate-checkbox')

    def set_target_library(self, target_library_name):
        # Click 'Target Table' tab page
        self.click_Tab(Helper.data_locale.TARGET_TABLE)
        Text(self.base_xpath, self.page, supplement_base_xpath="[contains(@aria-label, '"
                                                               + Helper.data_locale.LIBRARY + "')]").fill_text(target_library_name)
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

    def set_load_technique(self):
        """
        Set load technique in 'Options' tab page
        """
        # Click 'Options' tab page
        self.click_Tab(Helper.data_locale.OPTIONS)
        # self.click(self.checkbox_if_not_exist_create_one)
