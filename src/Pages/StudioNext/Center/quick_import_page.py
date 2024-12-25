"""
File: quick_import_page.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/9/14 11:03
Updated by Alice on 10/24/2023
Description: QuickImportPage will inherit from MainCenterPage class, thus the methods in MainCenterPage will be inherited automatically.
            You can also override these parent class methods in this QuickImportPage class if needed.


"""
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage


class QuickImportPage(MainCenterPage):

    def __init__(self, page):
        MainCenterPage.__init__(self, page)

    def apply_main_layout_horizontal(self):
        self.center_toolbar_helper.apply_main_layout_horizontal()

    def apply_main_layout_vertical(self):
        self.center_toolbar_helper.apply_main_layout_vertical()

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()
