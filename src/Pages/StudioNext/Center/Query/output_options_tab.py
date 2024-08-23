"""
@author: Frank (Feng) Jiang
@date: created on 2023/10/10
@description: define Query page -> Output Options tab, include elements and functionalities in this tab
"""

from src.Pages.StudioNext.Center.Query.query_page import *
from src.Pages.Common.radio_group import *
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.text import *
from src.Pages.StudioNext.Dialog.query_output_lib_dialog import *
from src.Pages.Common.checkbox import *
from src.Pages.Common.numeric_stepper import *
from src.Pages.Common.textarea import *


class OutputOptions(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = ("//div[@data-testid='tab-group-content-area']"
                           "[@class='sas_components-layouts-TabManager-TabGroup-TabContentContainer_tab-content"
                           "-wrapper']")
        self.radio = RadioGroup(self.base_xpath, page, data_test_id=TestID.QUERY_OUTPUT_OPTIONS_RADIO)
        self.alertdialog = Alert(page, "SAS Studio Next")
        self.combo_output_type = Combobox(self.base_xpath, page, data_test_id=TestID.QUERY_OUTPUT_OPTIONS_COMBO)
        self.input_output_lib = Text(self.base_xpath, page, data_test_id=TestID.QUERY_OUTPUT_OPTIONS_TEXT_OUTPUT_LIB)
        self.input_output_table = Text(self.base_xpath, page,
                                       data_test_id=TestID.QUERY_OUTPUT_OPTIONS_TEXT_OUTPUT_TABLE)
        self.output_lib_dialog = OutputLibDialog(page)
        self.checkbox_inobs = Checkbox(self.base_xpath, page, data_test_id=TestID.QUERY_OUTPUT_OPTIONS_CHECKBOX_INOBS)
        self.checkbox_outobs = Checkbox(self.base_xpath, page, data_test_id=TestID.QUERY_OUTPUT_OPTIONS_CHECKBOX_OUTOBS)
        self.numstepper_inobs = NumericStepper(self.base_xpath, page,
                                               data_test_id=TestID.QUERY_OUTPUT_OPTIONS_NUMSTEPPER_INOBS)
        self.numstepper_outobs = NumericStepper(self.base_xpath, page,
                                                data_test_id=TestID.QUERY_OUTPUT_OPTIONS_NUMSTEPPER_OUTOBS)
        self.checkbox_explipassthru = Checkbox(self.base_xpath, page,
                                               data_test_id=TestID.QUERY_OUTPUT_OPTIONS_CHECKBOX_EXPLPASSTHRU)
        self.textarea = Textarea(self.base_xpath, page, data_test_id=TestID.QUERY_OUTPUT_OPTIONS_TEXTAREA)

    @property
    def section_output_options(self):
        return self.locate_xpath("//div[@role='button'][.//span[contains(text(), '"
                                 + Helper.data_locale.QUERY_OUTPUT_OPTIONS_SECTION_OUTPUT + "')]]")

    def expand_section_output_options(self):
        if self.get_attribute(self.section_output_options, "aria-expanded").lower() != "true":
            self.click(self.section_output_options)

    def collapse_section_output_options(self):
        if self.get_attribute(self.section_output_options, "aria-expanded").lower() == "true":
            self.click(self.section_output_options)

    @property
    def section_passthrough(self):
        return self.locate_xpath("//div[@role='button'][.//span[contains(text(), '"
                                 + Helper.data_locale.QUERY_OUTPUT_OPTIONS_SECTION_PASSTHROUGH + "')]]")

    def expand_section_passthrough(self):
        if self.get_attribute(self.section_passthrough, "aria-expanded").lower() != "true":
            self.click(self.section_passthrough)

    def collapse_section_passthrough(self):
        if self.get_attribute(self.section_passthrough, "aria-expanded").lower() == "true":
            self.click(self.section_passthrough)

    def select_radio_sql(self):
        if not self.radio.is_checked("PROC SQL"):
            self.radio.set_check("PROC SQL")
            self.alertdialog.click_button_in_footer(Helper.data_locale.CONTINUE)

    def select_radio_fedsql(self):
        if not self.radio.is_checked("PROC FEDSQL"):
            self.radio.set_check("PROC FEDSQL")
            self.alertdialog.click_button_in_footer(Helper.data_locale.CONTINUE)

    def select_item_in_combo_output_type(self, item_label: str):
        self.combo_output_type.choose_item(item_label)

    def input_library(self, lib_name: str):
        if self.input_output_lib.get_attr("aira-disabled") == "true":
            self.select_item_in_combo_output_type(Helper.data_locale.TABLE)
        self.scroll_if_needed(self.input_output_lib.base_locator)
        self.input_output_lib.fill_text(lib_name)

    def clear_library(self):
        if self.input_output_lib.get_attr("aira-disabled") == "true":
            self.select_item_in_combo_output_type(Helper.data_locale.TABLE)
        self.scroll_if_needed(self.input_output_lib.base_locator)
        self.input_output_lib.clear_text()

    def input_table(self, table_name: str):
        if self.input_output_table.get_attr("aira-disabled") == "true":
            self.select_item_in_combo_output_type(Helper.data_locale.TABLE)
        self.scroll_if_needed(self.input_output_table.base_locator)
        self.input_output_table.fill_text(table_name)

    def clear_table(self):
        if self.input_output_table.get_attr("aira-disabled") == "true":
            self.select_item_in_combo_output_type(Helper.data_locale.TABLE)
        self.scroll_if_needed(self.input_output_table.base_locator)
        self.input_output_table.clear_text()

    @property
    def btn_browse(self):
        return self.get_by_test_id(TestID.QUERY_OUTPUT_OPTIONS_BTN_BROWSE)

    def set_output_table_by_btn_browse(self, lib_name: str, table_name: str):
        if self.input_output_lib.get_attr("aira-disabled") == "true":
            self.select_item_in_combo_output_type(Helper.data_locale.TABLE)
        self.scroll_if_needed(self.btn_browse)
        self.click(self.btn_browse)
        self.output_lib_dialog.fill_input_lib_name(lib_name)
        self.output_lib_dialog.fill_input_table_name(table_name)
        self.output_lib_dialog.click_button_in_footer("选择")

    def check_checkbox_inobs(self):
        self.scroll_if_needed(self.checkbox_inobs.base_locator)
        self.checkbox_inobs.set_check()

    def uncheck_checkbox_inobs(self):
        self.scroll_if_needed(self.checkbox_inobs.base_locator)
        self.checkbox_inobs.set_uncheck()

    def input_numstepper_inobs(self, value: int):
        self.check_checkbox_inobs()
        self.numstepper_inobs.set_value(value)

    def clear_numstepper_inobs(self):
        self.check_checkbox_inobs()
        self.numstepper_inobs.clear_value()

    def increase_numstepper_inobs(self, times=None):
        """
        Description: click increment button to increase value of number stepper.
        :param times: int value, great than 0, optional. If not set this param, click increment button once.
        """
        self.check_checkbox_inobs()
        self.numstepper_inobs.click_increment_value(times=times)

    def decrease_numstepper_inobs(self, times=None):
        """
        Description: click decrement button to decrease value of number stepper.
        :param times: int value, great than 0, optional. If not set this param, click decrement button once.
        """
        self.check_checkbox_inobs()
        self.numstepper_inobs.click_decrement_value(times=times)

    def check_checkbox_outobs(self):
        self.scroll_if_needed(self.checkbox_outobs.base_locator)
        self.checkbox_outobs.set_check()

    def uncheck_checkbox_outobs(self):
        self.scroll_if_needed(self.checkbox_outobs.base_locator)
        self.checkbox_outobs.set_uncheck()

    def input_numstepper_outobs(self, value: int):
        self.check_checkbox_outobs()
        self.numstepper_outobs.set_value(value)

    def clear_numstepper_outobs(self):
        self.check_checkbox_outobs()
        self.numstepper_outobs.clear_value()

    def increase_numstepper_outobs(self, times=None):
        """
        Description: click increment button to increase value of number stepper.
        :param times: int value, great than 0, optional. If not set this param, click increment button once.
        """
        self.check_checkbox_outobs()
        self.numstepper_outobs.click_increment_value(times=times)

    def decrease_numstepper_outobs(self, times=None):
        """
        Description: click decrement button to decrease value of number stepper.
        :param times: int value, great than 0, optional. If not set this param, click decrement button once.
        """
        self.check_checkbox_outobs()
        self.numstepper_outobs.click_decrement_value(times=times)

    def check_checkbox_explipassthru(self):
        self.checkbox_explipassthru.set_check()

    def uncheck_checkbox_explipassthru(self):
        self.checkbox_explipassthru.set_uncheck()

    def fill_textarea(self, text: str):
        self.scroll_if_needed(self.textarea.base_locator)
        self.textarea.fill_text(text)

    def clear_textarea(self):
        self.scroll_if_needed(self.textarea.base_locator)
        self.textarea.clear_text()

    def get_text_textarea(self):
        self.scroll_if_needed(self.textarea.base_locator)
        self.textarea.get_value()
