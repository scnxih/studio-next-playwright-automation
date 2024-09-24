"""
Author: Alice
Date: November 25, 2023
Description: This is test cases file for flow.
"""
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.conftest import *

def test_init(page,init):
    PageHelper.init_environments(page)
def test_01_add_page(page, init):
    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.flow_screenshot()
