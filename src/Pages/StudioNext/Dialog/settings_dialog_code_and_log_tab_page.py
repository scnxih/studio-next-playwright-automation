from src.Pages.Common.dialog import *
from src.Utilities.enums import log_options


class SettingsDialogCodeAndLogTabPage(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.CODE_AND_LOG)

    @property
    def checkbox_display_error_in_gutter(self):
        # test_id showSASCodeInLog-checkbox-checkbox
        return self.get_by_test_id("showSASCodeInLog-checkbox-checkbox")

    @property
    def checkbox_show_sas_code_in_log(self):
        # test_id displayErrorInGutter-checkbox-checkbox
        # return self.get_by_test_id("displayErrorInGutter-checkbox-checkbox")

        # xpath
        return self.locate_xpath('//span[label="' + log_options["displayErrorInGutter-checkbox-checkbox"] + '"]')

    def click_checkbox_display_error_in_gutter(self):
        self.checkbox_display_error_in_gutter.click()

    def click_checkbox_show_sas_code_in_log(self):
        self.checkbox_show_sas_code_in_log.click()
