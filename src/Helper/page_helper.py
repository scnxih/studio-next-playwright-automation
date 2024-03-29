from src.Pages.Common.login_page import LoginPage
from src.Pages.Common.tab_group import *
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.StudioNext.Center.top_tab_group import TopTabGroup
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.StudioNext.Dialog.document_recovery_dialog import DocumentRecoveryDialog
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import ManageShortcutsDialog
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog

from src.Pages.StudioNext.Left.accordion_page import AccordionPage
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Left.library_page import LibraryPage
from src.Pages.StudioNext.Left.openitems_page import OpenItemsPage
from src.Pages.StudioNext.Left.sas_content_server_page import SASContentServerPage
from src.Pages.StudioNext.Left.sascontent_page import SASContentPage
from src.Pages.StudioNext.Top.top_menu_page import *
from src.Pages.StudioNext.Center.codeeditor_page import *
from src.Pages.StudioNext.Top.top_right_toolbar import *
from src.Pages.StudioNext.Bottom.bottom_toolbar import *
from src.Pages.StudioNext.Center.submission_status_page import *
import time

from src.Pages.StudioNext.Center.xml_editor_page import *
from src.Pages.StudioNext.Center.plain_editor_pages import *
from src.Pages.StudioNext.Center.program_editor_pages import *
from src.Pages.StudioNext.Dialog.keyboard_shortcuts_dialog import *
from src.Pages.StudioNext.Dialog.add_profile_dialog import *
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import *

"""Added by Alice on 11/07/2023 start"""
from src.Helper.page_factory import *


def transform_from_TopMenuItem_to_CenterPageType(top_menu_item: TopMenuItem) -> CenterPageType:
    match top_menu_item:
        case TopMenuItem.new_sas_program:
            return CenterPageType.sas_program_page
        case TopMenuItem.new_python_program:
            return CenterPageType.python_program_page
        case TopMenuItem.new_flow:
            return CenterPageType.flow_page
        case TopMenuItem.new_query:
            return CenterPageType.query_page
        case TopMenuItem.new_custom_step:
            return CenterPageType.custom_step_page
        case TopMenuItem.new_quick_import:
            return CenterPageType.quick_import_page
        case TopMenuItem.new_job_definition:
            return CenterPageType.job_definition_page
        case TopMenuItem.new_file_types_json:
            return CenterPageType.json_page
        case TopMenuItem.new_file_types_text:
            return CenterPageType.text_page
        case TopMenuItem.new_file_types_xml:
            return CenterPageType.xml_page
        case TopMenuItem.new_file_types_workspace:
            return CenterPageType.work_space_page
        case TopMenuItem.view_submission_status:
            return CenterPageType.submission_status_page
        case TopMenuItem.view_deployed_and_scheduled_jobs:
            return CenterPageType.deployed_scheduled_job_page
        case TopMenuItem.view_startup_initialization_log:
            return CenterPageType.start_initialization_log_page


"""Added by Alice on 11/07/2023 end"""


