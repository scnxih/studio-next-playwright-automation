"""
@Project ：studio-next-playwright-automation 
@File    ：test_open_01.py
@Author  ：Allison
@Date    ：8/21/2023 12:22 AM 
"""
from src.conftest import *
from playwright.sync_api import Page, expect
from src.Pages.Common.dialog import *


def test_01_open(page, init):

    folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]

    PageHelper.open_file(page, folder_path, "测试2.sas")

    # expect(page.get_by_test_id("programView-editorPane-path-label")).to_contain_text("SAS 内容: /Public/测试1.sas")