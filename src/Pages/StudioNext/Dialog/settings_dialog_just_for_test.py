import time

from src.Pages.Common.dialog import Dialog
from src.Helper.helper import Helper
from src.Pages.Common.combobox import *
from src.Pages.Common.checkbox import *
from src.Pages.Common.text import Text
from src.Pages.Common.radio_group import *
from src.Pages.Common.numeric_stepper import *


# the class is just for test some common components: combobox, radio, checkbox,text and so on.
class SettingsDialogTest(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.SETTINGS)
        self.combobox_language = Combobox(container_base_xpath=self.base_xpath, page=page,
                                          data_test_id="settings-global-regionAndLanguageForm-formatLocale",
                                          items_count=100)
        self.combobox_offline_language = Combobox(container_base_xpath=self.base_xpath, page=page,
                                                  data_test_id="settings-global-regionAndLanguageForm"
                                                               "-offlineLocale", items_count=100)

    def wait_for_open(self):
        time.sleep(1)

    def text(self, data_test_id=""):
        return Text(container_base_xpath=self.base_xpath, page=self.page, data_test_id=data_test_id)

    def combobox(self, data_test_id="", items_count=20):
        return Combobox(container_base_xpath=self.base_xpath, page=self.page, data_test_id=data_test_id, items_count=items_count)

    def checkbox(self, label):
        return Checkbox(self.base_xpath, self.page, label=label)

    def radiogroup(self, data_test_id=""):
        return RadioGroup(container_base_xpath=self.base_xpath, page=self.page, data_test_id=data_test_id)

    def numeric_stepper(self, data_test_id=""):
        return NumericStepper(self.base_xpath, self.page, data_test_id=data_test_id)

    def tab_label(self, label):
        return self.locate_xpath(f"//label[text()='{label}']")

    def click_tab(self, tab_label):
        self.click(self.tab_label(tab_label))

    def select_language(self, language):
        # self.combobox_language.select_item(language)
        # or is there are too many combobox controls in this page, you can simply do like below rather than define
        # the var combobox_language
        self.combobox(data_test_id="settings-global-regionAndLanguageForm-formatLocale",
                      items_count=100).select_item(language)

    def select_offline_language(self, language):
        # self.combobox_offline_language.select_item(language)
        # or is there are too many combobox controls in this page, you can simply do like below rather than define
        # the var combobox_offline_language
        self.combobox(data_test_id="settings-global-regionAndLanguageForm-offlineLocale",
                      items_count=100).select_item(language)

    def set_check(self, label):
        self.checkbox(label).set_check()

    def set_uncheck(self, label):
        self.checkbox(label).set_uncheck()

    def fill_text(self, text_test_id, input_text):
        self.text(text_test_id).fill_text(input_text)

    def clear_text(self, text_test_id):
        self.text(text_test_id).clear_text()

    def set_recent_items_count(self, count: str):
        self.fill_text("recentItems-input-input", count)

    def set_size_value(self, count: str):
        self.fill_text("sizeValue-input-input", count)

    def set_save_interval(self, interval: str):
        self.fill_text("saveInterval-input-input", interval)

    def set_max_log_lines(self, value: str):
        self.fill_text("maxLogLines-input-input", value)

    def set_max_size(self, value: str):
        self.fill_text("maxSize-input-input", value)
