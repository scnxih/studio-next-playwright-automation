"""
@author: Alice
@date: Updated on 2024/04/12
@description: Define Exclude Columns dialog which is used in custom step designer.
"""

from src.Pages.Common.dialog import *
from src.Pages.Common.textarea import Textarea


class ExcludeColumnsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.EXCLUDE_COLUMNS)



