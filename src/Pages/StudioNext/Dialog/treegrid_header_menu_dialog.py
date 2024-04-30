"""
@author: Frank (Feng) Jiang
@date: 2024/03/20
@description: define column header menu dialog, include dialog elements and functionalities (temp)
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.treegrid_cont_menu import *
from src.Pages.Common.treegrid import *
import time


class HeaderMenuDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page)
        self.menu_list = TreegridContextMenu(self, page)
        self.input_search = Text(self, page)

    @property
    def tab_general(self):
        return self.locate_xpath("//span[@role='tab'][@aria-label='general']")

    @property
    def tab_columns(self):
        return self.locate_xpath("//span[@role='tab'][@aria-label='columns']")

    @property
    def tab_filter(self):
        return self.locate_xpath("//span[@role='tab'][@aria-label='filter']")

    def go_to_general_tab(self):
        is_selected = self.tab_general().get_attribute("class")
        if "selected" not in is_selected:
            self.click(self.tab_general())

    def go_to_columns_tab(self):
        is_selected = self.tab_columns().get_attribute("class")
        if "selected" not in is_selected:
            self.click(self.tab_columns())

    def go_to_filter_tab(self):
        is_selected = self.tab_filter().get_attribute("class")
        if "selected" not in is_selected:
            self.click(self.tab_filter())

    def no_pin_a_column(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.PIN_COLUMN)
        self.menu_list.click_menu_item_by_text(Helper.data_locale.NO_PIN)

    def left_pin_a_column(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.PIN_COLUMN)
        self.menu_list.click_menu_item_by_text(Helper.data_locale.PIN_LEFT)

    def right_pin_a_column(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.PIN_COLUMN)
        self.menu_list.click_menu_item_by_text(Helper.data_locale.PIN_RIGHT)

    def autosize_a_column(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.AUTOSIZE_THIS_COLUMN)

    def autosize_all_columns(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.AUTOSIZE_ALL_COLUMNS)

    def hide_a_column(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.HIDE_COLUMN)

    def manage_columns(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.MANAGE_COLUMNS_LOWER)

    def reset_states_of_columns(self):
        self.go_to_general_tab()
        self.menu_list.click_menu_item_by_text(Helper.data_locale.RESET_STATES_OF_COLUMNS)

    @property
    def checkbox_select_all_columns(self):
        return self.locate_xpath("//input[@type='checkbox'][@aria-label='Toggle Select All Columns']/..")

    def check_checkbox_select_all_columns(self):
        is_checked = self.get_attribute(self.checkbox_select_all_columns, "class")
        if "ag-check" not in is_checked:
            self.click(self.checkbox_select_all_columns)

    def uncheck_checkbox_select_all_columns(self):
        is_checked = self.get_attribute(self.checkbox_select_all_columns, "class")
        if "ag-check" in is_checked:
            self.click(self.checkbox_select_all_columns)

    def fill_input_search(self, search_text: str):
        self.go_to_columns_tab()
        self.input_search.fill_text(search_text)

    def clear_input_search(self):
        self.go_to_columns_tab()
        self.input_search.clear_text()

    def checkbox_column_header(self, col_label: str):
        return self.locate_xpath(f"//span[text()='{col_label}']/preceding-sibling::div[1]/div[2]")

    def check_checkbox_column_header(self, col_label: str):
        is_checked = self.get_attribute(self.checkbox_column_header(col_label), "class")
        if "ag-check" not in is_checked:
            self.scroll_if_needed(self.checkbox_column_header(col_label))
            self.click(self.checkbox_column_header(col_label))

    def uncheck_checkbox_column_header(self, col_label: str):
        is_checked = self.get_attribute(self.checkbox_column_header(col_label), "class")
        if "ag-check" in is_checked:
            self.scroll_if_needed(self.checkbox_column_header(col_label))
            self.click(self.checkbox_column_header(col_label))

    def apply_and_close(self):
        self.go_to_general_tab()
        self.click(self.tab_general)
