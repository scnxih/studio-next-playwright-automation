"""
Author: Alice
Date: October 23, 2023
Description: SAS Program/Python Program/Flow/Query/Quick Import will inherit this MainCenterPage class since they have
             similar toolbar methods.
"""
import time

from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.Common.tab_group import TabGroup


class MainCenterPage(CenterPage):
    def __init__(self, page):
        CenterPage.__init__(self, page)
        self.tab_group = TabGroup("", page)

    def run(self, if_wait_toast_disappear, if_wait_run_enabled=True):
        self.center_toolbar_helper.run(if_wait_toast_disappear, if_wait_run_enabled)

    def cancel(self, if_wait_toast_disappear):
        self.center_toolbar_helper.cancel(if_wait_toast_disappear)

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        self.center_toolbar_helper.save(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def saveas(self, folder_path: list, file_name, if_replace, if_wait_toast_disappear):
        self.center_toolbar_helper.saveas(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def schedule_as_job(self):
        self.center_toolbar_helper.schedule_as_job()
        # Dialog(self.toolbar.page, Helper.data_locale.ANALYZE_AND_CREATE_FLOW)

    def add_to_my_favorites(self):
        self.center_toolbar_helper.add_to_my_favorites()

    def open_in_browser_tab_summary(self):
        self.center_toolbar_helper.open_in_browser_tab_summary()

    def open_in_browser_tab_code(self):
        self.center_toolbar_helper.open_in_browser_tab_code()

    def open_in_browser_tab_log(self):
        self.center_toolbar_helper.open_in_browser_tab_log()

    def open_in_browser_tab_results(self):
        self.center_toolbar_helper.open_in_browser_tab_results()

    def open_in_browser_tab_listing(self):
        self.center_toolbar_helper.open_in_browser_tab_listing()

    def download_code_file(self):
        self.center_toolbar_helper.download_code_file()

    def download_log_file_html(self):
        self.center_toolbar_helper.download_log_file_html()

    def download_log_file_text(self):
        self.center_toolbar_helper.download_log_file_text()

    def download_results_file(self):
        self.center_toolbar_helper.download_results_file()

    def download_pdf_file(self):
        self.center_toolbar_helper.download_pdf_file()

    def download_word_file(self):
        self.center_toolbar_helper.download_word_file()

    def download_rtf_file(self):
        self.center_toolbar_helper.download_rtf_file()

    def download_excel_file(self):
        self.center_toolbar_helper.download_excel_file()

    def download_ppt_file(self):
        self.center_toolbar_helper.download_ppt_file()

    def download_listing_file(self):
        self.center_toolbar_helper.download_listing_file()

    def download_generated_data(self):
        self.center_toolbar_helper.download_generated_data()

    # def print_summary(self):
    #     self.center_toolbar_helper.print_summary()
    def email(self):
        self.center_toolbar_helper.email()

    def apply_detail_layout_standard(self):
        self.center_toolbar_helper.apply_detail_layout_standard()
        time.sleep(3)
        self.screenshot(self.base_xpath, "std")

    def apply_detail_layout_horizontal(self):
        self.center_toolbar_helper.apply_detail_layout_horizontal()
        time.sleep(3)
        self.screenshot(self.base_xpath, "horz")

    def apply_detail_layout_vertical(self):
        self.center_toolbar_helper.apply_detail_layout_vertical()
        time.sleep(3)
        self.screenshot(self.base_xpath, "vert")

    def hide_detail_tabs_code(self):
        self.center_toolbar_helper.hide_detail_tabs_code()
        time.sleep(1)
        self.screenshot(self.base_xpath, "hide_code")

    def show_detail_tabs_code(self):
        self.center_toolbar_helper.show_detail_tabs_code()
        time.sleep(1)
        self.screenshot(self.base_xpath, "show_code")

    def hide_detail_tabs_log(self):
        self.center_toolbar_helper.hide_detail_tabs_log()
        time.sleep(1)
        self.screenshot(self.base_xpath, "hide_log")

    def show_detail_tabs_log(self):
        self.center_toolbar_helper.show_detail_tabs_log()
        time.sleep(1)
        self.screenshot(self.base_xpath, "show_log")

    def hide_detail_tabs_result(self):
        self.center_toolbar_helper.hide_detail_tabs_result()
        time.sleep(1)
        self.screenshot(self.base_xpath, "hide_result")

    def show_detail_tabs_result(self):
        self.center_toolbar_helper.show_detail_tabs_result()
        time.sleep(1)
        self.screenshot(self.base_xpath, "show_details")

    def hide_detail_tabs_output_data(self):
        self.center_toolbar_helper.hide_detail_tabs_output_data()
        time.sleep(1)
        self.screenshot(self.base_xpath, "hide_output")

    def show_detail_tabs_output_data(self):
        self.center_toolbar_helper.show_detail_tabs_output_data()
        time.sleep(1)
        self.screenshot(self.base_xpath, "show_output")

    def hide_detail_tabs_listing(self):
        self.center_toolbar_helper.hide_detail_tabs_listing()
        time.sleep(1)
        self.screenshot(self.base_xpath, "hide_listing")

    def show_detail_tabs_listing(self):
        self.center_toolbar_helper.show_detail_tabs_listing()
        time.sleep(1)
        self.screenshot(self.base_xpath, "show_listing")

    def refresh(self):
        self.center_toolbar_helper.refresh()

    def background_submit(self, if_wait_toast_disappear=True):
        self.center_toolbar_helper.background_submit(if_wait_toast_disappear)
