from src.Helper.helper import Helper
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane


class BasicStepPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    def set_filter_input_data(self,filter:str):
        self.click_Tab(Helper.data_locale.DATA)
        get_text(self.base_xpath,self.page,parent_label=Helper.data_locale.FILTER_INPUT_DATA).fill_text(filter)

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
