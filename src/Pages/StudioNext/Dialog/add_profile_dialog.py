from src.Pages.Common.dialog import *
from playwright.sync_api import Page, expect
from src.Pages.Common.text import *
from src.Utilities.enums import *


class AddProfileDialog(Dialog):
    def __init__(self, page, title=Helper.data_locale.ADD_A_PROFILE):
        Dialog.__init__(self, page, title=title)

    @property
    def btn_browse_public(self):
        return self.locate_xpath('//div[@data-testid="gitProfileDialog-publicSSH-input"]/following-sibling::button')

    @property
    def btn_browse_private(self):
        return self.locate_xpath('//div[@data-testid="gitProfileDialog-privateSSH-input"]/following-sibling::button')

    def text(self, data_test_id=""):
        return Text(container_base_xpath=self.base_xpath, page=self.page, data_test_id=data_test_id)

    def fill_text(self, text_test_id, input_text):
        self.text(text_test_id).fill_text(input_text)

    def clear_text(self, text_test_id):
        self.text(text_test_id).clear_text()

    def input_profile_name(self, value: str):
        self.fill_text("gitProfileDialog-profileName-input", value)

    def clear_profile_name(self):
        self.clear_text("gitProfileDialog-profileName-input")

    def input_user_name(self, value: str):
        self.fill_text("gitProfileDialog-userName-input", value)

    def clear_user_name(self):
        self.clear_text("gitProfileDialog-userName-input")

    def input_email(self, value: str):
        self.fill_text("gitProfileDialog-email-input", value)

    def clear_email(self):
        self.clear_text("gitProfileDialog-email-input")

    def input_public_ssh(self, value: str):
        self.fill_text("gitProfileDialog-publicSSH-input-input", value)

    def clear_public_ssh(self):
        self.clear_text("gitProfileDialog-publicSSH-input-input")

    def input_private_ssh(self, value: str):
        self.fill_text("gitProfileDialog-privateSSH-input-input", value)

    def clear_private_ssh(self):
        self.clear_text("gitProfileDialog-privateSSH-input-input")

    def select_public_ssh(self):
        self.click(self.btn_browse_public)

    def select_private_ssh(self):
        self.click(self.btn_browse_private)

    def add_profile_input_ssh(self, profile_name, username, email, public_ssh, private_ssh):
        if self.title == Helper.data_locale.ADD_A_PROFILE:
            self.input_profile_name(profile_name)
            self.input_user_name(username)
            self.input_email(email)
            self.input_public_ssh(public_ssh)
            self.input_private_ssh(private_ssh)
            self.click(self.btn_in_dialog_footer(Helper.data_locale.OK))

    def add_profile_input_ssh_part(self, profile_name, username, email):
        if self.title == Helper.data_locale.ADD_A_PROFILE:
            self.input_profile_name(profile_name)
            self.input_user_name(username)
            self.input_email(email)
            self.click(self.btn_in_dialog_footer(Helper.data_locale.OK))

    def edit_profile_input_ssh(self, **profile_field):
        if self.title == Helper.data_locale.EDIT_PROFILE:
            for key, value in profile_field.items():
                match key:
                    case "profile_name":
                        self.clear_profile_name()
                        self.input_profile_name(value)
                        Helper.logger.debug("Edit profile name")
                    case "user_name":
                        self.clear_user_name()
                        self.input_user_name(value)
                        Helper.logger.debug("Edit user name")
                    case "email":
                        self.clear_email()
                        self.input_email(value)
                        Helper.logger.debug("Edit email")
                    case "public_ssh":
                        self.clear_public_ssh()
                        self.input_public_ssh(value)
                        Helper.logger.debug("Edit publish ssh key")
                    case "private_ssh":
                        self.clear_private_ssh()
                        self.input_private_ssh(value)
                        Helper.logger.debug("Edit private ssh key")
            self.click(self.btn_in_dialog_footer(Helper.data_locale.OK))
