from src.Helper.helper import Helper
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane


class BasicStepPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    def set_filter_input_data(self,filter_text:str):
        self.click_Tab(Helper.data_locale.DATA)
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_INPUT_DATA,input_text=filter_text)

    def set_check_create_output_nodes_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_OUTPUT_NODES_DATA)

    def set_uncheck_create_output_nodes_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_OUTPUT_NODES_DATA)

    def set_check_create_output_links_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CREATE_OUTPUT_LINKS_DATA)

    def set_uncheck_create_output_links_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CREATE_OUTPUT_LINKS_DATA)

    def set_check_replace_existing_output_table_for_nodes(self):
        get_checkbox(self.base_xpath,self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label[contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,Helper.data_locale.CREATE_OUTPUT_NODES_DATA)).set_check()


    def set_uncheck_replace_existing_output_table_for_nodes(self):
        get_checkbox(self.base_xpath,self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label[contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,Helper.data_locale.CREATE_OUTPUT_NODES_DATA)).set_uncheck()

    def set_check_replace_existing_output_table_for_links(self):
        get_checkbox(self.base_xpath,self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label[contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,Helper.data_locale.CREATE_OUTPUT_LINKS_DATA)).set_check()


    def set_uncheck_replace_existing_output_table_for_links(self):
        get_checkbox(self.base_xpath,self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../../preceding-sibling::div[.//label[contains(text(),'{1}')]]]".format(
                         Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE,Helper.data_locale.CREATE_OUTPUT_LINKS_DATA)).set_uncheck()


