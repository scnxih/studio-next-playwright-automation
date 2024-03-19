"""
@author: Frank (Feng) Jiang
@date: created on 2023/10/09
@description: define Query page -> Filter tab, include elements and functionalities in this tab
"""

from src.Pages.StudioNext.Center.Query.query_page import *
from src.Data.elements_ids import *


class Filter(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = ("//div[@data-testid='tab-group-content-area']"
                           "[@class='sas_components-layouts-TabManager-TabGroup-TabContentContainer_tab-content"
                           "-wrapper']")
        self.treegrid = TreeGrid(self.base_xpath, self.page)
        self.toolbar = Toolbar(self.base_xpath, page, data_test_id=TestID.QUERY_SELECT_COLUMNS_TOOLBAR)
        self.center_toolbar_helper = CentralToolbarHelper(self.toolbar)

    def sort_column(self, col_id: str, sort_order: str):
        self.treegrid.sort_column(col_id, sort_order)

    def select_a_row(self, row_index=None, name_text=None):
        self.treegrid.select_a_row(row_index=row_index, name_text=name_text)

    def delete_a_row_toolbar(self, row_index=None, name_text=None):
        self.select_a_row(row_index=row_index, name_text=name_text)
        self.toolbar.click_btn_by_title_contains(Helper.data_locale.DELETE)

    def set_filter_for_a_column(self, row_index=None, name_text=None):
        self.treegrid.click_btn_in_a_row(row_index=row_index, name_text=name_text)
        """To be continued"""

    def set_bool_operator(self, combo_item_text: str, row_index=None, name_text=None):
        self.treegrid.select_item_combo_in_a_row(combo_item_text, row_index=row_index, name_text=name_text)

    def select_context_menu_item(self, *context_menu_text, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(*context_menu_text, row_index=row_index, name_text=name_text)
