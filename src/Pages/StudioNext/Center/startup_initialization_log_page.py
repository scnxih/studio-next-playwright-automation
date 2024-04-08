"""
Author: Alice
Date: November 06, 2023
Description: StartupInitializationLogPage will inherit from CenterPage class。

"""
from src.Helper.helper import Helper
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.center_page import CenterPage


class StartupInitializationLogPage(CenterPage):

    def __init__(self, page):
        CenterPage.__init__(self, page)

    def saveas(self, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        self.center_toolbar_helper.saveas(folder_path,file_name,if_replace,if_wait_toast_disappear)

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()

    def add_to_my_favorites(self):
        self.center_toolbar_helper.add_to_my_favorites()

    def open_in_browser_tab(self):
        if not self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB):
            return

        self.page.bring_to_front()

    # MODIFIED
    # ADDED
    # <<< Modified by Jacky(ID: jawang) on Mar.28th, 2024
    def open_in_browser_tab2(self, page):
        """
        Added screenshot function for the whole web page
        """
        if not self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB):
            return

        self.page.bring_to_front()
        WholePage(page).screenshot_self("open_in_browser_tab_page")

    # Modified by Jacky(ID: jawang) on Mar.28th, 2024 >>>

    def email(self):
        self.center_toolbar_helper.email()

    def reload(self):
        self.center_toolbar_helper.reload()



