"""
Author: Alice
Date: October 23, 2023
Description: All central pages will inherit this CenterPage class directly or indirectly. Tab_group is removed from this
             class, meanwhile, TopTabGroup is added as independent class in order to better divide function.
             .

"""

from src.Pages.Common.toolbar import *
from src.Pages.Common.dialog import *
from src.Pages.StudioNext.Center.central_toolbar_helper import CentralToolbarHelper


class CenterPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-AppRoot-AppLayout_content']/descendant::section[2]/descendant::div[@data-testid='tab-group-content-area-_root_']"
        self.toolbar = Toolbar(self.base_xpath, page)
        """Added by Alice on 09/22/2023 start"""
        self.center_toolbar_helper = CentralToolbarHelper(self.toolbar)
        """Added by Alice on 09/22/2023 end"""
    def click_more_options(self):
        self.toolbar.click_more_options()
        time.sleep(1)