"""
Author: Alice
Date: Mar 07, 2024
Description: This is Table in flow Details pane.

"""
from src.Pages.Common.treegrid import TreeGrid
from src.Pages.Common.treeview_flow import TreeViewFlow
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane
from src.Pages.Common.text import *
from src.Pages.Common.textarea import *
from src.Utilities.enums import *


class SortPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)
        self.tree = TreeViewFlow(self.base_xpath, page)
        self.treegrid = TreeGrid(self.base_xpath, page)

    def add_sort(self, element_path: list, sort_way: SortWay):
        column_name = element_path[len(element_path) - 1]
        self.tree.navigate_to_element_and_dblclick(element_path)
        if sort_way == SortWay.descending:
            self.treegrid.select_item_combo_in_a_row(combo_item_text=Helper.data_locale.DESCENDING, name_text=column_name)
