"""
Author: Alice
Date: Jan 29, 2024
Description: This is checkbox in custom step designer.
"""
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control import DesignerControl


class DesignerCheckbox(DesignerControl):
    def __init__(self, page, control_number: int = 1):
        self._data_testid_prefix = "checkbox"
        DesignerControl.__init__(self, page, control_number=control_number)
