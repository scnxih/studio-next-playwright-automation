"""
Author: Alice
Date: October 24, 2023
Description: SASProgramPage will inherit from MainCenterPage class, thus the methods in MainCenterPage will be inherited automatically.
            You can also override these parent class methods in this SASProgramPage class if needed.

"""
from src.Helper.helper import Helper
from src.Pages.Common.dialog import Alert
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage
from src.Pages.Common.widget import Widget


class SASProgramPage(MainCenterPage):
    def __init__(self, page):
        MainCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)
        self.widget = Widget(self.base_xpath, page)

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot_self in SASProgramPage")

        self.click_dialog_title_or_studionext_header()

        self.wait_for_page_load()

        self.screenshot("//div[@id='app']",
                        pic_name,
                        user_assigned_xpath=True,
                        mask=self.utf8_encoding + self.recovery_number + self.success_status + self.submit_number + [
                            self.locator('//div[@data-testid="appMessageToast"]//span[@role="img"]'),
                            '//button[@data-testid="programViewPane-toolbar-runButton"]'] +
                             self.ln_col_number,  # mask[] of 'line & col number' in status bar
                        mask_color='#F4F4F6')

    def undo(self):
        self.center_toolbar_helper.undo()

        # //div[@data-testid="programView-editorPane-editor"]
        self.screenshot('//div[@data-testid="programView-editorPane-editor"]',
                        'sas_program_undo',
                        user_assigned_xpath=True)

    def redo(self):
        self.center_toolbar_helper.redo()

    def clear_code(self):
        self.center_toolbar_helper.clear_code()

        clear_code_alert = Alert(self.page, "Clear Code")

        if clear_code_alert.is_open():
            clear_code_alert.click_button_in_footer("Clear")

    def clear_all(self):
        self.center_toolbar_helper.clear_all()

    def clear_log(self):
        self.center_toolbar_helper.clear_log()

    def clear_results(self):
        self.center_toolbar_helper.clear_results()

    def clear_output_data(self):
        self.center_toolbar_helper.clear_output_data()

    def clear_listing(self):
        self.center_toolbar_helper.clear_listing()

    def code_to_flow(self):
        self.center_toolbar_helper.code_to_flow()

    def copy_to_flow(self):
        """
        Thursday, Feb 6, 2025
        Product change: 'Copy to flow' used to replace 'Code to flow' button located in sas program toolbar.
        """
        self.center_toolbar_helper.copy_to_flow()

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()

    def format_program(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.FORMAT_PROGRAM)

        self.click_dialog_title_or_studionext_header()
        # Works fine
        # Note: In addition to xpath, such as base_xpath, locator can be passes as the parameter.
        self.screenshot("//div[contains(@data-testid, 'container')][contains(@class, 'EditorPane')]", "formatted")

    """After the funtion is implemented in Studionext now, below method should be changed accordingly """

    def debug(self):
        # self.toolbar.click_btn_by_test_id("view-toolbar-debug")
        return

    def analyze_and_create_flow(self):
        self.center_toolbar_helper.analyze_and_create_flow()
