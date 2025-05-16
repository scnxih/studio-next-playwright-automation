"""
File: test_level0_show_about_dialog.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2024/1/17 10:09 
"""
import time

from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Pages.StudioNext.Dialog.about_dialog import AboutDialog


# \\huanghe\vtg\ECT\TESTCASE\SAS Studio\6.0\Automated\About0001_ShowAboutDialog.docx
def test_init(page,init):
    PageHelper.init_environments(page)

def test_01_show_about_dialog(page, init):
    """
    Take a screenshot of the About dialog
    """
    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_about()
    about_dialog = AboutDialog(page)

    # Step-2: Take the screenshot with mask
    about_dialog.wait_for_page_load()
    # time.sleep(1)

    # Take the screenshot and hide the release, site name and site number.
    about_dialog.screenshot_self('about_dialog',
                                 mask=[about_dialog.release_number, about_dialog.site_name, about_dialog.site_number],
                                 mask_color='#000000')

    # Step-3: Close the dialog
    about_dialog.close_dialog()
