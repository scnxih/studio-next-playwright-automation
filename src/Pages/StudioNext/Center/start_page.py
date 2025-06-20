"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: December 30th, 2024
"""
import time

from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Helper.helper import Helper


class StartPage(CenterPage):
    def __init__(self, page):
        CenterPage.__init__(self, page)

    # //div[contains(@class, "StartViewPane-RightView_list-full")]
    # [../../../descendant::span[text()="最近"]]
    @property
    def button_links_build_a_flow(self):
        """
        Click button-link 'Build a flow' in Start Page
        """
        # CORRECT
        return self.locate_xpath("//button[@id='flow']")

        # return self.locate_xpath("//button[@data-testid='button-links']")
        # return self.get_by_test_id('button-links')

        # JIRA Defect: SASSTUDIO-46181
        # https://rndjira.sas.com/browse/SASSTUDIO-46181
        # In Start Page, the uniqueness of @data-testid violated for button links

    @property
    def recent_files_list(self):
        """
        List of recent files, which would cause diffs in SDSTest.
        """
        return '//div[contains(@class, "StartViewPane-RightView_list-full")]' + '[../../../descendant::span[text()="' + Helper.data_locale.RECENTS + '"]]'

    @property
    def recovery_number_1(self):
        """
        The number of recoveries in status bar.
        """
        return ['//div[@id="app"]//button[@type="button"][contains(@aria-label, '
                '"' + Helper.data_locale.OPERATE_RECOVERY + '")]']

    def prt_scn(self, pic_name):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot_self in StartupInitializationLogPage")
        Helper.logger.debug("%%% Recovery number from base:" + str(self.recovery_number) + " %%%")
        # time.sleep(1)
        self.screenshot("//div[@id='app']", pic_name,
                        user_assigned_xpath=True, clip=None,
                        mask=[self.recent_files_list] + [self.locator('//div[@data-landmark-label="' + Helper.data_locale.STATUS_BAR + '"]')],
                        mask_color='#F5F4F6')

    def remove_all_recent_items(self):
        """
        RMC on list of 'Recents' and then select 'Clear all'
        """
        if self.page.is_visible(self.recent_files_list):
            Helper.logger.debug("Visible 'Recent' list")

            self.right_click(self.recent_files_list)
            # self.click_context_menu_by_right_click(self.recent_files_list, Helper.data_locale.REMOVE_ALL)

            self.wait_for_page_load()
            self.key_press("ArrowUp")

            self.wait_for_page_load()
            self.key_press("Enter")

            Helper.logger.debug("[Remova all] 'Recents' list")
        else:
            Helper.logger.debug("Unavailable 'Recent' list")

    def build_a_flow(self):
        """

        """
        self.button_links_build_a_flow.click()

