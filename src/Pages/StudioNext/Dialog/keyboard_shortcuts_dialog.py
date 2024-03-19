from src.Pages.Common.dialog import *
import time


class KeyboardShortcutsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.KEYBOARD_SHORTCUTS)

    @property
    def btn_footer_close(self):
        return self.get_by_test_id("keyboardShortcutsDialog-displayDialog-dismissButton")

    @property
    def input_search(self):
        return self.locate_xpath('//input[@class="sas_components-Input-Input_input"]')

    @property
    def link_manage_keyboard_shortcuts(self):
        return self.locate_xpath('//div[@data-testid="keyboardShortcutsDialog-displayDialog-footerControls'
                                 '"]/descendant::span[@class="sas_components-Button-__internal__-BaseButton_text"]')

    @property
    def icon_help(self):
        return self.locate_xpath('//button[contains(@class,"sas_components-Label-Label_help")]')

    @property
    def icon_clear(self):
        return self.locate_xpath('//button[contains(@class,"sas_components-Input-Input_clear-button")]')

    def search_keyboard_shortcuts(self, text):
        self.fill(self.input_search, text)
        self.wait_for_page_load()
        time.sleep(1)

    def clear_search_keyboard_shortcuts(self):
        self.click(self.icon_clear)
        self.wait_for_page_load()
        time.sleep(1)

    def close_keyboard_shortcuts(self):
        self.click(self.btn_footer_close)

    def check_help(self):
        self.click(self.icon_help)

    def goto_manage_keyboard_shortcuts(self):
        self.click(self.link_manage_keyboard_shortcuts)
