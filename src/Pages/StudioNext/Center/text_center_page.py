"""
Author: Alice
Date: October 25, 2023
Description: Json/Text/XML/Workspace will inherit this TextCenterPage class since they have
             similar toolbar methods.
"""
import time

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

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr. 9th, 2024
        self.toolbar.click_dialog_title_or_studionext_header()

        # END Added by Jacky(ID: jawang) on Apr. 9th, 2024 >>>

        self.page.bring_to_front()

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Apr. 9th, 2024
    def open_in_browser_tab2(self):
        """
        Open in a browser tab AND FOCUS on main page
        """
        if not self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB):
            return
        with self.toolbar.page.expect_popup() as browser_tab_page_info:
            self.toolbar.click_dialog_title_or_studionext_header()
        page2 = browser_tab_page_info.value
        time.sleep(1)
        self.page.bring_to_front()
        return page2

    # END Added by Jacky(ID: jawang) on Apr. 9th, 2024 >>>

    # def print_summary(self):
    #     self.center_toolbar_helper.print_summary()
    def email(self):
        self.center_toolbar_helper.email()

    def reload(self):
        # self.center_toolbar_helper.reload()
        pass

    def undo(self):
        self.center_toolbar_helper.undo()

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr. 9th, 2024
        # Wait for half second to avoid trouble caused by performance
        time.sleep(0.5)

        # self.screenshot_self('undo')
        # END Added by Jacky(ID: jawang) on Apr. 9th, 2024 >>>

        # data-testid="textViewPane-editorPane-editor"
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'undo',
                        user_assigned_xpath=True)

    def redo(self):
        self.center_toolbar_helper.redo()

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr. 9th, 2024
        # Wait for half second to avoid trouble caused by performance
        time.sleep(0.5)

        # self.screenshot_self('redo')
        # END Added by Jacky(ID: jawang) on Apr. 9th, 2024 >>>

        # data-testid="textViewPane-editorPane-editor"
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'redo',
                        user_assigned_xpath=True)

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()
