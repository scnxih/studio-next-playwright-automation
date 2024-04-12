"""
@author: Frank (Feng) Jiang
@date: 2024/04/10
@description: This class is grid. It is used in Query Join page
"""

from src.Pages.Common.common_component import CommonComponent
from src.Pages.Common.text import *
from src.Pages.Common.combobox import *


class Grid(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@role='grid']"

    def __init__(self, container_base_xpath, page, data_test_id=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id)

    def row_in_grid(self, row_index=None, grid_cell_text=None):
        """
        Description: get a row in a grid.
        :param row_index: int value, start from 1, optional.
        :param grid_cell_text: text shows in a cell of a row, case-sensitive, optional.
        :return: Locator
        """
        if row_index is None:
            return self.locate_xpath(f"//div[@role='row'][.//span[text()='{grid_cell_text}'] | .//input[@value='{grid_cell_text}']]")
        if grid_cell_text is None:
            return self.locate_xpath(f"//div[@role='row'][@aria-rowindex='{row_index}']")

    def select_a_row(self, row_index=None, grid_cell_text=None):
        """
        Description: select a row in a grid.
        :param row_index: int value, start from 1, optional.
        :param grid_cell_text: text shows in a cell of a row, case-sensitive, optional.
        :return: None
        """
        if row_index is None:
            if self.is_visible(self.row_in_grid(grid_cell_text=grid_cell_text)):
                self.click(self.row_in_grid(grid_cell_text=grid_cell_text))
            else:
                Helper.logger.debug("The row is not exist, please provide a correct string.")
        if grid_cell_text is None:
            if (self.is_visible(self.row_in_grid(row_index=row_index)) &
                    "empty" not in self.get_attribute(self.row_in_grid(row_index=row_index), "class")):
                self.click(self.row_in_grid(row_index=row_index))
            else:
                Helper.logger.debug("The row is not exist, please provide a correct row index.")

    def input_in_a_row(self, row_index: int, col_index: int):
        """
        Description: get an input object (not a locator) in a row.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        return Text(self.base_xpath + f"//div[@role='row'][@aria-rowindex='{row_index}']"
                                      f"//div[@role='gridcell'][@aria-colindex='{col_index}']", self.page)

    def get_value_input_in_a_row(self, row_index: int, col_index: int):
        """
        Description: get value of an input in a row.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        if self.is_visible(self.input_in_a_row(row_index, col_index).base_xpath):
            self.get_attribute(self.input_in_a_row(row_index, col_index), "value")
        else:
            Helper.logger.debug("The input is not available, please provide the correct input information.")

    def btn_in_a_row(self, row_index: int, col_index: int):
        """
        Description: get a button locator in a row.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return: Locator
        """
        return self.locate_xpath(f"//div[@role='row'][@aria-rowindex='{row_index}']//div[@role='gridcell']"
                                 f"[@aria-colindex='{col_index}']//button")

    def click_btn_in_a_row(self, row_index: int, col_index: int):
        if self.is_visible(self.row_in_grid(row_index)) & "empty" not in self.get_attribute(self.row_in_grid(row_index),
                                                                                            "class"):
            self.click(self.btn_in_a_row(row_index, col_index))
        else:
            Helper.logger.debug("This is an empty and invisible row, no button in this row, please provide a visible "
                                "row index.")

    def combo_in_a_row(self, row_index: int, col_index: int):
        """
        Description: get a combobox object (not a locator) in a row.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :return: Locator
        """
        return Combobox(self.base_xpath + f"//div[@role='row'][@aria-rowindex='{row_index}']"
                                          f"//div[@role='gridcell'][@aria-colindex='{col_index}']", self.page)

    def click_combo_in_a_row(self, row_index: int, col_index: int):
        """
        Description: click a combobox in a row to open dropdown list.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :return:
        """
        if self.is_visible(self.combo_in_a_row(row_index, col_index).base_xpath):
            self.combo_in_a_row(row_index, col_index).click_self()
        else:
            Helper.logger.debug("The combobox is not available, please provide the correct combobox information.")

    def select_item_combo_in_a_row(self, row_index: int, col_index: int, combo_item_text: str):
        """
        Description: select an item from a combobox.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :param combo_item_text:
        :return:
        """
        if self.is_visible(self.combo_in_a_row(row_index, col_index).base_xpath):
            self.combo_in_a_row(row_index, col_index).choose_item(combo_item_text)
        else:
            Helper.logger.debug("The combobox is not available, please provide the correct combobox information.")
