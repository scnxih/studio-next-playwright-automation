"""
Author: Alice
Date: Feb 01, 2024
Description: This is output table in custom step designer.
"""
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control import DesignerControl


class DesignerOutputTable(DesignerControl):
    def __init__(self, page, control_number: int = 1):
        self._data_testid_prefix = "outputtable"
        DesignerControl.__init__(self, page, control_number=control_number)
