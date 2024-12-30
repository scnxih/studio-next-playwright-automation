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
    def recent_files_list(self):
        """
        List of recent files, which would cause diffs in SDSTest.
        """
        return ['//div[contains(@class, "StartViewPane-RightView_list-full")]'
                '[../../../descendant::span[text()="' + Helper.data_locale.RECENT + '"]]']

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
        time.sleep(1)
        self.screenshot("//div[@id='app']", pic_name,
                        user_assigned_xpath=True, clip=None,
                        mask=self.recent_files_list + self.recovery_number,
                        mask_color='#000000')
