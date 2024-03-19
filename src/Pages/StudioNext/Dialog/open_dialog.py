from src.Pages.Common.dialog import *
import time

from src.Pages.Common.toolbar import Toolbar
from src.Pages.Common.treeview_nova import TreeViewNova
from src.Pages.Common.combobox import Combobox


class OpenDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.OPEN)
        self.folder_tree = TreeViewNova(self.base_xpath, page)
        """modified by Alice on 09/15/2023 since common component constructor has been changed"""
        self.toolbar = Toolbar(self.base_xpath, page)
        ''' modified by Alice on 09/15/2023 since all common component constructor has been changed'''
        self.combobox_type = Combobox(container_base_xpath=self.base_xpath, page=page, data_test_id="contentSelector"
                                                                                                   "-open-contentSelector-type")

    def select_file(self, file_name):
        return self.locate_xpath("//span[contains(text(),'" + file_name + "')]")

    def navigate_to_folder(self, folder_path: list):
        return self.folder_tree.navigate_to_element(folder_path)

    def open_file(self, folder_path: list, file_name):
        if not self.navigate_to_folder(folder_path):
            return False
        self.click(self.locate_xpath("//div[@data-testid='contentSelector-open-contentSelector-navigator-table']"))
        self.scroll_if_needed(self.select_file(file_name))
        if self.is_visible(self.select_file(file_name)):
            self.dblclick(self.select_file(file_name))
            time.sleep(2)
            return True
        Helper.logger.debug("Cannot find file:"+"/".join(map(str, folder_path))+file_name)
        return False

    def open_by_type(self, open_by_type):
        self.combobox_type.select_item(open_by_type)
