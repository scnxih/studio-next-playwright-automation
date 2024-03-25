"""
@author: Frank (Feng) Jiang
@date: 2024/03/20
@description: define Query Select Table dialog, include dialog elements and functionalities (temp)
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.treegrid import *
import time


class SelectTableDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.SELECT_A_TABLE)
        # Since this dialog loaded slow.
        time.sleep(1)
        self.libs_treegrid = TreeGrid(self.base_xpath + "//section//section[1]", self.page)
        self.tables_treegrid = TreeGrid(self.base_xpath + "//section//section[2]", self.page)

    def select_a_table(self, lib_name: str, table_name: str):
        self.wait_for(self.libs_treegrid)
        self.scroll_if_needed(self.libs_treegrid.row_in_treegrid(name_text=lib_name))
        self.libs_treegrid.select_a_row(name_text=lib_name)
        self.wait_for(self.tables_treegrid)
        self.scroll_if_needed(self.tables_treegrid.row_in_treegrid(name_text=table_name))
        self.tables_treegrid.select_a_row(name_text=table_name)
        self.click_button_in_footer(Helper.data_locale.OK)
