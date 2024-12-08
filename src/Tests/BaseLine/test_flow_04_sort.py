from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.sort_pane import SortPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import *
from src.Helper.page_helper import *

def test_init(page,init):
    PageHelper.init_environments(page)
def test_01_sasprogram_table_sort_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    time.sleep(0.5)
    flow.add_node(FlowNodeType.sas_program)
    time.sleep(0.8)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)
    # time.sleep(1)
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
    time.sleep(0.5)
    sasprogram_pane.type_into_text_area(str)
    # WholePage(page).screenshot_self(pic_name="01_before_fold")
    # time.sleep(1)
    sasprogram_pane.fold_all_regions()
    time.sleep(1)
    # WholePage(page).screenshot_self(pic_name="02_after_fold")
    sasprogram_pane.unfold_all_regions()
    time.sleep(1)

    # Original One
    # WholePage(page).screenshot_self(pic_name="03_after_unfold")

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="03_after_unfold",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')

    sasprogram_pane.pop_find_widget()
    sasprogram_pane.find("cars", False, False)
    time.sleep(1)

    # Original One
    # WholePage(page).screenshot_self(pic_name="04_after_find")

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="04_after_find",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')

    sasprogram_pane.replace_all("cars", "class", False, False, False)
    time.sleep(2)

    # Original One
    # WholePage(page).screenshot_self(pic_name="05_after_replace")

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="05_after_replace",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')

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

    # Original One
    # WholePage(page).screenshot_self(pic_name="06_after_link_two_nodes")

    # Mask flow toolbar so that noises from the icons can be avoided
    WholePage(page).screenshot_self(pic_name="06_after_link_two_nodes",
                                    mask=['//div[@role="group"][@data-testid="flowtoolbar"]'],
                                    mask_color='#000000')

    flow.run(False)
    flow.select_node_in_flow_canvas("CLASS")

    table_pane.refresh_table()
    table_pane.refresh_table()
    # table_pane.click_tab("预览数据")

    # Original
    # table_pane.click_tab("Preview Data")

    # Revised
    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)

    time.sleep(3)
    # WholePage(page).screenshot_self(pic_name="07_preview_before_sorted")
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

    flow.add_node(FlowNodeType.sort)
    # time.sleep(1)
    flow.arrange_nodes()

    # flow.link_two_nodes_in_flow("CLASS","排序")

    # Original
    # flow.link_two_nodes_in_flow("CLASS", "Sort")

    flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)

    # time.sleep(1)
    flow.arrange_nodes()

    # flow.select_node_in_flow_canvas("排序")

    # Original
    # flow.select_node_in_flow_canvas("Sort")

    flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)

    sort_pane = SortPane(page)

    list1 = ["Class", "Name"]
    sort_pane.add_sort(list1, SortWay.descending)
    # time.sleep(1)
    WholePage(page).screenshot_self(pic_name="08_add_sort")
    flow.add_node(FlowNodeType.table)
    # flow.select_node_in_flow_canvas("表")

    # Original
    # flow.select_node_in_flow_canvas("Table")

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table_pane.set_node_name("SORTED")
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
    time.sleep(2)
    flow.select_node_in_flow_canvas("SORTED")
    time.sleep(0.5)
    # table_pane.click_tab("预览数据")
    # table_pane.click_tab("Preview Data")
    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)
    time.sleep(2)
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
