"""
Author: Alice
Updated Date: October 23, 2023
Description: SAS Program will inherit from MainCenterPage class and some methods will be override as pass since sas program
            does not support.
"""
from src.Pages.Common.editor_text_area import EditorTextArea

from src.Pages.StudioNext.Center.main_center_page import MainCenterPage
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog
from src.Helper.helper import *




class CodeEditorPage(MainCenterPage):
    def __init__(self, page):
        MainCenterPage.__init__(self, page)
        """Updated by Alice on 09/22/2023 start"""
        self.editor = EditorTextArea(self.base_xpath, page)
        """Updated by Alice on 09/22/2023 end"""

    def type_code_in_codeeditor(self, text):
        self.editor.type_into_text_area(text)

    """Updated by Alice on 09/22/2023 start"""

    def save_file(self, folder_path: list, file_name, if_replace, if_wait_toast_disappear):
        self.center_toolbar_helper.saveas(folder_path, file_name, if_replace, if_wait_toast_disappear)

    """Updated by Alice on 09/22/2023 end"""

    def save_file_test_tile_view(self, folder_path, file_name, if_replace, if_wait_toast_disappear):
        return False
        self.toolbar.click_btn_by_title(Helper.data_locale.SAVE_AS)
        Helper.logger.debug("after click save as button")
        save_as_dialog = SaveAsDialog(self.page)
        Helper.logger.debug("create SaveAsDialog instance")
        if save_as_dialog.is_open():
            save_as_dialog.click_Tile_View()
            # just for test
            save_as_dialog.select_sort_by("修改日期")
            save_as_dialog.click_Table_View()
            return save_as_dialog.save_file(folder_path, file_name, if_replace)
        Helper.logger.error("save as failed.")
        return False


    def format_program(self):
        self.center_toolbar_helper.format_program()

    def debug(self):
        self.center_toolbar_helper.debug()

    def apply_main_layout_standard(self):
        pass

    def apply_main_layout_horizontal(self):
        pass

    def apply_main_layout_vertical(self):
        pass
