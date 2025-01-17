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
                            # MASK # Workspace icon in Open Items pane
                            self.locator(
                                '//div[@data-testid="open-files-list"]//span[@role="img"][contains(@aria-label, '
                                '"workspace")]/../../div[contains(@style, "margin")]'),

                            # MASK # Bell-shape icon in toast message
                            self.locator('//div[@data-testid="appMessageToast"]//span[@role="img"]'),

                            # MASK # Recovery Doc in Status Bar
                            "//button[@type='button'][.//span[contains(text(), '"
                            + Helper.data_locale.OPERATE_RECOVERY + "')]]",
                        ],
                        mask_color='#000000')
