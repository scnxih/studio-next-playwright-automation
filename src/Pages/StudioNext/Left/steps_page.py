"""
Author: Alice
Date: November 09, 2023
Description: StepsPage is child class of AccordionPage.
"""
import time

from src.Pages.Common.dialog import Alert
from src.Pages.Common.treeview_aggrid import TreeViewAGGrid
from src.Pages.Common.treeview_common import TreeViewCommon
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Utilities.enums import *
from src.Helper.helper import *


class StepsPage(AccordionPage):
    def __init__(self, page, title=''):
        AccordionPage.__init__(self, page, title)
        # self.tree = TreeViewCommon(self.base_xpath, self.page)
        self.tree = TreeViewAGGrid(self.base_xpath, self.page)

    def new(self, new_steps_type: NewStepsType):
        test_id_new = "stepsNavPane-toolBarNewButton-button"
        alert = Alert(self.page)
        match new_steps_type:
            case new_steps_type.quick_start:
                self.toolbar.click_btn_menu_by_test_id(test_id_new, Helper.data_locale.CUSTOM_STEP_QUICK_START)
                time.sleep(1)
                alert.screenshot_self("quick_start")
                alert.close_dialog()

            case new_steps_type.sample_controls:
                self.toolbar.click_btn_menu_by_test_id(test_id_new, Helper.data_locale.SAMPLE_CONTROLS)
                time.sleep(1)
                alert.screenshot_self("sample_controls")
                alert.close_dialog()
            case new_steps_type.basic_rank:
                self.toolbar.click_btn_menu_by_test_id(test_id_new, Helper.data_locale.STARTER_TEMPLATES,
                                                       Helper.data_locale.BASIC_RANK)
                time.sleep(1)
                alert.screenshot_self("basic_rank")
                alert.close_dialog()
            case new_steps_type.advanced_rank:
                self.toolbar.click_btn_menu_by_test_id(test_id_new, Helper.data_locale.STARTER_TEMPLATES,
                                                       Helper.data_locale.ADVANCED_RANK)
                time.sleep(1)
                alert.screenshot_self("advanced_rank")
                alert.close_dialog()
            case new_steps_type.advanced_define_column_structure:
                self.toolbar.click_btn_menu_by_test_id(test_id_new, Helper.data_locale.STARTER_TEMPLATES,
                                                       Helper.data_locale.ADVANCED_DEFINE_COLUMN_STRUCTURE)
                time.sleep(1)
                alert.screenshot_self("advanced_column_structure")
                alert.close_dialog()

    def show_menu_starter_templates(self):
        self.toolbar.click_btn_menu_by_test_id("stepsNavPane-toolBarNewButton-button",
                                               Helper.data_locale.STARTER_TEMPLATES)
        time.sleep(1)
        WholePage(self.page).screenshot_self("starter_templates")
        self.click_dialog_title_or_studionext_header()

    def navigate_to_step(self, step_path: list):
        locator = self.tree.navigate_to_element(step_path)
        time.sleep(0.5)
        return locator
    def add_to_flow(self,step_path: list):
        locator = self.navigate_to_step(step_path)
        self.click_context_menu(locator,Helper.data_locale.ADD_TO_FLOW)
        time.sleep(1)


