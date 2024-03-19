"""
File: custom_step_page.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/9/14 11:17
"""
from src.Pages.Common.toolbar import *
from src.Pages.Common.tab_group import TabGroup


class CustomStepPageTest(BasePage):
    """
    NOTE: This is a demo to test tab group.
    Modify this class if necessary.

    But, make sure your custom step class is composed of a  toolbar and tab group
    """

    def __init__(self, page):
        BasePage.__init__(self, page)
        self.toolbar = Toolbar("", page)
        self.tab_group = TabGroup("", page)
