"""
Author: Alice
Date: November 07, 2023
Description: This file includes functions which will create different pages.
"""

from typing import Dict
from typing import Type
from src.Pages.StudioNext.Center.center_page import CenterPage
from src.Pages.StudioNext.Dialog.about_dialog import AboutDialog
from src.Pages.StudioNext.Dialog.add_profile_dialog import AddProfileDialog
from src.Pages.StudioNext.Dialog.customcode_dialog import CustomCodeDialog
from src.Pages.StudioNext.Dialog.document_recovery_dialog import DocumentRecoveryDialog
from src.Pages.StudioNext.Dialog.keyboard_shortcuts_dialog import KeyboardShortcutsDialog
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import ManageGitConnectionDialog
from src.Pages.StudioNext.Dialog.manage_shortcuts_dialog import ManageShortcutsDialog
from src.Pages.StudioNext.Dialog.newfolder_dialog import NewFolderDialog
from src.Pages.StudioNext.Dialog.open_dialog import OpenDialog
from src.Pages.StudioNext.Dialog.query_output_lib_dialog import OutputLibDialog
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog
from src.Pages.StudioNext.Dialog.search_dialog import SearchDialog
from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Left.clinical_repository_page import ClinicalRepositoryPage
from src.Pages.StudioNext.Left.file_references_page import FileReferencesPage
from src.Pages.StudioNext.Left.git_repositories_page import GitRepositoriesPage
from src.Pages.StudioNext.Left.library_page import LibraryPage
from src.Pages.StudioNext.Left.openitems_page import OpenItemsPage
from src.Pages.StudioNext.Left.snippets_page import SnippetsPage
from src.Pages.StudioNext.Left.steps_page import StepsPage
from src.Utilities.enums import *
from playwright.sync_api import Page
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import CustomStepPage
from src.Pages.StudioNext.Center.deployed_scheduled_job_page import DeployedScheduledJobPage
from src.Pages.StudioNext.Center.job_definition_page import JobDefinitionPage
from src.Pages.StudioNext.Center.startup_initialization_log_page import StartupInitializationLogPage
from src.Pages.StudioNext.Center.workspace_page import WorkspacePage
from src.Pages.StudioNext.Center.xml_page import XMLPage
from src.Pages.StudioNext.Center.text_page import TextPage
from src.Pages.StudioNext.Center.json_page import JsonPage
from src.Pages.StudioNext.Center.Query.query_page import QueryPage
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Center.python_program_page import PythonProgramPage
from src.Pages.StudioNext.Center.quick_import_page import QuickImportPage
from src.Pages.StudioNext.Center.sas_program_page import SASProgramPage
from src.Pages.StudioNext.Center.submission_status_page import SubmissionStatusPage
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog
from src.Pages.StudioNext.Dialog.query_select_table_dialog import SelectTableDialog
from src.Pages.StudioNext.Left.sascontent_page import SASContentPage
from src.Pages.StudioNext.Left.sasserver_page import SASServerPage
from src.Pages.Common.dialog import *
from src.Pages.StudioNext.Left.accordion_page import AccordionPage


def get_center_page(page: Page, center_page_type: CenterPageType = CenterPageType.sas_program_page) -> CenterPage:
    """This is factory function to create center page"""
    created_page: Dict[center_page_type, Type[CenterPage]] = {
        CenterPageType.sas_program_page: SASProgramPage,
        CenterPageType.python_program_page: PythonProgramPage,
        CenterPageType.flow_page: FlowPage,
        CenterPageType.query_page: QueryPage,
        CenterPageType.quick_import_page: QuickImportPage,
        CenterPageType.json_page: JsonPage,
        CenterPageType.text_page: TextPage,
        CenterPageType.xml_page: XMLPage,
        CenterPageType.work_space_page: WorkspacePage,
        CenterPageType.deployed_scheduled_job_page: DeployedScheduledJobPage,
        CenterPageType.start_initialization_log_page: StartupInitializationLogPage,
        CenterPageType.submission_status_page: SubmissionStatusPage,
        CenterPageType.job_definition_page: JobDefinitionPage,
        CenterPageType.custom_step_page: CustomStepPage
    }
    return created_page[center_page_type](page)


def get_dialog_page(page: Page, dialog_type: DialogType) -> Dialog:
    created_dialog:Dict[dialog_type,Type[Dialog]] = {
        DialogType.about_dialog: AboutDialog,
        DialogType.add_profile_dialog: AddProfileDialog,
        DialogType.autoexec_dialog: AutoexecDialog,
        DialogType.custom_code_dialog: CustomCodeDialog,
        DialogType.document_recovery_dialog: DocumentRecoveryDialog,
        DialogType.keyboard_shortcuts_dialog: KeyboardShortcutsDialog,
        DialogType.manage_git_connection_dialog: ManageGitConnectionDialog,
        DialogType.manage_shortcuts_dialog: ManageShortcutsDialog,
        DialogType.new_folder_dialog: NewFolderDialog,
        DialogType.open_dialog: OpenDialog,
        DialogType.query_output_lib_dialog: OutputLibDialog,
        DialogType.query_select_table_dialog: SelectTableDialog,
        DialogType.save_as_dialog: SaveAsDialog,
        DialogType.search_dialog: SearchDialog,
        DialogType.settings_dialog: SettingsDialog
    }
    return created_dialog[dialog_type](page)


def get_accordion_page(page: Page, accordion_type: AccordionType) -> AccordionPage:
    created_page: Dict[accordion_type,Type[AccordionPage]] = {
        AccordionType.open_item: OpenItemsPage,
        AccordionType.sas_server: SASServerPage,
        AccordionType.sas_content: SASContentPage,
        AccordionType.steps: StepsPage,
        AccordionType.snippets: SnippetsPage,
        AccordionType.libraries: LibraryPage,
        AccordionType.git: GitRepositoriesPage,
        AccordionType.file_references: FileReferencesPage,
        AccordionType.clinical_repository: ClinicalRepositoryPage
    }
    return created_page[accordion_type](page)




