"""
Author: Alice
Date: October 25, 2023
Description: Json/Text/XML/Workspace will inherit this TextCenterPage class since they have
             similar toolbar methods.
"""
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Helper.helper import Helper


class TextCenterPage(CenterPage):
    def __init__(self, page):
        CenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        self.center_toolbar_helper.save(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def saveas(self, folder_path: list, file_name, if_replace, if_wait_toast_disappear):
        self.center_toolbar_helper.saveas(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def add_to_my_favorites(self):
        self.center_toolbar_helper.add_to_my_favorites()

    def open_in_browser_tab(self):
        if not self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB):
            return

        self.page.bring_to_front()


    # def print_summary(self):
    #     self.center_toolbar_helper.print_summary()
    def email(self):
        self.center_toolbar_helper.email()

    def reload(self):
        # self.center_toolbar_helper.reload()
        pass
    def undo(self):
        self.center_toolbar_helper.undo()

    def redo(self):
        self.center_toolbar_helper.redo()

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()
