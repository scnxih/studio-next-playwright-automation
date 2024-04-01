"""
Author: Alice
Date: November 06, 2023
Description: DeployedScheduledJobPage will inherit from CenterPage class。

"""
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.Common.tab_group import TabGroup
from src.Pages.StudioNext.Center.center_page import *


class JobDefinitionPage(CenterPage):

    def __init__(self, page):
        CenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)
        self.tab_group = TabGroup("",page)

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        self.center_toolbar_helper.save(folder_path,file_name,if_replace,if_wait_toast_disappear)
    def saveas(self, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        self.center_toolbar_helper.saveas(folder_path,file_name,if_replace,if_wait_toast_disappear)

    def undo(self):
        self.center_toolbar_helper.undo()

    def redo(self):
        self.center_toolbar_helper.redo()

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()

    def schedule_as_job(self):
        self.center_toolbar_helper.schedule_as_job()

    def __close_alert_if_needed(self):
        alert = Alert(self.page, Helper.data_locale.STUDIO_NEXT)
        if alert.is_open():
            # alert.close_alert_dialog(Helper.data_locale.CLOSE)
            alert.close_dialog()
    def open_in_browser_tab_code(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB)
        if not self.toolbar.is_menu_item_enabled(Helper.data_locale.CODE):
            self.toolbar.click_dialog_title_or_studionext_header()
            return
        self.toolbar.click_menu_item(Helper.data_locale.CODE)
        self.__close_alert_if_needed()

    def open_in_browser_tab_job_form(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB)
        if not self.toolbar.is_menu_item_enabled(Helper.data_locale.JOB_FORM):
            self.toolbar.click_dialog_title_or_studionext_header()
            return
        self.toolbar.click_menu_item(Helper.data_locale.JOB_FORM)
        self.__close_alert_if_needed()

    def apply_main_layout_standard(self):
        self.center_toolbar_helper.apply_main_layout_standard()

    def apply_main_layout_horizontal(self):
        self.center_toolbar_helper.apply_main_layout_horizontal()

    def apply_main_layout_vertical(self):
        self.center_toolbar_helper.apply_main_layout_vertical()

    def refresh(self):
        self.center_toolbar_helper.refresh()