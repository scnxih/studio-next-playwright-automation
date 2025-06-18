from src.Helper.helper import Helper
from src.Pages.Common.base_page import *
from src.Utilities.vars import *


class LoginPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)

    @property
    def user_name(self):
        return self.locate_xpath("//input[@id='username']")

    @property
    def user_password(self):
        return self.locate_xpath("//input[@id='password']")

    @property
    def btn_submit(self):
        return self.locate_xpath("//button[@id='submitBtn']")

    @property
    def btn_compute_context(self):
        return self.locate_xpath(
            '//button[@aria-disabled="false"][@data-testid="appHeaderToolbar-studioActiveServerButton"]')

    @property
    def alert_message(self):
        """
        Alert message 'Please enter a user ID and password.'
        """
        return self.locate_xpath("//div[@role='alert'][@id='message']")

    def _login(self):
        # Original
        url = "https://3xdaily.pgc.unx.sas.com/SASStudio/"

        # Backup server
        # url = "https://daily.pgc.unx.sas.com/SASStudio/"
        # url = "https://mwf.pgc.unx.sas.com/SASStudio/"
        # url = "https://tth.pgc.unx.sas.com/SASStudio/"
        # url = "https://analyst.dev.pgc.unx.sas.com/SASStudioNext/"
        # url = "https://analyst.de.dev.unx.sas.com/SASStudio/"
        self.goto(url)
        try:
            Helper.logger.info("enter _login.try")
            self.fill(self.user_name, "nlsbic")
            self.fill(self.user_password, "The power to know!")
            self.click(self.btn_submit)
        except Exception as e:
            Helper.logger.warning("login:", e)
        finally:
            self.wait_for(self.btn_compute_context)
            if self.is_visible(self.btn_compute_context):
                Helper.logger.info("_login:wait_for_login=True")
                return True
            Helper.logger.info("_login:wait_for_login=False")
            return False

    def login_studionext(self):

        if self.is_login_successful():
            return True
        for i in range(50):
            if self._login():
                return True
        return self.is_login_successful()

    def is_login_successful(self):
        if self.is_visible(self.btn_compute_context):
            return True
        return False
        # if self.locate_xpath("//span[text()='新建']").is_visible():
        #     return True

    def force_login(self):
        self._login()

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("Enter Logon page print screen ...")

        self.screenshot("//div[@class='content']", pic_name, user_assigned_xpath=True, clip=clip)

        Helper.logger.debug("... Exit Logon page print screen")
