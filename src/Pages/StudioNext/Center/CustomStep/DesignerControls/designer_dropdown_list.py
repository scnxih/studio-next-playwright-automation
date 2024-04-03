"""
Author: Alice
Date: Feb 01, 2024
Description: This is dropdown list in custom step designer.
"""
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control import DesignerControl


class DesignerDropDownList(DesignerControl):
    def __init__(self, page, control_number: int = 1):
        self._data_testid_prefix = "dropdown"
        DesignerControl.__init__(self, page, control_number=control_number)
