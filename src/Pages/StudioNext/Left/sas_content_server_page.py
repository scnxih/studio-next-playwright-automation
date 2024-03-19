import time

from src.Pages.StudioNext.Dialog.newfolder_dialog import NewFolderDialog
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.Common.treeview_aggrid import *
from src.Pages.Common.dialog import *
from src.Utilities.enums import AccordionType


class SASContentServerPage(AccordionPage):
    def __init__(self, page, title=''):
        AccordionPage.__init__(self, page, title)
        """Add first argument by Alice on 09/22/2023"""
        self.tree = TreeViewAGGrid(self.base_xpath, page)

    def navigate_to_folder(self, folder_path: list):
        self.collapse_all()
        time.sleep(1)
        return self.tree.navigate_to_element(folder_path)

    def navigate_and_click_context_menu_on_folder_or_file(self, folder_path_or_folder_file_path: list,
                                                          *context_menu_text):
        self.collapse_all()
        time.sleep(1)
        self.tree.navigate_to_element_and_click_context_menu(folder_path_or_folder_file_path, *context_menu_text)

    def open_file(self, folder_file_path: list):
        self.collapse_all()
        time.sleep(1)
        file = self.tree.navigate_to_element(folder_file_path)
        self.dblclick(file)

    def delete_file(self, folder_file_path: list):
        self.collapse_all()
        time.sleep(1)
        self.navigate_and_click_context_menu_on_folder_or_file(folder_file_path, Helper.data_locale.DELETE)
        delete_alert = Alert(self.page, Helper.data_locale.DELETE)
        time.sleep(1)
        if delete_alert.is_open():
            delete_alert.click_button_in_footer(Helper.data_locale.DELETE)

    def new_folder(self, entrance: str, folder_path: list, folder_name):
        folder = self.navigate_to_folder(folder_path)
        if folder is None:
            return False

        if entrance == "Toolbar":
            self.toolbar.click_btn_menu_by_title(Helper.data_locale.NEW, Helper.data_locale.FOLDER)
        if entrance == "ContextMenu":
            self.click_context_menu(folder, Helper.data_locale.NEW_FOLDER)

        new_folder = NewFolderDialog(self.page)
        new_folder.new_folder(folder_name)

    def delete_single_item(self, entrance: str, folder_path: list):
        folder = self.navigate_to_folder(folder_path)
        if folder is None:
            return False

        if entrance == "Toolbar":
            self.toolbar.click_btn_by_title_contains(Helper.data_locale.DELETE)
        if entrance == "ContextMenu":
            self.click_context_menu(folder, Helper.data_locale.DELETE)

        delete_folder = Alert(self.page, Helper.data_locale.DELETE)
        delete_folder.click_button_in_footer(Helper.data_locale.DELETE)

    def delete_multiple_items(self, entrance: str, folder_path: list):
        count = len(folder_path)
        for i in range(count):
            exist = self.navigate_to_folder(folder_path[i])
            self.key_down("Control")
            if not exist:
                return False
        self.key_up("Control")
        if entrance == "Toolbar":
            self.toolbar.click_btn_by_title_contains(Helper.data_locale.DELETE)
        if entrance == "ContextMenu":
            self.key_press('Shift+F10')
            self.click_menu_item(Helper.data_locale.DELETE)

        delete_folder = Alert(self.page, Helper.data_locale.DELETE)
        delete_folder.click_button_in_footer(Helper.data_locale.DELETE)

    def show_properties(self, entrance: str, folder_path: list):
        folder = self.navigate_to_folder(folder_path)
        if folder is None:
            return False
        if entrance == "Toolbar":
            self.toolbar.click_btn_by_title_contains(Helper.data_locale.PROPERTIES)
        if entrance == "ContextMenu":
            self.click_context_menu(folder, Helper.data_locale.PROPERTIES)

        properties = Dialog(self.page, Helper.data_locale.PROPERTIES)
        time.sleep(2)
        self.screenshot_critical('//div[@data-testid="contentProperties-Dialog-dialog"]', "properties", True)
        properties.click_button_in_footer(Helper.data_locale.CLOSE)

