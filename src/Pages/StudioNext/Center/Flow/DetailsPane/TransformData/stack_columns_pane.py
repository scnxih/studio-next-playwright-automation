from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Helper.helper import *


class StackColumnsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Below methods are in Data tab"""

    def set_number_of_stacked_cariables_to_create(self, value:int):
        self.set_value_for_numeric_stepper(parent_label="要创建的堆叠变量数",value=value)




