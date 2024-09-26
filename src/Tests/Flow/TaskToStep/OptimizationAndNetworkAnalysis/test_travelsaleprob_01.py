"""This is test case file for step Traveling Salesman Problem"""
import pytest
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.traveling_salesman_problem_pane import TravelingSalesmanProblemPane
from src.Data.input_data_zh import *
from src.Helper.page_factory import *
import time
from src.Helper.helper import Helper
from src.Helper.page_helper import PageHelper
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage


# @pytest.mark.level0_step
# def test_00_traveling_salesman_problem_in_flow(page, init):
#
