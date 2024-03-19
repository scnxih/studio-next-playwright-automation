"""
@author: Frank (Feng) Jiang
@date: 2023/09/19
@description: define Query page, include page elements and functionalities
@Updated by Alice on 10/24/2023
@Description: QueryPage will inherit from MainCenterPage class, thus the methods in MainCenterPage will be inherited automatically.
            You can also override these parent class methods in this QueryPage class if needed.


"""
from src.Pages.Common.treeview_common import TreeViewCommon
from src.Pages.StudioNext.Center.base_editor import BaseEditor
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem
from src.Pages.StudioNext.Center.center_page import *
from src.Pages.Common.treegrid import *
from src.Pages.Common.toolbar import *
from src.Pages.Common.tab_group import TabGroup
from src.Pages.StudioNext.Center.central_toolbar_helper import *


class QueryPage(MainCenterPage):
    def __init__(self, page):
        MainCenterPage.__init__(self, page)
        self.treegrid = TreeGrid(self.base_xpath, self.page)

        """Added by Alice on 00/27/2023 Start"""
        self.treeview = TreeViewCommon(self.base_xpath,page,supplement_base_xpath="[@test-id='query-columnsPane-selectColumnsTree']")
        """Added by Alice on 00/27/2023 End"""

    def tab(self, tab_label: str):
        return self.locate_xpath(
            "//div[@role='tab'][@data-sasrc-tablocation='bottom']//span[text()='{0}']".format(tab_label))

    def click_tab(self, tab_label: str):
        self.click(self.tab(tab_label))

    @property
    def btn_add_table_zero(self):
        return self.get_by_test_id("queryBuilder-tab-columns-zeroState-add")

    def click_add_table(self):
        self.click(self.btn_add_table_zero)

    def table_t1(self):
        return self.locate_xpath("//div[@role='treeitem']//label[contains(text(), 't1')]")

    def dbclick_t1(self):
        self.dblclick(self.table_t1())



    def apply_main_layout_horizontal(self):
        self.center_toolbar_helper.apply_main_layout_horizontal()

    def apply_main_layout_vertical(self):
        self.center_toolbar_helper.apply_main_layout_vertical()
    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()
