"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: September 18th, 2024
"""
from src.Pages.Common.whole_page import WholePage
from src.conftest import *
from src.Helper.page_factory import *


def test_01_accordion_steps(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA_QUALITY, Helper.data_locale.STEP_PARSE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_PYTHON_PROGRAM]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_PHONE_NUMBERS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_TABLE_ATTRIBUTES]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_INTEGRATE, Helper.data_locale.STEP_MERGE_TABLE]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING, Helper.data_locale.STEP_Robust_PRINCIPAL_COMPONENT_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MANAGE_MODELS, Helper.data_locale.STEP_REGISTER_PYTHON_MODEL]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS, Helper.data_locale.STEP_CORE_DECOMPOSITION]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA, Helper.data_locale.STEP_STANDARDIZE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL, Helper.data_locale.STEP_PARETO_ANALYSIS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    # WORKS FINE
    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SAME_BIRTHDAY_PROBABILITY]

    # step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS, Helper.data_locale.STEP_SUMMARY_STATISTICS]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA, Helper.data_locale.STEP_TRANSPOSE_DATA]
    steps.navigate_to_step_then_collapse_parent(step_path)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA, Helper.data_locale.STEP_TEXT_MAP]
    steps.navigate_to_step_then_collapse_parent(step_path)