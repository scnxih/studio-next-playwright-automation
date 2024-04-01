"""
@Project ：studio-next-playwright-automation
@File    ：library_page.py
@Author  ：Liu Jia
@Date    ：9/04/2023
"""
import time
from src.Pages.StudioNext.Dialog.newfolder_dialog import NewFolderDialog
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.Common.treeview_aggrid import *
from src.Pages.Common.dialog import *
from src.Utilities.enums import AccordionType


class LibraryPage(AccordionPage):
    def __init__(self, page, title=''):
        AccordionPage.__init__(self, page, title)
        self.tree = TreeViewAGGrid(self.base_xpath, page)

    def expand_library(self, library_name):
        self.collapse_all()
        time.sleep(1)
        label = library_name
        self.tree.icon_expand_element(self, label)

    def open_table(self, library_name, table_name):
        table_path = [Helper.data_locale.CONNECTED_LIBRARIES, library_name, table_name]
        self.tree.navigate_to_element_and_dblclick(table_path)


    def delete_table_btn(self, library_name, table_name):
        self.collapse_all()
        time.sleep(1)
        table_path = [Helper.data_locale.CONNECTED_LIBRARIES, library_name, table_name]
        table = self.tree.navigate_to_element(table_path)
        self.click(table)
        self.toolbar.click_btn_by_title(Helper.data_locale.DELETE)
        delete_table = Alert(self.page, Helper.data_locale.DELETE)
        delete_table.click_button_in_footer(Helper.data_locale.DELETE)

    def delete_table_menu(self, library_name, table_name):
        self.collapse_all()
        time.sleep(1)
        table_path = [Helper.data_locale.CONNECTED_LIBRARIES, library_name, table_name]
        table = self.tree.navigate_to_element(table_path)
        self.click(table)
        self.invoke_context_menu()
        self.click_menu_item(Helper.data_locale.DELETE)
        delete_table = Alert(self.page, Helper.data_locale.DELETE)
        delete_table.click_button_in_footer(Helper.data_locale.DELETE)

    def refresh_library_btn(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.REFRESH)

    def properties_btn(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.PROPERTIES)