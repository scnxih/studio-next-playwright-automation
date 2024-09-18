from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Helper.helper import *


class StackColumnsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Below methods are in Data tab"""

    def set_number_of_stacked_cariables_to_create(self, value:str):
        self.set_value_for_numeric_stepper(parent_label="要创建的堆叠变量数",value=value)
    def click_increment_value_for_number_of_stacked_variables_to_create(self, times:int):
        self.click_increment_value_for_numeric_stepper(parent_label="要创建的堆叠变量数",times=times)

    def click_decrement_value_for_number_of_stacked_variables_to_create(self, times:int):
        self.click_decrement_value_for_numeric_stepper(parent_label="要创建的堆叠变量数",times=times)


