"""
@author: Frank (Feng) Jiang
@date: created on 2023/10/25
@description: define Query page -> Columns pane, include elements and functionalities in this pane
"""

from src.Pages.StudioNext.Center.Query.query_page import *
from src.Data.elements_ids import *
from src.Pages.StudioNext.Dialog.query_select_table_dialog import *
from src.Pages.Common.context_menu import *


class Columns(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@data-testid='query-columnsPane-container']"
        self.toolbar = Toolbar(self.base_xpath, page, data_test_id=TestID.QUERY_COLUMNS_PANE_TOOLBAR)
        self.table_tree = TreeViewCommon(self.base_xpath, page)
        self.st_dialog = SelectTableDialog(page)
        self.alert_dialog = Alert(page, Helper.data_locale.REMOVE_TABLE)
        # self.cont_menu = ContextMenu(self, page)
        self.search_field = Text(self.base_xpath, page, data_test_id=TestID.QUERY_COLUMNS_PANE_SEARCH_INPUT)

    @property
    def btn_clear_search(self):
        return self.get_by_test_id("query-columnsPane-searchField-searchInput-clearButton")

    def clear_search_text(self):
        if self.is_visible(self.btn_clear_search):
            self.click(self.btn_clear_search)

    @property
    def btn_search(self):
        return self.get_by_test_id("query-columnsPane-searchField-searchButton")

    def fill_search_field(self, text):
        self.search_field.fill_text(text)

    def search_column(self, text):
        self.fill_search_field(text)
        self.click(self.btn_search)

    @property
    def btn_add_table_zero(self):
        return self.get_by_test_id("queryBuilder-tab-columns-zeroState-add")

    def click_btn_add_table(self):
        self.click(self.btn_add_table_zero)

    def add_table_zero_state(self, lib_name: str, table_name: str):
        self.click_btn_add_table()
        self.st_dialog.select_a_table(lib_name, table_name)

    def add_table_from_toolbar(self, lib_name: str, table_name: str):
        self.toolbar.click_btn_menu_by_test_id(TestID.QUERY_COLUMNS_PANE_TOOLBAR_ADD, Helper.data_locale.TABLE)
        self.st_dialog.select_a_table(lib_name, table_name)

    def add_a_column_by_dbclick(self, table_label, col_name):
        """
        Description: add a column from Columns pane to right pane by double-click the column.
        :param table_label: should be like "t1 (tablename)"
        :param col_name:
        """
        self.check_show_names_more_options()
        self.table_tree.navigate_to_element_and_dblclick([table_label, col_name])

    def add_a_column_by_context_menu(self, table_label, col_name):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        :param col_name:
        """
        self.check_show_names_more_options()
        self.table_tree.navigate_to_element_and_click_context_menu([table_label, col_name],
                                                                   Helper.data_locale.ADD_COLUMN)

    def add_all_columns_by_dbclick(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_dblclick([table_label])

    def add_all_columns_by_context_menu(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_click_context_menu([table_label], Helper.data_locale.ADD_COLUMNS)

    def delete_a_table_from_context_menu(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_click_context_menu([table_label], Helper.data_locale.REMOVE)
        if self.alert_dialog.is_open():
            self.alert_dialog.click_button_in_footer(Helper.data_locale.REMOVE)

    def delete_a_table_from_toolbar(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element([table_label])
        self.toolbar.click_btn_by_test_id(TestID.QUERY_COLUMNS_PANE_TOOLBAR_DELETE)
        if self.alert_dialog.is_open():
            self.alert_dialog.click_button_in_footer(Helper.data_locale.REMOVE)

    def collapse_all_table_tree(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.COLLAPSE_ALL)

    def expand_all_table_tree(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.EXPAND_ALL)

    def sort_table_tree_ascending_more_options(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.SORT_ASCENDING)

    def sort_table_tree_ascending_context_menu(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_click_context_menu([table_label], Helper.data_locale.SORT_ASCENDING)

    def sort_table_tree_descending_more_options(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.SORT_DESCENDING)

    def sort_table_tree_descending_context_menu(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_click_context_menu([table_label], Helper.data_locale.SORT_DESCENDING)

    def sort_table_tree_data_order_more_options(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.SORT_DATA_ORDER)

    def sort_table_tree_data_order_context_menu(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_click_context_menu([table_label], Helper.data_locale.SORT_DATA_ORDER)

    def check_select_non_dup_columns_more_options(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.SELECT_DISTINCT_ROWS_ONLY)

    def uncheck_select_non_dup_columns_more_options(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.SELECT_DISTINCT_ROWS_ONLY)

    def check_select_all_columns_more_options(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.SELECT_ALL_COLUMNS_IN_ALL_TABLES)

    def uncheck_select_all_columns_more_options(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.SELECT_ALL_COLUMNS_IN_ALL_TABLES)

    def check_show_names_more_options(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.SHOW_NAMES)

    def check_show_labels_more_options(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.SHOW_LABELS)

    def add_calculated_column(self):
        self.toolbar.click_btn_menu_by_test_id(TestID.QUERY_COLUMNS_PANE_TOOLBAR_ADD,
                                               Helper.data_locale.CALCULATE_COLUMNS)
        """incomplete"""

    def delete_a_calculated_column_from_toolbar(self, cal_col_name):
        self.table_tree.navigate_to_element([cal_col_name])
        self.toolbar.click_btn_by_test_id(TestID.QUERY_COLUMNS_PANE_TOOLBAR_DELETE)
        """incomplete"""

    def edit_a_calculated_column_from_toolbar(self, cal_col_name):
        self.table_tree.navigate_to_element([cal_col_name])
        self.toolbar.click_btn_by_test_id(TestID.QUERY_COLUMNS_PANE_TOOLBAR_EDIT)
        """incomplete"""

    def show_table_properties(self, table_label):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        """
        self.table_tree.navigate_to_element_and_click_context_menu([table_label], Helper.data_locale.PROPERTIES)
        """incomplete"""

    def show_column_properties(self, table_label, col_name):
        """
        Description: add a column from Columns pane to right pane by context menu.
        :param table_label: should be like "t1 (tablename)"
        :param col_name
        """
        self.check_show_names_more_options()
        self.table_tree.navigate_to_element_and_click_context_menu([table_label, col_name], Helper.data_locale.PROPERTIES)
        """incomplete"""
