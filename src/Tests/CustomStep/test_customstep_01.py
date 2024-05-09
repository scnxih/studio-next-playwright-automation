"""
Author: Alice
Date: November 14, 2023
Description: This is test cases file for custom step.
"""
import time

from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_checkbox import DesignerCheckbox
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_list import DesignerList
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_numeric_stepper import DesignerNumericStepper
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_text import DesignerText
from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.conftest import *
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import *
from src.Helper.page_helper import *


def test_01_add_page(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.add_page_by_toolbar()
    custom_step.add_page_on_page("第 1 页")


def test_02_delete_page(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()
    custom_step.add_page_by_toolbar()

    custom_step.delete_page_by_toolbar("第 1 页")
    custom_step.delete_page_by_toolbar("第 2 页")
    custom_step.delete_page_by_keyboard("第 3 页")
    custom_step.delete_page_by_keyboard("第 4 页")


def test_03_show_single_page_as_tab(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.check_show_single_page_as_tab()
    custom_step.add_page_by_toolbar()
    custom_step.uncheck_show_single_page_as_tab()


def test_04_page_context_menu(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.add_page_on_page("第 1 页")
    custom_step.add_page_on_page("第 2 页")
    custom_step.add_page_on_page("第 3 页")
    custom_step.move_up_on_page("第 1 页")
    custom_step.move_up_on_page("第 2 页")
    custom_step.move_up_on_page("第 3 页")
    custom_step.move_up_on_page("第 4 页")
    custom_step.move_down_on_page("第 1 页")
    custom_step.move_down_on_page("第 2 页")
    custom_step.move_down_on_page("第 3 页")
    custom_step.move_down_on_page("第 4 页")
    custom_step.move_to_top_on_page("第 1 页")
    custom_step.move_to_top_on_page("第 2 页")
    custom_step.move_to_top_on_page("第 3 页")
    custom_step.move_to_top_on_page("第 4 页")
    custom_step.move_to_end_on_page("第 1 页")
    custom_step.move_to_end_on_page("第 2 页")
    custom_step.move_to_end_on_page("第 3 页")
    custom_step.move_to_end_on_page("第 4 页")
    custom_step.insert_page_above_on_page("第 1 页")
    custom_step.insert_page_above_on_page("第 2 页")
    custom_step.insert_page_above_on_page("第 3 页")
    custom_step.insert_page_above_on_page("第 4 页")
    custom_step.insert_page_below_on_page("第 1 页")
    custom_step.insert_page_below_on_page("第 2 页")
    custom_step.insert_page_below_on_page("第 3 页")
    custom_step.insert_page_below_on_page("第 4 页")
    custom_step.duplicate_on_page("第 1 页")
    custom_step.delete_on_page("第 1 页")
    custom_step.cut_on_page("第 2 页")
    custom_step.copy_on_page("第 3 页")
    custom_step.paste_on_page("第 3 页")


def test_05_filter(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.filter_controls(Helper.data_locale.CHECK_BOX)
    time.sleep(0.5)
    custom_step.filter_controls("选取器")
    time.sleep(0.5)
    custom_step.filter_controls("列表")
    time.sleep(0.5)
    custom_step.filter_controls("数字")
    time.sleep(0.5)
    custom_step.filter_controls("单选")
    time.sleep(0.5)
    custom_step.filter_controls("区段")
    time.sleep(0.5)
    custom_step.filter_controls("文本")
    time.sleep(0.5)
    custom_step.filter_controls("文本区域")
    time.sleep(0.5)
    custom_step.filter_controls("文本或数值字段")
    time.sleep(0.5)
    custom_step.filter_controls("输入表")
    time.sleep(0.5)
    custom_step.filter_controls("新列")
    time.sleep(0.5)
    custom_step.filter_controls("输出表")
    time.sleep(0.5)
    custom_step.clear_filter()


def test_06_insert_all_controls(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.insert_control(DesignerControlType.link)
    custom_step.insert_control(DesignerControlType.list)
    custom_step.insert_control(DesignerControlType.numeric_stepper)
    custom_step.insert_control(DesignerControlType.radio_group)
    custom_step.insert_control(DesignerControlType.section)
    custom_step.insert_control(DesignerControlType.text)
    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.insert_control(DesignerControlType.output_table)


def test_07_insert_checkbox_and_select_checkbox_move(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.checkbox)
    designer_checkbox: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 1)
    designer_checkbox.move_up()
    designer_checkbox.move_down()
    designer_checkbox.move_to_top()
    designer_checkbox.move_to_end()
    designer_checkbox.move_to_section(Helper.data_locale.NEW_SECTION)
    designer_checkbox.move_to_page(Helper.data_locale.NEW_PAGE)


def test_08_insert_checkbox_and_select_checkbox_copy_duplicate_copy_paste_cut_delete(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.checkbox)
    designer_checkbox1: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 1)
    designer_checkbox1.duplicate()
    designer_checkbox1.copy()
    designer_checkbox1.paste()
    designer_checkbox1.cut()
    designer_checkbox2: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 2)
    designer_checkbox2.delete()


def test_09_insert_all_controls_twice(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.text)
    custom_step.insert_control(DesignerControlType.list)
    custom_step.insert_control(DesignerControlType.numeric_stepper)
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.insert_control(DesignerControlType.column_selector)
    custom_step.insert_control(DesignerControlType.section)
    custom_step.insert_control(DesignerControlType.output_table)
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.insert_control(DesignerControlType.link)
    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.insert_control(DesignerControlType.color_picker)

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.text)
    custom_step.insert_control(DesignerControlType.list)
    custom_step.insert_control(DesignerControlType.numeric_stepper)
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.insert_control(DesignerControlType.column_selector)
    custom_step.insert_control(DesignerControlType.section)
    custom_step.insert_control(DesignerControlType.output_table)
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.insert_control(DesignerControlType.link)
    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.insert_control(DesignerControlType.color_picker)

    designer_checkbox1: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 1)
    designer_checkbox1.move_down()

    designer_checkbox2: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 2)
    designer_checkbox2.move_to_top()


