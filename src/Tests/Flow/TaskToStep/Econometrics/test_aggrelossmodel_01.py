"""This is test case file for step Aggregate Loss Models"""
import time

from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Econometrics.aggregate_loss_models import *

from src.conftest import *
from src.Helper.page_factory import *


@pytest.mark.level0_step
def test_01_new_severity_new_count(page, init):
    flow: FlowPage = PageHelper.new_flow(page)

    flow.add_node(FlowNodeType.sas_program)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """
/* Simulate data for losses that several policyholders incur in a year */
data losses(keep=policyholderId age gender carType annualMiles education carSafety income noloss lossamount);
call streaminit(12345);
array cx{5} age gender carType annualMiles education;
array cbeta{6} _TEMPORARY_ (1 -0.75 1 0.6 -1 -0.25);
array sx{3} carType carSafety income;
array sbeta{4} _TEMPORARY_ (3.5 1.5 -0.8 0.6);
alpha = 1/3; theta = 1/alpha;
Sigma = 1;
do policyholderId=1 to 5000;
/* simulate policyholder and vehicle attributes */
age = MAX(int(rand('NORMAL', 35, 15)),16)/50;
if (rand('UNIFORM') < 0.5) then gender = 1; * female;
else gender = 2; * male;
if (rand('UNIFORM') < 0.7) then carType = 1; * sedan;
else carType = 2; * SUV;
annualMiles = MAX(1000, int(rand('NORMAL', 12000, 5000)))/5000;
educationLevel = rand('UNIFORM');
if (educationLevel < 0.5) then education = 1; *high school graduate;
else if (educationLevel < 0.85) then education = 2; *college graduate;
else education = 3; *advanced degree;
carSafety = rand('UNIFORM'); /* scaled to be between 0 & 1 */
income = MAX(15000,int(rand('NORMAL', education*30000, 50000)))/100000;
/* simulate number of losses incurred by this policyholder */
cxbeta = cbeta(1);
do i=1 to dim(cx);
cxbeta = cxbeta + cx(i) * cbeta(i+1);
end;
Mu = exp(cxbeta);
p = theta/(Mu+theta);
numloss = rand('NEGB',p,theta);
/* simulate severity of each loss */
if (numloss > 0) then do;
noloss = 0;
do iloss=1 to numloss;
Mu = sbeta(1);
do i=1 to dim(sx);
Mu = Mu + sx(i) * sbeta(i+1);
end;
lossamount = exp(Mu) * rand('LOGNORMAL')**Sigma;
output;
end;
end;
else do;
noloss = 1;
lossamount = .;
output;
end;
end;
run;
/* Aggregate number of annual loss events for each policyholder */
data losscounts(keep=age gender carType annualMiles education numloss);
set losses;
by policyholderId;
retain numloss 0;
if (noloss ne 1) then
numloss = numloss + 1;
if (last.policyholderId) then do;
output;
numloss = 0;
end;
run;
/* Generate the scenario data table for single policyholder */
data singlePolicy(keep=age gender carType annualMiles education carSafety income);
call streaminit(67897);
age = MAX(int(rand('NORMAL', 35, 15)),16)/50;
if (rand('UNIFORM') < 0.5) then gender = 1; * female;
else gender = 2; * male;
if (rand('UNIFORM') < 0.7) then carType = 1; * sedan;
else carType = 2; * SUV;
annualMiles = MAX(1000, int(rand('NORMAL', 12000, 5000)))/5000;
educationLevel = rand('UNIFORM');
if (educationLevel < 0.5) then education = 1; *high school graduate;
else if (educationLevel < 0.85) then education = 2; *college graduate;
else education = 3; *advanced degree;
carSafety = rand('UNIFORM'); /* scaled to be between 0 & 1 */
income = MAX(15000,int(rand('NORMAL', education*30000, 50000)))/100000;
output;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("Work")
    table_pane.set_table("LossCounts")
    time.sleep(0.8)

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LossCounts")
    flow.arrange_nodes()


    flow.add_node(FlowNodeType.table)

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("Work")
    table_pane.set_table("Losses")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "Losses")
    flow.arrange_nodes()
    flow.run(False)

    flow.add_node(FlowNodeType.table)

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("Work")
    table_pane.set_table("SinglePolicy")

    flow.click_context_menu_on_node_in_flow(Helper.data_locale.SAS_PROGRAM, Helper.data_locale.ADD_OUTPUT_PORT)

    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "SinglePolicy")
    flow.arrange_nodes()
    flow.run(False)