"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: July 26th, 2024
"""
from src.Pages.Common.dialog import Dialog
from src.Pages.Common.combobox import Combobox
from src.Pages.Common.text import Text

class AddFilterDialog(Dialog):
    """
    Add Filter dialog used in Flow and Query
    """

    def __init__(self, page):
        Dialog.__init__(self, page)
        self.condition_combo_box = Combobox("", page, data_test_id="quickFilterDialog-filterOperatorSelect")
        self.condition_value_input = Text("", page, data_test_id="quickFilterDialog-valueInput0-input-input")
    @property
    def button_cancel(self):
        """
        The 'Cancel' button at the bottom.
        """
        return self.get_by_test_id("quickFilterDialog-dismissButton")

    @property
    def button_filter(self):
        """
        The 'Filter' button at the bottom.
        """
        return self.get_by_test_id("quickFilterDialog-firstButton")

    @property
    def link_reset(self):
        """
        The 'Reset' link at the bottom.
        """
        # //a[@data-testid='quickFilterDialog-resetLink']
        return self.locate_xpath("//a[@data-testid='quickFilterDialog-resetLink']")

    def cancel_and_close(self):
        """
        Click the Cancel button to close the dialog.
        """
        # self.button_cancel.click()
        self.click(self.button_cancel)

    def set_condition_to(self, condition: str, value: str):
        """
        Set filter condition to ...
        """
        self.condition_combo_box.select_item(condition)
