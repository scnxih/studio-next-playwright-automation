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
from src.Utilities.enums import *


class CustomStepPropertiesPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-Layouts-Flow-Flow_flow_vertical sas_designer-components-Properties-Properties_properties-flow']"
        self.toolbar = Toolbar(self.base_xpath, self.page)

    def set_id(self, text: str):
        get_text(self.base_xpath, self.page, data_test_id="idInput-input").fill_text(text)

    def set_label(self, label: str):
        get_text(self.base_xpath, self.page, data_test_id="labelInput-input").fill_text(label)

    def set_check_by_default(self):
        get_checkbox(self.base_xpath, self.page, data_test_id="checkbox1_checkedByDefault-checkbox").set_check()

    def set_uncheck_by_default(self):
        get_checkbox(self.base_xpath, self.page, data_test_id="checkbox1_checkedByDefault-checkbox").set_uncheck()

    def set_indent(self, indent: str):
        get_numeric_stepper(self.base_xpath, self.page,
                            supplement_base_xpath="[ancestor::div[contains(@data-testid,'indentLevel')]]").set_value(
            indent)

    def expand_dependencies(self):
        # get_windowshade(self.base_xpath, self.page, supplement_base_xpath="[descendant::span[text()='{0}']]".format(
        #     Helper.data_locale.DEPENDENCIES)).expand()
        get_windowshade(self.base_xpath, self.page, parent_label=Helper.data_locale.DEPENDENCIES).expand()

    def collapse_dependencies(self):
        # get_windowshade(self.base_xpath, self.page, supplement_base_xpath="[descendant::span[text()='{0}']]".format(
        #     Helper.data_locale.DEPENDENCIES)).collapse()
        get_windowshade(self.base_xpath, self.page, parent_label=Helper.data_locale.DEPENDENCIES).collapse()


    def set_visibility(self, text: str):
        self.expand_dependencies()
        get_textarea(self.base_xpath, self.page, textarea_label=Helper.data_locale.VISIBILITY).fill_text(text)

    def set_enablement(self, text: str):
        self.expand_dependencies()
        get_textarea(self.base_xpath, self.page, textarea_label=Helper.data_locale.ENABLEMENT).fill_text(text)

    def click_select_color(self):
        get_button(self.base_xpath, self.page, supplement_base_xpath="[contains(@aria-label,'{0}')]".format(
            Helper.data_locale.CHOOSE_COLOR)).click_self()

    def set_RGB(self, red_value: int, green_value: int, blue_value: int):
        color_picker = get_color_picker("", self.page)
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

    def set_default_library(self, library: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_LIBRARY)).fill_text(library)
        get_text(self.base_xpath, self.page,parent_label= Helper.data_locale.DEFAULT_LIBRARY).fill_text(library)
    def set_default_table(self, table: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_TABLE)).fill_text(table)
        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.DEFAULT_TABLE).fill_text(table)

    def set_default_column_name(self, column_name: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_COLUNN_NAME)).fill_text(column_name)
        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.DEFAULT_COLUNN_NAME).fill_text(column_name)

    def set_default_column_label(self, column_label: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_COLUNN_LABEL)).fill_text(column_label)
        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.DEFAULT_COLUNN_LABEL).fill_text(column_label)

    def set_default_length(self, column_length: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_LENGTH)).fill_text(column_length)
        get_text(self.base_xpath, self.page,
                 parent_label = Helper.data_locale.DEFAULT_LENGTH).fill_text(column_length)

    def set_default_format(self, format: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_FORMAT)).fill_text(format)
        get_text(self.base_xpath, self.page,
                 parent_label = Helper.data_locale.DEFAULT_FORMAT).fill_text(format)

    def set_default_informat(self, informat: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_INFORMAT)).fill_text(informat)

        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.DEFAULT_INFORMAT).fill_text(informat)
    def set_placeholder_text(self, placeholder: str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.PLACEHOlDER_TEXT)).fill_text(placeholder)
        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.PLACEHOlDER_TEXT).fill_text(placeholder)

    def set_check_required(self):
        get_checkbox(self.base_xpath, self.page, data_test_id="requiredCheckbox-checkbox").set_check()

    def set_uncheck_required(self):
        get_checkbox(self.base_xpath, self.page, data_test_id="requiredCheckbox-checkbox").set_uncheck()

    def set_check_allow_display_all_column_properties(self):
        get_checkbox(self.base_xpath, self.page,
                     label=Helper.data_locale.ALLOW_DISPLAYING_ALL_COLUMN_PROPERTIES).set_check()

    def set_uncheck_allow_display_all_column_properties(self):
        get_checkbox(self.base_xpath, self.page,
                     label=Helper.data_locale.ALLOW_DISPLAYING_ALL_COLUMN_PROPERTIES).set_uncheck()

    def set_check_column_properties_are_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.COLUMNS_PROPERTIES_ARE_READ_ONLY).set_check()

    def set_uncheck_column_properties_are_read_only(self):
        get_checkbox(self.base_xpath, self.page,
                     label=Helper.data_locale.COLUMNS_PROPERTIES_ARE_READ_ONLY).set_uncheck()

    def set_check_control_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.MAKE_CONTROL_READ_ONLY).set_check()

    def set_uncheck_control_read_only(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.MAKE_CONTROL_READ_ONLY).set_uncheck()

    def set_check_hide_at_runtime(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.HIDE_CONTROL_AT_RUNTIME).set_check()

    def set_uncheck_hide_at_runtime(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.HIDE_CONTROL_AT_RUNTIME).set_uncheck()

    def select_link_input_table(self, item_value: str):
        # get_combobox(self.base_xpath, self.page, supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.LINK_TO_INPUT_TABLE)).select_item(item_value)
        get_combobox(self.base_xpath, self.page,parent_label=Helper.data_locale.LINK_TO_INPUT_TABLE).select_item(item_value)


    def select_column_type(self, item_value: str):
        # get_combobox(self.base_xpath, self.page, supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.COLUMN_TYPE)).select_item(item_value)
        get_combobox(self.base_xpath, self.page,
                     parent_label = Helper.data_locale.COLUMN_TYPE).select_item(item_value)

    def select_default_type(self, item_value: str):
        # get_combobox(self.base_xpath, self.page,
        #              supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.DEFAULT_TYPE)).select_item(item_value)
        get_combobox(self.base_xpath, self.page,
                     parent_label = Helper.data_locale.DEFAULT_TYPE).select_item(item_value)

    def set_check_allow_order_column(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.ALLOW_ORDER_COLUMN).set_check()

    def set_uncheck_allow_order_column(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.ALLOW_ORDER_COLUMN).set_uncheck()

    def set_min_columns(self, min_columns: str):
        # get_numeric_stepper(self.base_xpath, self.page,supplement_base_xpath="[.. /.. / descendant::label[contains("
        #                                                                      "text(), '{0}')]]".
        #                     format(Helper.data_locale.MINIMUM_COLUMNS)).set_value(min_columns)
        get_numeric_stepper(self.base_xpath, self.page, parent_label= Helper.data_locale.MINIMUM_COLUMNS).set_value(min_columns)

    def set_max_columns(self, max_columns: str):
        # get_numeric_stepper(self.base_xpath, self.page,
        #                     supplement_base_xpath="[.. /.. / descendant::label[contains(text(), '{0}')]]".format(
        #                         Helper.data_locale.MAXIMUM_COLUMNS)).set_value(max_columns)
        get_numeric_stepper(self.base_xpath, self.page,
                            parent_label = Helper.data_locale.MAXIMUM_COLUMNS).set_value(max_columns)

    def add_many_items(self, text: str):
        self.toolbar.click_btn_by_title(Helper.data_locale.ADD_MULTIPLE_ITEMS_TO_LIST)
        time.sleep(1)
        dlg = AddItemsDialog(self.page)
        dlg.fill_items(text)
        time.sleep(1)
        dlg.click_button_in_footer(Helper.data_locale.OK)

    def select_date_time_type(self, date_time_type: DateTimeType):
        # combobox = get_combobox(self.base_xpath, self.page,
        #                         supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #                             Helper.data_locale.QUERY_GRID_COLUMN_HEADER_TYPE))

        combobox = get_combobox(self.base_xpath, self.page,
                                parent_label = Helper.data_locale.QUERY_GRID_COLUMN_HEADER_TYPE)
        match date_time_type:
            case DateTimeType.date:
                combobox.select_item(Helper.data_locale.DATE)
            case DateTimeType.month:
                combobox.select_item(Helper.data_locale.MONTH)
            case DateTimeType.date_and_time:
                combobox.select_item(Helper.data_locale.DATE_AND_TIME)
            case DateTimeType.time:
                combobox.select_item(Helper.data_locale.TIME)

    def __get_aria_label(self, date_time_type: DateTimeType):
        aria_label = ""
        match date_time_type:
            case DateTimeType.date:
                aria_label = Helper.data_locale.SELECT_DATE
            case DateTimeType.month:
                aria_label = Helper.data_locale.SELECT_MONTH_AND_YEAR
            case DateTimeType.date_and_time:
                aria_label = Helper.data_locale.SELECT_DATE_AND_TIME
            case DateTimeType.time:
                aria_label = Helper.data_locale.SELECT_TIME
        return aria_label

    def click_default_value(self, date_time_type: DateTimeType):
        aria_label = self.__get_aria_label(date_time_type)
        get_button(self.base_xpath, self.page, aria_label=aria_label,
                   supplement_base_xpath="[../../../../descendant::label[contains(text(),'{0}')]]".format(
                       Helper.data_locale.DEFAULT_VALUE)).click_self()

    def click_minimum_value(self,date_time_type: DateTimeType):
        aria_label = self.__get_aria_label(date_time_type)
        get_button(self.base_xpath, self.page, aria_label=aria_label,
                   supplement_base_xpath="[../../../../descendant::label[contains(text(),'{0}')]]".format(
                       Helper.data_locale.MINIMUM_VALUE)).click_self()

    def click_maximum_value(self,date_time_type: DateTimeType):
        aria_label = self.__get_aria_label(date_time_type)
        get_button(self.base_xpath, self.page, aria_label=aria_label,
                   supplement_base_xpath="[../../../../descendant::label[contains(text(),'{0}')]]".format(
                       Helper.data_locale.MAXIMUM_VALUE)).click_self()

    def set_check_static_list(self):
        # get_radio_group(self.base_xpath,self.page,supplement_base_xpath="[../../descendant::label[contains(text(),'{0}')]]"
        #                 .format(Helper.data_locale.DETERMINE_WHERE_VALUES_COME_FROM)).set_check(Helper.data_locale.STATIC_LIST)
        get_radio_group(self.base_xpath, self.page,
                        parent_label = Helper.data_locale.DETERMINE_WHERE_VALUES_COME_FROM).set_check(Helper.data_locale.STATIC_LIST)

    def set_check_dynamic_list(self):
        # get_radio_group(self.base_xpath, self.page,
        #                 supplement_base_xpath="[../../descendant::label[contains(text(),'{0}')]]"
        #                 .format(Helper.data_locale.DETERMINE_WHERE_VALUES_COME_FROM)).set_check(
        #             Helper.data_locale.DYNAMIC_LIST)
        get_radio_group(self.base_xpath, self.page,
                        parent_label = Helper.data_locale.DETERMINE_WHERE_VALUES_COME_FROM).set_check(Helper.data_locale.DYNAMIC_LIST)


    def select_default_item(self,item_value:str):
        # get_combobox(self.base_xpath,self.page, supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.DEFAULT_ITEM)).select_item(item_value)

        get_combobox(self.base_xpath, self.page,
                     parent_label = Helper.data_locale.DEFAULT_ITEM).select_item(item_value)
    def set_default_item(self,text:str):
        # get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_ITEM)).fill_text(text)
        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.DEFAULT_ITEM).fill_text(text)

    def select_reference_column_selector(self,item_value):
        # get_combobox(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.REFERENCE_COLUMN_SELECTOR)).select_item(item_value)
        get_combobox(self.base_xpath, self.page,
                    parent_label = Helper.data_locale.REFERENCE_COLUMN_SELECTOR).select_item(item_value)
    def set_enter_text(self,text:str):
        # get_textarea(self.base_xpath,self.page,textarea_label=Helper.data_locale.ENTER_TEXT).fill_text(text)
        get_textarea(self.base_xpath, self.page, parent_label=Helper.data_locale.ENTER_TEXT).fill_text(text)

    def select_selector_type(self,file_or_folder:FileOrFolder):
        item_value = ""
        match file_or_folder:
            case FileOrFolder.file:
                item_value = Helper.data_locale.FILE
            case FileOrFolder.folder:
                item_value = Helper.data_locale.FOLDER
        # get_combobox(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.SELECTOR_TYPE)).select_item(item_value)
        get_combobox(self.base_xpath, self.page,
                     parent_label = Helper.data_locale.SELECTOR_TYPE).select_item(item_value)

    def set_link(self,url:str):
        # get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.LINK)).fill_text(url)
        get_text(self.base_xpath, self.page,
                 parent_label = Helper.data_locale.LINK).fill_text(url)


    def set_default_value_for_textarea(self,text:str):
        # get_textarea(self.base_xpath,self.page,textarea_label=Helper.data_locale.DEFAULT_VALUE).fill_text(text)
        get_textarea(self.base_xpath, self.page, parent_label=Helper.data_locale.DEFAULT_VALUE).fill_text(text)

    def set_placeholder_text_for_textarea(self,text:str):
        # get_textarea(self.base_xpath,self.page,textarea_label=Helper.data_locale.PLACEHOlDER_TEXT).fill_text(text)
        get_textarea(self.base_xpath, self.page, parent_label=Helper.data_locale.PLACEHOlDER_TEXT).fill_text(text)

    def set_minimum_number_of_values(self,min_number:str):
        # get_numeric_stepper(self.base_xpath,self.page,supplement_base_xpath="[.. /.. / descendant::label[contains(text(), '{0}')]]".format(
        #                         Helper.data_locale.MININUM_NUMBER_OF_VALUES)).set_value(min_number)
        get_numeric_stepper(self.base_xpath, self.page,
                            parent_label=Helper.data_locale.MININUM_NUMBER_OF_VALUES).set_value(min_number)

    def set_maximum_number_of_values(self,max_number:str):
        # get_numeric_stepper(self.base_xpath,self.page,supplement_base_xpath="[.. /.. / descendant::label[contains(text(), '{0}')]]".format(
        #                         Helper.data_locale.MAXINUM_NUMBER_OF_VALUES)).set_value(max_number)
        get_numeric_stepper(self.base_xpath, self.page,
                            parent_label = Helper.data_locale.MAXINUM_NUMBER_OF_VALUES).set_value(max_number)

    def set_check_allow_integer_values_only(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.ALLOW_INTEGER_VALUES_ONLY).set_check()

    def set_uncheck_allow_integer_values_only(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.ALLOW_INTEGER_VALUES_ONLY).set_uncheck()


    def set_default_value(self,value:str):
        # get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.DEFAULT_VALUE)).fill_text(value)
        get_text(self.base_xpath, self.page,
                 parent_label = Helper.data_locale.DEFAULT_VALUE).fill_text(value)

    def set_minimum_value(self,value:str):
        # get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.MINIMUM_VALUE)).fill_text(value)
        get_text(self.base_xpath, self.page,
                    parent_label=Helper.data_locale.MINIMUM_VALUE).fill_text(value)

    def set_maximum_value(self,value:str):
        # get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.MAXIMUM_VALUE)).fill_text(value)
        get_text(self.base_xpath, self.page,
                    parent_label=Helper.data_locale.MAXIMUM_VALUE).fill_text(value)

    def set_step_size(self,step_size:str):
        # get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.STEP_SIZE)).fill_text(step_size)
        get_text(self.base_xpath, self.page,
                 parent_label=Helper.data_locale.STEP_SIZE).fill_text(step_size)

    def select_default_radio_button(self,item_value:str):
        # get_combobox(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.DEFAULT_RADIO_BUTTON)).select_item(item_value)
        get_combobox(self.base_xpath, self.page,
                        parent_label=Helper.data_locale.DEFAULT_RADIO_BUTTON).select_item(item_value)

    def set_check_default_open(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.OPEN_BY_DEFAULt).set_check()

    def set_uncheck_default_open(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.OPEN_BY_DEFAULt).set_uncheck()

    def select_type_for_text_or_numeric_field(self,text_numeric_validation:TextNumericValidation):
        item_value = ""
        match text_numeric_validation:
            case TextNumericValidation.text:
                item_value = Helper.data_locale.TEXT
            case TextNumericValidation.numeric:
                item_value = Helper.data_locale.NUMERIC2
            case TextNumericValidation.validation:
                item_value = Helper.data_locale.VALIDATION
        # get_combobox(self.base_xpath, self.page,
        #              supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
        #              .format(Helper.data_locale.TYPE)).select_item(item_value)

        get_combobox(self.base_xpath, self.page,
                     parent_label = Helper.data_locale.TYPE).select_item(item_value)

    def set_regular_expression(self,text:str):
        # get_text(self.base_xpath, self.page,
        #          supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(
        #              Helper.data_locale.ENTER_REGULAR_EXPRESSION)).fill_text(text)
        get_text(self.base_xpath, self.page,
            parent_label=Helper.data_locale.ENTER_REGULAR_EXPRESSION).fill_text(text)


    def set_check_exclude_minimum_in_range(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.EXCLUDE_MINIMUM_IN_RANCE).set_check()

    def set_uncheck_exclude_minimum_in_range(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.EXCLUDE_MINIMUM_IN_RANCE).set_uncheck()

    def set_check_exclude_maximum_in_range(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.EXCLUDE_MAXIMUM_IN_RANCE).set_check()

    def set_uncheck_exclude_maximum_in_range(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.EXCLUDE_MAXIMUM_IN_RANCE).set_uncheck()