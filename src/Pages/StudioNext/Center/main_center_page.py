"""
Author: Alice
Date: October 23, 2023
Description: SAS Program/Python Program/Flow/Query/Quick Import will inherit this MainCenterPage class since they have
             similar toolbar methods.
"""
import time

from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.Common.tab_group import TabGroup
from src.Helper.helper import Helper


class MainCenterPage(CenterPage):
    def __init__(self, page):
        CenterPage.__init__(self, page)
        self.tab_group = TabGroup("", page)
        self.time_info_array = ['//span[@class="mtk25"][contains(text(),"CPU")]/..',
                                '//span[@class="mtk25"][contains(text(),"实际")]/..']

    @property
    def time_info_in_log(self):
        return ['//span[@class="mtk25"][contains(text(),"CPU")]/..',
                '//span[@class="mtk25"][contains(text(),"实际")]/..']

    @property
    def proc_print_page_num_in_log(self):
        return ['//span[@class="mtk25"][contains(text(),"已打印")]/..']

    @property
    def program_toolbar(self):
        return ['//div[@role="group"][@data-testid="programViewPane-toolbar"]']

    def selfie(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the vanilla screenshot_self method in BasePage
        """
        Helper.logger.debug("Enter MainCenterPage selfie ...")

        Helper.logger.debug("MainCenterPage: Overwrite the vanilla screenshot_self method in BasePage")
        time.sleep(0.5)
        self.click_dialog_title_or_studionext_header()
        time.sleep(0.5)
        self.screenshot(self.base_xpath, pic_name, clip=clip,

                        # Original
                        # mask=self.time_info_in_log + self.proc_print_page_num_in_log + [self.toolbar.btn_by_title(Helper.data_locale.RUN)],

                        # Revised on Thursday, Feb 20, 2025
                        mask=self.time_info_in_log + self.proc_print_page_num_in_log +
                             [self.toolbar.btn_by_test_id_contains("toolbar-runButton")],
                        mask_color="#000000")

        Helper.logger.debug("... Exit MainCenterPage selfie")

    def run(self, if_wait_toast_disappear, if_wait_run_enabled=True):
        self.center_toolbar_helper.run(if_wait_toast_disappear, if_wait_run_enabled)

    def cancel(self, if_wait_toast_disappear):
        self.center_toolbar_helper.cancel(if_wait_toast_disappear)

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        self.center_toolbar_helper.save(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def saveas(self, folder_path: list, file_name, if_replace, if_wait_toast_disappear):
        self.center_toolbar_helper.saveas(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def saveas2(self, folder_path: list, file_name, if_replace, if_wait_toast_disappear):
        """
        Supplemented a method to click SAS Content/SAS Server grid-cell while saving files.
        """
        self.center_toolbar_helper.saveas2(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def schedule_as_job(self):
        self.center_toolbar_helper.schedule_as_job()
        # Dialog(self.toolbar.page, Helper.data_locale.ANALYZE_AND_CREATE_FLOW)

    def add_to_my_favorites(self):
        self.center_toolbar_helper.add_to_my_favorites()

    def open_in_browser_tab_summary(self):
        self.center_toolbar_helper.open_in_browser_tab_summary()

    def open_in_browser_tab_submitted_code(self):
        self.center_toolbar_helper.open_in_browser_tab_submitted_code()

    def open_in_browser_tab_log(self):
        self.center_toolbar_helper.open_in_browser_tab_log()

    def open_in_browser_tab_results(self):
        self.center_toolbar_helper.open_in_browser_tab_results()

    def open_in_browser_tab_listing(self):
        self.center_toolbar_helper.open_in_browser_tab_listing()

    def download_submitted_code_file(self):
        self.center_toolbar_helper.download_submitted_code_file()

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
        # time.sleep(3)
        self.wait_for_page_load()
        """
        self.screenshot(self.base_xpath, "std",
                        mask=self.time_info_in_log,
                        mask_color="#000000")
        """

        # data-testid="importViewPane-toolbar-toggle-detail-layout"
        self.selfie("std")
        self.screenshot(self.base_xpath, "std",
                        mask=[self.get_by_test_id(
                            "importViewPane-toolbar-toggle-detail-layout")] + self.time_info_in_log + self.proc_print_page_num_in_log +
                             [self.toolbar.btn_by_title(Helper.data_locale.RUN)], mask_color="#000000")

    def apply_detail_layout_horizontal(self):
        self.center_toolbar_helper.apply_detail_layout_horizontal()
        # time.sleep(3)
        self.wait_for_page_load()
        self.selfie("horz")
        self.screenshot(self.base_xpath, "horz",
                        mask=self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.toolbar.btn_by_title(Helper.data_locale.RUN)] + [
                                 self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def apply_detail_layout_vertical(self):
        self.center_toolbar_helper.apply_detail_layout_vertical()

    def hide_detail_tabs_code(self):
        self.center_toolbar_helper.hide_detail_tabs_code()
        # time.sleep(1)
        self.wait_for_page_load()

        self.selfie("hide_code")
        self.screenshot(self.base_xpath, "hide_code",
                        mask=self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def show_detail_tabs_code(self):
        self.center_toolbar_helper.show_detail_tabs_code()
        # time.sleep(3)
        self.wait_for_page_load()
        self.selfie("show_code")
        self.screenshot(self.base_xpath, "show_code",
                        mask=self.program_toolbar + self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def hide_detail_tabs_submitted_code(self):
        self.center_toolbar_helper.hide_detail_tabs_submitted_code()
        # time.sleep(1)
        self.wait_for_page_load()
        self.selfie("hide_code")
        self.screenshot(self.base_xpath, "hide_code",
                        mask=self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def show_detail_tabs_submitted_code(self):
        self.center_toolbar_helper.show_detail_tabs_submitted_code()
        # time.sleep(3)
        self.wait_for_page_load()

        self.selfie("show_code")
        self.screenshot(self.base_xpath, "show_code",
                        mask=self.program_toolbar + self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def hide_detail_tabs_log(self):
        self.center_toolbar_helper.hide_detail_tabs_log()
        # time.sleep(1)
        self.wait_for_page_load()

        self.selfie("hide_log")
        self.screenshot(self.base_xpath, "hide_log",
                        mask=[self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def show_detail_tabs_log(self):
        self.center_toolbar_helper.show_detail_tabs_log()
        # time.sleep(3)
        self.wait_for_page_load()

        self.selfie("show_log")
        self.screenshot(self.base_xpath, "show_log",
                        mask=self.program_toolbar + self.proc_print_page_num_in_log + self.time_info_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def hide_detail_tabs_result(self):
        self.center_toolbar_helper.hide_detail_tabs_result()
        time.sleep(3)
        self.selfie("hide_result")
        self.screenshot(self.base_xpath, "hide_result",
                        mask=self.time_info_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def show_detail_tabs_result(self):
        self.center_toolbar_helper.show_detail_tabs_result()
        # time.sleep(1)
        self.wait_for_page_load()

        self.selfie("show_details")
        self.screenshot(self.base_xpath, "show_details",
                        mask=self.program_toolbar + self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def hide_detail_tabs_output_data(self):
        self.center_toolbar_helper.hide_detail_tabs_output_data()
        # time.sleep(1)
        self.wait_for_page_load()

        self.selfie("hide_output")
        self.screenshot(self.base_xpath, "hide_output",
                        mask=self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def show_detail_tabs_output_data(self):
        self.center_toolbar_helper.show_detail_tabs_output_data()
        # time.sleep(1)
        self.wait_for_page_load()

        self.selfie("show_output")
        self.screenshot(self.base_xpath, "show_output",
                        mask=self.program_toolbar + self.time_info_in_log + self.proc_print_page_num_in_log +
                             [self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def hide_detail_tabs_listing(self):
        Helper.logger.debug('Entering Hide detail tab-->Listing')

        self.center_toolbar_helper.hide_detail_tabs_listing()

        self.wait_for_page_load()

        self.selfie("hide_listing")
        self.screenshot(self.base_xpath, "hide_listing",
                        mask=self.time_info_array + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def show_detail_tabs_listing(self):
        Helper.logger.debug('Entering Show detail tab-->Listing')

        self.center_toolbar_helper.show_detail_tabs_listing()

        self.wait_for_page_load()

        self.selfie("show_listing")
        self.screenshot(self.base_xpath, "show_listing",
                        mask=self.time_info_in_log + self.proc_print_page_num_in_log + [
                            self.get_by_test_id("importViewPane-toolbar-toggle-detail-layout")],
                        mask_color="#000000")

    def reload(self):
        self.center_toolbar_helper.reload()

    def background_submit(self, if_wait_toast_disappear=True):
        self.center_toolbar_helper.background_submit(if_wait_toast_disappear)
