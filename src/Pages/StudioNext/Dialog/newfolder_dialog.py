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
        exist_alert = Alert(self.page, "SAS® Studio Next")
        time.sleep(1)
        if exist_alert.is_open():
            exist_alert.click_button_in_footer(Helper.data_locale.CLOSE)
            time.sleep(1)
            self.click_button_in_footer(Helper.data_locale.CANCEL)