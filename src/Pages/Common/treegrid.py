from src.Pages.Common.text import *
from src.Pages.Common.combobox import *

"""Added by Alice on 15/09/2023"""
from src.Pages.Common.common_component import CommonComponent


# This class is tree grid. It is used in Table page, Output tab, Submission Status page, Scheduled Jobs page, Query,
# Steps > Shared pane, Branch Rows step and Document Recovery dialog.
# For Table page and Output tab, col-id is integer, start from 0. Table row index column is 0, the first column is 1.


class TreeGrid(CommonComponent):
    """Added by Alice on 15/09/2023"""

    def set_base_xpath(self):
        self.base_xpath += "//div[@role='grid'or @role='treegrid']"

    """Modified by Alice on 15/09/2023"""

    def __init__(self, container_base_xpath, page, data_test_id="",supplement_base_xpath="",parent_label=""):
        if parent_label != "":
            supplement_base_xpath = "[.. /../../../../../ descendant::label[contains(text(), {0})]]".format(parent_label)
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page, data_test_id=data_test_id,supplement_base_xpath= supplement_base_xpath)

    def col_header(self, col_id: str):
        """
        Description: get column header by header's col-id.
        :param col_id: col-id of a column
        :return: Locator
        """
        return self.locate_xpath(f"//div[@col-id='{col_id}'][@role='columnheader']")

    def sort_column(self, col_id: str, sort_order: str):
        """
        Description: sort a column with 'none', 'ascending' or 'descending' order.
        :param col_id: col-id of a column
        :param sort_order: specify the sort order with 'none', 'ascending' or 'descending'
        :return:
        """
        Helper.logger.debug("Sort column")
        if self.is_visible(self.col_header(col_id)):
            while self.get_attribute(self.col_header(col_id), "aria-sort").lower() != sort_order.lower():
                self.click(self.col_header(col_id))
        else:
            Helper.logger.debug("The column maybe hidden or not exist, please provide a correct column information.")

    def btn_col_header_menu(self, col_id: str):
        """
        Description: get column header menu button by header's col-id.
        :param col_id: col-id of a column
        :return: Locator
        """
        return self.locate_xpath(f"//div[@col-id='{col_id}']//span[contains(@class, 'menu-button')]")

    def click_header_menu(self, col_id: str):
        """
        Description: click a menu button on a column header by col-id.
        If there is only one button in a row, don't specify test_id.
        :param col_id: col-id of a column
        """
        if self.is_visible(self.col_header(col_id)):
            self.click(self.btn_col_header_menu(col_id))
        else:
            Helper.logger.debug("The column maybe hidden or not exist, please provide a correct column information.")

    def row_in_treegrid(self, row_index=None, name_text=None):
        """
        Description: get a row in the grid by the name of the row or row-index, just need to give one param.
        :param row_index: start from 0
        :param name_text: the name text of a row
        :return: Locator
        """
        if name_text is None:
            return self.locate_xpath(f"//div[@role='row'][@row-index='{row_index}']")
        if row_index is None:

            if Helper.if_contain_quotation(name_text):
                escaped_text = Helper.escape_quotation_for_xpath(name_text)
                return self.locate_xpath(f"//div[@role='row'][contains(@class, 'ag-row')][.//span[text()={escaped_text}]|.//div[text()={escaped_text}]|.//div[@row-id={escaped_text}]]")
            else:
                return self.locate_xpath(
                    f"//div[@role='row'][contains(@class, 'ag-row')][.//span[text()='{name_text}'] | "
                    f".//div[text()='{name_text}'] | .//div[@row-id='{name_text}']]")


    def select_a_row(self, row_index=None, name_text=None):
        """
        Description: select a row in the grid by the name of the row or row-index, just need to give one param.
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        if self.is_visible(self.row_in_treegrid(row_index=row_index, name_text=name_text)):
            self.scroll_if_needed(self.row_in_treegrid(row_index=row_index, name_text=name_text))
            self.click(self.row_in_treegrid(row_index=row_index, name_text=name_text))
        else:
            Helper.logger.debug("The row is not available, please provide a correct row information.")

    def column_in_a_row(self, col_id: str, row_index=None, name_text=None):
        """
        Description: get a cell in a row by col-id and the name of the row or row-index.
        :param row_index: start from 0
        :param col_id: col-id of a column
        :param name_text: the name text of a row
        :return: Locator
        """
        if name_text is None:
            return self.locate_xpath(f"//div[@role='row'][@row-index='{row_index}']//div[@col-id='{col_id}']")
        if row_index is None:
            if Helper.if_contain_quotation(name_text):
                escaped_text = Helper.escape_quotation_for_xpath(name_text)
                return self.locate_xpath(f"//div[@role='row'][.//span[text()={escaped_text}]]//div[@col-id='{col_id}']")
            else:
                return self.locate_xpath(f"//div[@role='row'][.//span[text()='{name_text}']]//div[@col-id='{col_id}']")
    def click_column_in_a_row(self, col_id: str, row_index=None, name_text=None):
        """
        Description: if just select a row, give a none clickable column's col-id to param col_id.
        If click a functional or editable column in a row, give a clickable column's col-id to param col_id.
        For params row_index and name_text, just need one.
        :param row_index: start from 0
        :param col_id: col-id of a column
        :param name_text: the name text of a row
        """
        Helper.logger.debug("Click a column in a row")
        if self.is_visible(self.row_in_treegrid(row_index=row_index, name_text=name_text)):
            if self.is_visible(self.col_header(col_id)):
                self.click(self.column_in_a_row(col_id, row_index=row_index, name_text=name_text))
            else:
                Helper.logger.debug("The column maybe hidden or unavailable, please provide a correct column information.")
        else:
            Helper.logger.debug("The row is not available, please provide a correct row information.")

    def dbclick_column_in_a_row(self, col_id: str, row_index=None, name_text=None):
        """
        Description: double click a column in a row. For params row_index and name_text, just need one.
        :param row_index: start from 0
        :param col_id: col-id of a column
        :param name_text: the name text of a row
        """
        Helper.logger.debug("Click a column in a row")
        if self.is_visible(self.row_in_treegrid(row_index=row_index, name_text=name_text)):
            if self.is_visible(self.col_header(col_id)):
                self.dblclick(self.column_in_a_row(col_id, row_index=row_index, name_text=name_text))
            else:
                Helper.logger.debug(
                    "The column maybe hidden or unavailable, please provide a correct column information.")
        else:
            Helper.logger.debug("The row is not available, please provide a correct row information.")

    def input_in_a_row(self, test_id: str, row_index=None, name_text=None):
        """
        Description: get an input object (not a locator) in a row by data-testid and row-index or name of the row.
        :param test_id: data-testid of an input
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        if name_text is None:
            return Text(self.base_xpath + f"//div[@row-index='{row_index}']", self.page, data_test_id=test_id)
        if row_index is None:
            if Helper.if_contain_quotation(name_text):
                escaped_text = Helper.escape_quotation_for_xpath(name_text)
                return Text(self.base_xpath + f"//div[@role='row'][.//span[text()={escaped_text}]]", self.page,
                        data_test_id=test_id)
            else:
                return Text(self.base_xpath + f"//div[@role='row'][.//span[text()='{name_text}']]", self.page,
                            data_test_id=test_id)

    def fill_input_in_a_row(self, test_id: str, fill_text: str, row_index=None, name_text=None):
        """
        Description: fill an input in a row by data-testid and row-index or name of the row.
        :param test_id: data-testid of an input
        :param fill_text: filling text
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        if self.is_visible(self.input_in_a_row(test_id, row_index=row_index, name_text=name_text)):
            self.input_in_a_row(test_id, row_index=row_index, name_text=name_text).fill_text(fill_text)
        else:
            Helper.logger.debug("The input field is not available, please provide the correct input field information.")

    def clear_input_in_a_row(self, test_id: str, row_index=None, name_text=None):
        """
        Description: clear an input in a row by data-testid and row-index or name of the row.
        :param test_id: data-testid of an input
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        if self.is_visible(self.input_in_a_row(test_id, row_index=row_index, name_text=name_text)):
            self.input_in_a_row(test_id, row_index=row_index, name_text=name_text).clear_text()
        else:
            Helper.logger.debug("The input field is not available, please provide the correct input field information.")

    def get_value_input_in_a_row(self, test_id: str, row_index=None, name_text=None):
        """
        Description: get value from an input in a row by data-testid and row-index or name of the row.
        :param test_id: data-testid of an input
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        if self.is_visible(self.input_in_a_row(test_id, row_index=row_index, name_text=name_text)):
            return self.input_in_a_row(test_id, row_index=row_index, name_text=name_text).get_value()
        else:
            Helper.logger.debug("The input field is not available, please provide the correct input field information.")
            
    """Added by Alice on 2024/12/05 start"""

    def input_in_a_cell(self,col_id: str, row_index:int):
        """
        Description: get an input object (not a locator) in a cell by col_id and row_index.
        :param col_id: the string of col-id
        :param row_index: start from 0
        """

        return Text(self.base_xpath+"//div[@row-index='{0}']//div[@col-id='{1}']".format(row_index,col_id), self.page)


    def fill_input_in_a_cell(self,col_id: str, row_index:int, fill_text: str):
        """
        Description: fill an input in a cell by col_id and row_index.
        :param col_id: the string of col-id
        :param row_index: start from 0
        :param fill_text: filling text
        """
        text = self.input_in_a_cell(col_id=col_id, row_index=row_index)
        if self.is_visible(text):
            text.fill_text(fill_text)
        else:
            Helper.logger.debug("The input field is not available, please provide the correct input field information.")

    def clear_input_in_a_cell(self,col_id: str, row_index:int):
        """
        Description: clear an input in a cell by col_id and row_index.
        :param col_id: the string of col-id
        :param row_index: start from 0
        """
        text = self.input_in_a_cell(col_id=col_id, row_index=row_index)
        if self.is_visible(text):
            text.clear_text()
        else:
            Helper.logger.debug("The input field is not available, please provide the correct input field information.")

    def get_value_input_in_a_cell(self,col_id: str, row_index:int):
        """
        Description: get value from an input in a cell by col_id and row_index.
        :param col_id: the string of col-id
        :param row_index: start from 0
        """
        text = self.input_in_a_cell(col_id=col_id, row_index=row_index)
        if self.is_visible(text):
            return text.get_value()
        else:
            Helper.logger.debug("The input field is not available, please provide the correct input field information.")
    """Added by Alice on 224/12/05 end"""
    def btn_in_a_row(self, row_index=None, name_text=None, test_id=None):
        """
        Description: determine a row by row-index or name of the row, then get a button by data-testid if there is not
        only one button in a row. If there is only one button in a row, don't specify test_id.
        :param row_index: start from 0
        :param name_text: the name text of a row
        :param test_id: data-testid of a button
        :return: Locator
        """
        if name_text is None:
            if test_id is not None:
                return self.locate_xpath(f"//div[@row-index='{row_index}']//button[@data-testid='{test_id}']")
            else:
                return self.locate_xpath(f"//div[@row-index='{row_index}']//button[@type='button']")
        if row_index is None:
            if test_id is not None:
                if Helper.if_contain_quotation(name_text):
                    escaped_text = Helper.escape_quotation_for_xpath(name_text)
                    return self.locate_xpath(f"//div[@role='row'][.//span[text()={escaped_text}]]"
                                         f"//button[@data-testid='{test_id}']")
                else:
                    return self.locate_xpath(f"//div[@role='row'][.//span[text()='{name_text}']]"
                                             f"//button[@data-testid='{test_id}']")
            else:
                if Helper.if_contain_quotation(name_text):
                    escaped_text = Helper.escape_quotation_for_xpath(name_text)
                    return self.locate_xpath(f"//div[@role='row'][.//span[text()={escaped_text}]]//button[@type='button']")
                else:
                    return self.locate_xpath(
                        f"//div[@role='row'][.//span[text()='{name_text}']]//button[@type='button']")

    def click_btn_in_a_row(self, row_index=None, name_text=None, test_id=None):
        """
        Description: click a button in a row by row-index or name of the row and button data-testid if there is not only
        one button in a row. If there is only one button in a row, don't specify test_id.
        :param row_index: start from 0
        :param name_text: the name text of a row
        :param test_id: data-testid of a button
        """
        if self.is_visible(self.btn_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id)):
            self.scroll_if_needed(self.btn_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id))
            self.click(self.btn_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id))
        else:
            Helper.logger.debug("The button is not available, please provide the correct button information.")

    def combo_in_a_row(self, row_index=None, name_text=None, test_id=None):
        """
        Description: get a combobox object (not a locator) by row-index or name of the row.
        :param row_index: start from 0
        :param name_text: the name text of a row
        :param test_id: data-testid of combobox
        """
        if name_text is None:
            if test_id is not None:
                return Combobox(self.base_xpath + f"//div[@row-index='{row_index}']//div[@data-testid='{test_id}']/..",
                                self.page)
            else:
                return Combobox(self.base_xpath + f"//div[@row-index='{row_index}']", self.page)
        if row_index is None:
            if Helper.if_contain_quotation(name_text):
                escaped_text = Helper.escape_quotation_for_xpath(name_text)
                return Combobox(self.base_xpath + f"//div[@role='row'][.//span[text()={escaped_text}]]", self.page)
            else:
                return Combobox(self.base_xpath + f"//div[@role='row'][.//span[text()='{name_text}']]", self.page)

    def click_combo_in_a_row(self, row_index=None, name_text=None, test_id=None):
        """
        Description: click a combobox object (not a locator) in a row by row-index or name of the row.
        :param row_index: start from 0
        :param name_text: the name text of a row
        :param test_id: data-testid of combobox
        """
        # self.scroll_if_needed(self.base_xpath)
        if self.is_visible(self.combo_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id).base_xpath):
            self.combo_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id).click_self()
        else:
            Helper.logger.debug("The combobox is not available, please provide the correct combobox information.")

    def select_item_combo_in_a_row(self, combo_item_text: str, row_index=None, name_text=None, test_id=None):
        """
        Description: select item in a combobox in a row by row-index or name of the row.
        :param combo_item_text: text of item in combobox
        :param row_index: start from 0
        :param name_text: the name text of a row
        :param test_id: data-testid of combobox
        """
        # self.scroll_if_needed(self.base_xpath)
        if self.is_visible(self.combo_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id).base_xpath):
            self.combo_in_a_row(row_index=row_index, name_text=name_text, test_id=test_id).choose_item(combo_item_text)
        else:
            Helper.logger.debug("The combobox is not available, please provide the correct combobox information.")

    def select_context_menu_item(self, *context_menu_text, row_index=None, name_text=None):
        """
        Description: select a context menu item for a row.
        :param context_menu_text: text of menu item, support cascade.
        :param row_index: specify a row, start from 0.
        :param name_text: the name text of a row
        """
        if self.is_visible(self.row_in_treegrid(row_index=row_index, name_text=name_text)):
            self.click_context_menu_by_right_click(self.row_in_treegrid(row_index=row_index, name_text=name_text),
                                                   *context_menu_text)
        else:
            Helper.logger.debug("The row is not available, please provide a correct row information.")

    """Added by Alice on July 31, 2024 start"""
    def checkbox_container_in_a_row(self, row_index=None, name_text=None):
        """
        Description: get checkbox container by ro_index or name_text
        :param row_index: specify a row, start from 0.
        :param name_text: the name text of a row
        :return: Locator
        """
        if name_text is not None:
            if Helper.if_contain_quotation(name_text):
                row_id = str.replace(name_text,"'","&#39;")
                return self.locate_xpath(f"//div[@role='row'][@row-id='{row_id}']")
            else:
                return self.locate_xpath(f"//div[@role='row'][@row-id='{name_text}']")
        if row_index is not None:
            return self.locate_xpath(f"//div[@role='row'][@row-index='{row_index}']")

    def checkbox_in_a_row(self,row_index=None,name_text=None):
        """
        Description: get checkbox by ro_index or name_text
        :param row_index: specify a row, start from 0.
        :param name_text: the name text of a row
        :return: Locator
        """
        if name_text is not None:
            if Helper.if_contain_quotation(name_text):
                row_id = str.replace(name_text,"'","&#39;")
                return self.locate_xpath(f"//div[@role='row'][@row-id='{row_id}']//input[@type='checkbox']")
            else:
                return self.locate_xpath(f"//div[@role='row'][@row-id='{name_text}']//input[@type='checkbox']")
        if row_index is not None:
            return self.locate_xpath(f"//div[@role='row'][@row-index='{row_index}']//input[@type='checkbox']")

    def is_checked_in_a_row(self, row_index=None, name_text=None):
        """
        Description: check if a row is checked or not
        :param row_index: specify a row, start from 0.
        :param name_text: the name text of a row
        :return: Boolean
        """
        locator = self.checkbox_container_in_a_row(row_index = row_index,name_text=name_text)
        if self.get_attribute(locator,"aria-selected").lower() == "true":
            return True
        else:
            return False
    def set_check_in_a_row(self, row_index=None, name_text=None):
        """
        Description: Set check for a row
        :param row_index: specify a row, start from 0.
        :param name_text: the name text of a row
        :return: None
        """
        if self.is_checked_in_a_row(row_index=row_index,name_text=name_text):
            return
        else:
            self.click(self.checkbox_in_a_row(row_index=row_index,name_text=name_text))

    def set_uncheck_in_a_row(self, row_index=None, name_text=None):
        """
        Description: Set uncheck for a row
        :param row_index: specify a row, start from 0.
        :param name_text: the name text of a row
        :return: None
        """
        if self.is_checked_in_a_row(row_index=row_index,name_text=name_text):
            self.click(self.checkbox_in_a_row(row_index=row_index, name_text=name_text))
        else:
            return
    """Added by Alice on July 31, 2024 end"""