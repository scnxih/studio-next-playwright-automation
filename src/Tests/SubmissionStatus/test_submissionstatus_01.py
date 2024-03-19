from src.Helper.page_helper import *
from src.Pages.StudioNext.Center.submission_status_page import *
from src.Data.elements_ids import *
import time


def test_01_search_submissions(page, init):
    PageHelper.submission_status_fill_input_search_toolbar(page, "abc")


def test_02_sort_column(page, init):
    """modified by Alice on 09/15/2023 since common component constructor has been changed"""
    Toolbar("", page).click_btn_by_title(Helper.data_locale.SHOW_HIDE_SUBMISSION_STATUS)
    submission_status = SubmissionStatusPage(page)
    time.sleep(1)
    submission_status.sort_column(ColID.SUBMISSION_STATUS_CENTER_COL_HEAD_NAME, "descending")
    time.sleep(1)
    submission_status.sort_column(ColID.SUBMISSION_STATUS_CENTER_COL_HEAD_TYPE, "descending")


def test_03_select_rows(page, init):
    """modified by Alice on 09/15/2023 since common component constructor has been changed"""
    PageHelper.new_sas_program(page)
    text = '''data test;\nset error;\nrun;'''
    PageHelper.type_code_in_codeeditor(page, text)
    Toolbar("", page).click_btn_by_title(Helper.data_locale.RUN)
    time.sleep(5)
    PageHelper.new_sas_program(page)
    text = '''data test;\nset sashelp.class;\nrun;'''
    PageHelper.type_code_in_codeeditor(page, text)
    Toolbar("", page).click_btn_by_title(Helper.data_locale.RUN)
    time.sleep(5)
    Toolbar("", page).click_btn_by_title(Helper.data_locale.SHOW_HIDE_SUBMISSION_STATUS)
    submission_status = SubmissionStatusPage(page)
    time.sleep(1)
    submission_status.select_a_row(row_index=0)
    time.sleep(1)
    submission_status.select_a_row(name_text="SAS 程序.sas")


def test_04_sidebar_columns(page, init):
    """modified by Alice on 09/15/2023 since common component constructor has been changed"""
    Toolbar("", page).click_btn_by_title(Helper.data_locale.SHOW_HIDE_SUBMISSION_STATUS)
    submission_status = SubmissionStatusPage(page)
    time.sleep(1)
    submission_status.open_columns_pane()
    time.sleep(1)
    submission_status.uncheck_columns_in_columns_pane(Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_NAME,
                                                      Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_TYPE)
    time.sleep(1)
    submission_status.check_columns_in_columns_pane(Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_NAME,
                                                    Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_TYPE,
                                                    Helper.data_locale.SUBMISSION_SIDEBAR_COLUMNS_SUBMITTED)


def test_05_sidebar_filters(page, init):
    Toolbar("", page).click_btn_by_title(Helper.data_locale.SHOW_HIDE_SUBMISSION_STATUS)
    submission_status = SubmissionStatusPage(page)
    time.sleep(1)
    # submission_status.open_filters_pane()
    # time.sleep(1)
    submission_status.collapse_status_section_filters_pane()
    time.sleep(1)
    submission_status.expand_status_section_filters_pane()
    time.sleep(1)
    submission_status.fill_input_search_sidebar_filters("abc")
    time.sleep(1)
    submission_status.clear_input_search_sidebar_filters()
    submission_status.uncheck_checkboxes_sidebar_filters(Helper.data_locale.SUBMISSION_SIDEBAR_FILTERS_ERROR,
                                                         Helper.data_locale.SUBMISSION_SIDEBAR_FILTERS_SUCCESS)
    submission_status.check_checkboxes_sidebar_filters(Helper.data_locale.SUBMISSION_SIDEBAR_FILTERS_ERROR,
                                                       Helper.data_locale.SUBMISSION_SIDEBAR_FILTERS_SUCCESS)


def test_06_context_menu(page, init):
    PageHelper.new_sas_program(page)
    text = '''data test;\nset error;\nrun;'''
    PageHelper.type_code_in_codeeditor(page, text)
    Toolbar("", page).click_btn_by_title(Helper.data_locale.RUN)
    time.sleep(5)
    PageHelper.new_sas_program(page)
    text = '''data test;\nset sashelp.class;\nrun;'''
    PageHelper.type_code_in_codeeditor(page, text)
    Toolbar("", page).click_btn_by_title(Helper.data_locale.RUN)
    time.sleep(5)
    Toolbar("", page).click_btn_by_title(Helper.data_locale.SHOW_HIDE_SUBMISSION_STATUS)
    submission_status = SubmissionStatusPage(page)
    time.sleep(1)
    submission_status.select_context_menu_item("打开提交的代码", name_text="SAS 程序.sas")
    time.sleep(5)
    submission_status.select_context_menu_item("打开提交的代码", row_index=0)
    # time.sleep(2)
    # submission_status.open_submission_results(name_text="SAS 程序.sas")
    # time.sleep(2)
    # submission_status.open_submission_results(row_index=0)
