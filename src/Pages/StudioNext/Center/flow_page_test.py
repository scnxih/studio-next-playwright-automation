"""
File: flow_page.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/9/14 10:13
"""
from src.Pages.Common.toolbar import *
from src.Pages.Common.tab_group import TabGroup


class FlowPageTest(BasePage):
    """
    NOTE: This is a demo to test tab group.
    Modify this class if necessary.

    But, make sure your flow page class is composed of a  toolbar and tab group
    """

    def __init__(self, page):
        BasePage.__init__(self, page)
        self.toolbar = Toolbar("", page)
        self.tab_group = TabGroup("", page)
