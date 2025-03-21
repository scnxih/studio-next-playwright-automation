"""
@author: Frank (Feng) Jiang
@date: 2024/09/29
@description: define Select a Value dialog, include dialog elements and functionalities (temp)
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.treegrid import *
from src.Pages.Common.button import *
import time


class SelectAValueDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page)
        # Since this dialog loaded slow.
        time.sleep(1)
        self.combo_filter = Combobox(self.base_xpath, page, data_test_id=TestID.SELECT_A_VALUE_DIALOG_FILTER_COMBO)
        self.input_search = Text(self.base_xpath, page, data_test_id=TestID.SELECT_A_VALUE_DIALOG_SEARCH_INPUT)
        self.btn_search = Button(self.base_xpath, page, data_test_id=TestID.SELECT_A_VALUE_DIALOG_SEARCH_BTN)
        self.col_treegrid = TreeGrid(self.base_xpath, page)
        self.alert_dialog = Alert(page, Helper.data_locale.SELECT_A_VALUE_UPPER)

    def fill_input_search(self, search_text: str):
        self.input_search.fill_text(search_text)

    def clear_input_search(self):
        self.input_search.clear_text()

    def click_btn_search(self):
        self.btn_search.click_self()

    def select_a_value_and_OK(self, value: str):
        self.clear_input_search()
        if self.is_visible(self.col_treegrid.row_in_treegrid(name_text=value)):
            self.col_treegrid.select_a_row(name_text=value)
            self.click_button_in_footer(Helper.data_locale.OK)
        else:
            Helper.logger.debug("The value is not exist, please provide an existing value.")
