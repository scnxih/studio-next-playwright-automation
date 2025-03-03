"""
@author: Frank (Feng) Jiang
@date: 2024/04/08
@description: define Select a Column dialog, include dialog elements and functionalities (temp)
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.treegrid import *
from src.Pages.Common.button import *
import time


class SelectColumnDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page)
        # Since this dialog loaded slow.
        time.sleep(1)
        self.combo_filter = Combobox(self.base_xpath, page, data_test_id=TestID.SELECT_A_COLUMN_DIALOG_FILTER_COMBO)
        self.input_search = Text(self.base_xpath, page, data_test_id=TestID.SELECT_A_COLUMN_DIALOG_SEARCH_INPUT)
        self.btn_search = Button(self.base_xpath, page, data_test_id=TestID.SELECT_A_COLUMN_DIALOG_SEARCH_BTN)
        self.col_treegrid = TreeGrid(self.base_xpath, page)
        self.alert_dialog = Alert(page, Helper.data_locale.SELECT_A_COLUMN)

    def fill_input_search(self, search_text: str):
        self.input_search.fill_text(search_text)

    def clear_input_search(self):
        self.input_search.clear_text()

    def click_btn_search(self):
        self.btn_search.click_self()

    def select_a_column_and_OK(self, col_name: str):
        self.clear_input_search()
        self.fill_input_search(col_name)
        self.key_press("Enter")
        time.sleep(1)
        if self.is_visible(self.col_treegrid.row_in_treegrid(name_text=col_name)):
            self.col_treegrid.select_a_row(name_text=col_name)

            self.click_button_in_footer(Helper.data_locale.OK)

        else:
            Helper.logger.debug("The column is not exist, please provide an existing column name.")

    """Added by Alice on July 31, 2024 start"""
    def set_check_in_a_row(self,col_name:str):
        self.clear_input_search()
        if self.is_visible(self.col_treegrid.row_in_treegrid(name_text=col_name)):
            self.col_treegrid.set_check_in_a_row(name_text=col_name)
        else:
            Helper.logger.debug("The column is not exist, please provide an existing column name.")
    def set_uncheck_in_a_row(self,col_name:str):
        self.clear_input_search()
        if self.is_visible(self.col_treegrid.row_in_treegrid(name_text=col_name)):
            self.col_treegrid.set_uncheck_in_a_row(name_text=col_name)
        else:
            Helper.logger.debug("The column is not exist, please provide an existing column name.")
    """Added by Alice on July 31, 2024 end"""