def test_10_insert_checkbox_text_and_move_duplicate(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.text)

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.text)

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.text)

    designer_checkbox1: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 1)
    designer_checkbox1.move_down()

    designer_checkbox2: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 2)
    designer_checkbox2.move_to_top()

    designer_checkbox3: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 3)
    designer_checkbox3.duplicate()

    designer_checkbox4: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 4)
    designer_checkbox4.move_to_page(Helper.data_locale.NEW_PAGE)

    designer_text1: DesignerText = custom_step.select_control(DesignerControlType.text, 1)
    designer_text1.move_to_section(Helper.data_locale.NEW_SECTION)

    designer_text2: DesignerText = custom_step.select_control(DesignerControlType.text, 2)
    str_section = "区段标签 1"
    designer_text2.move_to_section(str_section)

    designer_text2.move_to_end()

    designer_checkbox1.move_to_section(str_section)
    designer_checkbox2.move_to_section(str_section)
    designer_checkbox3.move_to_section(str_section)

    designer_checkbox1.move_to_top()
    designer_checkbox2.move_down()
    designer_checkbox3.move_up()


def test_11_insert_list_numeric_stepper_and_move_duplicate_copy_paste(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.list)
    custom_step.insert_control(DesignerControlType.numeric_stepper)

    custom_step.insert_control(DesignerControlType.list)
    custom_step.insert_control(DesignerControlType.numeric_stepper)

    custom_step.insert_control(DesignerControlType.list)
    custom_step.insert_control(DesignerControlType.numeric_stepper)

    designer_list1: DesignerList = custom_step.select_control(DesignerControlType.list, 1)
    designer_list2: DesignerList = custom_step.select_control(DesignerControlType.list, 2)
    designer_list3: DesignerList = custom_step.select_control(DesignerControlType.list, 3)

    designer_numeric_stepper1: DesignerNumericStepper = custom_step.select_control(DesignerControlType.numeric_stepper,
                                                                                   1)
    designer_numeric_stepper2: DesignerNumericStepper = custom_step.select_control(DesignerControlType.numeric_stepper,
                                                                                   2)
    designer_numeric_stepper3: DesignerNumericStepper = custom_step.select_control(DesignerControlType.numeric_stepper,
                                                                                   3)
    designer_numeric_stepper1.move_to_top()
    designer_list3.duplicate()
    designer_numeric_stepper2.duplicate()
    designer_list1.move_down()
    designer_numeric_stepper3.move_to_page(Helper.data_locale.NEW_PAGE)
    designer_list2.move_to_top()
    designer_list1.move_down()
    designer_numeric_stepper2.move_to_section(Helper.data_locale.NEW_SECTION)
    designer_list1.move_to_page(Helper.data_locale.NEW_PAGE)


