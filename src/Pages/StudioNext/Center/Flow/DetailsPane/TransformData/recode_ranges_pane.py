from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane



class RecodeRangesPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Below methods are in Values tab"""

    def set_recode_values(self, col_id,):
        self.set_value_for_numeric_stepper(parent_label="要创建的堆叠变量数",value=value)