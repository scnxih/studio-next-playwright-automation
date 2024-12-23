"""
@author: Frank (Feng) Jiang
@date: Updated on 2023/09/19
@description: define Document Recovery dialog, include dialog elements and functionalities
"""
from src.Data.elements_ids import *
from src.Pages.Common.dialog import *
from src.Pages.Common.treegrid import *
import time


class DocumentRecoveryDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.DOCUMENT_RECOVERY)
        # Since this dialog loaded slow.
        self.treegrid = TreeGrid(self.base_xpath, self.page)
        time.sleep(1)

    @property
    def btn_recover_all(self):
        return self.get_by_test_id(TestID.DOC_RECOVERY_BTN_RECOVER_ALL)

    @property
    def btn_delete_all(self):
        return self.get_by_test_id(TestID.DOC_RECOVERY_BTN_DELETE_ALL)

    def selfie(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the vanilla screenshot_self method in BasePage
        """
        Helper.logger.debug("DocumentRecoveryDialog: Overwrite the vanilla screenshot_self method in BasePage")

        self.screenshot(self.base_xpath, pic_name, clip=clip,

                        # mask=["//div[contains(@class, 'breadcrumb')]", self.content_selector_navigator_tree,
                        # self.temp_content_selector],
                        # mask=[self.bread_crumb, self.content_selector_navigator_tree,
                        # self.temp_content_selector],

                        # Mask files list in dialog
                        mask=['//div[@role="rowgroup"][@class="ag-center-cols-container"]'
                              '[../../descendant::div[@data-testid="recoveryDialog-fileActionSelector"]]'],
                        mask_color="#000000")

    def cancel_dialog(self):
        Helper.logger.debug("Cancel Recovery dialog.")
        self.click_button_in_footer(Helper.data_locale.CANCEL)

    def recover_all(self, button_text: str):
        """
        Description: click 'Recover All' button, then apply.
        :param button_text: string, text of 'Apply' or 'Apply and Close' button
        """
        Helper.logger.debug("Recover all files.")
        self.click(self.btn_recover_all)
        time.sleep(1)
        self.click_button_in_footer(button_text)

    def delete_all(self, button_text: str):
        """
        Description: click 'Delete All' button, then apply.
        :param button_text: string, text of 'Apply' or 'Apply and Close' button
        """
        Helper.logger.debug("Delete all files.")
        self.click(self.btn_delete_all)
        time.sleep(1)
        self.click_button_in_footer(button_text)

    def recover_files(self, button_text: str, file_indexes=None, file_names=None):
        """
        Description: change operation of some files to Recover, then apply.
        :param button_text: string, text of 'Apply' or 'Apply and Close' button
        :param file_indexes: integer list, the min value should be greater than or equal to 0
        :param file_names: string list
        """
        if file_indexes is None:
            for i in range(len(file_names)):
                self.treegrid.dbclick_column_in_a_row(ColID.DOCUMENT_RECOVERY_ACTION, name_text=file_names[i])
                self.treegrid.select_item_combo_in_a_row(Helper.data_locale.OPERATE_RECOVERY, name_text=file_names[i])
                time.sleep(1)
        if file_names is None:
            for i in range(len(file_indexes)):
                self.treegrid.dbclick_column_in_a_row(ColID.DOCUMENT_RECOVERY_ACTION, row_index=file_indexes[i])
                self.treegrid.select_item_combo_in_a_row(Helper.data_locale.OPERATE_RECOVERY, row_index=file_indexes[i])
                time.sleep(1)
        self.click_button_in_footer(button_text)

    def delete_files(self, button_text: str, file_indexes=None, file_names=None):
        """
        Description: change operation of some files to Delete, then apply.
        :param button_text: integer list, the min value should be greater than or equal to 0
        :param file_names: string list
        :param file_indexes: integer value(s), support cascade, the min value should be greater than or equal to 0
        """
        if file_indexes is None:
            for i in range(len(file_names)):
                self.treegrid.dbclick_column_in_a_row(ColID.DOCUMENT_RECOVERY_ACTION, name_text=file_names[i])
                self.treegrid.select_item_combo_in_a_row(Helper.data_locale.DELETE, name_text=file_names[i])
                time.sleep(1)
        if file_names is None:
            for i in range(len(file_indexes)):
                self.treegrid.dbclick_column_in_a_row(ColID.DOCUMENT_RECOVERY_ACTION, row_index=file_indexes[i])
                self.treegrid.select_item_combo_in_a_row(Helper.data_locale.DELETE, row_index=file_indexes[i])
                time.sleep(1)
        self.click_button_in_footer(button_text)
