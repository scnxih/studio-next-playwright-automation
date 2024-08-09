import time

from src.Helper.helper import Helper
from src.Pages.Common.base_page import BasePage


class Dialog(BasePage):
    # Although title is not required, it is suggested to specify the title to better understand the code when create
    # dialog.
    def __init__(self, page, title=''):
        BasePage.__init__(self, page)

        self.base_xpath = "//div[@role='dialog']"
        if self.current_frame == "":
            self.set_iframe("//iframe")
        if title != '':
            self.title = title
            self.base_xpath += f"[.//span[text()='{title}']]"
        else:
            self.title = ""
    @property
    def span_header(self):
        return self.locate_xpath("//span[text()='" + self.title + "']")

    @property
    def btn_close(self):
        return self.locate_xpath("//button[contains(@class, 'close')]")

    def _footer_button(self, button_text):
        str = ""
        if Helper.if_contain_quotation(button_text):
            str = "//div[contains(@class,'footer')]//*[contains(text()," + Helper.escape_quotation_for_xpath(
                button_text) + ")]"
        else:
            str = "//div[contains(@class,'footer')]//*[contains(text(),'" + button_text + "')]"
        return self.locate_xpath(str)

    def btn_in_dialog_footer(self, button_label):
        return self._footer_button(button_label)

    def is_open(self):
        self.wait_for_open()
        if self.title != "":
            if self.is_visible(self.span_header):
                return True
            return False
        return True

    def close_dialog(self):
        self.click(self.btn_close)
        time.sleep(0.5)

    def click_button_in_footer(self, button_text):
        self.click(self.btn_in_dialog_footer(button_text))

    def verify_dialog(self, title):
        try:
            self.span_header.click()
        except Exception as e:
            Helper.logger.warning("verify dialog with title", title, e)

    def wait_for_open(self):
        pass

    def click_ok_button(self):
        self.click_button_in_footer(Helper.data_locale.OK)

    def click_cancel_button(self):
        self.click_button_in_footer(Helper.data_locale.CANCEL)
class Alert(Dialog):

    def __init__(self, page, title=''):
        Dialog.__init__(self, page, title)
        self.base_xpath = "//div[@role='alertdialog']"
        # if a specific title is passed, include it in the base locator
        if title != '':
            self.title = title
            self.base_xpath += f"[.//span[text()='" + title + "']]"

    @property
    def only_btn(self):
        return self.locate_xpath("//button")

    def close_dialog_by_text(self, button_text):
        """Call this method to close the Alert dialog when there is more than more buttons in this Alert dialog"""
        self.click(self.btn_in_dialog_footer(button_text))
        time.sleep(1)

    def close_dialog(self):
        """Call this method to close the Alert dialog when there is only button in this Alert dialog."""
        self.click(self.only_btn)
        time.sleep(1)
