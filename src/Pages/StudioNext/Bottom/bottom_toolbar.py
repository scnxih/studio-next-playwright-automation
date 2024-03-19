from src.Pages.Common.tab_group import TabGroup
from src.Utilities.enums import *
from src.Pages.Common.toolbar import *


class BottomToolbar(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.toolbar = Toolbar(self.base_xpath,page,
                               supplement_base_xpath="[.//button[@title='{0}']]".format(Helper.data_locale.SHOW_DOC_RECOVERY))
        self.tg = TabGroup("", page)

    def click_recovery(self):
        self.toolbar.click_btn_by_title_contains(Helper.data_locale.SHOW_DOC_RECOVERY)

    def click_submission_status(self):
        if not self.is_visible(self.tg.tab_by_text(Helper.data_locale.SUBMISSION_STATUS)):
            self.toolbar.click_btn_by_title_contains(Helper.data_locale.SHOW_OR_HIDE_SUBMISSION_STATUS)

    def click_keyboard_shortcuts(self):
        self.toolbar.click_btn_by_title_contains(Helper.data_locale.KEYBOARD_SHORTCUTS)
