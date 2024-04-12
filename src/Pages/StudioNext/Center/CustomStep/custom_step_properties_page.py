"""
Author: Alice
Date: Apr 03, 2024
Description: This is properties of checkbox in custom step designer.
"""
import time

from src.Pages.Common.base_page import BasePage
from src.Pages.Common.radio_group import RadioGroup
from src.Pages.Common.text import Text
from src.Pages.Common.toolbar import Toolbar
from src.Pages.Common.window_shade import WindowShade
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.numeric_stepper import NumericStepper
from src.Helper.helper import *
from src.Pages.Common.textarea import Textarea
from src.Pages.Common.button import Button
from src.Pages.Common.color_picker import ColorPicker
from src.Pages.Common.combobox import Combobox
from src.Pages.StudioNext.Dialog.add_items_dialog import AddItemsDialog


class CustomStepPropertiesPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-Layouts-Flow-Flow_flow_vertical sas_designer-components-Properties-Properties_properties-flow']"
        self.text_id = Text(self.base_xpath, self.page, data_test_id="idInput-input")
        self.text_label = Text(self.base_xpath, self.page, data_test_id="labelInput-input")
        self.check_box_by_default = Checkbox(self.base_xpath, self.page,
                                             data_test_id="checkbox1_checkedByDefault-checkbox")
        self.check_box_required = Checkbox(self.base_xpath,self.page,data_test_id="requiredCheckbox-checkbox")
        self.check_box_make_control_read_only = Checkbox(self.base_xpath, self.page, label=Helper.data_locale.MAKE_CONTROL_READ_ONLY)
        self.check_box_hide_control_at_runtime = Checkbox(self.base_xpath,self.page,label=Helper.data_locale.HIDE_CONTROL_AT_RUNTIME)
        self.text_default_library = Text(self.base_xpath,self.page,supplement_base_xpath= "[../../../descendant::label[contains(text(),'{0}')]]".format(Helper.data_locale.DEFAULT_LIBRARY))
        self.text_default_table = Text(self.base_xpath, self.page,
                                         supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                             Helper.data_locale.DEFAULT_TABLE))

        self.text_placeholder = Text(self.base_xpath, self.page,
                                       supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                           Helper.data_locale.PLACEHOlDER_TEXT))



        self.numeric_stepper_indent = NumericStepper(self.base_xpath, self.page,
                                                     supplement_base_xpath="[ancestor::div[@data-testid='datePickerAttributesIndent']]")
        self.window_shade_dependencies = WindowShade(self.base_xpath, self.page,
                                                     supplement_base_xpath="[descendant::span[text()='{0}']]".format(
                                                         Helper.data_locale.DEPENDENCIES))

        self.text_area_visibility = Textarea(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(Helper.data_locale.VISIBILITY))
        self.text_area_enablement = Textarea(self.base_xpath, self.page,
                                             supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
                                                 Helper.data_locale.ENABLEMENT))
        self.btn_color = Button(self.base_xpath,self.page,supplement_base_xpath="[contains(@aria-label,'{0}')]".format(Helper.data_locale.CHOOSE_COLOR))
        self.color_picker = ColorPicker("",self.page)
        self.combobox_link_input_table = Combobox(self.base_xpath,self.page,data_test_id="columnselector-1_inputTableSelect")
        self.combobox_column_type = Combobox(self.base_xpath,self.page,data_test_id="columnselector-1_columnTypeSelect")
        self.check_box_allow_order_column = Checkbox(self.base_xpath,self.page,label=Helper.data_locale.ALLOW_ORDER_COLUMN)
        self.numeric_stepper_min_columns = NumericStepper(self.base_xpath,self.page,data_test_id="columnselector-1_minimumNumericStepper")
        self.numeric_stepper_max_columns = NumericStepper(self.base_xpath,self.page,data_test_id="columnselector-1_maximumNumericStepper")
        self.toolbar = Toolbar(self.base_xpath,self.page)
        self.btn_exclude_columns = Button(self.base_xpath,self.page,data_test_id="columnExclusionsEditButton")


    # def set_id(self,text:str):
    #     self.text_id.fill_text(text)
    def get_text_by_contains_text(self,contains_text:str):
        return Text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(contains_text))

    def get_text_by_test_id(self,data_test_id:str):
        return Text(self.base_xpath,self.page,data_test_id=data_test_id)
    def set_label(self, label: str):
        self.get_text_by_test_id("labelInput-input").fill_text(label)

    def set_check_by_default(self):
        self.check_box_by_default.set_check()

    def set_uncheck_by_default(self):
        self.check_box_by_default.set_uncheck()

    def set_indent(self, indent: str):
        self.numeric_stepper_indent.set_value(indent)

    def expand_dependencies(self):
        self.window_shade_dependencies.expand()

    def collapse_dependencies(self):
        self.window_shade_dependencies.collapse()

    def set_visibility(self,text:str):
        self.expand_dependencies()
        self.text_area_visibility.fill_text(text)

    def set_enablement(self,text:str):
        self.expand_dependencies()
        self.text_area_enablement.fill_text(text)

    def click_select_color(self):
        self.btn_color.click_self()

    def set_RGB(self,red_value:int,green_value:int, blue_value:int):
        time.sleep(0.5)
        self.color_picker.click_custom()
        time.sleep(0.5)
        self.color_picker.set_red_value(red_value)
        time.sleep(0.5)
        self.color_picker.set_green_value(green_value)
        time.sleep(0.5)
        self.color_picker.set_blue_value(blue_value)
        time.sleep(0.5)
        self.color_picker.click_ok()
        time.sleep(0.5)
    def set_default_library(self,library:str):
        self.get_text_by_contains_text(Helper.data_locale.DEFAULT_LIBRARY).fill_text(library)

    def set_default_table(self,table:str):
        self.get_text_by_contains_text(Helper.data_locale.DEFAULT_TABLE).fill_text(table)

    def set_placeholder_text(self,placeholder:str):
        self.get_text_by_contains_text(Helper.data_locale.PLACEHOlDER_TEXT).fill_text(placeholder)

    def set_check_required(self):
        self.check_box_required.set_check()

    def set_uncheck_required(self):
        self.check_box_required.set_uncheck()

    def set_check_control_read_only(self):
        self.check_box_make_control_read_only.set_check()

    def set_uncheck_control_read_only(self):
        self.check_box_make_control_read_only.set_uncheck()
        
    def set_check_hide_at_runtime(self):
        self.check_box_hide_control_at_runtime.set_check()
        

    def set_uncheck_hide_at_runtime(self):
        self.check_box_hide_control_at_runtime.set_uncheck()

    def select_item_in_link_input_table(self,item_value:str):
        self.combobox_link_input_table.select_item(item_value)

    def select_item_in_column_type(self,item_value:str):
        self.combobox_column_type.select_item(item_value)
        
    def set_check_allow_order_column(self):
        self.check_box_allow_order_column.set_check()
    
    def set_uncheck_allow_order_column(self):
        self.check_box_allow_order_column.set_uncheck()

    def set_min_columns(self,min_columns:str):
        self.numeric_stepper_min_columns.set_value(min_columns)

    def set_max_columns(self,max_columns:str):
        self.numeric_stepper_max_columns.set_value(max_columns)

    def add_many_items(self,text:str):
        self.toolbar.click_btn_by_title(Helper.data_locale.ADD_MULTIPLE_ITEMS_TO_LIST)
        time.sleep(1)
        dlg = AddItemsDialog(self.page)
        dlg.fill_items(text)
        time.sleep(1)
        dlg.click_button_in_footer(Helper.data_locale.OK)

