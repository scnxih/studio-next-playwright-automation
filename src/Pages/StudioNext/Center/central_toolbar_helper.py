import time
from playwright.sync_api import Playwright, Page

from src.Pages.Common.base_page import BasePage
from src.Pages.Common.dialog import *
from src.Pages.Common.menu_page import MenuPage
from src.Pages.Common.toolbar import Toolbar
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog
from src.Helper.helper import *
from src.Pages.Common.windows_control import *



class CentralToolbarHelper:
    def __init__(self, toolbar: Toolbar):
        self.toolbar = toolbar

    def run(self, if_wait_toast_disappear, if_wait_run_enabled=True):
        self.toolbar.click_btn_by_title(Helper.data_locale.RUN)
        if if_wait_toast_disappear:
            self.toolbar.wait_toast_disappear()
        if if_wait_run_enabled:
            self.toolbar.wait_until_enabled(self.toolbar.btn_by_title(Helper.data_locale.RUN))

    def cancel(self, if_wait_toast_disappear):
        self.toolbar.click_btn_by_title(Helper.data_locale.CANCEL)
        if if_wait_toast_disappear:
            self.toolbar.wait_toast_disappear()

    def background_submit(self, if_wait_toast_disappear=True):
        self.toolbar.click_btn_by_title(Helper.data_locale.USE_ANOTHER_SESSION_BRG_SUBMISSION)
        if if_wait_toast_disappear:
            self.toolbar.wait_toast_disappear()

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        self.toolbar.click_btn_by_title(Helper.data_locale.SAVE)
        if folder_path is None or file_name == "":
            if if_wait_toast_disappear:
                self.toolbar.wait_toast_disappear()
            return True
        save_as_dialog = SaveAsDialog(self.toolbar.page)
        if save_as_dialog.is_open():
            return save_as_dialog.save_file(folder_path, file_name, if_replace, if_wait_toast_disappear)
        else:
            return False

    def saveas(self, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        self.toolbar.click_btn_by_title(Helper.data_locale.SAVE_AS)
        save_as_dialog = SaveAsDialog(self.toolbar.page)
        if save_as_dialog.is_open():
            return save_as_dialog.save_file(folder_path, file_name, if_replace, if_wait_toast_disappear)
        return False

    def undo(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.UNDO)

    def redo(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.REDO)

    def clear_code(self):
        self.toolbar.click_btn_menu_by_title(Helper.data_locale.CLEAR, Helper.data_locale.CODE)

    def clear_all(self):
        self.toolbar.click_btn_menu_by_title(Helper.data_locale.CLEAR, Helper.data_locale.ALL)

    def clear_log(self):
        self.toolbar.click_btn_menu_by_title(Helper.data_locale.CLEAR, Helper.data_locale.LOG)

    def clear_results(self):
        self.toolbar.click_btn_menu_by_title(Helper.data_locale.CLEAR, Helper.data_locale.RESULTS)

    def clear_output_data(self):
        self.toolbar.click_btn_menu_by_title(Helper.data_locale.CLEAR, Helper.data_locale.OUTPUT_DATA)

    def clear_listing(self):
        self.toolbar.click_btn_menu_by_title(Helper.data_locale.CLEAR, Helper.data_locale.LISTING)





    """After the funtion is implemented in Studionext now, below method should be changed accordingly """

    def code_to_flow(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.CODE_TO_FLOW)

    """After the funtion is implemented in Studionext now, below method should be changed accordingly """

    def add_to_snippets(self):
        self.toolbar.click_btn_by_test_id_contains("toolbar-snippet")
        time.sleep(1)
        self.close_alert_if_needed()

    """After the funtion is implemented in Studionext now, below method should be changed accordingly """
    def close_alert_if_needed(self):
        alert = Alert(self.toolbar.page, Helper.data_locale.STUDIO_NEXT)
        if alert.is_open():
            # alert.close_alert_dialog(Helper.data_locale.CLOSE)
            alert.close_dialog()
    def schedule_as_job(self):
        enabled = self.toolbar.click_menu_in_more_options(Helper.data_locale.SCHEDULE_AS_JOB)
        time.sleep(1)
        if enabled:
            Dialog(self.toolbar.page,"新建预定").click_button_in_footer(Helper.data_locale.CANCEL)




    """After the funtion is implemented in Studionext now, below method should be changed accordingly """

    def analyze_and_create_flow(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.ANALYZE_AND_CREATE_FLOW)
        time.sleep(0.5)
        Dialog(self.toolbar.page, Helper.data_locale.ANALYZE_AND_CREATE_FLOW).click_button_in_footer(Helper.data_locale.CANCEL)
        time.sleep(0.3)
    """After the funtion is implemented in Studionext now, below method should be changed accordingly """

    def add_to_my_favorites(self):
        # Comment temporarily since there is no time to handle this. I will re-visit it once I have time.(Alice)
        # self.toolbar.click_menu_in_more_options(Helper.data_locale.ADD_TO_MY_FAVORITES)
        # self.close_alert_if_needed()
        pass

    def __open_in_browser_tab_menu(self, menu_text: str):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB)
        if not self.toolbar.is_menu_item_enabled(menu_text):
            self.toolbar.click_dialog_title_or_studionext_header()
            return
        with self.toolbar.page.expect_popup() as page2_info:
            self.toolbar.click_menu_item(menu_text)
        page2 = page2_info.value
        time.sleep(1)
        self.toolbar.page.bring_to_front()
        return page2

    def open_in_browser_tab_summary(self):
        return self.__open_in_browser_tab_menu(Helper.data_locale.SUMMARY)

    def open_in_browser_tab_code(self):
        return self.__open_in_browser_tab_menu(Helper.data_locale.CODE)

    def open_in_browser_tab_log(self):
        return self.__open_in_browser_tab_menu(Helper.data_locale.LOG)

    def open_in_browser_tab_results(self):
        return self.__open_in_browser_tab_menu(Helper.data_locale.RESULTS)

    def open_in_browser_tab_listing(self):
        return self.__open_in_browser_tab_menu(Helper.data_locale.LISTING)

    def __download_file(self, menu_text: str):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.DOWNLOAD)

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr. 8th, 2024

        # Wait for 0.5 sec, otherwise items might have not been loaded.
        time.sleep(1)
        print('+++ self.toolbar.page' + str(self.toolbar.page) +'+++')

        base = BasePage(self.toolbar.page)

        time.sleep(1)

        # works only for programs NOT WORK for Quick Import
        # base.screenshot("//div[@data-testid='programViewPane-toolbar-download-menu-content']", "download", user_assigned_xpath=True)

        # works for Quick Import NOT for programs
        # base.screenshot("//div[@data-testid='importViewPane-toolbar-download-menu-content']", "download", user_assigned_xpath=True)

        base.screenshot("//div[contains(@data-testid, 'toolbar-download-menu-content')]", "download", user_assigned_xpath=True)

        # END Added by Jacky(ID: jawang) on Apr. 8th, 2024 >>>

        if not self.toolbar.is_menu_item_enabled(menu_text):
            self.toolbar.click_dialog_title_or_studionext_header()
            return
        with self.toolbar.page.expect_download() as download_info:
            self.toolbar.click_menu_item(menu_text)
        download = download_info.value
        time.sleep(1)
        return download

    def download_code_file(self):
        return self.__download_file(Helper.data_locale.CODE_FILE)

    def download_log_file_html(self):
        return self.__download_file(Helper.data_locale.LOG_FILE_HTML)

    def download_log_file_text(self):
        return self.__download_file(Helper.data_locale.LOG_FILE_TEXT)

    def download_results_file(self):
        return self.__download_file(Helper.data_locale.RESULTS_FILE)

    def download_pdf_file(self):
        return self.__download_file(Helper.data_locale.PDF_FILE)

    def download_word_file(self):
        return self.__download_file(Helper.data_locale.WORD_FILE)

    def download_rtf_file(self):
        return self.__download_file(Helper.data_locale.RTF_FILE)

    def download_excel_file(self):
        return self.__download_file(Helper.data_locale.EXCEL_FILE)

    def download_ppt_file(self):
        return self.__download_file(Helper.data_locale.PPT_FILE)

    def download_listing_file(self):
        return self.__download_file(Helper.data_locale.LISTING_FILE)

    def download_generated_data(self):
        return self.__download_file(Helper.data_locale.GENERATED_DATA)

    # def __print(self, menu_text: str):
    #     self.toolbar.page.on("dialog",lambda dialog: dialog.accept())
    #     self.toolbar.click_menu_in_more_options(Helper.data_locale.PRINT, menu_text)
    # def print_summary(self):
    #     return self.__print(Helper.data_locale.SUMMARY)
    #
    def email(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.EMAIL)
        time.sleep(1)

        # ADDED
        # <<< Modified by Jacky(ID: jawang) on Mar.28th, 2024
        Dialog(self.toolbar.page, Helper.data_locale.EMAIL).screenshot_self('email')
        # Modified by Jacky(ID: jawang) on Mar.28th, 2024 >>>

        Dialog(self.toolbar.page,Helper.data_locale.EMAIL).click_button_in_footer(Helper.data_locale.CANCEL)

    def apply_detail_layout_standard(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_DETAIL_LAYOUT,Helper.data_locale.STANDARD)
    def apply_detail_layout_horizontal(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_DETAIL_LAYOUT,Helper.data_locale.HORIZONTAL)
    def apply_detail_layout_vertical(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_DETAIL_LAYOUT,Helper.data_locale.VERTICAL)

    def hide_detail_tabs_code(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.CODE)

    def show_detail_tabs_code(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.CODE)

    def hide_detail_tabs_log(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.LOG)

    def show_detail_tabs_log(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.LOG)

    def hide_detail_tabs_result(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.RESULTS)

    def show_detail_tabs_result(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.RESULTS)

    def hide_detail_tabs_output_data(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.OUTPUT_DATA)

    def show_detail_tabs_output_data(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,Helper.data_locale.OUTPUT_DATA)

    def hide_detail_tabs_listing(self):
        self.toolbar.uncheck_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,
                                                  Helper.data_locale.LISTING)

    def show_detail_tabs_listing(self):
        self.toolbar.check_menu_in_more_options(Helper.data_locale.HIDE_OR_SHOW_DETAIL_TABS,
                                                Helper.data_locale.LISTING)

    def reload(self):
        # self.toolbar.click_menu_in_more_options(Helper.data_locale.REFRESH)
        # self.close_alert_if_needed()
        pass

    def apply_main_layout_standard(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_MAIN_LAYOUT,Helper.data_locale.STANDARD)

    def apply_main_layout_horizontal(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_MAIN_LAYOUT,Helper.data_locale.HORIZONTAL)

    def apply_main_layout_vertical(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_MAIN_LAYOUT,Helper.data_locale.VERTICAL)