class PageHelper:
    @staticmethod
    def login(page):
        login_page = LoginPage(page)
        login_page.login_studionext()

    @staticmethod
    def force_login(page):
        login_page = LoginPage(page)
        login_page.force_login()

    @staticmethod
    def new_all_items(page):
        top_menu = TopMenuPage(page)
        top_menu.new_item(TopMenuItem.new_sas_program)
        top_menu.new_item(TopMenuItem.new_python_program)
        top_menu.new_item(TopMenuItem.new_flow)
        top_menu.new_item(TopMenuItem.new_query)
        top_menu.new_item(TopMenuItem.new_custom_step)
        top_menu.new_item(TopMenuItem.new_quick_import)
        top_menu.new_item(TopMenuItem.new_job_definition)
        top_menu.new_item(TopMenuItem.new_file_types_json)
        top_menu.new_item(TopMenuItem.new_file_types_text)
        top_menu.new_item(TopMenuItem.new_file_types_xml)
        top_menu.new_item(TopMenuItem.new_file_types_workspace)

    """Updated by Alice on 11/07/2023 start"""
    """Added by Alice on 11/06/2023 start"""

    @staticmethod
    def new_item(page, top_menu_item: TopMenuItem) -> CenterPage:
        top_menu = TopMenuPage(page)
        top_menu.new_item(top_menu_item)

        return get_center_page(page, transform_from_TopMenuItem_to_CenterPageType(top_menu_item))

    """Added by Alice on 11/06/2023 end"""

    @staticmethod
    def new_sas_program(page) -> CenterPage:
        top_menu = TopMenuPage(page)
        top_menu.new_item(TopMenuItem.new_sas_program)
        return get_center_page(page, CenterPageType.sas_program_page)

    """Updated by Alice on 11/07/2023 end"""

    @staticmethod
    def close_all_tabs(page):
        top_tab_group = TopTabGroup(page)
        top_tab_group.close_all_tabs()

    @staticmethod
    def show_accordion(page, accordion_type: AccordionType):
        acc: AccordionPage = AccordionPage(page)
        acc.show_accordion(accordion_type)

    @staticmethod
    def show_all_accordion(page):
        acc: AccordionPage = AccordionPage(page)
        acc.show_accordion(AccordionType.open_item)
        acc.show_accordion(AccordionType.sas_server)
        acc.show_accordion(AccordionType.sas_content)
        acc.show_accordion(AccordionType.steps)
        acc.show_accordion(AccordionType.snippets)
        acc.show_accordion(AccordionType.libraries)
        acc.show_accordion(AccordionType.git)

    @staticmethod
    def sign_out(page):
        top_right = TopRightToolbar(page)
        top_right.click_sign_out()

    @staticmethod
    def type_code_in_codeeditor(page, text):
        code_page = CodeEditorPage(page)
        code_page.type_code_in_codeeditor(text)

    @staticmethod
    def set_autoexec(page, text):
        auto = AutoexecDialog(page)
        auto.type_code_run_save(text)


    # ADDED
    # <<< Added by Jacky(ID: jawang) on Oct.27th, 2023
    @staticmethod
    def clear_autoexec_thru_keyboard(page):
        auto = AutoexecDialog(page)
        auto.clear_autoexec_thru_keyboard()

    @staticmethod
    def clear_customcode_thru_keyboard(page):
        cus = CustomCodeDialog(page)
        cus.clear_custom_code_thru_keyboard()

    # Added by Jacky(ID: jawang) on Oct.27th, 2023 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Oct.30th, 2023
    @staticmethod
    def switch_to_standard_perspective(page):
        top_menu = TopMenuPage(page)
        # Comment this since the options is missing with latest build. Will uncomment it once it is fixed.
        # top_menu.click_options(TopMenuItem.options.options_change_perspective_standard)

    @staticmethod
    def switch_to_interactive_perspective(page):
        top_menu = TopMenuPage(page)
        # Comment this since the options is missing with latest build. Will uncomment it once it is fixed.
        # top_menu.click_options(TopMenuItem.options.options_change_perspective_interactive)

    # END Added by Jacky(ID: jawang) on Oct.30th, 2023 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Nov.7th, 2023
    @staticmethod
    def reset_settings_dialog(page):
        """
        Reset settings in 'Global/Region and Language', 'Global/General' & 'SAS Studio/General' of Settings dialog
        :param page:
        :return:
        """
        # Step-1: Open Settings dialog
        top_right = TopRightToolbar(page)
        top_right.click_settings()
        setting_dialog = SettingsDialog(page)

        # Step-2: Reset before operations
        setting_dialog.reset_global_general()
        setting_dialog.reset_sas_studio_general()
        setting_dialog.reset_region_and_language()

        # Step-3: Close the Settingds dialog
        setting_dialog.close_dialog()

    # END Added by Jacky(ID: jawang) on Nov.7th, 2023 >>>

    @staticmethod
    def click_options(page, top_menu_item: TopMenuItem):
        top_menu = TopMenuPage(page)
        top_menu.click_options(top_menu_item)

    """Add if_wait_toast_disappear argument by Alice on 09/22/2023"""

    @staticmethod
    def save_program(page, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        Helper.logger.debug("Enter PageHelper.save_program")
        code_page = CodeEditorPage(page)
        return code_page.save_file(folder_path, file_name, if_replace, if_wait_toast_disappear)

    @staticmethod
    def save_program_test_tile_view_combobox(page, folder_path, file_name, if_replace, if_wait_toast_disappear=True):
        Helper.logger.debug("Enter PageHelper.save_program")
        code_page = CodeEditorPage(page)
        return code_page.save_file_test_tile_view(folder_path, file_name, if_replace, if_wait_toast_disappear)

    @staticmethod
    def show_settings_dialog(page):
        top_right = TopRightToolbar(page)
        top_right.click_settings()

    @staticmethod
    def show_new_features_dialog(page):
        top_right = TopRightToolbar(page)
        top_right.click_new_features()

    @staticmethod
    def show_submission_status(page):
        top_right = BottomToolbar(page)
        top_right.click_submission_status()

    @staticmethod
    def show_document_recovery_dialog(page):
        top_right = BottomToolbar(page)
        top_right.click_recovery()

    @staticmethod
    def show_keyboard_shortcuts_dialog(page):
        top_right = BottomToolbar(page)
        top_right.click_keyboard_shortcuts()

    """ Added by Jacky(ID: jawang) on Sept. 4th, 2023 """

    @staticmethod
    def new_xml_file(page):
        """Create a xml file"""
        top_menu = TopMenuPage(page)
        top_menu.new_item(TopMenuItem.new_file_types_xml)

    @staticmethod
    def save_xml_file(page, folder_path, file_name, if_replace):
        Helper.logger.debug("Enter PageHelper.save_xml_file")
        xml_editor_page = XMLEditor(page)
        return xml_editor_page.save_file(folder_path, file_name, if_replace)

    """ Added by Jacky(ID: jawang) on Sept. 4th, 2023 """

    """ Added by Jacky(ID: jawang) on Sept. 5th, 2023 """

    @staticmethod
    def create_plain_editor_factory():
        return PlainEditorFactory()

    """ Added by Jacky(ID: jawang) on Sept. 5th, 2023 """

    """ Added by Jacky(ID: jawang) on Sept. 6th, 2023 """

    @staticmethod
    def create_program_editor_factory():
        return ProgramEditorFactory()

    """ Added by Jacky(ID: jawang) on Sept. 6th, 2023 """

    @staticmethod
    def new_flow(page) -> CenterPage:
        top_menu = TopMenuPage(page)
        top_menu.new_item(TopMenuItem.new_flow)
        return get_center_page(page, CenterPageType.flow_page)

    # Added by dommy 2023/8/23
    @staticmethod
    def search_keyboard_shortcuts(page, text):
        ks_dialog = KeyboardShortcutsDialog(page)
        ks_dialog.search_keyboard_shortcuts(text)

    @staticmethod
    def clear_search_keyboard_shortcuts(page):
        ks_dialog = KeyboardShortcutsDialog(page)
        ks_dialog.clear_search_keyboard_shortcuts()

    @staticmethod
    def close_keyboard_shortcuts(page):
        ks_dialog = KeyboardShortcutsDialog(page)
        ks_dialog.close_keyboard_shortcuts()

    @staticmethod
    def open_file(page, folder_path, file_name):
        open_file = TopMenuPage(page)
        return open_file.click_open_openfile(folder_path, file_name)

    @staticmethod
    def save_all_files(page, folder_path, file_name, if_replace):
        open_items = OpenItemsPage(page)
        return open_items.save_all_files(folder_path, file_name, if_replace)

    @staticmethod
    def openitems_open_file(page, folder_path, file_name):
        open_file = OpenItemsPage(page)
        return open_file.open_file(folder_path, file_name)

    # Added by liujia 20230823
    @staticmethod
    def set_customcode(page, text, tabenum):
        Cus = CustomCodeDialog(page)
        Cus.type_code_run_save(text, tabenum)

    @staticmethod
    def set_option(page):
        Cus = CustomCodeDialog(page)
        Cus.set_option()


    # Ended by liujia 20230823

    # ---------- modified by Frank on 09/22/2023 begin----------#
    @staticmethod
    def document_recovery_dialog_recover_all(page, button_text: str):
        """
        Description: recover all files
        :param page:
        :param button_text: text of Apply button or Apply and Close button
        """
        PageHelper.show_document_recovery_dialog(page)
        doc_recov = DocumentRecoveryDialog(page)
        doc_recov.recover_all(button_text)

    @staticmethod
    def document_recovery_dialog_delete_all(page, button_text: str):
        """
        Description: recover all files
        :param page:
        :param button_text: text of Apply button or Apply and Close button
        """
        PageHelper.show_document_recovery_dialog(page)
        doc_recov = DocumentRecoveryDialog(page)
        doc_recov.delete_all(button_text)

    @staticmethod
    def document_recovery_dialog_recover_files(page, button_text: str, file_indexes=None, file_names=None):
        """
        Description: recover file(s) by file_indexes(int list) or file_names(str list)
        :param page:
        :param button_text: text of Apply button or Apply and Close button
        :param file_indexes: int list, item min value is 0
        :param file_names: str list
        """
        PageHelper.show_document_recovery_dialog(page)
        doc_recov = DocumentRecoveryDialog(page)
        doc_recov.recover_files(button_text, file_indexes=file_indexes, file_names=file_names)

    @staticmethod
    def document_recovery_dialog_delete_files(page, button_text: str, file_indexes=None, file_names=None):
        """
        Description: delete file(s) by file_indexes(int list) or file_names(str list)
        :param page:
        :param button_text: text of Apply button or Apply and Close button
        :param file_indexes: int list, item min value is 0
        :param file_names: str list
        """
        PageHelper.show_document_recovery_dialog(page)
        doc_recov = DocumentRecoveryDialog(page)
        doc_recov.delete_files(button_text, file_indexes=file_indexes, file_names=file_names)

    # ---------- modified by Frank on 09/22/2023 end----------#

    # ----------Added by Allison, 9/1/2023 begin---- #
    @staticmethod
    def new_folder(page, entrance: str, folder_path: list, folder_name):
        new_folder = SASContentServerPage(page)
        return new_folder.new_folder(entrance, folder_path, folder_name)

    @staticmethod
    def delete_single_item(page, entrance: str, folder_path: list):
        delete_folder = SASContentServerPage(page)
        return delete_folder.delete_single_item(entrance, folder_path)

    @staticmethod
    def delete_multiple_items(page, entrance: str, folder_path: list):
        delete_folder = SASContentServerPage(page)
        return delete_folder.delete_multiple_items(entrance, folder_path)

    # ----------Added by Allison, 9/5/2023 end----- #

    # ----------Added by Dommy, 9/4/2023 begin---- #
    @staticmethod
    def mange_keyboard_input_shortcut(page, label, field_num: int, key, reassign):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.filter_shortcut_field(label)
        ms_dialog.input_shortcut(label, field_num, key, reassign)

    @staticmethod
    def mange_keyboard_clear_shortcut(page, label, field_num: int):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.clear_shortcut(label, field_num)

    @staticmethod
    def mange_keyboard_reset_shortcut(page, label, field_num: int):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.reset_shortcut(label, field_num)

    @staticmethod
    def mange_keyboard_reset_all(page):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.click_more_options()
        ms_dialog.reset_all_shortcuts()

    @staticmethod
    def mange_keyboard_export_shortcuts(page):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.click_more_options()
        ms_dialog.export_shortcuts()

    @staticmethod
    def mange_keyboard_check_help(page):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.check_help()

    @staticmethod
    def mange_keyboard_save(page):
        ms_dialog = ManageShortcutsDialog(page)
        ms_dialog.save_shortcut_setting()

    # ----------Added by Dommy, 9/4/2023 end---- #
    # ----------Modified by Liu Jia, 9/25/2023 begin---- #
    @staticmethod
    def open_table(page, library_name, table_name):
        open_table = LibraryPage(page)
        open_table.open_table(library_name, table_name)

    # ----------Added by Liu Jia, 9/25/2023 end----- #:
    # ----------Added by Dommy, 9/20/2023 begin---- #
    @staticmethod
    def add_git_profile_ssh(page, profile_name, username, email, public_ssh, private_ssh):
        add_profile_dialog = AddProfileDialog(page, Helper.data_locale.ADD_A_PROFILE)
        manage_git_conn = ManageGitConnectionDialog(page)
        manage_git_conn.go_to_add_profile_dialog()
        add_profile_dialog.add_profile_input_ssh(profile_name, username, email, public_ssh, private_ssh)
        manage_git_conn.close_alert_dup_profile()
        expect(manage_git_conn.profile_item(profile_name)).to_be_visible()

    @staticmethod
    def add_git_profile_ssh_part(page, profile_name, username, email):
        add_profile_dialog = AddProfileDialog(page, Helper.data_locale.ADD_A_PROFILE)
        manage_git_conn = ManageGitConnectionDialog(page)
        manage_git_conn.go_to_add_profile_dialog()
        add_profile_dialog.add_profile_input_ssh(profile_name, username, email)
        manage_git_conn.close_alert_dup_profile()
        expect(manage_git_conn.profile_item(profile_name)).to_be_visible()

    @staticmethod
    def edit_git_profile_ssh(page, previous_profile_name, **profile_field):
        edit_profile_dialog = AddProfileDialog(page, Helper.data_locale.EDIT_PROFILE)
        manage_git_conn = ManageGitConnectionDialog(page)
        if manage_git_conn.profile_item(previous_profile_name).is_visible():
            manage_git_conn.go_to_edit_profile_dialog(previous_profile_name)
            edit_profile_dialog.edit_profile_input_ssh(**profile_field)
            dup_profile_alert = Alert(page, "SAS® Studio Next")
            if dup_profile_alert.is_open():
                manage_git_conn.close_alert_dup_profile()
                Helper.logger.debug("New profile name is duplicated with existing one.")
            else:
                Helper.logger.debug("Go to Edit Profile dialog")
        else:
            Helper.logger.debug("The Profile you want to edit does not exist.")

    @staticmethod
    def delete_profile(page, profile_name):
        manage_git_conn = ManageGitConnectionDialog(page)
        manage_git_conn.delete_profile(profile_name)

    @staticmethod
    def set_profile_as_default(page, profile_name):
        manage_git_conn = ManageGitConnectionDialog(page)
        manage_git_conn.set_profile_as_default(profile_name)

    # ----------Added by Dommy, 9/22/2023 end-------#

    # ----------Added by Allison, 9/15/2023 begin---- #
    @staticmethod
    def show_properties(page, entrance: str, folder_path: list):
        show_properties = SASContentServerPage(page)
        return show_properties.show_properties(entrance, folder_path)

    # ----------Added by Allison, 9/20/2023 end---- #

    ''' ----- Added by Frank, 9/22/2023 begin ----- '''
    @staticmethod
    def submission_status_fill_input_search_toolbar(page, fill_text: str):
        """
        Description: fill Search input field on toolbar.
        :param page:
        :param fill_text: fill text.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.fill_input_search_toolbar(fill_text)
    ''' ----- Added by Frank, 9/22/2023 end ----- '''

    ''' ----- Updated by Frank, 3/18/2024 begin ----- '''
    @staticmethod
    def submission_status_clear_input_search_toolbar(page):
        """
        Description: clear Search input field on toolbar.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.clear_input_search_toolbar()

    @staticmethod
    def submission_status_click_btn_clear_search_text(page):
        """
        Description: click Clear button in Search input field on toolbar.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.click_btn_clear_search_text()

    @staticmethod
    def submission_status_cancel_all_jobs(page):
        """
        Description: cancel all running jobs.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.cancel_all_jobs()

    @staticmethod
    def submission_status_clear_all_completed_submissions(page):
        """
        Description: clear all completed submission.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.clear_all_completed_submissions()

    @staticmethod
    def submission_status_sort_column(page, col_id: str, sort_order: str):
        """
        Description: sort a column with 'none', 'ascending' or 'descending' order.
        :param page:
        :param col_id: give a column header's col-id
        :param sort_order: specify the sort order with 'none', 'ascending' or 'descending'
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.sort_column(col_id, sort_order)

    @staticmethod
    def submission_status_open_submission_result(page, row_index=None, name_text=None):
        """
        Description: open results of a submission indicated by row-index.
        :param page:
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.open_submission_result(row_index=row_index, name_text=name_text)

    @staticmethod
    def submission_status_filter_pane_expand_status_section(page):
        """
        Description: expand the title section in Filter pane if it is collapsed.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.expand_status_section_filter_pane()

    @staticmethod
    def submission_status_filter_pane_collapse_status_section(page):
        """
        Description: collapse the title section in Filter pane if it is expanded.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.collapse_status_section_filter_pane()

    @staticmethod
    def submission_status_reset_filter_in_filter_pane(page):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.reset_filter_in_filter_pane()

    @staticmethod
    def submission_status_filter_pane_check_statuses(page, *status_labels):
        """
        Description: check all or part of status in Filter pane.
        :param page:
        :param status_labels: labels of statuses, separated with comma.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.check_statuses_filter_pane(*status_labels)

    @staticmethod
    def submission_status_filter_pane_uncheck_statuses(page, *status_labels):
        """
        Description: uncheck all or part of status in Filter pane.
        :param page:
        :param status_labels: labels of statuses, separated with comma.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.uncheck_statuses_filter_pane(*status_labels)

    @staticmethod
    def submission_status_select_context_menu_item(page, *context_menu_text, row_index=None, name_text=None):
        """
        Description: select context menu using menu item text.
        :param page:
        :param context_menu_text: give menu item(s) text separated with comma
        :param row_index: start from 0
        :param name_text: the name text of a row
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.select_context_menu_item(*context_menu_text, row_index=row_index, name_text=name_text)
    ''' ----- Updated by Frank, 3/18/2024 end ----- '''

    ''' ----- Added by Frank, 3/18/2024 begin ----- '''
    @staticmethod
    def submission_status_open_overflow_menu(page):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.open_overflow_menu()

    @staticmethod
    def submission_status_close_overflow_menu(page):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.close_overflow_menu()

    @staticmethod
    def submission_status_select_show_all_submissions(page):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.check_show_all_submissions()

    @staticmethod
    def submission_status_deselect_show_all_submissions(page):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.uncheck_show_all_submissions()

    @staticmethod
    def submission_status_show_all_columns(page):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.show_all_columns()

    @staticmethod
    def submission_status_add_columns_to_page(page, *col_labels: str):
        """
        Description: add hidden columns to Submission Status page.
        :param page:
        :param col_labels: labels of columns, separated with comma.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.add_columns_to_page(*col_labels)

    @staticmethod
    def submission_status_remove_columns_from_page(page, *col_labels: str):
        """
        Description: remove some displayed columns from Submission Status page.
        :param page:
        :param col_labels: labels of columns, separated with comma.
        """
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.remove_columns_from_page(*col_labels)

    @staticmethod
    def submission_status_move_a_column_to_left(page, col_label: str):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.move_a_column_to_left(col_label)

    @staticmethod
    def submission_status_move_a_column_to_right(page, col_label: str):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.move_a_column_to_right(col_label)

    @staticmethod
    def submission_status_move_a_column_to_leftmost(page, col_label: str):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.move_a_column_to_leftmost(col_label)

    @staticmethod
    def submission_status_move_a_column_to_rightmost(page, col_label: str):
        PageHelper.show_submission_status(page)
        ss = SubmissionStatusPage(page)
        ss.move_a_column_to_rightmost(col_label)
    ''' ----- Added by Frank, 3/18/2024 end ----- '''

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Oct.12nd, 2023
    @staticmethod
    def show_accordion_tab_labels(page):
        acc: AccordionPage = AccordionPage(page)
        acc.show_tab_labels()

    # Added by Jacky(ID: jawang) on Oct.12nd, 2023 >>>

    """added by Alice on 10/26/2023 start"""

    @staticmethod
    def close_alert_if_needed(page):
        alert = Alert(page, Helper.data_locale.STUDIO_NEXT)
        if alert.is_open():
            # alert.close_alert_dialog(Helper.data_locale.CLOSE)
            alert.close_dialog()

    """added by Alice on 10/26/2023 end"""

    """Added by Alice on 11/03/2023 start"""

    """Check menu item in View in Top Menu, since StudioNext supports Submission status/Deployed and scheduled jobs/
    Start Page/Navigation panes now, so only these menu items are supported now."""

    @staticmethod
    def check_menu_item_in_view(page, topMenuItem: TopMenuItem) -> CenterPage | None:
        top_menu = TopMenuPage(page)
        top_menu.check_view_item(topMenuItem)
        if topMenuItem == TopMenuItem.view_submission_status or topMenuItem == TopMenuItem.view_deployed_and_scheduled_jobs or topMenuItem == TopMenuItem.view_startup_initialization_log:
            return get_center_page(page, transform_from_TopMenuItem_to_CenterPageType(topMenuItem))
        else:
            return None

    """Uncheck menu item in View in Top Menu, since StudioNext supports Submission status/Deployed and scheduled jobs/
        Start Page/Navigation panes now, so only these menu items are supported now."""

    @staticmethod
    def uncheck_menu_item_in_view(page, topMenuItem: TopMenuItem):
        top_menu = TopMenuPage(page)
        top_menu.uncheck_view_item(topMenuItem)

    """Added by Alice on 11/03/2023 end"""

    """Added by Alice on 11/06/2023 start"""

    @staticmethod
    def show_view_startup_initialization_log(page) -> StartupInitializationLogPage:
        top_menu = TopMenuPage(page)
        top_menu.show_view_startup_initialization_log()
        return get_center_page(page, CenterPageType.start_initialization_log_page)

    """Added by Alice on 11/06/2023 end"""

    """Added by Alice on 11/27/2023 start"""
    @staticmethod
    def clear_customcode(page: Page):
        Helper.logger.debug("Clear custom code dialog.")

        PageHelper.click_options(page, TopMenuItem.options_custom_code)
        PageHelper.clear_customcode_thru_keyboard(page)
    @staticmethod
    def clear_autoexec(page: Page):
        Helper.logger.debug("Clear autoexec dialog.")

        PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
        PageHelper.clear_autoexec_thru_keyboard(page)


    @staticmethod
    def init_environments(page: Page):
        PageHelper.clear_customcode(page)
        PageHelper.clear_autoexec(page)
        PageHelper.switch_to_standard_perspective(page)
        PageHelper.reset_settings_dialog(page)

    def reset_all_settings_dialog(page: Page):
        top_right = TopRightToolbar(page)
        top_right.click_settings()
        setting_dialog = SettingsDialog(page)
        setting_dialog.reset_settings_via_iteration()
        setting_dialog.close_dialog()

    """Added by Alice on 11/27/2023 end"""