def test_12_set_properties_01(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.insert_control(DesignerControlType.column_selector)
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.insert_control(DesignerControlType.date_and_time_picker)

    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)

    custom_step.select_control(DesignerControlType.checkbox, 1)
    properties.set_label("这是复选框001")
    properties.set_check_by_default()
    #properties.set_indent("1")    
    properties.set_visibility("true")
    properties.set_enablement("true")
    time.sleep(2)
    properties.collapse_dependencies()

    custom_step.select_control(DesignerControlType.color_picker, 1)
    properties.click_select_color()
    properties.set_RGB(160, 95, 238)
    time.sleep(2)

    custom_step.select_control(DesignerControlType.input_table, 1)
    time.sleep(1)
    properties.set_label("选择输入一个表：")
    properties.set_check_required()
    properties.set_check_control_read_only()
    properties.set_check_hide_at_runtime()
    properties.set_uncheck_hide_at_runtime()
    properties.set_uncheck_control_read_only()
    properties.set_default_library("SASHELP")
    properties.set_default_table("CLASS")
    properties.set_placeholder_text("选择输入一个表：")
    time.sleep(3)

    custom_step.select_control(DesignerControlType.column_selector, 1)
    time.sleep(1)
    properties.select_link_input_table("输入表标签 1  (inputtable1)")
    time.sleep(1)
    properties.select_column_type("字符")
    time.sleep(1)
    properties.set_check_allow_order_column()
    properties.set_min_columns("1")
    properties.set_max_columns("5")
    time.sleep(3)

    properties.add_many_items("Name \n Sex \n Height")
    time.sleep(2)

    custom_step.select_control(DesignerControlType.new_column, 1)
    time.sleep(1)
    properties.set_label("新列-年级")
    properties.set_check_required()
    properties.set_default_column_name("Grade")
    properties.set_default_column_label("年级")
    properties.select_default_type(Helper.data_locale.NUMERIC)
    properties.set_default_length("8")
    properties.set_default_format("BEST12.")
    properties.set_default_informat("BEST12.")
    properties.set_uncheck_allow_display_all_column_properties()
    # properties.set_indent(2)
    # properties.set_visibility("True")    # # properties.set_enablement("True")
    time.sleep(3)

    custom_step.select_control(DesignerControlType.date_and_time_picker, 1)
    properties.select_date_time_type(DateTimeType.date)
    properties.click_default_value(DateTimeType.date)
    date_time_dialog: DateTimeDialog = get_dialog_page(page, DialogType.date_time_dialog)
    date_time_dialog.click_next_month()
    time.sleep(1)
    date_time_dialog.select_month(Month.november)
    time.sleep(1)
    date_time_dialog.click_previous_month()
    time.sleep(1)
    date_time_dialog.set_year("2025")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(3)

    properties.click_minimum_value(DateTimeType.date)
    date_time_dialog.select_month(Month.january)
    time.sleep(1)
    date_time_dialog.set_year("2020")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    properties.click_maximum_value(DateTimeType.date)
    date_time_dialog.select_month(Month.december)
    time.sleep(1)
    for i in range(24):
        date_time_dialog.click_next_month()
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(2)

    custom_step.add_page_by_toolbar()
    custom_step.insert_control(DesignerControlType.section)
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 2)
    properties.select_date_time_type(DateTimeType.month)
    time.sleep(1)
    properties.click_default_value(DateTimeType.month)
    year_month_dialog: YearMonthDialog = get_dialog_page(page, DialogType.year_month_dialog)
    year_month_dialog.set_year("2030")
    year_month_dialog.select_month(Month.february)
    time.sleep(1)
    year_month_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(1)
    properties.click_minimum_value(DateTimeType.month)
    year_month_dialog.set_year("2010")
    year_month_dialog.select_month(Month.july)
    time.sleep(1)
    year_month_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(1)
    properties.click_maximum_value(DateTimeType.month)
    year_month_dialog.set_year("2050")
    year_month_dialog.select_month(Month.october)
    time.sleep(1)
    year_month_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(1)

    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 3)
    properties.select_date_time_type(DateTimeType.date_and_time)
    time.sleep(1)
    properties.click_default_value(DateTimeType.date_and_time)
    date_time_dialog.select_month(Month.december)
    date_time_dialog.set_year("2020")
    date_time_dialog.select_hour("05")
    date_time_dialog.select_minute("10")
    date_time_dialog.select_second("22")
    time.sleep(2)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(1)
    properties.click_minimum_value(DateTimeType.date_and_time)
    date_time_dialog.set_year("2001")
    date_time_dialog.select_hour("08")
    date_time_dialog.select_minute("05")
    date_time_dialog.select_second("18")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    properties.click_maximum_value(DateTimeType.date_and_time)
    date_time_dialog.set_year("2025")
    date_time_dialog.select_hour("23")
    date_time_dialog.select_minute("00")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 4)
    properties.select_date_time_type(DateTimeType.time)
    time.sleep(1)
    properties.click_default_value(DateTimeType.time)
    date_time_dialog.select_hour("08")
    date_time_dialog.select_minute("00")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)
    properties.click_minimum_value(DateTimeType.time)
    date_time_dialog.select_hour("00")
    date_time_dialog.select_minute("00")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)
    properties.click_maximum_value(DateTimeType.time)
    date_time_dialog.select_hour("23")
    date_time_dialog.select_minute("00")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)
    time.sleep(1)


