"""
Author: Alice
Date: November 02, 2023
Description: DeployedScheduledJobPage will inherit from CenterPage class。

"""
import time

from src.Pages.StudioNext.Center.center_page import *


class DeployedScheduledJobPage(CenterPage):

    def __init__(self, page):
        CenterPage.__init__(self, page)

    @property
    def mask_last_refresh_label(self):
        """
        In upper right corner of 'Deployed and Scheduled Jobs' page: Last Refresh (Time) Label
        # data-testid="scheduledJobsPane-monitoringTab-lastRefreshLabel"
        """
        return [self.page.get_by_test_id("scheduledJobsPane-monitoringTab-lastRefreshLabel")]

    @property
    def mask_deployed_and_scheduled_jobs_treegrid(self):
        """
        Container listing all jobs
        xpath: //div[@role='treegrid'][not (contains(@class, 'vertical'))]
        """
        return [self.page.locator("//div[@role='treegrid'][not (contains(@class, 'vertical'))]")]

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot_self in CodeEditorPage")

        self.screenshot("//div[@id='app']", pic_name, user_assigned_xpath=True, clip=clip,
                        mask=self.recovery_number +
                             self.mask_last_refresh_label +
                             self.mask_deployed_and_scheduled_jobs_treegrid,
                        mask_color='#F9FAFB')

    def run_now(self):
        self.toolbar.click_btn_by_test_id("scheduledJobsPane-runNowButton")
        time.sleep(3)
        self.screenshot(self.base_xpath, "run_schedule")

    def edit_schedule(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.EDIT_SCHEDULE)
        time.sleep(1)
        self.screenshot(self.base_xpath, "edit_schedule")

    def remove_schedule(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.REMOVE_SCHEDULE)
        time.sleep(1)
        self.screenshot(self.base_xpath, "remove_schedule")

    def refresh_list(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.REFRESH_LIST)
        time.sleep(1)
        self.screenshot(self.base_xpath, "refresh_schedule")

    """This method has not been implemented yet, need to rewrite in future"""

    def column_setting(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.COLUMN_SETTINGS)
        time.sleep(1)
        Dialog(self.page, Helper.data_locale.COLUMN_SETTINGS).click_button_in_footer(Helper.data_locale.CANCEL)
