"""
@author: Frank (Feng) Jiang
@date: Updated on 2023/09/19
@description: define Document Recovery dialog, include dialog elements and functionalities
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.StudioNext.Dialog.column_settings_dialog import *
from src.Pages.Common.treegrid import *
import time


class ManageColumns(ColumnSettings):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.MANAGE_COLUMNS)

    def remove_all_columns_to_hidden(self):
        self.input_filter().clear_text()
        self.select_a_column(Helper.data_locale.TABLE)
        if self.btn_remove_all.is_visible():
            self.click(self.btn_remove_all)
        else:
            self.click(self.btn_add_all)
            self.click(self.btn_remove_all)
        self.click_ok_btn()
