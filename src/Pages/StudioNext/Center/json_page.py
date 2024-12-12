"""
Author: Alice
Date: October 25, 2023
Description: JsonPage will inherit from TextCenterPage class, thus the methods in TextCenterPage will be inherited automatically.
            You can also override these methods in this JsonPage class if needed.

"""
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.text_center_page import TextCenterPage
import time


class JsonPage(TextCenterPage):
    def __init__(self, page):
        TextCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)

    def undo(self):
        self.center_toolbar_helper.undo()
        time.sleep(3.0)
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'json_undo',
                        user_assigned_xpath=True)

    def redo(self):
        self.center_toolbar_helper.redo()
        time.sleep(3.0)
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'json_redo',
                        user_assigned_xpath=True)
