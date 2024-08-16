"""
Author: Alice
Date: October 24, 2023
Description: FlowPage will inherit from MainCenterPage class, thus the methods in MainCenterPage will be inherited automatically.
            You can also override these methods in this FlowPage class if needed, for example, run/save/save_as methods are override
            since thees methods n parent class MainCenterPage are not suitable for this FlowPage. And open_in_browser_tab_listing/
            download_code_file/download_listing_file/email/apply_detail_layout_standard are override as pass because flow does not support these methods.

"""
import time

from src.Pages.Common.tab_group import TabGroup
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog
from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.StudioNext.Left.steps_page import StepsPage
from src.Utilities.enums import FlowNodeType, AccordionType
from src.Helper.helper import *


class FlowPage(MainCenterPage):
    def __init__(self, page):
        MainCenterPage.__init__(self, page)

    def run(self, if_wait_toast_disappear, if_wait_run_enabled=True):
        self.toolbar.click_btn_by_test_id("flowtoolbar-runButton")
        if if_wait_toast_disappear:
            self.toolbar.wait_toast_disappear()
        if if_wait_run_enabled:
            self.toolbar.wait_until_enabled(self.toolbar.btn_by_title(Helper.data_locale.RUN))

    def save(self, folder_path=None, file_name="", if_replace=True, if_wait_toast_disappear=True):
        self.toolbar.click_btn_by_test_id("flowtoolbar-saveButton")
        if folder_path is None or file_name == "":
            if if_wait_toast_disappear:
                self.toolbar.wait_toast_disappear()
            return True
        save_as_dialog = SaveAsDialog(self.toolbar.page)
        if save_as_dialog.is_open():
            return save_as_dialog.save_file(folder_path, file_name, if_replace, if_wait_toast_disappear)
        else:
            return False

    def saveas(self, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        self.toolbar.click_btn_by_test_id("flowtoolbar-saveAsButton")
        save_as_dialog = SaveAsDialog(self.toolbar.page)
        if save_as_dialog.is_open():
            return save_as_dialog.save_file(folder_path, file_name, if_replace, if_wait_toast_disappear)
        return False

    def run_single_node(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-runSelectedNodeButton")

    def run_nodes_downstream(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-runFromNodeButton")

    def run_nodes_upstream(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-runToNodeButton")

    def background_submit(self, if_wait_toast_disappear=True):
        self.toolbar.click_btn_by_test_id("flowtoolbar-backgroundSubmitButton")
        """need to handle toast when the feature is completed"""

    def paste_step(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-pasteButton")

    def copy_step(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-pasteButton")

    def cut_step(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-cutButton")

    def undo(self):
        self.center_toolbar_helper.undo()

    def redo(self):
        self.center_toolbar_helper.redo()

    def add_node(self, node_type: FlowNodeType):
        data_testid = "flowtoolbar-addStepMenuButton-button"
        match node_type:
            case FlowNodeType.table:
                self.toolbar.click_btn_menu_by_test_id(data_testid, Helper.data_locale.TABLE)
            case FlowNodeType.file:
                self.toolbar.click_btn_menu_by_test_id(data_testid, Helper.data_locale.FILE)
            case FlowNodeType.branch_rows:
                self.toolbar.click_btn_menu_by_test_id(data_testid, Helper.data_locale.BRANCH_ROWS)
            case FlowNodeType.calculate_columns:
                self.toolbar.click_btn_menu_by_test_id(data_testid, Helper.data_locale.CALCULATE_COLUMNS)
            case FlowNodeType.sas_program:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.SAS_PROGRAM_Upper_case)
            case FlowNodeType.execute_decisions:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.EXECUTE_DECISIONS)
            case FlowNodeType.export:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.EXPORT)
            case FlowNodeType.filter_rows:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.FILTER_ROWS)
            case FlowNodeType.implement_scd:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.IMPLEMENT_SCD)
            case FlowNodeType.import_data:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.IMPORT_FILES)
            case FlowNodeType.insert_rows:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.INSERT_ROWS)
            case FlowNodeType.load_table:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.LOAD_TABLE)
            case FlowNodeType.manage_columns:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.MANAGE_COLUMNS)
            case FlowNodeType.merge_table:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.MERGE_TABLE)

            case FlowNodeType.python_program:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.PYTHON_PROGRAM)
            case FlowNodeType.query:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.QUERY)
            case FlowNodeType.sort:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.SORT)

            case FlowNodeType.union_rows:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.UNION_ROWS)

            case FlowNodeType.notes:
                self.toolbar.click_btn_menu_by_test_id(data_testid,
                                                       Helper.data_locale.NOTES)
        time.sleep(0.5)
    def view_collapse_all_ports(self):
        self.toolbar.click_btn_menu_by_test_id("flowtoolbar-viewMenuButton-button",
                                               Helper.data_locale.COLLAPSE_ALL_PORTS)

    def view_expand_all_ports(self):
        self.toolbar.click_btn_menu_by_test_id("flowtoolbar-viewMenuButton-button", Helper.data_locale.EXPAND_ALL_PORTS)

    def arrange_nodes(self):
        self.toolbar.click_btn_by_test_id("flowtoolbar-arrangeButton")

    def show_over_view_map(self):
        self.toolbar.press_btn_by_test_id("flowtoolbar-overviewButton")

    def hide_over_view_map(self):
        self.toolbar.unpress_btn_by_test_id("flowtoolbar-overviewButton")

    def open_in_browser_tab_listing(self):
        pass

    def download_code_file(self):
        pass

    def download_listing_file(self):
        pass

    def apply_main_layout_standard(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.APPLY_MAIN_LAYOUT, Helper.data_locale.STANDARD)

    def apply_main_layout_horizontal(self):
        self.center_toolbar_helper.apply_main_layout_horizontal()

    def apply_main_layout_vertical(self):
        self.center_toolbar_helper.apply_main_layout_vertical()

    def add_to_snippets(self):
        self.center_toolbar_helper.add_to_snippets()

    def apply_detail_layout_standard(self):
        pass

    def email(self):
        pass

    def flow_screenshot(self):
        self.screenshot(self.base_locator, "test")

    def select_node_in_flow_canvas(self, node_name):
        select_node_in_flow_canvas(self.page, node_name)

    def link_two_nodes_in_flow(self, node1_name, node2_name):
        link_two_nodes_in_flow(self.page, node1_name, node2_name)

    def open_context_menu_for_the_node_in_flow(self, node_name):
        open_context_menu_for_the_node_in_flow(self.page, node_name)

    def click_context_menu_for_the_node_in_flow(self,node_name,  *menu_item_text):
        self.open_context_menu_for_the_node_in_flow(node_name)
        self.click_menu_item(*menu_item_text)

    def open_context_menu_for_canvas_in_flow(self):
        open_context_menu_for_canvas_in_flow(self.page)

    def select_input_port_node_in_flow(self, node_name):
        select_input_port_node_in_flow(self.page, node_name)

    def select_output_port_node_in_flow(self, node_name):
        select_output_port_node_in_flow(self.page, node_name)

    def open_context_menu_for_input_port_of_node_in_flow(self, port_number, node_name):
        open_context_menu_for_input_port_of_node_in_flow(self.page, port_number, node_name)

    def open_context_menu_for_output_port_of_node_in_flow(self, port_number, node_name):
        open_context_menu_for_output_port_of_node_in_flow(self.page, port_number, node_name)

    def validate_node_tooltip_of_the_node_in_flow(self, node_name, expected_node_tooltip):
        validate_node_tooltip_of_the_node_in_flow(self.page, node_name, expected_node_tooltip)

    def select_node_status_dialog_of_the_node_in_flow(self, node_name):
        select_node_status_dialog_of_the_node_in_flow(self.page, node_name)

    def validate_the_flow_canvas_node_count_in_zero_state(self):
        validate_the_flow_canvas_node_count_in_zero_state(self.page)

    def validate_count_of_nodes_in_flow(self, expected_node_count):
        validate_count_of_nodes_in_flow(self.page, expected_node_count)

    def validate_input_port_count_for_node_in_flow(self, node_name, expected_input_port_count):
        validate_input_port_count_for_node_in_flow(self.page,node_name,expected_input_port_count)

    def validate_output_port_count_for_node_in_flow(self, node_name, expected_output_port_count):
        validate_output_port_count_for_node_in_flow(self.page,node_name,expected_output_port_count)

    def validate_input_port_is_in_expanded_state_for_node_in_flow(self, node_name):
        validate_input_port_is_in_expanded_state_for_node_in_flow(self.page,node_name)

    def validate_output_port_is_in_expanded_state_for_node_in_flow(self, node_name):
        validate_output_port_is_in_expanded_state_for_node_in_flow(self.page,node_name)

    def validate_input_port_is_in_collapsed_state_for_node_in_flow(self, node_name):
        validate_input_port_is_in_collapsed_state_for_node_in_flow(self.page,node_name)

    def validate_output_port_is_in_collapsed_state_for_node_in_flow(self, node_name):
        validate_output_port_is_in_collapsed_state_for_node_in_flow(self.page,node_name)

    def validate_output_port_color_for_node_in_flow(self, port_number, node_name, expected_port_color):
        validate_output_port_color_for_node_in_flow(self.page,port_number,node_name,expected_port_color)

    def add_step_from_stepspane_to_flow(self,step_path:list):
        acc: AccordionPage = AccordionPage(self.page)
        acc.show_accordion(AccordionType.steps)
        step_page = StepsPage(self.page)
        step_page.add_to_flow(step_path)
        
