"""
Author: Alice
Date: Mar 22, 2024
Description: This is the whole page of StudioNext. It is used to screenshot all the whole page.
"""
from src.Pages.Common.base_page import *


class WholePage(BasePage):
    def __init__(self, page: Page):
        BasePage.__init__(self,page)
        self.base_xpath += "//div[@id='app']"
