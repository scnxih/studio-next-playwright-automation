"""
Author: Alice
Date: Mar 22, 2024
Description: This is the whole page of StudioNext. It is used to screenshot all the whole page.
"""
from src.Pages.Common.base_page import *


class WholePage(BasePage):
    def __init__(self, page: Page):
        BasePage.__init__(self, page)
        self.base_xpath += "//div[@id='app']"

    def screenshot_self(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot in WholePage")

        # Overwrite the screenshot_self function in basePage
        self.screenshot(self.base_xpath, pic_name, clip=clip,
                        mask=[
                            self.locator('//div[@data-testid="appMessageToast"]//span[@role="img"]'),
                            "//button[@type='button'][.//span[contains(text(), '" + Helper.data_locale.OPERATE_RECOVERY + "')]]",
                            # "//span[contains(@class,'BaseButton' )][contains(text(), " + Helper.data_locale.COLUMN + ")]",
                            # "//div[@role='button'][@title='" + Helper.data_locale.USER_OPTION + "']",
                            # '//button[@data-testid="programViewPane-toolbar-runButton"]'
                        ],
                        mask_color='#000000')
