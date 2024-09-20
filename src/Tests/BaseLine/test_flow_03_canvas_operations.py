from src.Helper.page_helper import PageHelper
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.sort_pane import SortPane
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import *
from src.Utilities.enums import *
import time


def test_01_flow_canvas_select_node_table_file_branchrows_calculatecolumns(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.file)
    flow.add_node(FlowNodeType.branch_rows)
    flow.add_node(FlowNodeType.calculate_columns)
    flow.add_node(FlowNodeType.sas_program)
    flow.add_node(FlowNodeType.execute_decisions)
    flow.add_node(FlowNodeType.export)
    flow.add_node(FlowNodeType.filter_rows)
    flow.add_node(FlowNodeType.implement_scd)
    flow.add_node(FlowNodeType.import_data)
    flow.add_node(FlowNodeType.insert_rows)
    flow.add_node(FlowNodeType.load_table)
    flow.add_node(FlowNodeType.manage_columns)
    flow.add_node(FlowNodeType.merge_table)
    flow.add_node(FlowNodeType.python_program)
    flow.add_node(FlowNodeType.query)
    flow.add_node(FlowNodeType.sort)
    flow.add_node(FlowNodeType.union_rows)
    flow.add_node(FlowNodeType.notes)

    # Take a screenshot after all nodes have been added into canvas
    time.sleep(1)
    WholePage(page).screenshot_self("whole_page_flow_canvas_with_nodes",
                                    mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                    mask_color="#000000")

    CenterPage(page).screenshot_self("center_page_flow_canvas_with_nodes",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    # MODIFIED
    # Changed waiting and screenshot order to eliminte diffs caused by the undo/redo icon status
    # <<< Modified by Jacky(ID: jawang) on Sept.10th, 2024
    select_node_in_flow_canvas(page, Helper.data_locale.TABLE)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_table",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    select_node_in_flow_canvas(page, Helper.data_locale.FILE)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_file",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    select_node_in_flow_canvas(page, Helper.data_locale.BRANCH_ROWS)
    time.sleep(1)
    # CenterPage(page).screenshot_self("selected_branch_rows")
    CenterPage(page).screenshot_self("selected_branch_rows",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    select_node_in_flow_canvas(page, Helper.data_locale.CALCULATE_COLUMNS)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_calculate_columns",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    # Modified by Jacky(ID: jawang) on Sept.10th, 2024 >>>


def test_02_flow_canvas_select_node_sasprogram_executedecisions_export_filter_rows(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.add_node(FlowNodeType.execute_decisions)
    flow.add_node(FlowNodeType.export)
    flow.add_node(FlowNodeType.filter_rows)

    # Take a screenshot after all nodes have been added into canvas
    time.sleep(1)

    WholePage(page).screenshot_self("whole_page_flow_canvas_with_nodes",
                                    mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                    mask_color="#000000")

    CenterPage(page).screenshot_self("center_page_flow_canvas_with_nodes",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    # Screenshot: Flow canvas + Details pane below
    select_node_in_flow_canvas(page, Helper.data_locale.SAS_PROGRAM)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_sas_program",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    select_node_in_flow_canvas(page, Helper.data_locale.EXECUTE_DECISIONS)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_execute_decisions",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    select_node_in_flow_canvas(page, Helper.data_locale.EXPORT)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_export",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    select_node_in_flow_canvas(page, Helper.data_locale.FILTER_ROWS)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_filter_rows",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")


def test_03_flow_canvas_link_nodes_toolbar_operations(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.query)
    flow.add_node(FlowNodeType.filter_rows)
    flow.add_node(FlowNodeType.manage_columns)
    flow.add_node(FlowNodeType.sort)
    flow.add_node(FlowNodeType.export)
    time.sleep(1)

    # Take a screenshot after all nodes have been added into canvas
    time.sleep(1)
    WholePage(page).screenshot_self("whole_page_flow_canvas_with_nodes")

    CenterPage(page).screenshot_self("center_page_flow_canvas_with_nodes")

    flow.link_two_nodes_in_flow(Helper.data_locale.TABLE, Helper.data_locale.QUERY)
    # Screenshot: Flow canvas + Details pane below
    time.sleep(1)
    CenterPage(page).screenshot_self("linked_table_and_query",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.link_two_nodes_in_flow(Helper.data_locale.QUERY, Helper.data_locale.FILTER_ROWS)
    # Screenshot: Flow canvas + Details pane below
    time.sleep(1)
    CenterPage(page).screenshot_self("linked_query_and_filter_rows",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.link_two_nodes_in_flow(Helper.data_locale.FILTER_ROWS, Helper.data_locale.MANAGE_COLUMNS)
    # Screenshot: Flow canvas + Details pane below
    time.sleep(1)
    CenterPage(page).screenshot_self("linked_filter_rows_and_manage_columns",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.link_two_nodes_in_flow(Helper.data_locale.MANAGE_COLUMNS, Helper.data_locale.SORT)
    # Screenshot: Flow canvas + Details pane below
    time.sleep(1)
    CenterPage(page).screenshot_self("linked_manage_columns_and_sort",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.link_two_nodes_in_flow(Helper.data_locale.SORT, Helper.data_locale.EXPORT)
    # Screenshot: Flow canvas + Details pane below
    time.sleep(1)
    CenterPage(page).screenshot_self("linked_sort_and_export",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.arrange_nodes()
    time.sleep(2)
    CenterPage(page).screenshot_self("arrange_nodes",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    # flow._open_context_menu_for_the_node_in_flow(Helper.data_locale.TABLE)
    # time.sleep(1)
    #
    # # Original
    # # CenterPage(page).screenshot_self("table_node_context_menu")
    # # Mask the 'Preview Code' button
    # # CenterPage(page).screenshot_self("table_node_context_menu",
    # #                                  mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
    # #                                  mask_color="#000000")
    #
    # page.get_by_text(Helper.data_locale.COPY).click()

    flow.click_copy_in_context_menu_on_node(Helper.data_locale.TABLE)
    time.sleep(1)

    # flow._open_context_menu_on_canvas_in_flow()
    # time.sleep(1)
    # 
    # page.get_by_text(Helper.data_locale.PASTE).click()
    flow.click_paste_in_context_menu_on_canvas()
    time.sleep(1)
    CenterPage(page).screenshot_self("paste_node_in_flow_canvas",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.view_expand_all_ports()
    time.sleep(2)
    CenterPage(page).screenshot_self("expanded_all_ports",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.view_collapse_all_ports()
    time.sleep(2)

    # Mask 'Preview Code' button to eliminate noises
    # //button[@data-testid="flowtoolbar-previewCodeButton"]
    CenterPage(page).screenshot_self("collapsed_all_ports",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.show_over_view_map()
    time.sleep(2)
    CenterPage(page).screenshot_self("show_over_view_map",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.hide_over_view_map()
    time.sleep(2)
    CenterPage(page).screenshot_self("hide_over_view_map",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    flow.saveas(Helper.public_folder_path, "test_flow.sas", True, True)

    flow.copy_step()

    flow.paste_step()
    time.sleep(2)
    CenterPage(page).screenshot_self("flow_paste_step",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.cut_step()
    time.sleep(2)
    CenterPage(page).screenshot_self("flow_cut_step",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.undo()
    time.sleep(2)
    CenterPage(page).screenshot_self("hide_over_view_map",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.redo()
    time.sleep(2)
    CenterPage(page).screenshot_self("hide_over_view_map",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    flow.schedule_as_job()
    flow.add_to_my_favorites()

    flow.apply_detail_layout_horizontal()
    time.sleep(1)
    flow.apply_detail_layout_vertical()
    time.sleep(1)
    flow.apply_main_layout_vertical()
    time.sleep(1)
    flow.apply_main_layout_standard()
    time.sleep(1)
    flow.apply_main_layout_horizontal()
    time.sleep(1)
    flow.reload()
    time.sleep(1)


def test_04_details_pane_table(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)

    # Take a screenshot after all nodes have been added into canvas
    time.sleep(1)
    WholePage(page).screenshot_self("whole_page_flow_canvas_with_nodes")
    CenterPage(page).screenshot_self("center_page_flow_canvas_with_nodes")

    flow.apply_detail_layout_vertical()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    time.sleep(1)
    CenterPage(page).screenshot_self("selected_table",
                                     mask=[flow.toolbar.btn_by_title(Helper.data_locale.PREVIEW_CODE)],
                                     mask_color="#000000")

    table = TablePane(page)
    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name("class表")
    time.sleep(1)
    table.set_node_description("这是sashelp.class表。")
    time.sleep(1)
    table.set_notes("这是sashelp.class表的注释信息。")
    time.sleep(1)
    table.preview_data()
    time.sleep(1)


def test_06_sasprogram_table_sort_zh_CN(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)

    # flow.add_node(FlowNodeType.sort)
    # flow.apply_detail_layout_vertical()

    # flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)

    # time.sleep(3)
    # time.sleep(1)
    select_node_in_flow_canvas(page, Helper.data_locale.SAS_PROGRAM)

    # time.sleep(1)
    sasprogram_pane = SASProgramPane(page)
    str = """
/***************************************************
This is demo for flow.
First, create data set class in work library in sas program step.
Then user will sort this table work.class by age descending.
Next sorted table will be generated.
***************************************************/

data cars;
set sashelp.cars;
run;
"""
    sasprogram_pane.type_into_text_area(str)
    # time.sleep(1)
    sasprogram_pane.fold_all_regions()
    time.sleep(1)
    sasprogram_pane.unfold_all_regions()
    time.sleep(1)
    sasprogram_pane.pop_find_widget()
    sasprogram_pane.find("cars", False, False)
    time.sleep(1)
    sasprogram_pane.replace_all("cars", "class", False, False, False)
    time.sleep(2)
    sasprogram_pane.set_node_name("Create class")
    # time.sleep(1)
    sasprogram_pane.set_notes("This is SAS program notes for expo.")
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    # time.sleep(1)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    # time.sleep(1)
    table_pane.set_table("CLASS")
    # time.sleep(1)
    table_pane.set_node_name("CLASS")
    # time.sleep(1)
    table_pane.set_node_description("This is class table created by SAS program.")
    # time.sleep(1)
    flow.link_two_nodes_in_flow("Create class", "CLASS")
    # time.sleep(1)
    flow.arrange_nodes()

    flow.run(True)
    flow.select_node_in_flow_canvas("CLASS")
    # table_pane.click_tab("预览数据")
    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)
    time.sleep(3)
    flow.add_node(FlowNodeType.sort)
    # time.sleep(1)
    flow.arrange_nodes()
    # flow.link_two_nodes_in_flow("CLASS","排序")
    flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)
    # time.sleep(1)
    flow.arrange_nodes()
    # flow.select_node_in_flow_canvas("排序")
    flow.select_node_in_flow_canvas(Helper.data_locale.SORT)

    sort_pane = SortPane(page)

    list1 = ["Class", "Name"]
    sort_pane.add_sort(list1, SortWay.descending)
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    # flow.select_node_in_flow_canvas("表")
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table_pane.set_node_name("SORTED")
    table_pane.set_library("WORK")
    table_pane.set_table("SORTED")
    table_pane.refresh_table()
    # flow.link_two_nodes_in_flow("排序","SORTED")
    flow.link_two_nodes_in_flow(Helper.data_locale.SORT, "SORTED")
    # time.sleep(1)
    flow.arrange_nodes()
    # time.sleep(1)
    # flow.run(False)
    time.sleep(3)
    flow.select_node_in_flow_canvas("SORTED")
    time.sleep(2)
    # table_pane.click_tab("预览数据")
    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)
    time.sleep(2)

    # PageHelper.show_accordion(page,AccordionType.libraries)
    # lib = LibraryPage(page)
    # lib.open_table("WORK","SORTED")
    # time.sleep(2)


def test_07_sasprogram_table_sort_en_US(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)

    # flow.add_node(FlowNodeType.sort)
    # flow.apply_detail_layout_vertical()
    time.sleep(3)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)

    # time.sleep(1)
    sasprogram_pane = SASProgramPane(page)
    str = """
/***************************************************
This is demo for flow.
First, create data set class in work library in sas program step.
Then user will sort this table work.class by age descending.
Next sorted table will be generated.
***************************************************/

data cars;
set sashelp.cars;
run;
"""
    sasprogram_pane.type_into_text_area(str)
    # time.sleep(1)
    sasprogram_pane.fold_all_regions()
    time.sleep(1)
    sasprogram_pane.unfold_all_regions()
    time.sleep(1)
    sasprogram_pane.pop_find_widget()
    sasprogram_pane.find("cars", False, False)
    time.sleep(1)
    sasprogram_pane.replace_all("cars", "class", False, False, False)
    time.sleep(2)
    sasprogram_pane.set_node_name("Create class")
    # time.sleep(1)
    sasprogram_pane.set_notes("This is SAS program notes for expo.")
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    # time.sleep(1)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    # time.sleep(1)
    table_pane.set_table("CLASS")
    # time.sleep(1)
    table_pane.set_node_name("CLASS")
    # time.sleep(1)
    table_pane.set_node_description("This is class table created by SAS program.")
    # time.sleep(1)
    flow.link_two_nodes_in_flow("Create class", "CLASS")
    # time.sleep(1)
    flow.arrange_nodes()

    flow.run(True)
    flow.select_node_in_flow_canvas("CLASS")
    table_pane.click_tab("预览数据")
    # table_pane.click_tab("Preview Data")
    time.sleep(3)
    flow.add_node(FlowNodeType.sort)
    # time.sleep(1)
    flow.arrange_nodes()
    flow.link_two_nodes_in_flow("CLASS", "排序")
    # flow.link_two_nodes_in_flow("CLASS", "Sort")
    # time.sleep(1)
    flow.arrange_nodes()
    flow.select_node_in_flow_canvas("排序")
    # flow.select_node_in_flow_canvas("Sort")

    sort_pane = SortPane(page)

    list1 = ["Class", "Name"]
    sort_pane.add_sort(list1, SortWay.descending)
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas("表")
    # flow.select_node_in_flow_canvas("Table")

    table_pane.set_node_name("SORTED")
    table_pane.set_library("WORK")
    table_pane.set_table("SORTED")
    table_pane.refresh_table()
    flow.link_two_nodes_in_flow("排序", "SORTED")
    # flow.link_two_nodes_in_flow("Sort", "SORTED")
    # time.sleep(1)
    flow.arrange_nodes()
    # time.sleep(1)
    # flow.run(False)
    time.sleep(3)
    flow.select_node_in_flow_canvas("SORTED")
    time.sleep(2)
    table_pane.click_tab("预览数据")
    # table_pane.click_tab("Preview Data")
    time.sleep(2)

    # PageHelper.show_accordion(page,AccordionType.libraries)
    # lib = LibraryPage(page)
    # lib.open_table("WORK","SORTED")
    # time.sleep(2)
