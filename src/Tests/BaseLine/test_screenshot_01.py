"""
Author: Alice
Date: Mar 22, 2024
Description: This is the test case file for screenshots.
"""

import time

from src.Pages.Common.menu_page import MenuPage
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.conftest import *
from src.Helper.page_factory import *


def test_01_screenshot_new_centerpages_more_options(page, init):
    program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    program.click_more_options()
    WholePage(page).screenshot_trivial_self("program")
    MenuPage(page).screenshot_trivial_self("program_more_options")

    python: PythonProgramPage = PageHelper.new_item(page, TopMenuItem.new_python_program)
    python.click_more_options()
    WholePage(page).screenshot_trivial_self("python")
    MenuPage(page).screenshot_trivial_self("python_more_options")

    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.click_more_options()
    WholePage(page).screenshot_trivial_self("flow")
    MenuPage(page).screenshot_trivial_self("flow_more_options")

    query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)
    query.click_more_options()
    WholePage(page).screenshot_trivial_self("query")
    MenuPage(page).screenshot_trivial_self("query_more_options")

    importpage: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    importpage.click_more_options()
    WholePage(page).screenshot_trivial_self("import")
    MenuPage(page).screenshot_trivial_self("import_more_options")

    jsonpage: JsonPage = PageHelper.new_item(page, TopMenuItem.new_file_types_json)
    jsonpage.click_more_options()
    WholePage(page).screenshot_trivial_self("json")
    MenuPage(page).screenshot_trivial_self("json_more_options")

    text: TextPage = PageHelper.new_item(page, TopMenuItem.new_file_types_text)
    text.click_more_options()
    WholePage(page).screenshot_trivial_self("text")
    MenuPage(page).screenshot_trivial_self("text_more_options")

    xml: XMLPage = PageHelper.new_item(page, TopMenuItem.new_file_types_xml)
    xml.click_more_options()
    WholePage(page).screenshot_trivial_self("xml")
    MenuPage(page).screenshot_trivial_self("xml_more_options")

    workspace: WorkspacePage = PageHelper.new_item(page, TopMenuItem.new_file_types_workspace)
    workspace.click_more_options()
    WholePage(page).screenshot_trivial_self("workspace")
    MenuPage(page).screenshot_trivial_self("workspace_more_options")

    job: JobDefinitionPage = PageHelper.new_item(page, TopMenuItem.new_job_definition)
    job.click_more_options()
    WholePage(page).screenshot_trivial_self("job")
    MenuPage(page).screenshot_trivial_self("job_more_options")

    step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    step.click_more_options()
    WholePage(page).screenshot_trivial_self("step")
    MenuPage(page).screenshot_trivial_self("step_more_options")


def test_02_screenshot_top_menu(page, init):
    top_menu_page: TopMenuPage = TopMenuPage(page)
    top_menu_page.click_menu_item_new()
    time.sleep(1)
    MenuPage(page).screenshot_trivial_self("new")
    top_menu_page.click_menu_item_options()
    time.sleep(1)
    MenuPage(page).screenshot_trivial_self("options")
    top_menu_page.click_menu_item_view()
    time.sleep(1)
    MenuPage(page).screenshot_trivial_self("view")
    top_menu_page.click_menu_item_open()
    time.sleep(1)
    open_dlg = OpenDialog(page)
    time.sleep(1)
    open_dlg.screenshot_trivial_self("open_dialog")
    open_dlg.close_dialog()
    time.sleep(1)
    WholePage(page).screenshot_trivial_self("close_open")


def test_03_screenshot_navigation_panes(page, init):
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_file_references)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_open_items)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_snippets)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_steps)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_sas_server)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_sas_content)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_library_connections)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_git_repositories)
    TopMenuPage(page).check_view_item(TopMenuItem.view_navigation_panes_clinical_repositories)

    acc: AccordionPage = AccordionPage(page)
    acc.show_accordion(AccordionType.open_item)
    time.sleep(1)
    acc.screenshot_trivial_self("open_item")
    acc.show_accordion(AccordionType.sas_server)
    time.sleep(1)
    acc.screenshot_trivial_self("sas_server")
    acc.show_accordion(AccordionType.sas_content)
    time.sleep(1)
    acc.screenshot_trivial_self("sas_content")
    acc.show_accordion(AccordionType.steps)
    time.sleep(1)
    acc.screenshot_trivial_self("steps")
    acc.show_accordion(AccordionType.snippets)
    time.sleep(1)
    acc.screenshot_trivial_self("snippets")
    acc.show_accordion(AccordionType.libraries)
    time.sleep(1)
    acc.screenshot_trivial_self("libraries")
    acc.show_accordion(AccordionType.git)
    time.sleep(1)
    acc.screenshot_trivial_self("git")
    acc.show_accordion(AccordionType.clinical_repository)
    time.sleep(1)
    acc.screenshot_trivial_self("clinical_repository")
    acc.show_accordion(AccordionType.file_references)
    time.sleep(1)
    acc.screenshot_trivial_self("file_reference")


