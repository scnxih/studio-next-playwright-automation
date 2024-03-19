"""
@author: Frank (Feng) Jiang
@date: 2023/09/19
@description: define Query Select Table dialog, include dialog elements and functionalities (temp)
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
import time


class SelectTableDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, "选择表")
        # Since this dialog loaded slow.
        time.sleep(1)

    @property
    def input_lib_name(self):
        return self.locate_xpath("//input[@role='input_libraryname']")

    def fill_input_lib_name(self, text):
        self.fill(self.input_lib_name, text)

    def clear_input_lib_name(self):
        self.clear(self.input_lib_name)

    @property
    def input_table_name(self):
        return self.locate_xpath("//input[@role='input_tablename']")

    def fill_input_table_name(self, text):
        self.fill(self.input_table_name, text)

    def clear_input_table_name(self):
        self.clear(self.input_table_name)
