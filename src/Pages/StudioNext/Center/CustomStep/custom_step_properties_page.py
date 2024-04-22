"""
Author: Alice
Date: Apr 03, 2024
Description: This is properties of checkbox in custom step designer.
"""
import time

from src.Pages.Common.base_page import BasePage
from src.Helper.helper import *
from src.Pages.StudioNext.Dialog.add_items_dialog import AddItemsDialog
from src.Pages.Common.common_component_factory import *

class CustomStepPropertiesPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-Layouts-Flow-Flow_flow_vertical sas_designer-components-Properties-Properties_properties-flow']"
        self.toolbar = Toolbar(self.base_xpath,self.page)


    def get_numeric_stepper_by_data_test_id(self,data_test_id:str):
        return NumericStepper(self.base_xpath,self.page,data_test_id=data_test_id)
    def get_textarea_by_label(self,textarea_label:str):
        return Textarea(self.base_xpath, self.page, textarea_label=textarea_label)
    def get_text_by_contains_text(self,contains_text:str):
        return Text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(contains_text))

    def get_text_by_test_id(self,data_test_id:str):
        return Text(self.base_xpath,self.page,data_test_id=data_test_id)

    def get_combobox_by_data_test_id(self,data_test_id:str):
        return Combobox(self.base_xpath,self.page,data_test_id=data_test_id)

    def get_checkbox_by_data_test_id(self,data_test_id:str):
        return Checkbox(self.base_xpath,self.page,data_test_id=data_test_id)

    def get_checkbox_by_label(self,label:str):
        return Checkbox(self.base_xpath,self.page,label=label)
    def set_id(self,text:str):
        get_text(self.base_xpath,self.page,data_test_id="idInput-input").fill_text(text)
    def set_label(self, label: str):
        get_text(self.base_xpath, self.page, data_test_id="labelInput-input").fill_text(label)

    def set_check_by_default(self):
        get_checkbox(self.base_xpath,self.page,data_test_id="checkbox1_checkedByDefault-checkbox").set_check()

    def set_uncheck_by_default(self):
        get_checkbox(self.base_xpath, self.page, data_test_id="checkbox1_checkedByDefault-checkbox").set_uncheck()

    def set_indent(self, indent: str):
        get_numeric_stepper(self.base_xpath, self.page, supplement_base_xpath="[ancestor::div[@data-testid='datePickerAttributesIndent']]").set_value(indent)

    def expand_dependencies(self):
        get_windowshade(self.base_xpath,self.page,supplement_base_xpath="[descendant::span[text()='{0}']]".format(
                                                         Helper.data_locale.DEPENDENCIES)).expand()

    def collapse_dependencies(self):
        get_windowshade(self.base_xpath, self.page, supplement_base_xpath="[descendant::span[text()='{0}']]".format(
            Helper.data_locale.DEPENDENCIES)).collapse()
    def set_visibility(self,text:str):
        self.expand_dependencies()
        get_textarea(self.base_xpath,self.page,textarea_label=Helper.data_locale.VISIBILITY).fill_text(text)

    def set_enablement(self,text:str):
        self.expand_dependencies()
        get_textarea(self.base_xpath, self.page, textarea_label=Helper.data_locale.ENABLEMENT).fill_text(text)

    def click_select_color(self):
        get_button(self.base_xpath,self.page,supplement_base_xpath="[contains(@aria-label,'{0}')]".format(Helper.data_locale.CHOOSE_COLOR)).click_self()


    def set_RGB(self,red_value:int,green_value:int, blue_value:int):
        color_picker = get_color_picker("",self.page)
        time.sleep(0.5)
        color_picker.click_custom()
        time.sleep(0.5)
        color_picker.set_red_value(red_value)
        time.sleep(0.5)
        color_picker.set_green_value(green_value)
        time.sleep(0.5)
        color_picker.set_blue_value(blue_value)
        time.sleep(0.5)
        color_picker.click_ok()
        time.sleep(0.5)
    def set_default_library(self,library:str):
        get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(Helper.data_locale.DEFAULT_LIBRARY)).fill_text(library)

    def set_default_table(self,table:str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.DEFAULT_TABLE)).fill_text(table)
    def set_default_column_name(self,column_name:str):
        get_text(self.base_xpath,self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.DEFAULT_COLUNN_NAME)).fill_text(column_name)
    def set_default_column_label(self,column_label:str):
        get_text(self.base_xpath,self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.DEFAULT_COLUNN_LABEL)).fill_text(column_label)

    def set_default_length(self,column_length:str):
        get_text(self.base_xpath,self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.DEFAULT_LENGTH)).fill_text(column_length)

    def set_default_format(self,format:str):
        get_text(self.base_xpath,self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.DEFAULT_FORMAT)).fill_text(format)
    def set_default_informat(self,informat:str):
        get_text(self.base_xpath,self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.DEFAULT_INFORMAT)).fill_text(informat)
    def set_placeholder_text(self,placeholder:str):
        get_text(self.base_xpath, self.page,
                 supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                     Helper.data_locale.PLACEHOlDER_TEXT)).fill_text(placeholder)


    def set_check_required(self):
        get_checkbox(self.base_xpath,self.page,data_test_id="requiredCheckbox-checkbox").set_check()

    def set_uncheck_required(self):
        get_checkbox(self.base_xpath, self.page, data_test_id="requiredCheckbox-checkbox").set_uncheck()
    
    def set_check_allow_display_all_column_properties(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.ALLOW_DISPLAYING_ALL_COLUMN_PROPERTIES).set_check()
    def set_uncheck_allow_display_all_column_properties(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.ALLOW_DISPLAYING_ALL_COLUMN_PROPERTIES).set_uncheck()

    def set_check_column_properties_are_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.COLUMNS_PROPERTIES_ARE_READ_ONLY).set_check()
    def set_uncheck_column_properties_are_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.COLUMNS_PROPERTIES_ARE_READ_ONLY).set_uncheck()
    def set_check_control_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.MAKE_CONTROL_READ_ONLY).set_check()

    def set_uncheck_control_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.MAKE_CONTROL_READ_ONLY).set_uncheck()
        self.get_checkbox_by_label(Helper.data_locale.MAKE_CONTROL_READ_ONLY).set_uncheck()
        
    def set_check_hide_at_runtime(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.HIDE_CONTROL_AT_RUNTIME).set_check()

    def set_uncheck_hide_at_runtime(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.HIDE_CONTROL_AT_RUNTIME).set_uncheck()

    def select_item_in_link_input_table(self,item_value:str):
        get_combobox(self.base_xpath, self.page, data_test_id="columnselector-1_inputTableSelect").select_item(item_value)

    def select_item_in_column_type(self,item_value:str):
        get_combobox(self.base_xpath, self.page, data_test_id="columnselector-1_columnTypeSelect").select_item(
            item_value)

    def select_item_in_default_type(self,item_value:str):
        get_combobox(self.base_xpath, self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
                     .format(Helper.data_locale.DEFAULT_TYPE)).select_item(item_value)

        
    def set_check_allow_order_column(self):
        get_checkbox(self.base_xpath, self.page,label=Helper.data_locale.ALLOW_ORDER_COLUMN).set_check()

    def set_uncheck_allow_order_column(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.ALLOW_ORDER_COLUMN).set_uncheck()
    def set_min_columns(self,min_columns:str):
        get_numeric_stepper(self.base_xpath, self.page,data_test_id="columnselector-1_minimumNumericStepper").set_value(min_columns)

    def set_max_columns(self,max_columns:str):
        get_numeric_stepper(self.base_xpath, self.page,data_test_id="columnselector-1_maximumNumericStepper").set_value(max_columns)
    def add_many_items(self,text:str):
        self.toolbar.click_btn_by_title(Helper.data_locale.ADD_MULTIPLE_ITEMS_TO_LIST)
        time.sleep(1)
        dlg = AddItemsDialog(self.page)
        dlg.fill_items(text)
        time.sleep(1)
        dlg.click_button_in_footer(Helper.data_locale.OK)

