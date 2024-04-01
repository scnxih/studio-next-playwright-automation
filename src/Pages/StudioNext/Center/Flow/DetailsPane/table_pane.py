"""
Author: Alice
Date: Mar 05, 2024
Description: This is Table in flow Details pane.

"""

from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.text import *
from src.Pages.Common.textarea import *
from src.Pages.Common.button import *

class TablePane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    def set_library(self,library_name):
        self.click_Tab(Helper.data_locale.TABLE_PROPERTIES)
        Text(self.base_xpath,self.page,data_test_id="tableProperties-library-input-input").fill_text(library_name)

    def set_table(self,table_name):
        self.click_Tab(Helper.data_locale.TABLE_PROPERTIES)
        Text(self.base_xpath, self.page, aria_label=Helper.data_locale.TABLE_NAME_INPUT).fill_text(table_name)

    def preview_data(self):
        self.click_Tab(Helper.data_locale.PREVIEW_DATA)

    def refresh_table(self):
        self.click_Tab(Helper.data_locale.TABLE_PROPERTIES)
        Button(self.base_xpath, self.page,aria_label=Helper.data_locale.REFRESH).click_self()




