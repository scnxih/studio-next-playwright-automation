"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: Nov. 2nd, 2024
"""

from src.Pages.Common.dialog import *


class NewSnippetsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.NEW_SNIPPETS)