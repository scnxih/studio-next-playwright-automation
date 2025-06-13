"""
Author: Alice
Date: November 14, 2023
Description: This is test cases file for custom step.
"""
import time

from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_checkbox import DesignerCheckbox
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_list import DesignerList
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_numeric_stepper import DesignerNumericStepper
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_text import DesignerText
from src.conftest import *
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import *


def test_init(page, init):
    PageHelper.init_environments(page)


def test_01_add_page(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.wait_for_page_load()

    custom_step.add_page_by_toolbar()
    custom_step.add_page_on_page("第 1 页")
    custom_step.screenshot_self("overwrite_vanilla")


def test_02_delete_page(page, init):
    whole = WholePage(page)
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.add_page_by_toolbar()
    # time.sleep(1)
    whole.screenshot_self("page1")
    custom_step.prt_scn("page1")

    custom_step.add_page_by_toolbar()
    # time.sleep(1)

    custom_step.add_page_by_toolbar()
    # time.sleep(1)

    custom_step.add_page_by_toolbar()
    # time.sleep(1)

    whole.screenshot_self("page2")
    custom_step.prt_scn("page2")

    custom_step.delete_page_by_toolbar("第 1 页")
    # time.sleep(1)
    whole.screenshot_self("delete_page_1")
    custom_step.prt_scn("delete_page_1")

    custom_step.delete_page_by_toolbar("第 2 页")
    # time.sleep(1)

    custom_step.delete_page_by_keyboard("第 3 页")
    # time.sleep(1)

    custom_step.delete_page_by_keyboard("第 4 页")
    # time.sleep(1)
    whole.screenshot_self("delete_page_2")
    custom_step.prt_scn("delete_page_2")


def test_03_show_single_page_as_tab(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    whole = WholePage(page)

    custom_step.check_show_single_page_as_tab()

    whole.screenshot_self("single")
    custom_step.prt_scn("single")

    # time.sleep(1)
    custom_step.add_page_by_toolbar()
    # time.sleep(1)

    # Original
    # whole.screenshot_self("add_page")
    # Masked
    whole.screenshot_self("add_page",
                          mask=[custom_step.toolbar.btn_by_title(Helper.data_locale.SAVE_AS),
                                custom_step.toolbar.btn_by_title(Helper.data_locale.SAVE)],
                          mask_color="#000000")
    custom_step.prt_scn("add_page")
    custom_step.uncheck_show_single_page_as_tab()
    # time.sleep(1)

    # Original
    # whole.screenshot_self("uncheck_single")
    whole.screenshot_self("uncheck_single",
                          mask=[custom_step.toolbar.btn_by_title(Helper.data_locale.SAVE_AS),
                                custom_step.toolbar.btn_by_title(Helper.data_locale.SAVE)],
                          mask_color="#000000")
    custom_step.prt_scn("uncheck_single")


def test_04_page_context_menu(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    whole = WholePage(page)

    custom_step.wait_for_page_load()
    custom_step.add_page_on_page("第 1 页")
    # time.sleep(1)

    whole.screenshot_self("01")
    custom_step.prt_scn("01")

    custom_step.add_page_on_page("第 2 页")

    custom_step.add_page_on_page("第 3 页")

    # custom_step.move_up_on_page("第 1 页")

    custom_step.move_up_on_page("第 2 页")

    custom_step.move_up_on_page("第 3 页")

    custom_step.move_up_on_page("第 4 页")

    # custom_step.move_down_on_page("第 1 页")

    custom_step.move_down_on_page("第 2 页")

    custom_step.move_down_on_page("第 3 页")

    custom_step.move_down_on_page("第 4 页")

    custom_step.move_to_top_on_page("第 1 页")

    custom_step.move_to_top_on_page("第 2 页")

    custom_step.move_to_top_on_page("第 3 页")

    custom_step.move_to_top_on_page("第 4 页")

    # custom_step.move_to_end_on_page("第 1 页")

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
    # time.sleep(1)
    custom_step.wait_for_page_load()

    # Mask 'Save As' button to eliminate noise
    # //button[@data-testid="customStepViewPane-toolbar-saveAsButton"]
    whole.screenshot_self("02",
                          mask=[custom_step.toolbar.btn_by_title(Helper.data_locale.SAVE_AS),
                                custom_step.toolbar.btn_by_title(Helper.data_locale.SAVE)],
                          mask_color="#000000")
    custom_step.prt_scn("02")


def test_05_filter(page, init):
    whole = WholePage(page)
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.filter_controls(Helper.data_locale.CHECK_BOX)
    # time.sleep(0.5)
    custom_step.filter_controls("选取器")
    # time.sleep(1)
    whole.screenshot_self("selector")
    custom_step.prt_scn("selector")

    # time.sleep(0.5)
    custom_step.filter_controls("列表")

    # time.sleep(0.5)
    custom_step.filter_controls("数字")

    # time.sleep(0.5)
    custom_step.filter_controls("单选")

    # time.sleep(0.5)
    custom_step.filter_controls("区段")

    # time.sleep(0.5)
    custom_step.filter_controls("文本")
    # time.sleep(1)
    whole.screenshot_self("Text")
    custom_step.prt_scn("Text")

    # time.sleep(0.5)
    custom_step.filter_controls("文本区域")
    # time.sleep(1)
    whole.screenshot_self("Text_Area")
    custom_step.prt_scn("Text_Area")

    # time.sleep(0.5)
    custom_step.filter_controls("文本或数值字段")
    # time.sleep(1)
    whole.screenshot_self("Field")
    custom_step.prt_scn("Field")

    # time.sleep(0.5)
    custom_step.filter_controls("输入表")

    # time.sleep(0.5)
    custom_step.filter_controls("新列")

    # time.sleep(0.5)
    custom_step.filter_controls("输出表")
    # time.sleep(1)
    whole.screenshot_self("Output_Table")
    custom_step.prt_scn("Output_Table")

    # time.sleep(0.5)
    custom_step.clear_filter()


def test_06_insert_all_controls(page, init):
    whole = WholePage(page)
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.color_picker)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.drop_down_list)
    # time.sleep(1)

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
    # time.sleep(1)
    whole.screenshot_self("01")
    custom_step.prt_scn("01")


def test_07_insert_checkbox_and_select_checkbox_move(page, init):
    whole = WholePage(page)
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.checkbox)

    custom_step.insert_control(DesignerControlType.checkbox)

    designer_checkbox: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 1)
    designer_checkbox.move_up()

    designer_checkbox.move_down()

    designer_checkbox.move_to_top()

    designer_checkbox.move_to_end()

    designer_checkbox.move_to_section(Helper.data_locale.NEW_SECTION)
    # time.sleep(1)
    custom_step.wait_for_page_load()

    designer_checkbox.move_to_page(Helper.data_locale.NEW_PAGE)
    # time.sleep(1)
    custom_step.wait_for_page_load()

    whole.screenshot_self("01")
    custom_step.prt_scn("01")


