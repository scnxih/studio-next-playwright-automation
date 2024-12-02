"""
@author: Frank (Feng) Jiang
@date: 2024/04/10
@description: This class is grid. It is used in Query Join page, custom step > column selector > select columns dialog,
select date dialog, value list in List/Drop-down controls
"""

from src.Pages.Common.common_component import CommonComponent
from src.Pages.Common.text import *
from src.Pages.Common.combobox import *
from src.Pages.Common.checkbox import *


class Grid(CommonComponent):
    def set_base_xpath(self):
        self.base_xpath += "//div[@role='grid']"

    def __init__(self, container_base_xpath, page, data_test_id="",supplement_base_xpath=""):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,
                                 supplement_base_xpath=supplement_base_xpath)

    def row_in_grid(self, row_index=None, grid_cell_text=None):
        """
        Description: get a row in a grid.
        :param row_index: int value, start from 1, optional.
        :param grid_cell_text: text shows in a cell of a row, case-sensitive, optional.
        :return: Locator
        """
        if row_index is None:
            return self.locate_xpath(
                f"//div[@role='row'][.//span[text()='{grid_cell_text}'] | .//input[@value='{grid_cell_text}']]")
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

    def input_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: get an input object (not a locator) in a cell.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        return Text(self.base_xpath + f"//div[@role='row'][@aria-rowindex='{row_index}']"
                                      f"//div[@role='gridcell'][@aria-colindex='{col_index}']", self.page)

    def get_value_input_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: get value of an input in a cell.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        if self.is_visible(self.input_in_a_cell(row_index, col_index).base_xpath):
            self.input_in_a_cell(row_index, col_index).get_value()
        else:
            Helper.logger.debug("The input is not available, please provide the correct input information.")

    def fill_input_in_a_cell(self, row_index: int, col_index: int, fill_text: str):
        """
        Description: input value to an input in a cell. Used in value list of List/Drop-down List control in custom step.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :param fill_text:
        :return:
        """
        if self.is_visible(self.input_in_a_cell(row_index, col_index).base_xpath):
            self.input_in_a_cell(row_index, col_index).fill_text(fill_text)
        else:
            Helper.logger.debug("The input is not available, please provide the correct input information.")

    def clear_input_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: clear value of an input in a cell. Used in value list of List/Drop-down List control in custom step.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :return:
        """
        if self.is_visible(self.input_in_a_cell(row_index, col_index).base_xpath):
            self.input_in_a_cell(row_index, col_index).clear_text()
        else:
            Helper.logger.debug("The input is not available, please provide the correct input information.")

    def btn_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: get a button locator in a cell.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return: Locator
        """
        return self.locate_xpath(f"//div[@role='row'][@aria-rowindex='{row_index}']//div[@role='gridcell']"
                                 f"[@aria-colindex='{col_index}']//button")

    def click_btn_in_a_cell(self, row_index: int, col_index: int):
        if self.is_visible(self.row_in_grid(row_index)) & "empty" not in self.get_attribute(self.row_in_grid(row_index),
                                                                                            "class"):
            self.click(self.btn_in_a_cell(row_index, col_index))
        else:
            Helper.logger.debug("This is an empty and invisible row, no button in this row, please provide a visible "
                                "row index.")

    def checkbox_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: get a checkbox object (not a locator) in a cell.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        return Checkbox(self.base_xpath + f"//div[@role='row'][@aria-rowindex='{row_index}']"
                                      f"//div[@role='gridcell'][@aria-colindex='{col_index}']", self.page)

    def check_checkbox_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: check a checkbox in a cell.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        if self.is_visible(self.checkbox_in_a_cell(row_index, col_index).base_xpath):
            self.checkbox_in_a_cell(row_index, col_index).set_check()
        else:
            Helper.logger.debug("The checkbox is not available, please provide the correct checkbox information.")

    def uncheck_checkbox_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: uncheck a checkbox in a cell.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1
        :return:
        """
        if self.is_visible(self.checkbox_in_a_cell(row_index, col_index).base_xpath):
            self.checkbox_in_a_cell(row_index, col_index).set_uncheck()
        else:
            Helper.logger.debug("The checkbox is not available, please provide the correct checkbox information.")

    def combo_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: get a combobox object (not a locator) in a row.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :return:
        """
        return Combobox(self.base_xpath + f"//div[@role='row'][@aria-rowindex='{row_index}']"
                                          f"//div[@role='gridcell'][@aria-colindex='{col_index}']", self.page)

    def click_combo_in_a_cell(self, row_index: int, col_index: int):
        """
        Description: click a combobox in a row to open dropdown list.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :return:
        """
        if self.is_visible(self.combo_in_a_cell(row_index, col_index).base_xpath):
            self.combo_in_a_cell(row_index, col_index).click_self()
        else:
            Helper.logger.debug("The combobox is not available, please provide the correct combobox information.")

    def select_item_combo_in_a_cell(self, row_index: int, col_index: int, combo_item_text: str):
        """
        Description: select an item from a combobox.
        :param row_index: int value, start from 1.
        :param col_index: int value, start from 1.
        :param combo_item_text:
        :return:
        """
        if self.is_visible(self.combo_in_a_cell(row_index, col_index).base_xpath):
            self.combo_in_a_cell(row_index, col_index).choose_item(combo_item_text)
        else:
            Helper.logger.debug("The combobox is not available, please provide the correct combobox information.")

    def grid_cell(self, cell_label=None, row_index=None, col_index=None):
        if row_index is None or col_index is None:
            return self.locate_xpath(f"//div[@role='gridcell'][.//span[text()='{cell_label}']]")
        if cell_label is None:
            return self.locate_xpath(f"//div[@role='row'][@aria-rowindex='{row_index}']"
                                     f"//div[@role='gredcell'][@aria-colindex='{col_index}']")

    def click_grid_cell(self, cell_label=None, row_index=None, col_index=None):
        if cell_label is None:
            if (self.is_visible(self.row_in_grid(row_index=row_index)) &
                    "empty" not in self.get_attribute(self.row_in_grid(row_index=row_index), "class")):
                self.click(self.grid_cell(row_index=row_index, col_index=col_index))
            else:
                Helper.logger.debug("The grid cell is not exist, please provide a correct row index.")
        if row_index is None or col_index is None:
            if self.is_visible(self.grid_cell(cell_label)):
                self.click(self.grid_cell(cell_label))
            else:
                Helper.logger.debug("The grid cell is not exist, please provide a correct cell label.")

    def col_header(self, header_label=None, col_index=None):
        if header_label is None:
            return self.locate_xpath(f"//div[@role='columnheader'][@aria-colindex='{col_index}']")
        if col_index is None:
            return self.locate_xpath(f"//div[@role='columnheader'][.//span[text()='{header_label}']]")

    def checkbox_on_col_header(self, col_index: int):
        """
        Description: get a checkbox object (not a locator) on column header.
        :param col_index: int value, start from 1.
        :return:
        """
        return Checkbox(self.base_xpath + f"//div[@role='columnheader'][@aria-colindex='{col_index}']", self.page)

    def check_checkbox_on_col_header(self, col_index: int):
        self.checkbox_on_col_header(col_index).set_check()

    def uncheck_checkbox_on_col_header(self, col_index: int):
        self.checkbox_on_col_header(col_index).set_uncheck()
