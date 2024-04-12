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
        self.toolbar = Toolbar(self.base_xpath, page, data_test_id=TestID.QUERY_SELECT_GROUPS_TOOLBAR)
        self.center_toolbar_helper = CentralToolbarHelper(self.toolbar)

    def select_a_row(self, row_index=None, name_text=None):
        self.treegrid.select_a_row(row_index=row_index, name_text=name_text)

    """incomplete
        def cut_a_row_by_context_menu(self, row_index=None, name_text=None):
            self.treegrid.select_context_menu_item(Helper.data_locale.CUT, row_index=row_index, name_text=name_text)

        def paste_before_a_row_by_context_menu(self, row_index=None, name_text=None):
            self.treegrid.select_context_menu_item(Helper.data_locale.PASTE_BEFORE, row_index=row_index, name_text=name_text)

        def paste_after_a_row_by_context_menu(self, row_index=None, name_text=None):
            self.treegrid.select_context_menu_item(Helper.data_locale.PASTE_AFTER, row_index=row_index, name_text=name_text)
        incomplete"""

    def delete_a_row_by_context_menu(self, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(Helper.data_locale.DELETE, row_index=row_index, name_text=name_text)

    def move_a_row_to_top_by_context_menu(self, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(Helper.data_locale.MOVE_TO_TOP, row_index=row_index, name_text=name_text)

    def move_a_row_to_end_by_context_menu(self, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(Helper.data_locale.MOVE_TO_END, row_index=row_index, name_text=name_text)

    def move_a_row_up_by_context_menu(self, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(Helper.data_locale.MOVE_UP, row_index=row_index, name_text=name_text)

    def move_a_row_down_by_context_menu(self, row_index=None, name_text=None):
        self.treegrid.select_context_menu_item(Helper.data_locale.MOVE_DOWN, row_index=row_index, name_text=name_text)

    """incomplete
    def move_a_row_before_a_row(self, selected_row_index=None, selected_row_name=None, moved_row_index=None, moved_row_name=None):

        Description: move the moved_row to the place before the selected_row
        :param selected_row_index:
        :param selected_row_name:
        :param moved_row_index:
        :param moved_row_name:
        :return:

    def move_a_row_after_a_row(self, selected_row_index=None, selected_row_name=None, moved_row_index=None, moved_row_name=None):

        Description: move the moved_row to the place before the selected_row
        :param selected_row_index:
        :param selected_row_name:
        :param moved_row_index:
        :param moved_row_name:
        :return:

    incomplete"""

    def delete_a_row_by_toolbar(self, row_index=None, name_text=None):
        self.select_a_row(row_index=row_index, name_text=name_text)
        self.toolbar.click_btn_by_test_id(TestID.QUERY_SELECT_COLUMNS_TOOLBAR_BTN_REMOVE)

    def sort_a_column_ascending(self, col_id: str):
        self.treegrid.sort_column(col_id, "ascending")

    def sort_a_column_descending(self, col_id: str):
        self.treegrid.sort_column(col_id, "descending")

    def reset_a_sorted_column(self, col_id: str):
        self.treegrid.sort_column(col_id, "none")

    def uncheck_toolbar_checkbox(self):
        self.toolbar.uncheck_checkbox_by_test_id(TestID.QUERY_SELECT_GROUPS_TOOLBAR_CHECKBOX)

    def check_toolbar_checkbox(self):
        self.toolbar.check_checkbox_by_test_id(TestID.QUERY_SELECT_GROUPS_TOOLBAR_CHECKBOX)
        if Alert(self.page, Helper.data_locale.RESET_TO_AUTO_GROUP_DATA).is_open():
            Alert(self.page, Helper.data_locale.RESET_TO_AUTO_GROUP_DATA).click_button_in_footer(Helper.data_locale.RESET)
