"""
@author: Frank (Feng) Jiang
@date: created on 2023/10/09
@description: define Query page -> Select Groups tab, include elements and functionalities in this tab
"""

from src.Pages.StudioNext.Center.Query.query_page import *
from src.Data.elements_ids import *


class SelectGroups(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = ("//div[@data-testid='tab-group-content-area']"
                           "[@class='sas_components-layouts-TabManager-TabGroup-TabContentContainer_tab-content"
                           "-wrapper']")
        self.treegrid = TreeGrid(self.base_xpath, self.page)
        self.toolbar = Toolbar(self.base_xpath, page, data_test_id=TestID.QUERY_SELECT_COLUMNS_TOOLBAR)
        self.center_toolbar_helper = CentralToolbarHelper(self.toolbar)

    def select_a_row(self, row_index=None, name_text=None):
        self.treegrid.select_a_row(row_index=row_index, name_text=name_text)

    def select_context_menu_item(self, *context_menu_text, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(*context_menu_text, row_index=row_index, name_text=name_text)

    def delete_a_row(self, row_index=None, name_text=None):
        self.select_a_row(row_index=row_index, name_text=name_text)
        self.toolbar.click_btn_by_test_id(TestID.QUERY_TABS_TOOLBAR_BTN_REMOVE)
