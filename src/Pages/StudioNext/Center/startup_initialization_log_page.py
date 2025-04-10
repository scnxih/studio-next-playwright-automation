"""
Author: Alice
Date: November 06, 2023
Description: StartupInitializationLogPage will inherit from CenterPage class。

"""
import time

from src.Helper.helper import Helper
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.center_page import CenterPage


class StartupInitializationLogPage(CenterPage):

    def __init__(self, page):
        CenterPage.__init__(self, page)

    @property
    def time_info_in_log(self):
        """
        Time information in start-up initialization log file
        Since this keeps changing, masking is an absolute necessity.
        """

        return ['//span[contains(text(),"CPU")]/..',
                '//span[contains(text(),"实际")]/..']

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot_self in StartupInitializationLogPage")

        self.screenshot("//div[@id='app']", pic_name, user_assigned_xpath=True, clip=clip,
                        mask=self.time_info_in_log + [
                            self.locator(
                                "//button[@type='button'][.//span[contains(text(), '" + Helper.data_locale.OPERATE_RECOVERY + "')]]"),
                        ],
                        mask_color='#F9FAFB')

    def saveas(self, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        self.center_toolbar_helper.saveas(folder_path, file_name, if_replace, if_wait_toast_disappear)

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()

    def add_to_my_favorites(self):
        self.center_toolbar_helper.add_to_my_favorites()

    def open_in_browser_tab(self):
        if not self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB):
            return
        time.sleep(2)
        self.page.bring_to_front()
        time.sleep(1)

    # MODIFIED
    # ADDED
    # <<< Modified by Jacky(ID: jawang) on Mar.28th, 2024
    def open_in_browser_tab2(self, page):
        """
        Added screenshot function for the whole web page
        """
        if not self.toolbar.click_menu_in_more_options(Helper.data_locale.OPEN_IN_BROWSER_TAB):
            return
        time.sleep(2)

        # does NOT work
        # WholePage(self.page).screenshot_self("browser_tab_page")

        self.page.bring_to_front()

        # Original
        # WholePage(page).screenshot_self("open_in_browser_tab_page")

        # Added
        self.toolbar.click_dialog_title_or_studionext_header()

        # Added waiting time to avoid diffs caused by scrollbar
        time.sleep(2)

        # Mask CPU Time & Real Time
        WholePage(page).screenshot_self("open_in_browser_tab_page",
                                        mask=['//span[@class="mtk1"][contains(text(),"CPU")]/..',
                                              "//button[@type='button'][.//span[contains(text(), '" + Helper.data_locale.OPERATE_RECOVERY + "')]]",
                                              '//span[@class="mtk1"][contains(text(),"实际")]/..'],
                                        mask_color="#000000")

        time.sleep(1)

    # Modified by Jacky(ID: jawang) on Mar.28th, 2024 >>>

    def email(self):
        self.center_toolbar_helper.email()

    def reload(self):
        self.center_toolbar_helper.reload()
