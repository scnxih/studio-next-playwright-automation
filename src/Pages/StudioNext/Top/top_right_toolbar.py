from src.Utilities.enums import *
from src.Pages.Common.toolbar import *


class TopRightToolbar(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.toolbar = Toolbar(self.base_xpath,page,
                               supplement_base_xpath="[.//button[@aria-label='{0}']]".format(Helper.data_locale.SEARCH))

    def click_search(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.OPEN_SEARCH_WINDOW)

    def click_unread_notifications(self):
        self.toolbar.click_btn_by_title_contains(Helper.data_locale.UNREAD_NOTIFICATIONS)

    def click_new_features(self):
        self.toolbar.click_div_menu_by_title(Helper.data_locale.USER_OPTION,Helper.data_locale.WHATSNEW)

    def click_settings(self):
        self.toolbar.click_div_menu_by_title(Helper.data_locale.USER_OPTION,Helper.data_locale.SETTINGS)

    def click_sign_out(self):
        self.toolbar.click_div_menu_by_title(Helper.data_locale.USER_OPTION,Helper.data_locale.SIGN_OUT)

    def click_help(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.HELP)

    def click_user_option(self):
        self.toolbar.click_div_by_title(Helper.data_locale.USER_OPTION)

    def click_about(self):
        self.toolbar.click_div_menu_by_title(Helper.data_locale.USER_OPTION,Helper.data_locale.ABOUT)

    def click_manage_features(self):
        self.toolbar.click_div_menu_by_title(Helper.data_locale.USER_OPTION,Helper.data_locale.MANAGE_FEATURES)