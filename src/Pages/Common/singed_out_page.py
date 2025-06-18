from src.Pages.Common.base_page import *


class SignedOutPage(BasePage):
    """
    The page after user signed out
    """
    def __init__(self, page):
        BasePage.__init__(self, page)

    @property
    def btn_sign_in(self):
        """
        The [Sign in] button.
        """
        return self.locate_xpath("//a[@id='submitBtn']")

    @property
    def page_content(self):
        """

        """
        return self.locate_xpath("//div[@class='block whiteBox']")

    def selfie(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the vanilla screenshot_self method in BasePage
        """
        Helper.logger.debug("SaveAsDialog: Overwrite the vanilla screenshot_self method in BasePage")
        self.screenshot(self.base_xpath, pic_name, clip=clip,
                        mask_color="#000000")

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("Enter Signed Out page print screen ...")

        # Click header to avoid any possible noise
        # self.click_dialog_title_or_studionext_header()

        self.screenshot("//div[@class='content']", pic_name, user_assigned_xpath=True, clip=clip)

        Helper.logger.debug("... Exit  Signed Out print screen")


