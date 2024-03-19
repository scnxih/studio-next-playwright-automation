"""
Author: Alice
Date: October 25, 2023
Description: WorkspacePage will inherit from TextCenterPage class, thus the methods in TextCenterPage will be inherited automatically.
            You can also override these methods in this WorkspacePage class if needed.

"""
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.text_center_page import TextCenterPage


class WorkspacePage(TextCenterPage):
    def __init__(self, page):
        TextCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)
