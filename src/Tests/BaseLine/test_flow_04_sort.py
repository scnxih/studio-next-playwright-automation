from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.sort_pane import SortPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import *
from src.Helper.page_helper import *


def test_init(page, init):
    PageHelper.init_environments(page)


def test_01_sasprogram_table_sort_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    # time.sleep(0.5)
    flow.wait_for_page_load()

    flow.add_node(FlowNodeType.sas_program)
    flow.wait_for_page_load()

    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)

    sasprogram_pane = SASProgramPane(page)
    str = """
/***************************************************
This is demo for flow.
First, create data set class in work library in sas program step.
Then user will sort this table work.class by name descending.
Next sorted table will be generated.
***************************************************/

data cars;
set sashelp.cars;
run;
"""

    flow.wait_for_page_load()

    sasprogram_pane.type_into_text_area(str)

    sasprogram_pane.fold_all_regions()
    flow.wait_for_page_load()

    sasprogram_pane.unfold_all_regions()
    flow.wait_for_page_load()

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="03_after_unfold",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')

    flow.prt_scn("03_after_unfold")

    sasprogram_pane.pop_find_widget()
    sasprogram_pane.find("cars", False, False)
    flow.wait_for_page_load()

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="04_after_find",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')
    flow.prt_scn("04_after_find")

    sasprogram_pane.replace_all("cars", "class", False, False, False)
    flow.wait_for_page_load()

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="05_after_replace",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')
    flow.prt_scn("05_after_replace")

    sasprogram_pane.set_node_name("Create class")
    # time.sleep(1)
    sasprogram_pane.set_notes("This is SAS program notes for expo.")
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    flow.wait_for_page_load()
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    flow.wait_for_page_load()
    table_pane.set_table("CLASS")
    flow.wait_for_page_load()
    table_pane.set_node_name("CLASS")
    flow.wait_for_page_load()
    table_pane.set_node_description("This is class table created by SAS program.")
    flow.wait_for_page_load()
    flow.link_two_nodes_in_flow("Create class", "CLASS")
    flow.wait_for_page_load()
    flow.arrange_nodes()

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="06_after_link_two_nodes",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')

    flow.prt_scn("06_after_link_two_nodes")

    flow.run(False)
    flow.select_node_in_flow_canvas("CLASS")

    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)
    flow.wait_for_page_load()

    WholePage(page).screenshot_self("07_preview_before_sorted",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]',
                                          '//span[contains(@class,"BaseButton" )][contains(text(), "列")]',
                                          '//div[@class="visible scrollbar horizontal"]',
                                          '//div[@class="visible scrollbar vertical"]',
                                          WholePage(page).locator(
                                              '//div[@data-testid="appMessageToast"]//span[''@role="img"]'),
                                          '//button[@data-testid="programViewPane-toolbar-runButton"]'
                                          ],
                                    mask_color='#000000')
    flow.prt_scn("07_preview_before_sorted")

    flow.add_node(FlowNodeType.sort)
    flow.wait_for_page_load()
    flow.arrange_nodes()
    flow.wait_for_page_load()
    flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)
    flow.wait_for_page_load()
    flow.arrange_nodes()
    flow.wait_for_page_load()
    flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)

    sort_pane = SortPane(page)

    list1 = ["Class", "Name"]
    sort_pane.add_sort(list1, SortWay.descending)
    flow.wait_for_page_load()
    WholePage(page).screenshot_self(pic_name="08_add_sort")

    flow.prt_scn("08_add_sort")

    flow.add_node(FlowNodeType.table)
    flow.wait_for_page_load()
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    flow.wait_for_page_load()

    table_pane.set_node_name("SORTED")
    flow.wait_for_page_load()

    table_pane.set_library("WORK")

    table_pane.set_table("SORTED")
    table_pane.refresh_table()
    # flow.link_two_nodes_in_flow("排序","SORTED")
    # flow.link_two_nodes_in_flow("Sort", "SORTED")
    flow.link_two_nodes_in_flow(Helper.data_locale.SORT, "SORTED")
    # time.sleep(1)
    flow.arrange_nodes()
    # time.sleep(1)
    # flow.run(False)
    flow.wait_for_page_load()

    flow.select_node_in_flow_canvas("SORTED")
    flow.wait_for_page_load()

    # table_pane.click_tab("预览数据")
    # table_pane.click_tab("Preview Data")
    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)
    flow.wait_for_page_load()

    WholePage(page).screenshot_self(pic_name="09_preview_sorted_table",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]',
                                          '//span[contains(@class,"BaseButton" )][contains(text(), "列")]',
                                          '//div[@class="visible scrollbar horizontal"]',
                                          '//div[@class="visible scrollbar vertical"]',
                                          WholePage(page).locator(
                                              '//div[@data-testid="appMessageToast"]//span[''@role="img"]'),
                                          '//button[@data-testid="programViewPane-toolbar-runButton"]'
                                          ],
                                    mask_color='#000000')
    flow.prt_scn("09_preview_sorted_table")