def test_08_insert_checkbox_and_select_checkbox_copy_duplicate_copy_paste_cut_delete(page, init):
    whole = WholePage(page)
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.checkbox)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.checkbox)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.checkbox)
    # time.sleep(1)

    designer_checkbox1: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 1)

    designer_checkbox1.duplicate()
    custom_step.wait_for_page_load()

    designer_checkbox1.copy()
    custom_step.wait_for_page_load()

    designer_checkbox1.paste()
    custom_step.wait_for_page_load()

    designer_checkbox1.cut()
    custom_step.wait_for_page_load()
    # time.sleep(1)

    designer_checkbox2: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 2)
    designer_checkbox2.delete()
    custom_step.wait_for_page_load()
    # time.sleep(1)
    whole.screenshot_self("01")
    custom_step.prt_scn("01")


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
    custom_step.wait_for_page_load()

    designer_checkbox2: DesignerCheckbox = custom_step.select_control(DesignerControlType.checkbox, 2)
    designer_checkbox2.move_to_top()
    custom_step.wait_for_page_load()


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

    # Original
    # designer_text2.move_to_section(str_section)
    # designer_text2.move_to_end()

    designer_text1.move_to_section(Helper.data_locale.NEW_SECTION)
    designer_text1.move_to_end()

    designer_checkbox1.move_to_section(str_section)
    designer_checkbox2.move_to_section("区段标签 2")
    designer_checkbox3.move_to_section(Helper.data_locale.NEW_SECTION)

    designer_checkbox1.move_to_top()
    designer_checkbox2.move_down()
    designer_checkbox3.move_up()


def test_11_insert_list_numeric_stepper_and_move_duplicate_copy_paste(page, init):
    whole = WholePage(page)
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    custom_step.insert_control(DesignerControlType.list)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.numeric_stepper)
    # time.sleep(1)

    custom_step.insert_control(DesignerControlType.list)
    # time.sleep(1)

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
    custom_step.wait_for_page_load()

    designer_list3.duplicate()
    custom_step.wait_for_page_load()

    designer_numeric_stepper2.duplicate()
    custom_step.wait_for_page_load()

    designer_list1.move_down()
    custom_step.wait_for_page_load()

    designer_numeric_stepper3.move_to_page(Helper.data_locale.NEW_PAGE)
    custom_step.wait_for_page_load()

    designer_list2.move_to_top()
    custom_step.wait_for_page_load()

    designer_list1.move_down()
    # time.sleep(1)
    custom_step.wait_for_page_load()

    designer_numeric_stepper2.move_to_section(Helper.data_locale.NEW_SECTION)
    # time.sleep(1)
    custom_step.wait_for_page_load()

    designer_numeric_stepper2.move_to_page(Helper.data_locale.NEW_PAGE)
    # time.sleep(1)
    custom_step.wait_for_page_load()

    whole.screenshot_self("01")
    custom_step.prt_scn("01")
