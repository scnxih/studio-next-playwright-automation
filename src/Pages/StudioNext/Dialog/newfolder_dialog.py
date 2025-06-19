"""
@Project: studio-next-playwright-automation 
@File: newfolder_dialog.py
@Author: Allison
@Date: 8/25/2023 4:59 AM 

"""
import time

from src.Pages.Common.dialog import *


class NewFolderDialog(Dialog):

    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.NEW_FOLDER)

    @property
    def input_folder_name(self):
        return self.get_by_test_id("newFolderDialog-newNameInput-input")

    def new_folder(self, folder_name):
        self.input_folder_name.clear()
        self.fill(self.input_folder_name, folder_name)
        self.click_button_in_footer(Helper.data_locale.OK)

        # Thursday, June 19, 2025,
        # Title updated to current 'SAS Studio' from former 'SAS® Studio Next'.
        # exist_alert = Alert(self.page, "SAS® Studio Next")

        exist_alert = Alert(self.page, "SAS Studio")
        time.sleep(1)
        if exist_alert.is_open():
            Helper.logger.debug("Path already exist.")
            exist_alert.click_button_in_footer(Helper.data_locale.CLOSE)
            # time.sleep(1)
            self.wait_for_page_load(time_out=3000)
            self.click_button_in_footer(Helper.data_locale.CANCEL)