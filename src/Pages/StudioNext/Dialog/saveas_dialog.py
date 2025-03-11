import time

from src.Pages.Common.dialog import *
from src.Pages.Common.treeview_aggrid import TreeViewAGGrid
from src.Pages.Common.treeview_nova import *
from src.Pages.Common.toolbar import Toolbar
from src.Pages.Common.combobox import Combobox


class SaveAsDialog(Dialog):
    def __init__(self, page):
        # Dialog.__init__(self, page, Helper.data_locale.SAVE_AS_A_Upper_Case)
        Dialog.__init__(self, page, "")

        # self.folder_tree = TreeViewNova(self.base_xpath, page)
        self.folder_tree = TreeViewAGGrid(self.base_xpath, page,
                                          supplement_base_xpath="[descendant::span[@class='ag-icon ag-icon-tree-closed']]")
        self.toolbar = Toolbar(self.base_xpath, page)
        self.combobox_sort_by = Combobox(container_base_xpath=self.base_xpath, page=page,
                                         data_test_id="contentSelector-save-contentSelector-navigator-actionbar-sort-by")

    @property
    def input_file_name(self):
        return self.get_by_test_id("contentSelector-save-contentSelector-name-input")

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Apr.22nd, 2024
    @property
    def temp_content_selector(self):
        """
        Content Selector in the right part of 'Save As' Dialog
        Note: This is a temporary solution, would be replaced after related common components are fully implemented.
        //div[@data-testid="contentSelector-save-contentSelector-navigator-table-gridWrapper"]
        """
        return self.get_by_test_id("contentSelector-save-contentSelector-navigator-table-gridWrapper")

    # END Added by Jacky(ID: jawang) on Apr.22nd, 2024 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on May.21st, 2024
    @property
    def content_selector_navigator_tree(self):
        """
        Content Selector Navigator Tree in the middle of 'Save As' Dialog
        Note: This is a temporary solution, would be replaced after related common components are fully implemented.
        //div[@data-testid="contentSelector-save-contentSelector-navigator-tree"]
        """
        return self.get_by_test_id("contentSelector-save-contentSelector-navigator-tree")

    # END Added by Jacky(ID: jawang) on May.21st, 2024 >>>

    @property
    def button_new(self):
        """
        'New' button next to 'Refresh' on the right upper corner.
        NOTE: This button would be available when the folder navigated to (in navigator tree) is autherized to save
        PS: Need to check this button visibility, otherwise error would occur.
        """
        return self.locator(
            "//button[@type='button'][contains(@data-testid, 'contentSelector')][@title='" + Helper.data_locale.NEW + "']")

    @property
    def bread_crumb(self):
        """
        breadcrumb located in the upper left corner of 'Save as' dialog that serves to lead or guide
        NOTE: This breadcrumb causes SDSTest diffs, which require masks
        """
        return self.locator("//div[contains(@class, 'breadcrumb')][contains(@data-testid, 'contentSelector')]")

    @property
    def sas_content_gridcell(self):
        """
        Grid-cell 'SAS Content' in Save-as dialog
        """
        return self.locate_xpath("//div[@role='gridcell']//span[text()= '" + Helper.data_locale.SAS_CONTENT + "']")

    @property
    def sas_server_gridcell(self):
        """
        Grid-cell 'SAS Server' in Save-as dialog
        """
        return self.locate_xpath("//div[@role='gridcell']//span[text()= '" + Helper.data_locale.SAS_SERVER + "']")

    def save_file2(self, folder_path: list, file_name: str, if_replace, if_wait_toast_disappear=True):
        """
        Supplemented a method to click SAS Content/SAS Server grid-cell while saving files.
        """

        # Determine if destination is SAS Content or SAS Server
        if folder_path[0] == Helper.data_locale.SAS_CONTENT:
            self.click(self.sas_content_gridcell)
        else:
            if folder_path[0] == Helper.data_locale.SAS_SERVER:
                self.click(self.sas_server_gridcell)
            else:
                Helper.logger.debug("Error location!")
                self.close_dialog()

        # Original
        if not self.navigate_to_folder(folder_path):
            return False

        self.fill(self.input_file_name, file_name)
        time.sleep(0.3)

        # Click dialog title to avoid noise in input text-input-box
        self.click_dialog_title_or_studionext_header()

        self.screenshot(self.base_xpath,
                        "save_file",
                        # mask=[self.temp_content_selector, self.content_selector_navigator_tree],
                        mask_color="#000000")

        time.sleep(0.5)

        self.selfie('save_file')
        # self.wait_for(self.button_new)

        self.click_button_in_footer(Helper.data_locale.SAVE)
        time.sleep(1)

        path_alert = self.page.get_by_test_id("contentSelector-save-contentSelector-errorDialog-dialog")

        time.sleep(1)
        if path_alert.is_visible():
            Helper.logger.debug("WARNING: Path is not specified for save-as process")
            path_alert.get_by_text(Helper.data_locale.CLOSE).click()
            self.click_button_in_footer(Helper.data_locale.CANCEL)
            return False

        replace_alert = Alert(self.page, Helper.data_locale.SAVE_AS)
        time.sleep(1)
        if replace_alert.is_open():
            if if_replace:
                replace_alert.click_button_in_footer(Helper.data_locale.REPLACE)
                if if_wait_toast_disappear:
                    self.wait_toast_disappear()
                return True
            else:
                replace_alert.click_button_in_footer(Helper.data_locale.CANCEL)
                return False
        else:
            if if_wait_toast_disappear:
                self.wait_toast_disappear()
            return True

    def selfie(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the vanilla screenshot_self method in BasePage
        """
        Helper.logger.debug("SaveAsDialog: Overwrite the vanilla screenshot_self method in BasePage")
        self.screenshot(self.base_xpath, pic_name, clip=clip,
                        # mask=[self.bread_crumb, self.content_selector_navigator_tree, self.temp_content_selector],  # Comment out masks Jan 21, 2025
                        mask=[self.temp_content_selector],  # Supplemented  masks Jan 24, 2025
                        mask_color="#000000")

    def wait_for_open(self):
        # self.wait_for(self.input_file_name)
        time.sleep(2)

    def navigate_to_folder(self, folder_path: list):
        return self.folder_tree.navigate_to_element(folder_path)

    def save_file(self, folder_path: list, file_name: str, if_replace, if_wait_toast_disappear=True):

        # Since Save as does not work due to Nova 43.1, comment this save_file method temporarily.
        # self.close_dialog()
        # return False

        # Determine if destination is SAS Content or SAS Server
        if folder_path[0] == Helper.data_locale.SAS_CONTENT:
            self.click(self.sas_content_gridcell)
        else:
            if folder_path[0] == Helper.data_locale.SAS_SERVER:
                self.click(self.sas_server_gridcell)
            else:
                Helper.logger.debug("Error location!")
                self.close_dialog()

        # Original
        if not self.navigate_to_folder(folder_path):
            return False

        self.fill(self.input_file_name, file_name)
        time.sleep(0.3)

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on {Monday, January 13, 2025}
        # Click dialog title to avoid noise in input text-input-box
        self.click_dialog_title_or_studionext_header()
        # END Added by Jacky(ID: jawang) on {Monday, January 13, 2025} >>>

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on May.21st, 2024
        # Mask both the content selector on the right hand side and the navigator tree in the middle

        self.screenshot(self.base_xpath,
                        "save_file",
                        mask=[self.temp_content_selector, self.content_selector_navigator_tree],
                        mask_color="#000000")

        # END Added by Jacky(ID: jawang) on May.21st, 2024 >>>

        time.sleep(0.5)

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Oct.17th, 2024
        self.selfie('save_file')

        if folder_path[0] == Helper.data_locale.SAS_CONTENT:
            self.wait_for(self.button_new)
        else:
            time.sleep(1.0)

        self.click_button_in_footer(Helper.data_locale.SAVE)
        time.sleep(1)

        path_alert = self.page.get_by_test_id("contentSelector-save-contentSelector-errorDialog-dialog")

        time.sleep(1)
        if path_alert.is_visible():
            Helper.logger.debug("WARNING: Path is not specified for save-as process")
            path_alert.get_by_text(Helper.data_locale.CLOSE).click()
            self.click_button_in_footer(Helper.data_locale.CANCEL)
            return False
        # END Added by Jacky(ID: jawang) on Nov.12th, 2024 >>>

        replace_alert = Alert(self.page, Helper.data_locale.SAVE_AS)
        time.sleep(1)
        if replace_alert.is_open():
            if if_replace:
                replace_alert.click_button_in_footer(Helper.data_locale.REPLACE)
                if if_wait_toast_disappear:
                    self.wait_toast_disappear()
                return True
            else:
                replace_alert.click_button_in_footer(Helper.data_locale.CANCEL)
                return False
        else:
            if if_wait_toast_disappear:
                self.wait_toast_disappear()
            return True

    def click_Tile_View(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.TILE_VIEW)

    def click_Table_View(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.TABLE_VIEW)

    def select_sort_by(self, sort_by_text):
        self.click_Tile_View()
        self.combobox_sort_by.select_item(sort_by_text)
