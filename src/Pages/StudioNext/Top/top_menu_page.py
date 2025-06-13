import time

from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import ManageGitConnectionDialog
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import ManageShortcutsDialog
from src.Pages.StudioNext.Dialog.open_dialog import OpenDialog
from src.Utilities.enums import *
from src.Pages.Common.toolbar import *

from src.Pages.Common.dialog import Alert
from src.Data.data import Data


class TopMenuPage(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)

        # Original
        # self.toolbar = Toolbar(self.base_xpath, page, data_test_id="appHeaderToolbar-toolbar")

        # Changed on Wednesday, April 9, 2025,
        self.toolbar = Toolbar(self.base_xpath, page, data_test_id="appHeaderToolbar-view")

    def click_options(self, top_menu: TopMenuItem):
        test_id = "appHeaderToolbar-options-button"
        match top_menu:
            case TopMenuItem.options_autoexec_file:

                self.toolbar.click_btn_menu_by_test_id_wait_until_enabled(test_id, Helper.data_locale.AUTOEXEC_FILE)
                auto = AutoexecDialog(self.page)
                if auto.is_open():
                    return
            case TopMenuItem.options_manage_keyboard_shortcuts:
                self.toolbar.click_btn_menu_by_test_id_wait_until_enabled(test_id,
                                                                          Helper.data_locale.MANAGE_KEYBOARD_SHORTCUTS)
                if ManageShortcutsDialog(self.page).is_open():
                    return
            case TopMenuItem.options_custom_code:
                self.toolbar.click_btn_menu_by_test_id_wait_until_enabled(test_id, Helper.data_locale.CUSTOM_CODE)
                custom_code = CustomCodeDialog(self.page)
                if custom_code.is_open():
                    return
            case TopMenuItem.options_manage_git_connections:
                self.toolbar.click_btn_menu_by_test_id_wait_until_enabled(test_id,
                                                                          Helper.data_locale.MANAGE_GIT_CONNECTION)
                if ManageGitConnectionDialog(self.page).is_open():
                    return
            # ADDED
            # BEGIN <<< Added by Jacky(ID: jawang) on Oct.30th, 2023

            # Options/Change perspective/Standard
            case TopMenuItem.options_change_perspective_standard:
                self.toolbar.click_btn_menu_by_test_id_wait_until_enabled(test_id,
                                                                          Helper.data_locale.CHANGE_PERSPECTIVE,
                                                                          Helper.data_locale.STANDARD)

                # NOTE: Alert Dialog would pop up at the moment
                # Remove the following code after this function has been fully implemented
                alert = Alert(self.toolbar.page, Helper.data_locale.STUDIO_NEXT)
                if alert.is_open():
                    time.sleep(3)
                    # alert.close_alert_dialog(Helper.data_locale.CLOSE)
                    alert.close_dialog()

            # Options/Change perspective/Interactive
            case TopMenuItem.options_change_perspective_interactive:
                self.toolbar.click_btn_menu_by_test_id_wait_until_enabled(test_id,
                                                                          Helper.data_locale.CHANGE_PERSPECTIVE,
                                                                          Helper.data_locale.INTERACTIVE)
                alert = Alert(self.toolbar.page, Helper.data_locale.STUDIO_NEXT)
                if alert.is_open():
                    time.sleep(3)
                    # alert.close_alert_dialog(Helper.data_locale.CLOSE)
                    alert.close_dialog()

            # END Added by Jacky(ID: jawang) on Oct.30th, 2023 >>>

    def new_item(self, top_menu: TopMenuItem):
        test_id = "appHeaderToolbar-new-button"
        match top_menu:
            case TopMenuItem.new:
                self.toolbar.click_btn_by_test_id(test_id)
            case TopMenuItem.new_sas_program:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.SAS_PROGRAM)
            case TopMenuItem.new_python_program:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.PYTHON_PROGRAM)
            case TopMenuItem.new_flow:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.FLOW)
            case TopMenuItem.new_query:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.QUERY)
            case TopMenuItem.new_custom_step:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.CUSTOM_STEP)
            case TopMenuItem.new_quick_import:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.QUICK_IMPORT)
            case TopMenuItem.new_job_definition:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.JOB_DEFINITION)
            case TopMenuItem.new_file_types:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.MORE_FILE_TYPES)
            case TopMenuItem.new_file_types_json:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.MORE_FILE_TYPES,
                                                       Helper.data_locale.JSON)
            case TopMenuItem.new_file_types_text:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.MORE_FILE_TYPES,
                                                       Helper.data_locale.TEXT)
            case TopMenuItem.new_file_types_xml:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.MORE_FILE_TYPES,
                                                       Helper.data_locale.XML)
            case TopMenuItem.new_file_types_workspace:
                self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.MORE_FILE_TYPES,
                                                       Helper.data_locale.WORK_SPACE)

    def click_open_openfile(self, folder_path, file_name):
        self.toolbar.click_btn_by_test_id("appHeaderToolbar-open")
        time.sleep(1)
        open_file = OpenDialog(self.page)
        open_file.open_file(folder_path, file_name)

    def check_view_item(self, top_menu: TopMenuItem):
        """
        Original one
        On Aug.31st 2024, it was found that zh-CN strings for menu items were missing.
        """
        test_id = "appHeaderToolbar-view-button"
        match top_menu:
            case TopMenuItem.view:
                self.toolbar.click_btn_by_test_id(test_id)

            case TopMenuItem.view_submission_status:
                # Try
                # base.screenshot("//div[@data-testid='appHeaderToolbar-view-menu']", str(TopMenuItem.view), user_assigned_xpath=True)

                # Original
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.SUBMISSION_STATUS)

                # Work-Around: Missing zh-CN string
                # self.toolbar.check_btn_menu_by_test_id(test_id, Data.SUBMISSION_STATUS)

            case TopMenuItem.view_deployed_and_scheduled_jobs:

                # Original
                # self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.DEPLOYED_AND_SCHEDULED_JOBS)

                # Work-Around: Missing zh-CN string
                # self.toolbar.check_btn_menu_by_test_id(test_id, Data.DEPLOYED_AND_SCHEDULED_JOBS)

                # Changed on Wednesday, April 9, 2025,
                # Removal of this menu item
                Helper.logger.debug('Product Change: Removal of View -> Deployed and scheduled jobs')
                return

            case TopMenuItem.view_start_page:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.START_PAGE)
                # self.toolbar.check_btn_menu_by_test_id(test_id, "Start page")
            case TopMenuItem.view_startup_initialization_log:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.STARTUP_INITIALIZATION_LOG)
            case TopMenuItem.view_navigation_panes_open_items:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.OPEN_ITEMS)
            case TopMenuItem.view_navigation_panes_sas_server:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.SAS_SERVER)
            case TopMenuItem.view_navigation_panes_sas_content:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.SAS_CONTENT)
            case TopMenuItem.view_navigation_panes_steps:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.STEPS)
            case TopMenuItem.view_navigation_panes_snippets:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.SNIPPETS)
            case TopMenuItem.view_navigation_panes_library_connections:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.LIBRARY_CONNECTIONS)

            case TopMenuItem.view_navigation_panes_git_repositories:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.GIT_REPOSITORIES)
            case TopMenuItem.view_navigation_panes_file_references:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.FILE_REFERENCES)

            case TopMenuItem.view_navigation_panes_clinical_repositories:
                Helper.logger.debug('Product Change: Removal of View -> Navigation Pane -> Clinical Repository')
                return

                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Helper.data_locale.CLINICAL_REPOSITORY)
        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr. 9th, 2024

        # WRONG: Only toolbar was cathed
        # self.toolbar.screenshot_self('check_view_item')

        # Open menu to take screenshot
        # self.toolbar.click_btn_by_test_id(test_id)
        # base = BasePage(self.toolbar.page)
        # base.screenshot("//div[@data-testid='appHeaderToolbar-view-menu']", "check_view_item", user_assigned_xpath=True)

        # END Added by Jacky(ID: jawang) on Apr. 9th, 2024 >>>
        time.sleep(0.3)

    def check_view_item_zh_CN(self, top_menu: TopMenuItem):
        """
        Aug.31st 2024,
        src.Pages.StudioNext.Top.top_menu_page.TopMenuPage.check_view_item
        It was found that zh-CN strings for View/Navigation menu items were missing.
        """
        test_id = "appHeaderToolbar-view-button"
        match top_menu:
            case TopMenuItem.view:
                self.toolbar.click_btn_by_test_id(test_id)

            case TopMenuItem.view_submission_status:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.SUBMISSION_STATUS)
            case TopMenuItem.view_deployed_and_scheduled_jobs:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.DEPLOYED_AND_SCHEDULED_JOBS)
            case TopMenuItem.view_start_page:
                # self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.START_PAGE)
                self.toolbar.check_btn_menu_by_test_id(test_id, "Start page")
            case TopMenuItem.view_startup_initialization_log:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.STARTUP_INITIALIZATION_LOG)
            case TopMenuItem.view_navigation_panes_open_items:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "Open items")
            case TopMenuItem.view_navigation_panes_sas_server:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "SAS server")
            case TopMenuItem.view_navigation_panes_sas_content:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "SAS content")
            case TopMenuItem.view_navigation_panes_steps:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Data.STEPS)
            case TopMenuItem.view_navigation_panes_snippets:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       Data.SNIPPETS)
            case TopMenuItem.view_navigation_panes_library_connections:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "Library connections")

            case TopMenuItem.view_navigation_panes_git_repositories:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "Git repositories")
            case TopMenuItem.view_navigation_panes_file_references:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "File references")

            case TopMenuItem.view_navigation_panes_clinical_repositories:
                self.toolbar.check_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                       "Clinical repository")

        time.sleep(0.3)

    def uncheck_view_item(self, top_menu: TopMenuItem):
        test_id = "appHeaderToolbar-view-button"
        self.wait_until_enabled("//button[@data-testid='appHeaderToolbar-view-button']")
        time.sleep(1)
        match top_menu:
            case TopMenuItem.view:
                self.toolbar.click_btn_by_test_id(test_id)
            case TopMenuItem.view_submission_status:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.SUBMISSION_STATUS)
            case TopMenuItem.view_deployed_and_scheduled_jobs:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.DEPLOYED_AND_SCHEDULED_JOBS)
            case TopMenuItem.view_start_page:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.START_PAGE)
                # self.toolbar.uncheck_btn_menu_by_test_id(test_id, "Start page")
            case TopMenuItem.view_startup_initialization_log:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.STARTUP_INITIALIZATION_LOG)
            case TopMenuItem.view_navigation_panes_open_items:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.OPEN_ITEMS)
            case TopMenuItem.view_navigation_panes_sas_server:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.SAS_SERVER)
            case TopMenuItem.view_navigation_panes_sas_content:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.SAS_CONTENT)
            case TopMenuItem.view_navigation_panes_steps:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.STEPS)
            case TopMenuItem.view_navigation_panes_snippets:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.SNIPPETS)
            case TopMenuItem.view_navigation_panes_library_connections:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.LIBRARY_CONNECTIONS)

            case TopMenuItem.view_navigation_panes_git_repositories:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.GIT_REPOSITORIES)
            case TopMenuItem.view_navigation_panes_file_references:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.FILE_REFERENCES)

            case TopMenuItem.view_navigation_panes_clinical_repositories:
                self.toolbar.uncheck_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES,
                                                         Helper.data_locale.CLINICAL_REPOSITORY)
        time.sleep(0.3)

    def show_view_startup_initialization_log(self):
        test_id = "appHeaderToolbar-view-button"
        self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.STARTUP_INITIALIZATION_LOG)

    def show_document_recovery(self):
        test_id = "appHeaderToolbar-view-button"
        self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.DOCUMENT_RECOVERY)

    def click_menu_item_new(self):
        test_id = "appHeaderToolbar-new-button"
        self.toolbar.click_btn_by_test_id(test_id)
        self.toolbar.wait_for_page_load()

    def click_menu_item_options(self):
        test_id = "appHeaderToolbar-options-button"
        self.toolbar.click_btn_by_test_id(test_id)
        self.toolbar.wait_for_page_load()

    def click_menu_item_view(self):
        test_id = "appHeaderToolbar-view-button"
        self.toolbar.click_btn_by_test_id(test_id)
        self.toolbar.wait_for_page_load()

    def click_menu_item_open(self):
        test_id = "appHeaderToolbar-open"
        self.toolbar.click_btn_by_test_id(test_id)
        self.toolbar.wait_for_page_load()

    def click_menu_item_saveall(self):
        test_id = "appHeaderToolbar-saveall"
        self.toolbar.click_btn_by_test_id(test_id)

    def click_menu_item_view_navigation(self):
        test_id = "appHeaderToolbar-view-button"
        self.toolbar.click_btn_menu_by_test_id(test_id, Helper.data_locale.NAVIGATION_PANES)
