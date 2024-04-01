from playwright.sync_api import expect
from src.Pages.Common.dialog import *
from src.Pages.Common.toolbar import *


class ManageGitConnectionDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.MANAGE_GIT_CONNECTION)
        self.toolbar = Toolbar(self.base_xpath, page, supplement_base_xpath="class='sas_components-Toolbar"
                                                                            "-__internal__-BaseToolbar_toolbar'")

    @property
    def btn_close(self):
        return self.get_by_test_id("gitDialog-mgtConnection-dismissButton")

    def profile_item(self, profile_name):
        return self.locate_xpath(
            "//div[@class='sas_components-List-Item-Item_single-line']/span[contains(text(),'" + profile_name + "')]")

    def default_icon(self, profile_name):
        return self.locate_xpath(
            "//div[@class='sas_components-List-Item-Item_single-line']/span[contains(text(),'" + profile_name +
            "')]/parent::div/preceding-sibling::span[contains(@class,'sas_components-List-Item-Item_item-icon')]")

    def go_to_add_profile_dialog(self):
        self.toolbar.click_btn_by_test_id("gitDialog-mgtConnection-profilePane-addProfileButton")

    def go_to_edit_profile_dialog(self, profile_name):
        self.click(self.profile_item(profile_name))
        self.toolbar.click_btn_by_test_id("gitDialog-mgtConnection-profilePane-editProfileButton")
        Helper.logger.debug("Go to Edit Profile dialog")

    def close_manage_git_connection_dialog(self):
        self.click(self.btn_close)

    def close_alert_dup_profile(self):
        dup_profile_alert = Alert(self.page, "SAS® Studio Next")
        if dup_profile_alert.is_open():
            # dup_profile_alert.close_alert_dialog(Helper.data_locale.CLOSE)
            dup_profile_alert.close_dialog()
            Helper.logger.debug("Duplicated profile name.")

    def delete_profile(self, profile_name):
        del_profile_alert = Alert(self.page, Helper.data_locale.DELETE)
        if self.profile_item(profile_name).is_visible():
            self.click(self.profile_item(profile_name))
            self.toolbar.click_btn_by_test_id("gitDialog-mgtConnection-profilePane-deleteProfileButton")
            if del_profile_alert.is_open():
                # del_profile_alert.close_alert_dialog(Helper.data_locale.DELETE)
                del_profile_alert.close_dialog()
                expect(self.profile_item(profile_name)).not_to_be_visible()
                Helper.logger.debug("Profile is deleted.")
        else:
            Helper.logger.debug("The Profile you want to delete does not exist.")

    def set_profile_as_default(self, profile_name):
        del_profile_alert = Alert(self.page, Helper.data_locale.DELETE)
        if self.profile_item(profile_name).is_visible():
            self.click(self.profile_item(profile_name))
            self.toolbar.click_btn_by_test_id("gitDialog-mgtConnection-profilePane-setDefaultProfileButton")
            expect(self.default_icon(profile_name)).to_be_visible()
            Helper.logger.debug("Profile is set as default.")
        else:
            Helper.logger.debug("Profile does not exist.")

    def wait_for_open(self):
        time.sleep(2)

    @property
    def tab_profile(self):
        return self.locate_xpath("//div[@data-testid='gitDialog-mgtConnection-navPane-profileTab']")
    @property
    def tab_repository(self):
        return self.locate_xpath("//div[@data-testid='gitDialog-mgtConnection-navPane-repositoryTab']")

    def click_tab_profile(self):
        self.click(self.tab_profile)

    def click_tab_repository(self):
        self.click(self.tab_repository)