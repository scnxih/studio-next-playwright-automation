from src.Pages.Common.dialog import *
from src.Pages.Common.base_page import *
from src.Utilities.enums import *
from src.Pages.Common.toolbar import *
from playwright.sync_api import Playwright, Page
import time


class ManageShortcutsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.MANAGE_KEYBOARD_SHORTCUTS)
        """modified by Alice on 09/15/2023 since common component constructor has been changed"""
        self.toolbar = Toolbar(self.base_xpath,page)

    @property
    def input_filter(self):
        return self.locate_xpath('//div[contains(@class,"sas_components-SearchField-SearchField_search-input'
                                 '")]//input[@class="sas_components-Input-Input_input"]')

    @property
    def combo_platform(self):
        return self.locate_xpath('//div[@role="combobox"]')


    @property
    def btn_more_options(self):
        return self.locate_xpath('//*[@href="#sas-svg-overflow"]')
        # return self.locate_xpath("'//button[@title=" +Helper.data_locale.MORE_OPTIONS+ "]'")

    @property
    def more_options_import(self):
        return self.locate_xpath("//span[text()='" + Helper.data_locale.IMPORTSHORTCUTS + "']")

    @property
    def more_options_export(self):
        return self.locate_xpath("//span[text()='" + Helper.data_locale.EXPORTSHORTCUTS + "']")

    @property
    def more_options_resetall(self):
        return self.locate_xpath("//span[text()='" + Helper.data_locale.RESETALLSHORTCUTS + "']")

    @property
    def icon_help(self):
        return self.locate_xpath('//button[contains(@class,"sas_components-Label-Label_help")]')

    @property
    def btn_save(self):
        return self.get_by_test_id("keyboardShortcutsDialog-manageDialog-firstButton")

    @property
    def btn_cancel(self):
        return self.get_by_test_id("keyboardShortcutsDialog-manageDialog-dismissButton")

    def field_keyboard_shortcut(self, label, field_num: int):
        """
        :param label: the label above the shortcuts field, e.g. 'Open the context menu:'
        :param field_num: 1 or 2
        """
        return self.locate_xpath(
            "//input[@aria-label='" + label + " " + Helper.data_locale.SHORTCUT + " " + str(
                field_num) + "']")

    def btn_reset_shortcut(self, label, field_num: int):
        """
        :param label: the label above the shortcuts field, e.g. 'Open the context menu:'
        :param field_num: 1 or 2
        """
        return self.locate_xpath(
            "//button[@aria-label='" + label + " " + Helper.data_locale.SHORTCUT + " " + str(
                field_num) + " " + Helper.data_locale.RESET + "']")

    def btn_clear_shortcut(self, label, field_num: int):
        """
        :param label: the label above the shortcuts field, e.g. 'Open the context menu:'
        :param field_num: 1 or 2
        """
        return self.locate_xpath(
            "//button[contains(@aria-label,'" + label + " " + Helper.data_locale.SHORTCUT + " " + str(
                field_num) + " " + Helper.data_locale.CLEAR + "')]")

    def filter_shortcut_field(self, label):
        label = label.rstrip(' :')
        self.fill(self.input_filter, label)
        self.wait_for_page_load()

    # def select_combo_item(self, dropdown_platform: Platform):
    #     match dropdown_platform:
    #         case Platform.microsoft_windows:
    #             self.combo_platform.select_option(Helper.data_locale.WINDOWS)
    #         case Platform.apple:
    #             self.combo_platform.select_option(Helper.data_locale.APPLE)
    #         case Platform.linux:
    #             self.combo_platform.select_option(Helper.data_locale.LINUX)

    def click_shortcut_field(self, label, field_num: int):
        self.click(self.field_keyboard_shortcut(label, field_num))
        self.wait_for_page_load()

    def input_shortcut(self, label, field_num: int, key, reassign):
        # self.filter_shortcut_field(label)
        # Helper.logger.debug("Search the keyboard short cut for edit")
        self.click_shortcut_field(label, field_num)
        self.key_press(key)
        edit_alert = Alert(self.page, Helper.data_locale.EDIT_SHORTCUT)
        if edit_alert.is_open():
            if reassign == 'reassign':
                Helper.logger.debug("Reassign the shortcut")
                edit_alert.click_button_in_footer(Helper.data_locale.REASSIGN)
                self.wait_for_page_load()
            elif reassign == 'cancel':
                Helper.logger.debug("Cancel the reassign")
                edit_alert.click_button_in_footer(Helper.data_locale.CANCEL)
                self.wait_for_page_load()
            elif reassign == 'close':
                Helper.logger.debug("Cannot reassign, close the error dialog")
                edit_alert.click_button_in_footer(Helper.data_locale.CLOSE)
                self.wait_for_page_load()

    def reset_shortcut(self, label, field_num: int):
        self.click(self.btn_reset_shortcut(label, field_num))
        self.wait_for_page_load()

    def clear_shortcut(self, label, field_num: int):
        self.click(self.btn_clear_shortcut(label, field_num))
        self.wait_for_page_load()

    def save_shortcut_setting(self):
        self.click(self.btn_save)

    def click_more_options(self):
        self.click(self.btn_more_options)

    def reset_all_shortcuts(self):
        self.click_menu_item(Helper.data_locale.RESETALLSHORTCUTS)

    def export_shortcuts(self):
        # self.toolbar.click_btn_in_more_options(Helper.data_locale.EXPORTSHORTCUTS)
        self.click_menu_item(Helper.data_locale.EXPORTSHORTCUTS)

    def check_help(self):
        self.click(self.icon_help)
