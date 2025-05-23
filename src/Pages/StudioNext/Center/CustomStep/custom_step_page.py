"""
Author: Alice
Date: November 07, 2023
Description: CustomStepPage will inherit from CenterPage class。
"""
import time

from src.Pages.Common.tab_group import TabGroup
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control import DesignerControl
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control_factory import get_designer_control
from src.Pages.StudioNext.Center.center_page import *
from src.Pages.Common.listbox import Listbox
from src.Utilities.enums import *
from src.Pages.Common.text import Text

from src.Pages.StudioNext.Center.CustomStep.custom_step_properties_page import CustomStepPropertiesPage
from src.Pages.Common.treeview_common import TreeViewCommon
from src.Pages.Common.treeview_aggrid import TreeViewAGGrid


def convert_control_type_to_testid_prefix(control_type: DesignerControlType) -> str:
    test_id: str = ""
    match control_type:
        case DesignerControlType.checkbox:
            test_id = "checkbox"
        case DesignerControlType.color_picker:
            test_id = "colorpicker"
        case DesignerControlType.date_and_time_picker:
            test_id = "datetime"
        case DesignerControlType.drop_down_list:
            test_id = "dropdown"
        case DesignerControlType.file_or_folder_selector:
            test_id = "fileorfolderselector"
        case DesignerControlType.link:
            test_id = "link"
        case DesignerControlType.list:
            test_id = "list"
        case DesignerControlType.numeric_stepper:
            test_id = "numstepper"
        case DesignerControlType.radio_group:
            test_id = "radiogroup"
        case DesignerControlType.section:
            test_id = "section"
        case DesignerControlType.text:
            test_id = "text"
        case DesignerControlType.textarea:
            test_id = "textarea"
        case DesignerControlType.text_or_numeric_field:
            test_id = "inputfield"
        case DesignerControlType.input_table:
            test_id = "inputtable"
        case DesignerControlType.output_table:
            test_id = "outputtable"
        case DesignerControlType.column_selector:
            test_id = "columnselector"
        case DesignerControlType.new_column:
            test_id = "newcolumn"
    return test_id


def convert_control_type_to_text(control_type: DesignerControlType) -> str:
    text: str = ""
    match control_type:
        case DesignerControlType.checkbox:
            text = Helper.data_locale.CHECK_BOX
        case DesignerControlType.color_picker:
            text = Helper.data_locale.COLOR_PICKER
        case DesignerControlType.date_and_time_picker:
            text = Helper.data_locale.DATE_AND_TIME_PICKER
        case DesignerControlType.drop_down_list:
            text = Helper.data_locale.DROP_DOWN_LIST
        case DesignerControlType.file_or_folder_selector:
            text = Helper.data_locale.FILE_OR_FOLDER_SELECTOR
        case DesignerControlType.link:
            text = Helper.data_locale.LINK
        case DesignerControlType.list:
            text = Helper.data_locale.LIST
        case DesignerControlType.numeric_stepper:
            text = Helper.data_locale.NUMERIC_STEPPER
        case DesignerControlType.radio_group:
            text = Helper.data_locale.RADIO_BUTTON_GROUP
        case DesignerControlType.section:
            text = Helper.data_locale.SECTION
        case DesignerControlType.text:
            text = Helper.data_locale.TEXT
        case DesignerControlType.textarea:
            text = Helper.data_locale.TEXT_AREA
        case DesignerControlType.text_or_numeric_field:
            text = Helper.data_locale.TEXT_OR_NUMERIC_FIELD
        case DesignerControlType.input_table:
            text = Helper.data_locale.INPUT_TABLE
        case DesignerControlType.output_table:
            text = Helper.data_locale.OUTPUT_TABLE
        case DesignerControlType.column_selector:
            text = Helper.data_locale.COLUMN_SELECTOR
        case DesignerControlType.new_column:
            text = Helper.data_locale.NEW_COLUMN
    return text


