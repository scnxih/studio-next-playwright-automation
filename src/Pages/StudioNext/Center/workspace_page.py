"""
Author: Alice
Date: October 25, 2023
Description: WorkspacePage will inherit from TextCenterPage class, thus the methods in TextCenterPage will be inherited automatically.
            You can also override these methods in this WorkspacePage class if needed.

"""
import time
from src.Helper.helper import Helper
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Pages.StudioNext.Center.text_center_page import TextCenterPage


class WorkspacePage(TextCenterPage):
    def __init__(self, page):
        TextCenterPage.__init__(self, page)
        self.editor = EditorTextArea(self.base_xpath, page)

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("screenshot_self in JobDefinitionPage")

        # NOT Real whole page
        # self.screenshot(self.base_xpath, pic_name, clip=clip,
        self.screenshot("//div[@id='app']", pic_name, user_assigned_xpath=True, clip=clip,
                        mask=[
                                 self.locator('//div[@data-testid="appMessageToast"]//span[@role="img"]'),
                                 self.locator(
                                     "//button[@type='button'][.//span[contains(text(), '" + Helper.data_locale.OPERATE_RECOVERY + "')]]"),
                                 '//button[@data-testid="programViewPane-toolbar-runButton"]',
                                 self.locator('//div[@data-testid="open-files-list"]//span[@role="img"][contains(@aria-label, "workspace")]/../../div[contains(@style, "margin")]')] + self.ln_col_number,
                        # mask[] of 'line & col number' in status bar
                        mask_color='#F9FAFB')

    def undo(self):
        self.center_toolbar_helper.undo()
        time.sleep(0.5)
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'workspace_undo',
                        user_assigned_xpath=True)

    def redo(self):
        self.center_toolbar_helper.redo()
        time.sleep(0.5)
        self.screenshot('//div[@data-testid="textViewPane-editorPane-editor"]',
                        'workspace_redo',
                        user_assigned_xpath=True)
