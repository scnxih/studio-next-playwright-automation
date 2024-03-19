"""
@Project ：studio-next-playwright-automation 
@File    ：openitems_page.py
@Author  ：Allison
@Date    ：8/21/2023 3:49 AM 
"""
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.Common.dialog import *
from src.Pages.StudioNext.Dialog.open_dialog import OpenDialog


class OpenItemsPage(AccordionPage):
    def __init__(self, page):
        AccordionPage.__init__(self, page, Helper.data_locale.OPEN_ITEMS)

    def link_open(self):
        return self.locate_xpath('//div[@data-testid="openFilesNavPane-zeroState-flow"]/descendant::button')

    def btn_saveall(self):
        return self.locate_xpath('//*[@href="#sas-svg-saveall"]')

    def save_all_files(self, folder_path: list, file_name: list, if_replace):
        self.click(self.btn_saveall())

        Helper.logger.debug("after click save all button")
        count = len(folder_path)
        for i in range(count):
            save_as_dialog = SaveAsDialog(self.page)
            if save_as_dialog.is_open():
                save_as_dialog.save_file(folder_path[i], file_name[i], if_replace)

        Helper.logger.debug("create SaveAsDialog instance")

    def open_file(self, folder_path, file_name):
        self.click(self.link_open())
        open_file = OpenDialog(self.page)
        open_file.open_file(folder_path, file_name)