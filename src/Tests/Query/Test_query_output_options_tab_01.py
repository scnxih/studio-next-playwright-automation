import time

from src.Pages.StudioNext.Center.Query.query_page import *
from src.Pages.StudioNext.Center.Query.output_options_tab import *


def test_01_output_options(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_query)
    query = QueryPage(page)
    query.click_tab("输出选项")
    output_options = OutputOptions(page)
    output_options.collapse_section_output_options()
    time.sleep(1)
    output_options.expand_section_output_options()
    time.sleep(1)
    output_options.select_radio_fedsql()
    time.sleep(1)
    output_options.select_radio_sql()
    time.sleep(1)
    output_options.select_item_in_combo_output_type(Helper.data_locale.REPORT)
    time.sleep(1)
    output_options.select_item_in_combo_output_type(Helper.data_locale.TABLE)
    time.sleep(1)


def test_02_output_options(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_query)
    query = QueryPage(page)
    query.click_tab("输出选项")
    output_options = OutputOptions(page)
    output_options.input_library("sashelp")
    time.sleep(1)
    output_options.input_table("class")
    time.sleep(1)
    output_options.set_output_table_by_btn_browse("work", "test")
    time.sleep(1)


def test_03_output_options(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_query)
    query = QueryPage(page)
    query.click_tab("输出选项")
    output_options = OutputOptions(page)
    output_options.collapse_section_passthrough()
    time.sleep(1)
    output_options.expand_section_passthrough()
    time.sleep(1)
    output_options.fill_textarea("sashelp")
    output_options.get_text_textarea()
    output_options.clear_textarea()


def test_04_output_options(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_query)
    query = QueryPage(page)
    query.click_tab("输出选项")
    output_options = OutputOptions(page)
    output_options.check_checkbox_outobs()
    time.sleep(1)
    output_options.input_numstepper_outobs(3)
    time.sleep(1)
    output_options.decrease_numstepper_outobs(times=4)
    time.sleep(2)
    output_options.increase_numstepper_outobs(times=3)
    time.sleep(2)
    output_options.decrease_numstepper_outobs()
    time.sleep(2)
    output_options.increase_numstepper_outobs()
    time.sleep(3)
    output_options.clear_numstepper_outobs()
    time.sleep(2)
