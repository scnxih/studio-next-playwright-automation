"""
@author: Frank (Feng) Jiang
@date: 2023/10/11
@description: define Query Output Library dialog, include dialog elements and functionalities (temp)
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
import time


class OutputLibDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, "输出逻辑库:")
        # Since this dialog loaded slow.
        time.sleep(1)

    @property
    def input_lib_name(self):
        return self.locate_xpath("//input[@role='input_libraryname']")

    def fill_input_lib_name(self, lib_name: str):
        self.fill(self.input_lib_name, lib_name)

    @property
    def input_table_name(self):
        return self.locate_xpath("//input[@role='input_tablename']")

    def fill_input_table_name(self, table_name: str):
        self.fill(self.input_table_name, table_name)

    def clear_input_table_name(self):
        self.clear(self.input_table_name)
