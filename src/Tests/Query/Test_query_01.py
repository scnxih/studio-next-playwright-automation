from src.Pages.StudioNext.Center.Query.query_page import *
from src.Pages.StudioNext.Dialog.select_a_table_dialog import *


def test_01_query(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_query)
    query = QueryPage(page)
    select_table = SelectTableDialog(page)
    query.click_add_table()
    select_table.fill_input_table_name("CLASS")
    select_table.click_button_in_footer("选择")
    time.sleep(10)
    query.dbclick_t1()
    query.treegrid.click_btn_in_a_row(name_text="Sex", test_id=TestID.QUERY_SELECT_COLUMNS_BTN_FORMAT)
    time.sleep(2)
    query.treegrid.click_btn_in_a_row(row_index=1, test_id=TestID.QUERY_SELECT_COLUMNS_BTN_INFORMAT)
    time.sleep(2)
    query.treegrid.clear_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_NAME, row_index=0)
    query.treegrid.fill_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_NAME, "名字", row_index=0)
    query.treegrid.fill_input_in_a_row(TestID.QUERY_SELECT_COLUMNS_INPUT_LABEL, "标签", name_text="Sex")
    query.click_tab("排序")
    query.dbclick_t1()
    time.sleep(2)
    query.treegrid.select_item_combo_in_a_row("降序", row_index=0)
    query.click_tab("过滤")
    query.dbclick_t1()
    time.sleep(2)
    query.treegrid.select_item_combo_in_a_row("OR", name_text="Sex")
