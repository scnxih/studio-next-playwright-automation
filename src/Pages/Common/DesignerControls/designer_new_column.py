"""
Author: Alice
Date: Feb 01, 2024
Description: This is new column in custom step designer.
"""
from src.Pages.Common.DesignerControls.designer_control import DesignerControl


class DesignerNewColumn(DesignerControl):
    def __init__(self, page, control_number: int = 1):
        self._data_testid_prefix = "newcolumn"
        DesignerControl.__init__(self, page, control_number=control_number)
