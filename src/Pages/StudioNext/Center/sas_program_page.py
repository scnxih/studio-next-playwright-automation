"""
Author: Alice
Date: October 24, 2023
Description: SASProgramPage will inherit from MainCenterPage class, thus the methods in MainCenterPage will be inherited automatically.
            You can also override these parent class methods in this SASProgramPage class if needed.

"""
from src.Helper.helper import Helper
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage

# ADDED
# <<< Added by Jacky(ID: jawang) on Jan.12th, 2024
from src.Pages.Common.widget import Widget
# Added by Jacky(ID: jawang) on Jan.12th, 2024 >>>

class SASProgramPage(MainCenterPage):
    def __init__(self, page):
        MainCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)

        # ADDED
        # <<< Added by Jacky(ID: jawang) on Jan.12th, 2024
        self.widget = Widget(self.base_xpath, page)
        # Added by Jacky(ID: jawang) on Jan.12th, 2024 >>>

    def undo(self):
        self.center_toolbar_helper.undo()

    def redo(self):
        self.center_toolbar_helper.redo()

    def clear_code(self):
        self.center_toolbar_helper.clear_code()

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

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()

    def format_program(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.FORMAT_PROGRAM)

        # Works fine but __screenshot is the area contains tab group on the RHS
        # self.screenshot(self.base_xpath, "formatted")

        # Works fine
        # Note: In addition to xpath, such as base_xpath, locator can be passes as the parameter.
        self.screenshot("//div[contains(@data-testid, 'container')][contains(@class, 'EditorPane')]", "formatted")


    """After the funtion is implemented in Studionext now, below method should be changed accordingly """
    def debug(self):
        # self.toolbar.click_btn_by_test_id("view-toolbar-debug")
        return


    def analyze_and_create_flow(self):
        self.center_toolbar_helper.analyze_and_create_flow()
