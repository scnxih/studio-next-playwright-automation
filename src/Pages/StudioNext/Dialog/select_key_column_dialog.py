"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 2nd, 2024
"""
# -*- coding: UTF-8 -*-

from src.Pages.Common.dialog import Dialog
from src.Pages.Common.combobox import Combobox
from src.Pages.Common.text import Text
from src.Pages.Common.grid import Grid


class SelectKeyColumnDialog(Dialog):
    """
    'Select Key Column' dialog for 'Load Table' (Load Technique = Update rows)
    """

    def __init__(self, page):
        Dialog.__init__(self, page)
        self.select_key_column_grid = Grid("", page)



