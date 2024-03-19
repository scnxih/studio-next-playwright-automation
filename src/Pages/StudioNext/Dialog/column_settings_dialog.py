"""
@author: Frank (Feng) Jiang
@date: Updated on 2023/09/19
@description: define Document Recovery dialog, include dialog elements and functionalities
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.treegrid import *
import time


class ColumnSettings(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.COLUMN_SETTINGS)

    def input_filter(self):
        return Text(self.base_xpath, self.page)

    @property
    def label_hidden_columns(self):
        label = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_HIDDEN_COLUMNS_LBL
        return self.locate_xpath(f"//label[contains(text(), '{label}')]")

    @property
    def label_displayed_columns(self):
        label = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_DISPLAYED_COLUMNS_LBL
        return self.locate_xpath(f"//label[contains(text(), '{label}')]")

    def column_by_label(self, col_label: str):
        return self.locate_xpath(f"//span[text()='{col_label}']")

    @property
    def btn_undo(self):
        btn_title = Helper.data_locale.UNDO
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_add(self):
        btn_title = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_add_all(self):
        btn_title = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_ALL_BTN
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_remove(self):
        btn_title = Helper.data_locale.REMOVE
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_remove_all(self):
        btn_title = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_REMOVE_ALL_BTN
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_move_to_top(self):
        btn_title = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_MOVE_TOP_BTN
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_move_up(self):
        btn_title = Helper.data_locale.MOVE_UP
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_move_down(self):
        btn_title = Helper.data_locale.MOVE_DOWN
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    @property
    def btn_move_to_bottom(self):
        btn_title = Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_MOVE_BOTTOM_BTN
        return self.locate_xpath(f"//button[@title='{btn_title}']")

    def clear_filter(self):
        self.input_filter().clear_text()

    def filter_column(self, col_label: str):
        is_disabled = self.input_filter().get_attribute("aria-disabled")
        if is_disabled == "false":
            self.clear_filter()
            self.input_filter().fill_text(col_label)

    def click_undo_btn(self):
        is_disabled = self.btn_undo.get_attribute("aria-disabled")
        if is_disabled == "false":
            Helper.logger.debug("Undo the previous operation.")
            self.click(self.btn_undo)
            return True
        else:
            Helper.logger.debug("No operation before, or 'Undo' has already done.")
            return False

    def select_a_column(self, col_label: str):
        self.input_filter().clear_text()
        is_selected = self.locate_xpath(f"//span[text()='{col_label}']/../../../..").get_attribute("class")
        if "Table_selected" in is_selected:
            Helper.logger.debug("The column is already selected.")
        else:
            Helper.logger.debug("Select column " + col_label)
            self.click(self.column_by_label(col_label))

    def add_a_column_to_display(self, col_label: str):
        self.input_filter().clear_text()
        self.select_a_column(col_label)
        title = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                  + "']/../following-sibling::div[1]/button").get_attribute("title")
        if title == Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN:
            Helper.logger.debug("Add column " + col_label + " to Displayed columns list.")
            self.click(self.btn_add)
        else:
            Helper.logger.debug("The selected column is already in Displayed columns list.")

    def add_all_columns_to_display(self):
        is_hidden_list_empty = self.input_filter().get_attribute("aria-disabled")
        is_btn_available = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                             + "']/../following-sibling::div[2]/button").get_attribute("title")
        if is_hidden_list_empty == "true":
            Helper.logger.debug("All columns have been added to Displayed columns list.")
        else:
            if is_btn_available != Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_ALL_BTN:
                Helper.logger.debug("Select a column in Hidden columns list, then click Add all button.")
                self.input_filter().clear_text()
                self.click(self.locate_xpath("//label[contains(text(), '"
                                             + Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_HIDDEN_COLUMNS_LBL
                                             + "')]/../../following-sibling::div[1]//div[@role='row']"
                                               "[@aria-rowindex='1']"))
                self.click(self.btn_add_all)
            else:
                Helper.logger.debug("Clear filter, then add all columns to Displayed columns list.")
                self.input_filter().clear_text()
                self.click(self.btn_add_all)

    def remove_a_column_to_hidden(self, col_label: str):
        self.input_filter().clear_text()
        self.select_a_column(col_label)
        title = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                  + "']/../following-sibling::div[1]/button").get_attribute("title")
        is_disabled = self.btn_remove.get_attribute("aria-disabled")
        if title == Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN:
            Helper.logger.debug("The selected column is already in Hidden columns list.")
        else:
            if is_disabled == "true":
                Helper.logger.debug("The columns " + Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_STATUS + ", "
                                    + Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_BACKGROUND_SUBMIT + " and "
                                    + Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_NAME
                                    + " can't be removed to Hidden columns list.")
            else:
                Helper.logger.debug("Remove column " + col_label + " to Hidden columns list.")
                self.click(self.btn_remove)

    def move_a_column_to_top(self, col_label: str):
        self.input_filter().clear_text()
        self.select_a_column(col_label)
        is_displayed_column = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                  + "']/../following-sibling::div[1]/button").get_attribute("title")
        is_disabled = self.btn_move_to_top.get_attribute("aria-disabled")
        if is_displayed_column == Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN:
            Helper.logger.debug("Column " + col_label + " is in Hidden columns list. "
                                                        "Add this column to Displayed columns list firstly, "
                                                        "then move it to the top.")
            self.click(self.btn_add)
            self.select_a_column(col_label)
            self.click(self.btn_move_to_top)
        else:
            if is_disabled == "true":
                Helper.logger.debug("Column " + col_label + " is already at the top.")
            else:
                Helper.logger.debug("Column " + col_label + " is in Displayed columns list, and not at the top. "
                                                            "Now, move it to the top.")
                self.click(self.btn_move_to_top)

    def move_a_column_to_bottom(self, col_label: str):
        self.input_filter().clear_text()
        self.select_a_column(col_label)
        is_displayed_column = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                                + "']/../following-sibling::div[1]/button").get_attribute("title")
        is_disabled = self.btn_move_to_bottom.get_attribute("aria-disabled")
        if is_displayed_column == Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN:
            Helper.logger.debug("Column " + col_label + " is in Hidden columns list. "
                                                        "Add this column to Displayed columns list firstly, "
                                                        "it will displays at the bottom.")
            self.click(self.btn_add)
        else:
            if is_disabled == "true":
                Helper.logger.debug("Column " + col_label + " is already at the bottom.")
            else:
                Helper.logger.debug("Column " + col_label + " is in Displayed columns list, and not at the bottom. "
                                                            "Now, move it to the bottom.")
                self.click(self.btn_move_to_bottom)

    def move_a_column_up(self, col_label: str):
        self.input_filter().clear_text()
        self.select_a_column(col_label)
        is_displayed_column = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                                + "']/../following-sibling::div[1]/button").get_attribute("title")
        is_disabled = self.btn_move_up.get_attribute("aria-disabled")
        if is_displayed_column == Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN:
            Helper.logger.debug("Column " + col_label + " is in Hidden columns list. "
                                                        "Add this column to Displayed columns list firstly, "
                                                        "then move it up.")
            self.click(self.btn_add)
            self.select_a_column(col_label)
            self.click(self.btn_move_up)
        else:
            if is_disabled == "true":
                Helper.logger.debug("Column " + col_label + " is already at the top, can't move up.")
            else:
                Helper.logger.debug("Column " + col_label + " is in Displayed columns list, and not at the top. "
                                                            "Now, move it up.")
                self.click(self.btn_move_up)

    def move_a_column_down(self, col_label: str):
        self.input_filter().clear_text()
        self.select_a_column(col_label)
        is_displayed_column = self.locate_xpath("//button[@title='" + Helper.data_locale.UNDO
                                                + "']/../following-sibling::div[1]/button").get_attribute("title")
        is_disabled = self.btn_move_down.get_attribute("aria-disabled")
        if is_displayed_column == Helper.data_locale.SUBMISSION_COLUMN_SETTINGS_ADD_BTN:
            Helper.logger.debug("Column " + col_label + " is in Hidden columns list. "
                                                        "Add this column to Displayed columns list firstly, "
                                                        "it will displays at the bottom, no need to move down.")
            self.click(self.btn_add)
        else:
            if is_disabled == "true":
                Helper.logger.debug("Column " + col_label + " is already at the bottom, can't move down.")
            else:
                Helper.logger.debug("Column " + col_label + " is in Displayed columns list, and not at the bottom. "
                                                            "Now, move it down.")
                self.click(self.btn_move_down)

    def close_dialog(self):
        self.click(self.btn_close)

    def click_ok_btn(self):
        self.click(self.btn_in_dialog_footer(Helper.data_locale.OK))

    def click_cancel_btn(self):
        self.click(self.btn_in_dialog_footer(Helper.data_locale.CANCEL))
