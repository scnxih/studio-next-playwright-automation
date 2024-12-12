"""
Author: Alice
Date: October 25, 2023
Description: XMLPage will inherit from TextCenterPage class, thus the methods in TextCenterPage will be inherited automatically.
            You can also override these methods in this XMLPage class if needed.

"""
import time

from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.text_center_page import TextCenterPage


class XMLPage(TextCenterPage):
    def __init__(self, page):
        TextCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)

    def undo(self):
        self.center_toolbar_helper.undo()
        time.sleep(0.5)
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'xml_undo',
                        user_assigned_xpath=True)

    def redo(self):
        self.center_toolbar_helper.redo()
        time.sleep(0.5)
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'xml_redo',
                        user_assigned_xpath=True)
