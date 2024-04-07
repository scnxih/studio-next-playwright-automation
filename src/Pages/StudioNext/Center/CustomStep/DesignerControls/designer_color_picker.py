"""
Author: Alice
Date: Feb 01, 2024
Description: This is color picker in custom step designer.
"""
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control import DesignerControl


class DesignerColorPicker(DesignerControl):
    def __init__(self, page, control_number: int = 1):
        self._data_testid_prefix = "colorpicker"
        DesignerControl.__init__(self, page, control_number=control_number)
