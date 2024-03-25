"""
@author: Frank (Feng) Jiang
@date: 2023/08/28
@description: define Submission Status page, include page elements and functionalities
"""
import time

from src.Data.elements_ids import *
from src.Pages.StudioNext.Center.center_page import *
from src.Pages.Common.treegrid import *
from src.Pages.Common.checkbox import *
from src.Pages.StudioNext.Dialog.column_settings_dialog import *


class SubmissionStatusPage(CenterPage):
    def __init__(self, page):
        CenterPage.__init__(self, page)
        self.treegrid = TreeGrid(self.base_xpath, self.page)
        self.col_settings_dialog = ColumnSettings(page)
        time.sleep(1)

    @property
    def input_search_toolbar(self):
        return Text(self.base_xpath, self.page, data_test_id=TestID.SUBMISSION_STATUS_TOOLBAR_INPUT_SEARCHINPUT)

    def fill_input_search_toolbar(self, fill_text: str):
        self.input_search_toolbar.fill_text(fill_text)

    def clear_input_search_toolbar(self):
        self.input_search_toolbar.clear_text()

    @property
    def btn_clear_search_text(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_TOOLBAR_BTN_SEARCHINPUT_CLEAR)

    def click_btn_clear_search_text(self):
        self.click(self.btn_clear_search_text)

    @property
    def btn_cancel_all(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_TOOLBAR_BTN_CANCEL_ALL)

    def cancel_all_jobs(self):
        """
        Description: click Cancel All button to cancel all jobs.
        """
        Helper.logger.debug("Cancel all jobs.")
        self.click(self.btn_cancel_all)

    @property
    def btn_clear_all(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_TOOLBAR_BTN_CLEAR_ALL)

    def clear_all_completed_submissions(self):
        """
        Description: click Clear All button to clear all completed submission.
        """
        Helper.logger.debug("Clear all completed submission.")
        self.click(self.btn_clear_all)

    def sort_column(self, col_header_col_id: str, sort_order: str):
        """
        Description: sort a column with 'none', 'ascending' or 'descending' order.
        :param col_header_col_id: give a column header's col-id
        :param sort_order: specify the sort order with 'none', 'ascending' or 'descending'
        """
        self.treegrid.sort_column(col_header_col_id, sort_order)

    def select_a_row(self, row_index=None, name_text=None):
        """
        Description: select a row of submissions indicated by row-index.
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        Helper.logger.debug("Select a row")
        self.treegrid.select_a_row(name_text=name_text, row_index=row_index)

    def open_submission_result(self, row_index=None, name_text=None):
        """
        Description: open results of a submission indicated by row-index.
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        Helper.logger.debug("Open submission results")
        self.treegrid.click_column_in_a_row(ColID.SUBMISSION_STATUS_CENTER_COL_HEAD_NAME, row_index=row_index,
                                            name_text=name_text)

    @property
    def filter_pane(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_FILTER_PANE)

    @property
    def status_section_filter_pane(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_FILTER_PANE_STATUS_SECTION)

    def expand_status_section_filter_pane(self):
        """
        Description: expand the title section if it is collapsed.
        """
        Helper.logger.debug("Expand the 'Status' title section")
        if self.get_attribute(self.status_section_filter_pane, "aria-expanded") == "false":
            self.click(self.status_section_filter_pane)

    def collapse_status_section_filter_pane(self):
        """
        Description: collapse the title section if it is expanded.
        """
        Helper.logger.debug("Collapse the 'Status' title section")
        if self.get_attribute(self.status_section_filter_pane, "aria-expanded") == "true":
            self.click(self.status_section_filter_pane)

    @property
    def btn_reset_filter_pane(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_FILTER_PANE_BTN_RESET)

    def reset_filter_in_filter_pane(self):
        """
        Description: click reset button to reset the status filter
        """
        Helper.logger.debug("Reset status filter")
        if self.get_attribute(self.btn_reset_filter_pane, "aria-disabled") == "false":
            self.btn_reset_filter_pane.click()

    def checkbox_status_filter_pane(self, status_label: str):
        # return Checkbox(self.base_xpath, self.page, label=status_label)
        return self.locate_xpath(f"//span[text()='{status_label}']/../../../../../../../..//div[@role='checkbox']")

    def check_statuses_filter_pane(self, *status_labels):
        """
        Description: check all or part of status checkboxes in Filter pane.
        :param status_labels: labels of status checkboxes, separated with comma.
        """
        self.expand_status_section_filter_pane()
        Helper.logger.debug("Check status checkboxes")
        for label in status_labels:
            # self.checkbox_status_filter_pane(label).set_check()
            is_checked = self.checkbox_status_filter_pane(label).get_attribute("aria-checked")
            if is_checked == "false":
                self.click(self.checkbox_status_filter_pane(label))

    def uncheck_statuses_filter_pane(self, *status_labels):
        """
        Description: uncheck all or part of status checkboxes in Filter pane.
        :param status_labels: labels of status checkboxes, separated with comma.
        """
        self.expand_status_section_filter_pane()
        Helper.logger.debug("Uncheck status checkboxes")
        for label in status_labels:
            # self.checkbox_status_filter_pane(label).set_check()
            is_checked = self.checkbox_status_filter_pane(label).get_attribute("aria-checked")
            if is_checked == "true":
                self.click(self.checkbox_status_filter_pane(label))

    def select_context_menu_item(self, *context_menu_text, row_index=None, name_text=None):
        """
        Description: select context menu using menu item text.
        :param context_menu_text: give menu item(s) text separated with comma
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        self.treegrid.select_context_menu_item(*context_menu_text, row_index=row_index, name_text=name_text)

    @property
    def btn_overflow(self):
        return self.get_by_test_id(TestID.SUBMISSION_STATUS_OVERFLOW)

    def open_overflow_menu(self):
        is_opened = self.get_attribute(self.btn_overflow, 'style')
        if "transparent" not in is_opened:
            self.click(self.btn_overflow)

    def close_overflow_menu(self):
        is_opened = self.get_attribute(self.btn_overflow, 'style')
        if "transparent" in is_opened:
            self.click(self.btn_overflow)

    @property
    def overflow_menu_item_column_settings(self):
        return self.locate_xpath(f"//ul[contains(@class, 'MenuList')]"
                                 f"//li[@data-testid='{TestID.SUBMISSION_STATUS_OVERFLOW_COLUMN_SETTINGS}']")

    @property
    def overflow_menu_item_show_all_submissions(self):
        return self.locate_xpath(f"//ul[contains(@class, 'MenuList')]"
                                 f"//li[@data-testid='{TestID.SUBMISSION_STATUS_OVERFLOW_SHOW_ALL_SUBMISSIONS}']")

    def check_show_all_submissions(self):
        self.open_overflow_menu()
        is_checked = self.overflow_menu_item_show_all_submissions().get_attribute("aria-checked")
        if is_checked == "false":
            self.click(self.overflow_menu_item_show_all_submissions())

    def uncheck_show_all_submissions(self):
        self.open_overflow_menu()
        is_checked = self.overflow_menu_item_show_all_submissions().get_attribute("aria-checked")
        if is_checked == "true":
            self.click(self.overflow_menu_item_show_all_submissions())

    def open_column_settings_dialog(self):
        self.open_overflow_menu()
        self.click(self.overflow_menu_item_column_settings())

    def show_all_columns(self):
        self.open_column_settings_dialog()
        self.col_settings_dialog.add_all_columns_to_display()
        self.col_settings_dialog.click_ok_btn()

    def add_columns_to_page(self, *col_labels: str):
        """
        Description: add hidden columns to Submission Status page.
        :param col_labels: labels of columns, separated with comma.
        """
        self.open_column_settings_dialog()
        for label in col_labels:
            self.col_settings_dialog.add_a_column_to_display(label)
        self.col_settings_dialog.click_ok_btn()

    def remove_columns_from_page(self, *col_labels: str):
        """
        Description: remove some displayed columns from Submission Status page.
        :param col_labels: labels of columns, separated with comma.
        """
        self.open_column_settings_dialog()
        for label in col_labels:
            self.col_settings_dialog.remove_a_column_to_hidden(label)
        self.col_settings_dialog.click_ok_btn()

    def move_a_column_to_left(self, col_label: str):
        self.open_column_settings_dialog()
        self.col_settings_dialog.move_a_column_up(col_label)
        self.col_settings_dialog.click_ok_btn()

    def move_a_column_to_right(self, col_label: str):
        self.open_column_settings_dialog()
        self.col_settings_dialog.move_a_column_down(col_label)
        self.col_settings_dialog.click_ok_btn()

    def move_a_column_to_leftmost(self, col_label: str):
        self.open_column_settings_dialog()
        self.col_settings_dialog.move_a_column_to_top(col_label)
        self.col_settings_dialog.click_ok_btn()

    def move_a_column_to_rightmost(self, col_label: str):
        self.open_column_settings_dialog()
        self.col_settings_dialog.move_a_column_to_bottom(col_label)
        self.col_settings_dialog.click_ok_btn()
