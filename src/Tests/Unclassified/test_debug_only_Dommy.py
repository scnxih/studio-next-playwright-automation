from time import sleep

from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Statistics.multiple_regression_statistical_power_pane import \
    MultipleRegressionStatisticalPowerPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.bar_line_chart_pane import BarLineChartPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.VisualizeData.text_map_pane import TextMapPane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *






def test_01_multiple_regression_statistical_power_in_flow_l0(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_STATISTICS,
                 Helper.data_locale.STEP_MULTIPLE_REGRESSION_STATISTICAL_POWER]
    flow.add_step_from_stepspane_to_flow(step_path)

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_MULTIPLE_REGRESSION_STATISTICAL_POWER)
    multiple_regression_statistical_power_pane = MultipleRegressionStatisticalPowerPane(page)
    multiple_regression_statistical_power_pane.expand_windowshade_number_of_predictors()
    multiple_regression_statistical_power_pane.set_number_of_full_model_predictors("4")
    multiple_regression_statistical_power_pane.set_number_of_reduced_model_predictors("2")
    multiple_regression_statistical_power_pane.expand_windowshade_variance_accounted_for()
    multiple_regression_statistical_power_pane.set_full_model_rsquare_value("0.4")
    multiple_regression_statistical_power_pane.set_reduced_model_rsquare_value("0.3")

    multiple_regression_statistical_power_pane.expand_windowshade_sample_size()
    multiple_regression_statistical_power_pane.set_sample_size_value("9")

    flow.run(True)
