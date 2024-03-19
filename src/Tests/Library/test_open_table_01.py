"""
@Project ：studio-next-playwright-automation
@File    ：test_open_table_01.py
@Author  ：Liu Jia
@Date    ：9/05/2023
"""
from src.Utilities.enums import AccordionType
from src.conftest import *
from playwright.sync_api import Page, expect
from src.Pages.Common.dialog import *


def test_01_opentable(page, init):
    PageHelper.show_accordion(page, AccordionType.libraries)
    PageHelper.open_table(page,"SASHELP", "CARS")