def test_13_set_properties_dropdownlist(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    #
    # custom_step.insert_control(DesignerControlType.input_table)
    # time.sleep(1)
    # custom_step.select_control(DesignerControlType.input_table,1)
    # properties.set_label("输入表:")
    #
    #
    # properties.set_default_library("SASHELP")
    # properties.set_default_table("CLASS")
    #
    # custom_step.insert_control(DesignerControlType.column_selector)
    # time.sleep(1)
    # custom_step.select_control(DesignerControlType.column_selector,1)
    # properties.select_link_input_table("输入表标签 1  (inputtable1)")
    # properties.set_check_allow_order_column()
    # properties.set_max_columns("1")
    #
    # custom_step.insert_control(DesignerControlType.drop_down_list)
    # time.sleep(1)
    # custom_step.select_control(DesignerControlType.drop_down_list,1)
    # properties.set_check_static_list()
    # properties.add_many_items("column1\ncolumn2\ncolumn3")
    # properties.select_default_item("column3")
    #
    # custom_step.insert_control(DesignerControlType.drop_down_list)
    # time.sleep(1)
    # custom_step.select_control(DesignerControlType.drop_down_list, 2)
    # properties.set_check_dynamic_list()
    # properties.select_reference_column_selector("列选择器标签 1  (columnselector1)")
    # properties.set_default_item("Alfred")
    # properties.set_placeholder_text("这是该列的下拉列表")
    #
    # custom_step.insert_control(DesignerControlType.text)
    # time.sleep(1)
    # custom_step.select_control(DesignerControlType.text,1)
    # properties.set_enter_text("测试")
    # time.sleep(3)
    #
    # custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    # custom_step.select_control(DesignerControlType.file_or_folder_selector,1)
    # properties.select_selector_type(FileOrFolder.folder)

    custom_step.insert_control(DesignerControlType.link)
    custom_step.select_control(DesignerControlType.link, 1)
    properties.set_link("https://inside.sas.com")
    time.sleep(1)

    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.select_control(DesignerControlType.textarea, 1)
    properties.set_default_value_for_textarea("这是默认值")
    properties.set_placeholder_text_for_textarea("这是占位符文本")


def insert_section(page: Page, section_number: int, label: str):
    custom_step: CustomStepPage = CustomStepPage(page)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.defocus_designer_control()
    time.sleep(0.3)
    custom_step.insert_control(DesignerControlType.section)
    time.sleep(0.5)
    custom_step.select_control(DesignerControlType.section, section_number)
    properties.set_label(label)

def insert_text(page: Page, text_number: int, text: str):
    custom_step: CustomStepPage = CustomStepPage(page)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    #properties.set_indent("1")    
    properties.set_enter_text(text)

def insert_group_text(page,  number: int, text: str):
    custom_step: CustomStepPage = CustomStepPage(page)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, number)
    properties.set_enter_text(text)
