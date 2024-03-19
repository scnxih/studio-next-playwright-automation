"""
Author: Alice
Date: Feb 01, 2024
Description: This is textarea in custom step designer.
"""
from src.Pages.Common.DesignerControls.designer_control import DesignerControl


class DesignerTextArea(DesignerControl):
    def __init__(self, page, control_number: int = 1):
        self._data_testid_prefix = "textarea"
        DesignerControl.__init__(self, page, control_number=control_number)
