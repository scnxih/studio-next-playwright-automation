"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: Nov. 2nd, 2024
"""

from src.Pages.Common.dialog import *


class NewSnippetsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.NEW_SNIPPETS)

    @property
    def input_snippet_name(self):
        return self.get_by_test_id("newSnippetDialog-snippetName-input")

    @property
    def input_snippet_abbreviation(self):
        return self.get_by_test_id("newSnippetDialog-abbreviation-input")

    @property
    def textarea_snippet_description(self):
        return self.locate_xpath('//textarea[@data-testid="newSnippetDialog-description-textarea"]')

    def new_snippet(self, snippet_name, snippet_abbreviation, snippet_description):
        self.input_snippet_name.clear()

        self.fill(self.input_snippet_name, snippet_name)

        self.input_snippet_abbreviation.clear()

        self.fill(self.input_snippet_abbreviation, snippet_abbreviation)

        self.textarea_snippet_description.clear()

        self.fill(self.textarea_snippet_description, snippet_description)

        self.screenshot_self('new_snippet')

        self.click_button_in_footer(Helper.data_locale.OK)


        exist_alert = Alert(self.page, Helper.data_locale.SAVE_AS)
        time.sleep(1)

        if exist_alert.is_open():
            Helper.logger.debug("New Snippets Failed")
            exist_alert.click_button_in_footer(Helper.data_locale.CLOSE)
            time.sleep(1)
            # self.click_button_in_footer(Helper.data_locale.CANCEL)


    def new_abbreviation(self, snippet_abbreviation):
        """
        Type in abbreviation
        """
        self.input_snippet_abbreviation.clear()

        self.fill(self.input_snippet_abbreviation, snippet_abbreviation)

        self.screenshot_self('snippet_abbreviation')

        self.click_button_in_footer(Helper.data_locale.OK)

        exist_alert = Alert(self.page, Helper.data_locale.SAVE_AS)
        time.sleep(1)

        if exist_alert.is_open():
            Helper.logger.debug("New Snippets Failed")
            exist_alert.click_button_in_footer(Helper.data_locale.CLOSE)
            time.sleep(1)
