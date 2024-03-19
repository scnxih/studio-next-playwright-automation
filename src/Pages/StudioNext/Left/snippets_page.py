"""
Author: Alice
Date: November 09, 2023
Description: SnippetsPage is child class of AccordionPage.
"""
from src.Pages.StudioNext.Left.accordion_page import AccordionPage


class SnippetsPage(AccordionPage):
    def __init__(self, page, title=''):
        AccordionPage.__init__(self, page, title)
