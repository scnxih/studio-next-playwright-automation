"""
Author: Alice
Date: October 23, 2023
Description: PythonProgramPage will inherit from MainCenterPage class, thus the methods in MainCenterPage will be inherited automatically.
            You can also override these methods in this PythonProgramPage class if needed.

"""
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage


class PythonProgramPage(MainCenterPage):
    def __init__(self, page):
        MainCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)

    def undo(self):
        self.center_toolbar_helper.undo()

        # //div[@data-testid="programView-editorPane-editor"]
        self.screenshot('//div[@data-testid="programView-editorPane-editor""]',
                        'python_undo',
                        user_assigned_xpath=True)

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

    def copy_to_flow(self):
        """
        Thursday, Feb 6, 2025
        Product change: 'Copy to flow' used to replace 'Code to flow' button located in sas program toolbar.
        """
        self.center_toolbar_helper.copy_to_flow()

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()
