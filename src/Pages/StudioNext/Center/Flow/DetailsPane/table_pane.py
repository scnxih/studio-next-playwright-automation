"""
Author: Alice
Date: Mar 05, 2024
Description: This is Table in flow Details pane.

"""

from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.text import *
from src.Pages.Common.textarea import *
from src.Pages.Common.button import *
import sys


class TablePane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    def set_library(self, library_name):
        self.click_Tab(Helper.data_locale.TABLE_PROPERTIES)

        # Text(self.base_xpath, self.page, data_test_id="tableProperties-library-input-input").fill_text(library_name)

        # undefinedlibrary-input-input
        Text(self.base_xpath, self.page, data_test_id="undefinedlibrary-input-input").fill_text(library_name)
        time.sleep(1)

        # Method-1: Explicitly pic name
        self.screenshot(self.base_xpath, "set_library")

        # Method-2: Get function name by using inspect
        # self.screenshot(self.base_xpath, str(list((inspect.currentframe().f_locals.keys()))[-1]))

        # Debug
        # self.screenshot(self.base_xpath, '')

    def set_table(self, table_name):
        self.click_Tab(Helper.data_locale.TABLE_PROPERTIES)
        Text(self.base_xpath, self.page, aria_label=Helper.data_locale.TABLE_NAME_INPUT).fill_text(table_name)

        # Wait 1 sec
        time.sleep(1)

        # Method-1: Explicitly pic name
        self.screenshot(self.base_xpath, "set_table")

        # Method-2: Get function name by using inspect
        # self.screenshot(self.base_xpath, str(list((inspect.currentframe().f_locals.keys()))[-1]))

        # Debug
        # self.screenshot(self.base_xpath, '')

    def preview_data(self):
        self.click_Tab(Helper.data_locale.PREVIEW_DATA)

        # Wait 3 sec to counteract delay owing to performance issue
        time.sleep(3)

        # Method-1: Explicitly pic name
        self.screenshot(self.base_xpath, "preview_data")

        # print('+++ preview data ' + str(inspect.currentframe()) + '***')
        # Method-2: Get function name by using inspect
        # self.screenshot(self.base_xpath, str(inspect.getframeinfo(inspect.currentframe().f_back).code_context[-1].split('.')[-1]).split('()')[0])

        # Debug
        # self.screenshot(self.base_xpath, '')

    def refresh_table(self):
        self.click_Tab(Helper.data_locale.TABLE_PROPERTIES)
        Button(self.base_xpath, self.page, aria_label=Helper.data_locale.REFRESH).click_self()

        # Wait 3 sec to counteract delay owing to performance issue
        time.sleep(3)

        # Method-1: Explicitly pic name
        self.screenshot(self.base_xpath, "refresh_table")

        # print('reload table: ' + str(inspect.currentframe()) + '***')
        # Method-2: Get function name by using inspect
        # self.screenshot(self.base_xpath, str(inspect.getframeinfo(inspect.currentframe().f_back).code_context[-1].split('.')[-1]).split('()')[0])

        # Debug
        # self.screenshot(self.base_xpath, '')