def test_14_demo_zh_CN(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.check_show_single_page_as_tab()
    properties.set_label("数据")
    section_number = 1
    text_number = 1

    insert_section(page,section_number,"输入数据控件")
    section_number += 1
    insert_text(page,text_number,"使用输入表控件选择源表。该示例需要输入表。")
    text_number += 1

    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.select_control(DesignerControlType.input_table, 1)
    #properties.set_indent("1")    
    properties.set_label("选择源表:")
    properties.set_default_library("SASHELP")
    properties.set_default_table("CLASS")


    insert_section(page, section_number, "列选择器控件")
    section_number += 1
    insert_text(page,text_number,"使用列选择器控件从链接的输入表添加列。您可以控制可以添加的列数、列的类型以及是否可以对列重新排序。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.column_selector)
    custom_step.select_control(DesignerControlType.column_selector,1)
    #properties.set_indent("1")    
    properties.set_label("选择一列:")
    properties.select_link_input_table("输入表标签 1  (inputtable1)")
    properties.select_column_type("字符")
    properties.set_max_columns("1")

    # custom_step.insert_control(DesignerControlType.column_selector)
    # custom_step.select_control(DesignerControlType.column_selector, 2)
    # #properties.set_indent("1")    
    # properties.set_label("选择多个列:")
    # properties.select_link_input_table("输入表标签 1  (inputtable1)")
    # properties.set_min_columns("1")
    # properties.set_max_columns("3")
    # properties.set_check_allow_order_column()


    insert_section(page, section_number, "新建列控件")
    section_number+=1
    insert_text(page, text_number,
                "使用新的列控件向输出表添加列。您可以定义默认列属性，并指定自定义步骤的用户是否可以编辑这些属性。若可以编辑属性，则用户点击“编辑”图标以打开“列属性”窗口并编辑任何属性。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.select_control(DesignerControlType.new_column,1)
    #properties.set_indent("1")    
    properties.set_label("添加新列:")
    properties.set_default_column_name("Grade")
    properties.set_default_column_label("年级")
    properties.select_default_type("数字")
    properties.set_default_length("8")
    properties.set_default_format("Best12.")
    properties.set_default_informat("Best12.")

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 1")
    insert_section(page,section_number,"复选框控件")
    section_number += 1
    insert_text(page,text_number,"使用复选框在两个相反的状态、操作或值之间进行选择。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox,1)
    properties.set_label("复选框")
    #properties.set_indent("1")    
    properties.set_check_by_default()

    insert_section(page,section_number,"颜色选取器控件")
    section_number+=1
    insert_text(page,text_number,"使用颜色选取器控件选择一个颜色。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.select_control(DesignerControlType.color_picker,1)
    #properties.set_indent("1")    
    properties.click_select_color()
    properties.set_RGB(160, 95, 238)

    # insert_section(page,6,"日期和时间控件")
    # insert_text(page,6, "使用日期和时间控件选择日期和时间。")

    insert_section(page,section_number,"文件或文件夹选择器控件")
    section_number+=1
    insert_text(page,text_number,"""使用文件或文件夹选择器控件指定文件或文件夹的路径。路径必须是 URL 格式。作为路径的一部分，您必须指定文件或文件夹是在“SAS 内容”中还是在 SAS 服务器上。

示例:
sascontent:/path/to/fileorfolder
sasserver:/path/to/fileorfolder""")
    text_number+=1
    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.select_control(DesignerControlType.file_or_folder_selector,1)
    #properties.set_indent("1")    
    properties.set_label("文件选择器:")
    properties.select_selector_type(FileOrFolder.file)

    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.select_control(DesignerControlType.file_or_folder_selector, 2)
    #properties.set_indent("1")    
    properties.set_label("文件夹选择器:")
    properties.select_selector_type(FileOrFolder.folder)
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 2")
    insert_section(page,section_number,"链接控件")
    section_number+=1
    insert_text(page,text_number,"使用链接控件支持自定义步骤中的超链接。为了安全起见，默认情况下禁用链接。管理员使用 SAS Environment Manager 启用该功能并为链接指定验证规则。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.link)
    custom_step.select_control(DesignerControlType.link,1)
    #properties.set_indent("1")    
    properties.set_label("SAS网站：")
    properties.set_link("https://www.sas.com")
    time.sleep(1)

    insert_section(page,section_number,"文本控件")
    section_number+=1
    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text,text_number)
    text_number+=1
    #properties.set_indent("1")    
    properties.set_enter_text("使用文本控件提供静态解释文本。")

    insert_section(page,section_number,"文本区域控件")
    section_number+=1
    insert_text(page,text_number,"使用文本区域控件输入或编辑一行或多行文本。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.select_control(DesignerControlType.textarea,1)
    #properties.set_indent("1")    
    properties.set_placeholder_text_for_textarea("这里可以输入一行或多行文字")
    time.sleep(2)

    insert_section(page,section_number,"文本字段控件")
    section_number += 1

    insert_text(page,text_number,"验证文本的示例。已应用包含 5 个字符的正则表达式。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field,1)
    #properties.set_indent("1")    
    properties.set_label("验证:")
    properties.select_type_for_text_or_numeric_field(TextNumericValidation.validation)
    properties.set_regular_expression("\w{5}")
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 3")
    insert_section(page, section_number, "日期和时间控件")
    section_number+=1
    insert_text(page, text_number,"使用日期和时间控件选择日期和时间。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker,1)
    #properties.set_indent("1")    
    properties.set_label("日期和时间:")
    properties.select_date_time_type(DateTimeType.date_and_time)
    properties.click_default_value(DateTimeType.date_and_time)
    date_time_dialog: DateTimeDialog = get_dialog_page(page, DialogType.date_time_dialog)
    date_time_dialog.set_year("2025")
    for i in range(5):
        date_time_dialog.click_next_month()
    date_time_dialog.select_hour("03")
    date_time_dialog.select_minute("10")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 2)
    #properties.set_indent("1")    
    properties.set_label("月:")
    properties.select_date_time_type(DateTimeType.month)
    properties.click_default_value(DateTimeType.month)
    year_month_dialog: YearMonthDialog = get_dialog_page(page,DialogType.year_month_dialog)
    year_month_dialog.set_year("2010")
    year_month_dialog.select_month(Month.october)
    year_month_dialog.click_button_in_footer(Helper.data_locale.OK)

    # custom_step.insert_control(DesignerControlType.date_and_time_picker)
    # custom_step.select_control(DesignerControlType.date_and_time_picker, 3)
    # #properties.set_indent("1")    
    # properties.set_label("时间:")
    # properties.select_date_time_type(DateTimeType.time)
    # properties.click_default_value(DateTimeType.time)
    # date_time_dialog.select_hour("03")
    # date_time_dialog.select_minute("08")
    # date_time_dialog.select_second("00")
    # date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    insert_section(page,section_number,"下拉列表控件")
    section_number+=1
    insert_text(page,text_number,"当您想要显示包含选项列表的菜单时，使用下拉列表控件。选项列表可以是项的静态列表，也可以是项的动态列表。")
    text_number+=1
    insert_text(page,text_number,
                "使用静态下拉列表用一组预定义值填充列表。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list,1)
    #properties.set_indent("1")    
    properties.set_label("静态下拉列表:")
    properties.add_many_items("Judy\nWilliam\nHenry")
    properties.select_default_item("Henry")


    insert_text(page,text_number,"使用动态下拉列表用来自链接列选择器的非重复值填充列表中的项。例如，以下下拉列表填充了来自“数据”页面上第一个列选择器中所选列的非重复值。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list,2)
    #properties.set_indent("1")    
    properties.set_label("动态下拉列表:")
    properties.set_check_dynamic_list()
    properties.select_reference_column_selector("列选择器标签 1  (columnselector1)")
    properties.set_default_item("Carol")
    time.sleep(2)


    custom_step.add_page_by_toolbar()
    properties.set_label("控件 4")
    insert_section(page,section_number,"列表控件")
    section_number +=1
    insert_text(page,text_number,"当您想要允许从项列表中选择多个选项时，使用列表控件。选项列表可以是项的静态列表，也可以是项的动态列表。")
    text_number+=1
    insert_text(page, text_number,
                "使用静态列表用一组预定义值填充列表。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.list)
    custom_step.select_control(DesignerControlType.list,1)
    #properties.set_indent("1")    
    properties.add_many_items("小学\n初中\n高中\n大学")
    properties.set_minimum_number_of_values("1")
    properties.set_maximum_number_of_values("4")
    insert_text(page,text_number,"使用动态列表用来自链接列选择器的非重复值填充列表中的项。例如，以下列表填充了来自“数据”页面上第一个列选择器中所选列的非重复值。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.list)
    custom_step.select_control(DesignerControlType.list,2)
    #properties.set_indent("1")    
    properties.set_check_dynamic_list()
    properties.select_reference_column_selector("列选择器标签 1  (columnselector1)")
    properties.set_minimum_number_of_values("1")
    properties.set_maximum_number_of_values("5")


    custom_step.add_page_by_toolbar()
    properties.set_label("控件 5")
    insert_section(page,section_number,"数值字段控件")
    section_number += 1
    insert_text(page,text_number,"使用数值字段输入数值。最小值为 0，最大值为 100。当字段为空时，占位符文本向用户提供说明。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field,2)
    #properties.set_indent("1")    
    properties.set_label("数值字段:")
    properties.select_type_for_text_or_numeric_field(TextNumericValidation.numeric)
    properties.set_check_allow_integer_values_only()
    properties.set_default_value("5")
    properties.set_minimum_value("0")
    properties.set_maximum_value("100")
    properties.set_placeholder_text("输入 0 和 100 之间的数值。")
    properties.set_check_exclude_minimum_in_range()
    properties.set_check_exclude_maximum_in_range()


    insert_text(page,text_number,"使用数字步进器的向上和向下箭头以指定的增量变换数字。默认值为 10。最小值为 0，最大值为 20。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.numeric_stepper)
    custom_step.select_control(DesignerControlType.numeric_stepper,1)
    #properties.set_indent("1")    
    properties.set_label("数字步进器:")
    properties.set_check_allow_integer_values_only()
    properties.set_default_value("10")
    properties.set_minimum_value("0")
    properties.set_maximum_value("20")
    properties.set_step_size("2")


    insert_section(page,section_number,"单选按钮组控件")
    section_number += 1
    insert_text(page,text_number,"使用单选按钮组控件将互斥选项列表显示为单选按钮。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.radio_group)
    custom_step.select_control(DesignerControlType.radio_group,1)
    #properties.set_indent("1")    
    properties.set_label("单选按钮组:")
    properties.add_many_items("单选按钮 2")
    properties.select_default_radio_button("单选按钮 2")
    time.sleep(1)



    custom_step.add_page_by_toolbar()
    properties.set_label("依赖关系")


    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    properties.set_enter_text("依赖关系使您能够根据另一个提示的值显示或隐藏提示。")
    text_number += 1

    insert_section(page,section_number,"复选框示例")
    section_number+=1
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox,2)
    #properties.set_indent("1")    
    properties.set_label("选中框以显示文本字段")
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field,3)
    #properties.set_indent("1")    
    properties.set_label("文本字段:")
    properties.set_placeholder_text("选中复选框时显示")
    properties.set_visibility("$checkbox2")
    time.sleep(1)
    
    insert_section(page,section_number,"下拉列表示例")
    section_number+=1
    insert_text(page,text_number,"从下拉列表中选择的类别决定了出现的复选框。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list,3)
    #properties.set_indent("1")    
    properties.set_label("选择水果类别:")
    properties.add_many_items("浆果类\n瓜类")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox,3)
    #properties.set_indent("1")    
    properties.set_label("草莓")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"浆果类\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 4)
    #properties.set_indent("1")    
    properties.set_label("蓝莓")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"浆果类\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 5)
    #properties.set_indent("1")    
    properties.set_label("西瓜")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"瓜类\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 6)
    #properties.set_indent("1")    
    properties.set_label("哈密瓜")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"瓜类\"]")


    custom_step.add_page_by_toolbar()
    properties.set_label("输出")
    insert_section(page,section_number,"输出数据控件")
    section_number+=1
    insert_text(page,text_number,"使用输出表控件指定输出表。在流中，输出表控件表示为输出端口。")
    text_number+=1
    custom_step.insert_control(DesignerControlType.output_table)
    custom_step.select_control(DesignerControlType.output_table,1)
    #properties.set_indent("1")    
    properties.set_label("输出数据控件:")
    properties.set_check_required()
    properties.set_placeholder_text("请选择输出数据")
    time.sleep(1)





    
    



    







    
                               

