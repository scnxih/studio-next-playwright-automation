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
    def tab_submissions(self):
        """
        Tab page 'Submissions'
        """
        return self.locator("//div[@aria-label='{0}']".format(Helper.data_locale.SUBMIT))

    @property
    def tab_monitoring_jobs(self):
        """

        """
        return self.locator("//div[@aria-label='{0}']".format(Helper.data_locale.MONITORING_JOBS))

    @property
    def tab_deployed_jobs(self):
        """

        """
        return self.locator("//div[@aria-label='{0}']".format(Helper.data_locale.DEPLOYED_JOBS))

    @property
    def tab_scheduled_jobs(self):
        """

        """
        return self.locator("//div[@aria-label='{0}']".format(Helper.data_locale.SCHEDULED_JOBS))

    @property
    def mask_last_refresh_label(self):
        """
        In upper right corner of 'Deployed and Scheduled Jobs' page: Last Refresh (Time) Label
        # data-testid="scheduledJobsPane-monitoringTab-lastRefreshLabel"
        """
        return [self.page.get_by_test_id("scheduledJobsPane-monitoringTab-lastRefreshLabel")]

    @property
    def mask_last_refresh_label_time(self):
        """
        In upper right corner of 'Deployed and Scheduled Jobs' page: Last Refresh (Time) Label
        # data-testid="scheduledJobsPane-monitoringTab-lastRefreshLabel"
        """
        return [self.page.locator("//div[contains(@data-testid, 'lastRefreshLabel')]")]

    @property
    def mask_deployed_and_scheduled_jobs_treegrid(self):
        """
        Container listing all jobs
        xpath: //div[@role='treegrid'][not (contains(@class, 'vertical'))]
        """
        # Changed on May 19, 2025
        # return [self.page.locator("//div[@role='treegrid'][not (contains(@class, 'vertical'))]")]

        # NOT perfect
        # return [self.page.locator("//div[contains(@class, 'ag-center-cols-viewport')][(contains(@style, '29'))]")]

        # return [self.page.locator("//div[contains(@class, 'ag-center-cols-viewport')][not (contains(@style, '1008'))]")]

        return self.page.locator("//div[contains(@class, 'ag-center-cols-viewport')][not (contains(@style, '1008'))]")

    @property
    def btn_clear_completed_submissions(self):
        """

        """
        return self.get_by_test_id("submissionStatusPane-toolBarClearAllButton")

    def clear_all_completed_submissions(self):
        """
        First, switch to 'Submissions' tab page.
        Next, check the button status.
        Finally, click the 'Clear completed submissions' button if it has been enabled.
        """

        self.tab_submissions.click()
        self.wait_for_page_load()

        if self.is_enabled(self.btn_clear_completed_submissions):
            Helper.logger.debug("Enabled button [Clear completed submissions]")

            self.btn_clear_completed_submissions.clear()
            self.wait_for_page_load()
            Helper.logger.debug("Clicked button [Clear completed submissions]")

        Helper.logger.debug("Exiting [Clear completed submissions]")

    def delete_all_submitted_jobs(self):
        """
        INCOMPLETE
        """
        self.tab_monitoring_jobs.click()
        self.wait_for_page_load()
        self.click_context_menu_by_right_click(Helper.data_locale.DELETE_SUBMITTED_JOB)
        self.wait_for_page_load()


    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot_self in CodeEditorPage")

        self.click_dialog_title_or_studionext_header()

        self.screenshot("//div[@id='app']", pic_name, user_assigned_xpath=True, clip=clip,
                        mask=[self.locator(
                            '//div[@data-landmark-label="' + Helper.data_locale.STATUS_BAR + '"]')] +
                             self.mask_last_refresh_label_time,  # self.mask_deployed_and_scheduled_jobs_treegrid,
                        mask_color='#F5F4F6')

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
