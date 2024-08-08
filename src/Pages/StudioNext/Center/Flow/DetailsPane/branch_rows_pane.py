"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: July 23rd, 2024
"""
# -*- coding: UTF-8 -*-
from playwright.sync_api import expect
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.button import *
from src.Pages.StudioNext.Dialog.select_a_column_dialog import SelectColumnDialog


class BranchRowsPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    @property
    def button_add_a_row(self):
        """
        Button 'Add a row' in toolbar
        """
        return ''


    def select_a_column(self):
        Button(self.base_xpath, self.page,
               data_test_id="branchConditionCard0-filterViewContent-filterColumn0-columnCompositeInputCompositeInput-button").click_self()
        # select_column_dialog = SelectColumnDialog(self.page)
        # select_column_dialog.select_a_column_and_OK('Sex')
