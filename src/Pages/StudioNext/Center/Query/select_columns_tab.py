"""
@author: Frank (Feng) Jiang
@date: created on 2023/09/27
@description: define Query page -> Select Columns tab, include elements and functionalities in this tab
"""

from src.Pages.StudioNext.Center.Query.query_page import *
from src.Data.elements_ids import *
from src.Pages.StudioNext.Dialog.manage_columns_dialog import *
from src.Pages.StudioNext.Dialog.treegrid_header_menu_dialog import *


class SelectColumns(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = ("//div[@data-testid='tab-group-content-area']"
                           "[@class='sas_components-layouts-TabManager-TabGroup-TabContentContainer_tab-content"
                           "-wrapper']")
        self.treegrid = TreeGrid(self.base_xpath, page)
        self.toolbar = Toolbar(self.base_xpath, page, data_test_id=TestID.QUERY_SELECT_COLUMNS_TOOLBAR)
        self.center_toolbar_helper = CentralToolbarHelper(self.toolbar)
        self.mc_dialog = ManageColumns(page)
        self.header_menu = HeaderMenuDialog(page)

    @property
    def btn_manage_columns(self):
        manage_columns = Helper.data_locale.MANAGE_COLUMNS_LOWER
        return self.locate_xpath(f"//button[.//span[text()='{manage_columns}']]")

    def open_header_menu(self, col_id: str):
        if self.is_visible(self.btn_manage_columns):
            self.click(self.btn_manage_columns)
            self.mc_dialog.add_all_columns_to_display()
        self.treegrid.click_header_menu(col_id)

    def open_header_menu_mouse_right_click(self, col_id: str):
        if self.is_visible(self.btn_manage_columns):
            self.click(self.btn_manage_columns)
            self.mc_dialog.add_all_columns_to_display()
        self.treegrid.col_header(col_id).click(button="right")

    def select_a_row(self, row_index=None, name_text=None):
        self.treegrid.select_a_row(row_index=row_index, name_text=name_text)

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

    def fill_name_field_for_a_column(self, fill_text: str, row_index=None, name_text=None):
        self.treegrid.fill_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_NAME, fill_text, row_index=row_index,
                                          name_text=name_text)

    def fill_label_field_for_a_column(self, fill_text: str, row_index=None, name_text=None):
        self.treegrid.fill_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_LABEL, fill_text, row_index=row_index,
                                          name_text=name_text)

    def clear_name_field_for_a_column(self, row_index=None, name_text=None):
        self.treegrid.clear_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_NAME, row_index=row_index,
                                           name_text=name_text)

    def clear_label_field_for_a_column(self, row_index=None, name_text=None):
        self.treegrid.clear_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_LABEL, row_index=row_index,
                                           name_text=name_text)

    def get_value_from_input_in_a_row(self, test_id: str, row_index=None, name_text=None):
        self.treegrid.get_value_input_in_a_row(test_id, row_index=row_index, name_text=name_text)

    """incomplete"""
    def set_format_for_a_column(self, row_index=None, name_text=None):
        self.treegrid.click_btn_in_a_row(row_index=row_index, name_text=name_text,
                                         test_id=TestID.QUERY_SELECT_COLUMNS_BTN_FORMAT)

    def set_informat_for_a_column(self, row_index=None, name_text=None):  # incomplete
        self.treegrid.click_btn_in_a_row(row_index=row_index, name_text=name_text,
                                         test_id=TestID.QUERY_SELECT_COLUMNS_BTN_INFORMAT)
    """incomplete"""

    def delete_a_row_by_toolbar(self, row_index=None, name_text=None):
        self.select_a_row(row_index=row_index, name_text=name_text)
        self.toolbar.click_btn_by_test_id(TestID.QUERY_TABS_TOOLBAR_BTN_REMOVE)

    def sort_a_column_ascending(self, col_id: str):
        self.treegrid.sort_column(col_id, "ascending")

    def sort_a_column_descending(self, col_id: str):
        self.treegrid.sort_column(col_id, "descending")

    def reset_a_sorted_column(self, col_id: str):
        self.treegrid.sort_column(col_id, "none")
