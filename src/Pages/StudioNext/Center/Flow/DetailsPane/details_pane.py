"""
Author: Alice
Date: Macr 05, 2024
Description: This is base class of all Flow details pane.

"""

from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
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

    def set_option_for_radio_group(self, parent_label: str, item_index: int = None, item_value: str = None):
        """
        Description: set eigenvector calculation method option by item index(index starts from 0) or by item value.
        """
        if item_index != None:
            get_radio_group(self.base_xpath, self.page,
                            parent_label=parent_label).set_check_for_index(item_index=item_index)
            return
        if item_value != None:
            get_radio_group(self.base_xpath, self.page,
                            parent_label=parent_label).set_check(item_value=item_value)
            return

    def _get_add_column_button(self,parent_label:str):
        return get_button(self.base_xpath,self.page,supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(Helper.data_locale.ADD_COLUMN,parent_label))
    def _get_add_exact_column_button(self,parent_label:str):
        return get_button(self.base_xpath,self.page,supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']]".format(Helper.data_locale.ADD_COLUMN,parent_label))
    def _get_delete_column_button(self,parent_label:str):
        return get_button(self.base_xpath,self.page,supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(Helper.data_locale.DELETE_COLUMNS,parent_label))
    def _get_delete_exact_column_button(self,parent_label:str):
        return get_button(self.base_xpath,self.page,supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']]".format(Helper.data_locale.DELETE_COLUMNS,parent_label))


    def click_add_column_button(self,parent_label:str):
        self._get_add_column_button(parent_label=parent_label).click_self()

    def click_delete_column_button(self,parent_label:str):
        self._get_delete_column_button(parent_label=parent_label).click_self()

    def click_add_exact_column_button(self,parent_label:str):
        self._get_add_exact_column_button(parent_label=parent_label).click_self()

    def click_delete_exact_column_button(self,parent_label:str):
        self._get_delete_exact_column_button(parent_label=parent_label).click_self()