class CustomStepPage(CenterPage):

    def __init__(self, page):
        CenterPage.__init__(self, page)
        self.toolbar_control_library = Toolbar(self.base_xpath, self.page,
                                               supplement_base_xpath="[.//span[text()='{0}']]".format(
                                                   Helper.data_locale.ADD_PAGE_P_UPPER_CASE))
        # self.listbox_pages = Listbox(self.base_xpath, self.page, data_test_id="pageList")
        # self.listbox_pages = Listbox(self.base_xpath, self.page)
        self.control_library_pages = TreeViewAGGrid(self.base_xpath, self.page)
        # self.control_library_grid = TreeViewAGGrid(self.base_xpath, self.page, supplement_base_xpath="[@grid-id='2']")
        self.control_library_grid = TreeViewAGGrid(self.base_xpath, self.page)

        self.listbox_controls = Listbox(self.base_xpath, self.page, aria_labelledby="controlList")
        self.tab_group = TabGroup("", page)
        # self.text_filter = Text(self.base_xpath, page, aria_label=Helper.data_locale.FILTER)
        self.text_filter = Text(self.base_xpath, page, aria_label=Helper.data_locale.FILTER_CONTROLS)
        # self.control_category_tree = TreeViewCommon(self.base_xpath, page)
        self.control_category_tree = TreeViewAGGrid(self.base_xpath, page)

    """The save functions is not implemented in StudioNext, so pass now"""

    def __designer_canvas(self):
        return self.locate_xpath("//div[@data-testid='designCanvasTestID']")

    def prt_scn(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the screenshot_self function in src.Pages.Common.base_page.BasePage.screenshot_self
        so that masks can be added, removed and modified in the same place.
        """

        Helper.logger.debug("Enter CustomStepPage print screen ...")

        # Click the designer canvas
        self.__designer_canvas().click(position={"x": 500, "y": 400})

        # Scroll down twelve times so that noise caused by scrollbar can be avoided
        for i in range(12):
            self.page.mouse.wheel(0, 200)
            Helper.logger.debug("Mouse wheel " + str(i + 1) + " time(s)")

        # Click header to avoid any possible noise
        self.click_dialog_title_or_studionext_header()

        self.screenshot("//div[@id='app']", pic_name, user_assigned_xpath=True, clip=clip,
                        mask=[self.locator('//div[@data-landmark-label="' + Helper.data_locale.STATUS_BAR + '"]'),
                              self.toolbar.btn_by_title(Helper.data_locale.SAVE),
                              self.toolbar.btn_by_title(Helper.data_locale.SAVE_AS)],
                        mask_color='#F4F4F6')

        Helper.logger.debug("... Exit CustomStepPage print screen")

    def screenshot_self(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the vanilla screenshot_self method in BasePage
        """
        Helper.logger.debug("CustomStepPage: Overwrite the vanilla screenshot_self method in BasePage")
        self.screenshot(self.base_xpath, pic_name, clip=clip,
                        mask=[self.toolbar.btn_by_title(Helper.data_locale.SAVE),
                              self.toolbar.btn_by_title(Helper.data_locale.SAVE_AS)],
                        mask_color="#123321")

    def defocus_designer_control(self):
        self.__designer_canvas().click(position={"x": 1, "y": 1})

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        # self.center_toolbar_helper.save(folder_path, file_name, if_replace, if_wait_toast_disappear)
        pass

    """The save functions is not implemented in StudioNext, so pass now"""

    def saveas(self, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        # self.center_toolbar_helper.saveas(folder_path, file_name, if_replace, if_wait_toast_disappear)
        pass

    """The undo functions is not implemented in StudioNext, so pass now"""

    def undo(self):
        # self.center_toolbar_helper.undo()
        pass

    """The redo functions is not implemented in StudioNext, so pass now"""

    def redo(self):
        # self.center_toolbar_helper.redo()
        pass

    """The reload functions is not implemented in StudioNext, so pass now"""

    def reload(self):
        # self.center_toolbar_helper.reload()
        pass

    def apply_main_layout_standard(self):
        self.center_toolbar_helper.apply_main_layout_standard()

    def apply_main_layout_horizontal(self):
        self.center_toolbar_helper.apply_main_layout_horizontal()

    def apply_main_layout_vertical(self):
        self.center_toolbar_helper.apply_main_layout_vertical()

    def add_page_by_toolbar(self):
        self.toolbar_control_library.click_btn_by_test_id("addPageButton")
        self.wait_for_page_load()
        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.add_page_by_toolbar ')

    def add_page_by_context_menu(self, page_text: str):
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.ADD_PAGE)
        self.control_library_grid.click_context_menu_on_grid_item(page_text, Helper.data_locale.ADD_PAGE)

    def delete_page_by_toolbar(self, page_text: str):
        self.control_library_pages.click_grid_item(page_text)
        self.wait_for_page_load()

        self.toolbar_control_library.click_btn_by_test_id("deletePageButton")
        self.wait_for_page_load()

        delete_alert = Alert(self.page, Helper.data_locale.DELETE_A_PAGE)

        if delete_alert.is_open():
            delete_alert.click_button_in_footer(Helper.data_locale.DELETE)
            Helper.logger.debug('Closed alert dialog of DELETE_A_PAGE')

        self.wait_for_page_load()

        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.delete_page_by_toolbar')

    def delete_page_by_keyboard(self, page_text: str):
        # self.listbox_pages.click_list_item(page_text)
        # self.listbox_pages.click_grid_item(page_text)
        self.control_library_pages.click_grid_item(page_text)
        self.wait_for_page_load()

        self.key_press("Delete")
        self.wait_for_page_load()

        delete_alert = Alert(self.page, Helper.data_locale.DELETE_A_PAGE)
        self.wait_for_page_load()

        if delete_alert.is_open():
            delete_alert.click_button_in_footer(Helper.data_locale.DELETE)

        self.wait_for_page_load()

    def check_show_single_page_as_tab(self):
        self.toolbar_control_library.check_menu_in_more_options(Helper.data_locale.SHOW_SINGLE_PAGE_AS_TAB)
        self.wait_for_page_load()
        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.check_show_single_page_as_tab')

    def uncheck_show_single_page_as_tab(self):
        self.toolbar_control_library.uncheck_menu_in_more_options(Helper.data_locale.SHOW_SINGLE_PAGE_AS_TAB)
        self.wait_for_page_load()
        Helper.logger.debug('src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.uncheck_show_single_page_as_tab')

    def add_page_on_page(self, page_text: str):
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.ADD_PAGE)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.ADD_PAGE)
        self.wait_for_page_load()
        Helper.logger.debug('Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.add_page_on_page ')

    def move_up_on_page(self, page_text: str):
        """
        Move up
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.MOVE_UP)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.MOVE_UP)

        self.wait_for_page_load()
        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.move_up_on_page')

    def move_down_on_page(self, page_text: str):
        """
        Move down
        """
        # self.listbox_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.MOVE_DOWN)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.MOVE_DOWN)

        self.wait_for_page_load()
        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.move_down_on_page')

    def move_down_on_page2(self, page_text: str):
        """
        Use tree-grid instead
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.MOVE_DOWN)
        # self.control_library_grid.label_element_name(page_text).click()
        self.click(self.control_library_grid.label_element_name(page_text))
        self.wait_for_page_load()

        # time.sleep(1)

        self.right_click(self.control_library_grid.label_element_name(page_text))
        self.wait_for_page_load()

        # time.sleep(1)

        self.key_press("ArrowDown")
        self.wait_for_page_load()

        # time.sleep(1)

        self.key_press("ArrowDown")
        self.wait_for_page_load()

        # time.sleep(1)

        self.key_press("Enter")
        self.wait_for_page_load()

    def move_to_top_on_page(self, page_text: str):
        """
        Move to top
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.MOVE_TO_TOP)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.MOVE_TO_TOP)

        self.wait_for_page_load()
        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.move_to_top_on_page')

    def move_to_end_on_page(self, page_text: str):
        """

        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.MOVE_TO_END)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.MOVE_TO_END)

        self.wait_for_page_load()
        Helper.logger.debug('Exiting src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.move_to_end_on_page')

    def insert_page_above_on_page(self, page_text: str):
        """
        Insert a new page above current one
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.INSERT_PAGE_ABOVE)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.INSERT_PAGE_ABOVE)

        self.wait_for_page_load()
        Helper.logger.debug('src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.insert_page_above_on_page')

    def insert_page_below_on_page(self, page_text: str):
        """
        Insert a new page below current one
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.INSERT_PAGE_BELOW)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.INSERT_PAGE_BELOW)

        self.wait_for_page_load()
        Helper.logger.debug('src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage'
                            '.insert_page_below_on_page')

    def duplicate_on_page(self, page_text: str):
        """
        Duplicate on page
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.DUPLICATE)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.DUPLICATE)

        self.wait_for_page_load()
        Helper.logger.debug('src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.duplicate_on_page')

    def delete_on_page(self, page_text: str):
        """
        Delete a page
        """
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.DELETE)

        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.DELETE)

        delete_alert = Alert(self.page, Helper.data_locale.DELETE_A_PAGE)

        if delete_alert.is_open():
            delete_alert.click_button_in_footer(Helper.data_locale.DELETE)

        self.wait_for_page_load()
        Helper.logger.debug('src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.delete_on_page')

    def cut_on_page(self, page_text: str):
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.CUT)

        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.CUT)

        self.wait_for_page_load()
        Helper.logger.debug("Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.cut_on_page")

    def copy_on_page(self, page_text: str):
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.COPY)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.COPY)
        self.wait_for_page_load()
        Helper.logger.debug("Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.copy_on_page")

    def paste_on_page(self, page_text: str):
        # self.listbox_pages.click_context_menu_on_list_item(page_text, Helper.data_locale.PASTE)
        self.control_library_pages.click_context_menu_on_grid_item(page_text, Helper.data_locale.PASTE)

        self.wait_for_page_load()
        Helper.logger.debug("Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.paste_on_page")

    def filter_controls(self, search_text: str):
        self.text_filter.fill_text(search_text)

        self.wait_for_page_load()
        Helper.logger.debug(
            "Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.filter_controls")

    def clear_filter(self):
        self.text_filter.clear_text()

        self.wait_for_page_load()
        Helper.logger.debug("Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.clear_filter")

    def insert_control_former(self, control_type: DesignerControlType):

        text = convert_control_type_to_text(control_type)
        self.listbox_controls.click_context_menu_on_list_item(text, Helper.data_locale.INSERT_CONTROL)

        self.wait_for_page_load()
        Helper.logger.debug("Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage"
                            ".insert_control_former")

    def select_control(self, control_type: DesignerControlType, control_number: int) -> DesignerControl:
        """

        """
        designer_control = get_designer_control(self.page, control_type, control_number)

        designer_control.base_locator.click(position={"x": 2, "y": 2})
        # time.sleep(0.3)
        self.wait_for_page_load()

        return designer_control

    def insert_control(self, control_type: DesignerControlType):
        """
        Organization changed: Common tree is adopted to categorize controls
        """
        text = convert_control_type_to_text(control_type)

        if control_type in [DesignerControlType.column_selector, DesignerControlType.new_column,
                            DesignerControlType.input_table, DesignerControlType.output_table]:
            Helper.logger.debug('Control type: ' + text)
            Helper.logger.debug('Control Category: ' + 'Data')

            self.control_category_tree.navigate_to_element_and_dblclick(['Data', text])
            # self.control_category_tree.navigate_to_element_and_dblclick([Helper.data_locale.DATA, text])
            # self.control_category_tree.navigate_to_element_and_click_context_menu([Helper.data_locale.COMMON, text], Helper.data_locale.INSERT_CONTROL)
            Helper.logger.debug('Control Category: ' + text)

        else:
            self.control_category_tree.navigate_to_element_and_dblclick(['Common', text])
            # self.control_category_tree.navigate_to_element_and_dblclick([Helper.data_locale.COMMON, text])
            # self.control_category_tree.navigate_to_element_and_click_context_menu([Helper.data_locale.COMMON, text], Helper.data_locale.INSERT_CONTROL)

        self.wait_for_page_load()
        Helper.logger.debug(
            "Exit src.Pages.StudioNext.Center.CustomStep.custom_step_page.CustomStepPage.insert_control")
