"""
@author: Alice
@date: Updated on 2024/04/12
@description: Define Add Items dialog which is used in custom step designer.
"""

from src.Pages.Common.dialog import *
from src.Pages.Common.textarea import Textarea


class AddItemsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.ADD_ITEMS)
        self.text_area = Textarea(self.base_xpath,self.page)

    def fill_items(self,text:str):
        self.text_area.fill_text(text)
