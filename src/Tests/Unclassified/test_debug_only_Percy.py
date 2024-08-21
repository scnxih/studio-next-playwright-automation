from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.bubble_map_pane import BubbleMapPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane

from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


def test_01_custom_step_columnselector(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.check_show_single_page_as_tab()
    properties.set_label("Data")

    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.select_control(DesignerControlType.input_table, 1)
    properties.set_indent("1")
    properties.set_label("Select the source table:")
    properties.set_default_library("SASHELP")
    properties.set_default_table("CLASS")


def test_Bubble_Map_in_flow_level0(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
cas; 
libname mycas cas;
data city_loc (label='Nevada Cities'
               keep=county city city2 lat long county_name);
  set mapsgfk.uscity_all(where=(state=32));
run;
proc sort data=city_loc;
  by city2;
run;
data city_pop (label='Nevada County Seat Populations');
  length city $65 city2 $55;
  infile datalines dlm=',';
  input city population_city county;
  label city            = 'County Seat'
        city2           = 'Normalized city name'
        population_city = 'City Population'
        county          = 'County FIPS Code';
  city2 = upcase(compress(city));
cards;
Fallon, 8458, 1
Las Vegas, 623747, 3
Minden, 3180, 5
Elko, 20279, 7
Goldfield, 443, 9
Eureka, 487, 11
Winnemucca, 7887, 13
Battle Mountain, 3276, 15
Pioche, 911, 17
Yerington, 3064, 19
Hawthorne, 3095, 21
Tonopah, 2360 , 23
Lovelock, 1878, 27
Virginia City, 717, 29
Reno, 241445, 31
Ely, 4134, 33
Carson City, 54521, 510
;
proc sort data=city_pop;
  by city2;
run;
data &_output1;
  merge city_pop (in=a) city_loc;
  by city2;
  if a;
run;
"""

    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("city_pop_loc")
    time.sleep(0.8)

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "city_pop_loc")
    flow.arrange_nodes()

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,Helper.data_locale.STEP_BUBBLE_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("city_pop_loc",Helper.data_locale.STEP_BUBBLE_MAP)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BUBBLE_MAP)
    bubble_map_pane=BubbleMapPane(page)
    bubble_map_pane.set_filter_input_data("population_city > 1000")
    bubble_map_pane.add_column(Helper.data_locale.LATITUDE,'LAT',None)
    bubble_map_pane.add_column(Helper.data_locale.LONGITUDE,'LONG',None)
    bubble_map_pane.add_column(Helper.data_locale.BUBBLE_SIZE,'population_city',None)
    bubble_map_pane.add_column(Helper.data_locale.GROUP, 'COUNTY_NAME', None)

    flow.run(True)
def test_Bubble_Map_in_flow_level1_01(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
cas; 
libname mycas cas;
data city_loc (label='Nevada Cities'
               keep=county city city2 lat long county_name);
  set mapsgfk.uscity_all(where=(state=32));
run;
proc sort data=city_loc;
  by city2;
run;
data city_pop (label='Nevada County Seat Populations');
  length city $65 city2 $55;
  infile datalines dlm=',';
  input city population_city county;
  label city            = 'County Seat'
        city2           = 'Normalized city name'
        population_city = 'City Population'
        county          = 'County FIPS Code';
  city2 = upcase(compress(city));
cards;
Fallon, 8458, 1
Las Vegas, 623747, 3
Minden, 3180, 5
Elko, 20279, 7
Goldfield, 443, 9
Eureka, 487, 11
Winnemucca, 7887, 13
Battle Mountain, 3276, 15
Pioche, 911, 17
Yerington, 3064, 19
Hawthorne, 3095, 21
Tonopah, 2360 , 23
Lovelock, 1878, 27
Virginia City, 717, 29
Reno, 241445, 31
Ely, 4134, 33
Carson City, 54521, 510
;
proc sort data=city_pop;
  by city2;
run;
data &_output1;
  merge city_pop (in=a) city_loc;
  by city2;
  if a;
run;

data &_output2;
  set mapsgfk.us_counties(where=(state=32)
                          drop=x y
                          rename=(long=x lat=y));
run;
data county_pop (label='Nevada Counties');
  length county_name $55;
  infile datalines dlm=',';
  state=32;
  input county_name county population_county;
  label state             = 'State FIPS Code'
        county_name       = 'County Name'
        county            = 'County FIPS Code'
        population_county = '2010 Census County Population'
        group             = 'Population range';
  /* Add five population ranges as groups to map response data. */
  if      population_county > 100000 then group='Greater than 100,000';
  else if population_county > 10000  then group='10,000 - 100,000';
  else if population_county > 5000   then group='5,000 - 10,000';
  else if population_county > 1000   then group='1,000 - 5,000';
  else                                    group='Less than 1,000';
cards;
Churchill, 1, 24877
Clark, 3, 2069681
Douglas, 5, 47710
Elko, 7, 52766
Esmeralda, 9, 783
Eureka, 11, 1987
Humboldt, 13, 17019
Lander, 15, 5775
Lincoln, 17, 5036
Lyon, 19, 52585
Mineral, 21, 4772
Nye, 23, 43946
Pershing, 27, 6753
Storey, 29, 3987
Washoe, 31, 446903
White Pine, 33, 10030
Carson City, 510, 54521
;
"""

    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("city_pop_loc")
    time.sleep(0.8)

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "city_pop_loc")
    flow.arrange_nodes()

    flow.add_node(FlowNodeType.table)

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("MYCAS")
    table_pane.set_table("nevada")

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.SAS_PROGRAM, "添加输出端口")

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "nevada")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,Helper.data_locale.STEP_BUBBLE_MAP]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.link_two_nodes_in_flow("city_pop_loc",Helper.data_locale.STEP_BUBBLE_MAP)
    flow.arrange_nodes()

    flow.click_context_menu_for_the_node_in_flow(Helper.data_locale.STEP_BUBBLE_MAP, "添加输入端口","{sasstudio-steps-gui-icu.genericText.inputport.nodesData.title}")
    flow.link_two_nodes_in_flow("nevada", Helper.data_locale.STEP_BUBBLE_MAP)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_BUBBLE_MAP)
    bubble_map_pane=BubbleMapPane(page)
    bubble_map_pane.set_filter_input_data("population_city > 1000")
    bubble_map_pane.add_column(Helper.data_locale.LATITUDE,'LAT',None)
    bubble_map_pane.add_column(Helper.data_locale.LONGITUDE,'LONG',None)
    bubble_map_pane.add_column(Helper.data_locale.BUBBLE_SIZE,'population_city',None)
    bubble_map_pane.add_column(Helper.data_locale.GROUP, 'COUNTY_NAME', None)

    bubble_map_pane.set_choropleth_map_layer()
    bubble_map_pane.set_filter_map_data("density>2")
    bubble_map_pane.add_column_for_ID_variable_Map_data(column_name='ID')
    bubble_map_pane.set_Base_map_(item_index=1)
    flow.run(True)