def test_04_screenshot_top_menu_options(page, init):
    top_menu_page: TopMenuPage = TopMenuPage(page)
    top_menu_page.click_options(TopMenuItem.options_autoexec_file)
    time.sleep(1)
    auto = AutoexecDialog(page)
    auto.screenshot_trivial_self("auto_code")
    auto.click_tab_log()
    time.sleep(0.5)
    auto.screenshot_trivial_self("auto_log")
    auto.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_custom_code)
    time.sleep(1)
    cus = CustomCodeDialog(page)
    cus.screenshot_trivial_self("custom_pre")
    cus.click_tab_postamble()
    time.sleep(0.5)
    cus.screenshot_trivial_self("custom_post")
    cus.click_tab_option()
    time.sleep(0.5)
    cus.screenshot_trivial_self("custom_options")
    cus.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_manage_git_connections)
    git = ManageGitConnectionDialog(page)
    time.sleep(0.5)
    git.screenshot_trivial_self("git_profile")
    git.click_tab_repository()
    git.screenshot_trivial_self("git_repository")
    git.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_manage_keyboard_shortcuts)
    short = ManageShortcutsDialog(page)
    short.screenshot_trivial_self("shortcut")
    short.close_dialog()


def test_05_screenshot_top_menu_view(page, init):
    top = TopMenuPage(page)
    top.check_view_item(TopMenuItem.view_submission_status)
    WholePage(page).screenshot_trivial_self("submission_status")

    top.check_view_item(TopMenuItem.view_deployed_and_scheduled_jobs)
    WholePage(page).screenshot_trivial_self("submission_status")

    top.uncheck_view_item(TopMenuItem.view_start_page)
    top.check_view_item(TopMenuItem.view_start_page)
    WholePage(page).screenshot_trivial_self("start")

    top.check_view_item(TopMenuItem.view_startup_initialization_log)
    WholePage(page).screenshot_trivial_self("init")

    top.show_document_recovery()
    doc = DocumentRecoveryDialog(page)
    time.sleep(1)
    doc.screenshot_trivial_self("document")
    doc.close_dialog()

    top.click_menu_item_view_navigation()
    time.sleep(0.5)

    MenuPage(page, data_test_id="appHeaderToolbar-navigationPanes-menu-content").screenshot_trivial_self("navigation")


def test_06_screenshot_top_right_items(page, init):
    p: Page = page
    top = TopRightToolbar(page)
    top.click_search()
    time.sleep(1)
    Dialog(page).screenshot_trivial_self("search")

    Dialog(page).close_dialog()

    top.click_unread_notifications()
    time.sleep(1)
    Dialog(page).screenshot_trivial_self("unread_notification")
    Dialog(page).close_dialog()

    top.click_help()
    time.sleep(1)
    WholePage(page).screenshot_trivial_self("help")

    time.sleep(1)
    top.click_new_features()
    time.sleep(2)
    Dialog(page).screenshot_trivial_self("new_features")
    Dialog(page).close_dialog()

    top.click_about()
    time.sleep(2)
    Dialog(page).screenshot_trivial_self("about")
    Dialog(page).close_dialog()

    top.click_manage_features()
    time.sleep(2)
    Dialog(page).screenshot_trivial_self("manage_features")
    Dialog(page).close_dialog()

    top.click_user_option()
    time.sleep(2)
    WholePage(page).screenshot_trivial_self("user_option")


def test_07_mask(page, init):
    top_menu_page = TopMenuPage(page)
    top_menu_page.click_options(TopMenuItem.options_custom_code)
    time.sleep(1)
    cus = CustomCodeDialog(page)
    cus.screenshot_trivial_self("custom_pre", mask=[cus.tab_Code,cus.tab_log,cus.tab_preamble,cus.btn_save])
    cus.screenshot_trivial_self("custom_pre", mask=[cus.tab_Code, cus.tab_log, cus.tab_preamble, cus.btn_save])
    cus.screenshot_trivial_self("custom_pre", mask=[cus.tab_Code, cus.tab_log, cus.tab_preamble, cus.btn_save])
    cus.close_dialog()
