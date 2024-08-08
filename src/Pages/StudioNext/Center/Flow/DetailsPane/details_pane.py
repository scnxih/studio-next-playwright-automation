"""
Author: Alice
Date: Macr 05, 2024
Description: This is base class of all Flow details pane.

"""
from src.Pages.Common.base_page import BasePage
from src.Pages.Common.tab_group import TabGroup
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog
from src.Utilities.enums import FlowNodeType
from src.Helper.helper import *
from src.Pages.Common.text import *
from src.Pages.Common.textarea import *


class DetailsPane(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-views-dataflow-FlowView_selected-pane']"
        self.tab_group = TabGroup("", page)

    def click_Tab(self,text):
        self.tab_group.click_tab_by_text(text)

    def set_node_name(self, name):
        self.click_Tab(Helper.data_locale.NODE)
        Text(self.base_xpath,self.page,supplement_base_xpath = "[../../../descendant::label[contains(text(),'"+Helper.data_locale.NODE_NAME+"')]]").fill_text(name)


    def set_node_description(self,description):
        self.click_Tab(Helper.data_locale.NODE)
        Textarea(self.base_xpath,self.page).fill_text(description)

    def set_notes(self,notes):
        self.click_Tab(Helper.data_locale.NOTES)
        Textarea(self.base_xpath,self.page).fill_text(notes)

    def click_data_tab(self):
        self.click_Tab(Helper.data_locale.DATA)

    def click_options_tab(self):
        self.click_Tab(Helper.data_locale.OPTIONS)

    def click_output_tab(self):
        self.click_Tab(Helper.data_locale.OUTPUT)

    def click_node_tab(self):
        self.click_Tab(Helper.data_locale.NODE)

    def click_notes_tab(self):
        self.click_Tab(Helper.data_locale.NOTES)