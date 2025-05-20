from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.codeeditor_page import CodeEditorPage
from src.Pages.StudioNext.Center.custom_step_page_test import CustomStepPageTest
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.conftest import *
from src.Helper.page_factory import *
from playwright.sync_api import Page, expect
from src.Pages.StudioNext.Center.start_page import StartPage
from src.Pages.StudioNext.Center.Query.columns_pane import Columns


def test_init(page, init):
    PageHelper.init_environments(page)


@pytest.mark.xfail(reason="Enabled import local files")
def test_01_import_local_files(page, init):
    """
    """
    quick_import: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    quick_import.wait_for_page_load()
    expect(quick_import.get_by_test_id("zeroStateLocalFile")).not_to_be_enabled(enabled=False, timeout=1000)


@pytest.mark.xfail(reason="Enabled details switch")
def test_02_import_details_button(page, init):
    """
    """
    quick_import: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    quick_import.wait_for_page_load()
    expect(quick_import.get_by_test_id("importViewPane-toolbar-toggle-detail-layout-button")).not_to_be_visible(
        timeout=1000)


@pytest.mark.xfail(reason="Run an empty SAS Program settings")
def test_03_run_empty_sas_program(page, init):
    """
    Several buttons & functions will be disabled for an empty sas program
    """
    PageHelper.new_sas_program(page)

    editor = CodeEditorPage(page)
    editor.wait_for_page_load()

    editor.editor.type_into_text_area("data null; call sleep(60,1);run;")

    editor.run(if_wait_run_enabled=False, if_wait_toast_disappear=False)
    expect(editor.toolbar.btn_by_title(Helper.data_locale.CANCEL)).not_to_be_enabled(enabled=True, timeout=1000)


@pytest.mark.xfail(reason='Submission and Job Status')
def test_04_submission_and_job_status(page, init):
    PageHelper.show_submission_status(page)
    deployed_and_scheduled_jobs_page: DeployedScheduledJobPage = PageHelper.new_item(page,
                                                                                     TopMenuItem.view_deployed_and_scheduled_jobs)

    deployed_and_scheduled_jobs_page.tab_monitoring_jobs.click()
    expect(deployed_and_scheduled_jobs_page.mask_last_refresh_label).not_to_be_enabled(enabled=False, timeout=1000)


@pytest.mark.xfail(reason='Submission and Job Status')
def test_05_submission_and_job_status(page, init):
    PageHelper.show_submission_status(page)
    deployed_and_scheduled_jobs_page: DeployedScheduledJobPage = PageHelper.new_item(page,
                                                                                     TopMenuItem.view_deployed_and_scheduled_jobs)

    deployed_and_scheduled_jobs_page.tab_deployed_jobs.click()
    expect(deployed_and_scheduled_jobs_page.get_by_test_id("scheduledJobsPane-runNowButton")).to_be_enabled(
        enabled=True, timeout=1000)


@pytest.mark.xfail(reason='Submission and Job Status')
def test_06_submission_and_job_status(page, init):
    PageHelper.show_submission_status(page)
    submission_status = SubmissionStatusPage(page)
    submission_status.wait_for_page_load()

    expect(submission_status.btn_clear_all).to_be_enabled(enabled=True, timeout=1000)


@pytest.mark.xfail(reason='Query')
def test_07_query_add_a_table(page, init):
    """

    """
    query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)

    query.wait_for_page_load()
    expect(query.btn_add_table_zero).not_to_be_enabled(enabled=False, timeout=1000)


@pytest.mark.xfail(reason='Query')
def test_08_query_add_a_table(page, init):
    """

    """
    query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)
    query.wait_for_page_load()

    expect(Columns(page).btn_search).to_be_visible(visible=True, timeout=1000)


@pytest.mark.xfail(reason='Start page is derived of toolbar')
def test_09_start_page_elements(page, init):
    """

    """
    start_page = PageHelper.show_start_page(page)

    start_page.wait_for_page_load()

    expect(start_page.toolbar.btn_by_title(Helper.data_locale.RUN)).not_to_be_visible()


@pytest.mark.xfail(reason="Invisible [format program] button")
def test_09_startup_init_log(page, init):
    startup_page = PageHelper.show_view_startup_initialization_log(page)
    startup_page.wait_for_page_load()

    (expect(startup_page.toolbar.btn_by_title(Helper.data_locale.FORMAT_PROGRAM)).
     to_be_visible(visible=True, timeout=1000))


@pytest.mark.xfail(reason="Disabled [format program] button")
def test_10_custom_steps_zero_state(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_custom_step)

    custom_step_page = CustomStepPageTest(page)
    custom_step_page.wait_for_page_load()

    (expect(custom_step_page.toolbar.btn_by_title(Helper.data_locale.FORMAT_PROGRAM)).
     to_be_enabled(enabled=True, timeout=1000))


@pytest.mark.xfail(reason="Enabled [format program] button")
def test_11_custom_steps_zero_state(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_custom_step)

    custom_step_page = CustomStepPageTest(page)
    custom_step_page.wait_for_page_load()

    custom_step_page.tab_group.click_tab_by_text(Helper.data_locale.JSON)
    custom_step_page.wait_for_page_load()

    (expect(custom_step_page.toolbar.btn_by_title(Helper.data_locale.FORMAT_PROGRAM)).
     not_to_be_enabled(enabled=False, timeout=1000))


@pytest.mark.xfail(reason="Enabled [format program] button")
def test_12_custom_steps_zero_state(page, init):
    top_menu = TopMenuPage(page)
    top_menu.new_item(TopMenuItem.new_custom_step)

    custom_step_page = CustomStepPageTest(page)
    custom_step_page.wait_for_page_load()

    custom_step_page.tab_group.click_tab_by_text(Helper.data_locale.CUSCODE_PROGRAM)
    custom_step_page.wait_for_page_load()

    (expect(custom_step_page.toolbar.btn_by_title(Helper.data_locale.FORMAT_PROGRAM)).
     not_to_be_enabled(enabled=False, timeout=1000))


@pytest.mark.xfail(reason="Disabled [redo] button")
def test_13_json_zero_state(page, init):
    json: JsonPage = PageHelper.new_item(page, TopMenuItem.new_file_types_json)
    json.editor.type_into_text_area('''{"type":"json file","name":"json example"}''')
    json.wait_for_page_load()
    expect(json.toolbar.btn_by_title(Helper.data_locale.REDO)).to_be_enabled(enabled=True, timeout=1000)


@pytest.mark.xfail(reason="Disabled [format program] button")
def test_14_work_space_zero_state(page, init):
    work_space: WorkspacePage = PageHelper.new_item(page, TopMenuItem.new_file_types_workspace)
    work_space.wait_for_page_load()
    expect(work_space.toolbar.btn_by_title(Helper.data_locale.FORMAT_PROGRAM)).to_be_enabled(enabled=True, timeout=1000)


@pytest.mark.xfail(reason="Disabled [save as] button")
def test_15_txt_page_zero_state(page, init):
    text: TextPage = PageHelper.new_item(page, TopMenuItem.new_file_types_text)
    text.wait_for_page_load()
    expect(text.toolbar.btn_by_title(Helper.data_locale.SAVE_AS)).not_to_be_enabled(enabled=False, timeout=1000)


@pytest.mark.xfail(reason="Disabled [save all] button")
def test_16_close_all_tabs(page, init):
    PageHelper.new_all_items(page)

    acc: AccordionPage = AccordionPage(page)
    acc.show_accordion(AccordionType.open_item)

    open_items = OpenItemsPage(page)
    expect(open_items.btn_saveall()).to_be_enabled(enabled=True, timeout=3000)


@pytest.mark.xfail(reason="Insufficient SAS Program settings")
def test_17_empty_sas_program(page, init):
    """
    Several buttons & functions will be disabled for an empty sas program
    """
    PageHelper.new_sas_program(page)

    editor = CodeEditorPage(page)
    editor.wait_for_page_load()

    # DISABLED Cancel button for an empty program
    expect(editor.toolbar.btn_by_title(Helper.data_locale.CANCEL)).to_be_enabled(timeout=3000)


@pytest.mark.xfail(reason="Insufficient Flow settings")
def test_18_empty_flow(page, init):
    """
    JIRA Story: SASSTUDIO-28198 Finalize Flow Toolbar
    Figma UX Design: https://www.figma.com/design/4MylsH8qoEi8wX5NJAZkW5/Flow-Framework?node-id=801-15871&t=SR2JKFDk6mcwaxNp-0

    """
    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.wait_for_page_load(page)

    expect(flow.toolbar.btn_by_title(Helper.data_locale.RUN)).to_be_enabled(enabled=True, timeout=3000)


@pytest.mark.xfail(reason="Insufficient Import File settings")
def test_19_empty_import(page, init):
    # Step-1: Open Settings dialog
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    settings_dialog = SettingsDialog(page)

    # Step-2: First switch to other tab pages to verify normality
    settings_dialog.enable_pdf_output()
    settings_dialog.close_dialog()

    # Step-3:Download PDF of Import File
    quick_import: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    quick_import.wait_for_page_load()

    expect(quick_import.toolbar.btn_by_title(Helper.data_locale.CANCEL)).to_be_enabled(enabled=True, timeout=3000)


@pytest.mark.xfail(reason="App name changed for upcoming release")
def test_21_app_name_change_for_new_release(page, init):
    """
    Removal of the word 'Next' from App heading for the upcoming release.
    Check out SASSTUDIO-44771 on JIRA for details
    """

    # WholePage(page).locator("//span[text()='{0}']".format(Helper.data_locale.STUDIO_NEXT_DEV_CODE_AND_FLOW))
    WholePage(page).wait_for_page_load()
    expect(WholePage(page).locator("//span[text()='{0}']".format(Helper.data_locale.STUDIO_NEXT_DEV_CODE_AND_FLOW))).not_to_be_visible()


@pytest.mark.xfail(reason="Pre-requisite in Settings dialog for file-downloading")
def test_22_download_import_with_default_setting(page, init):
    """
    Tuesday, May 6, 2025,
    Default status changed to DISABLED for downloading word/excel/rtf/pdf... in overflow menu
    """
    quick_import: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)

    quick_import.toolbar.btn_by_title(Helper.data_locale.MORE_OPTIONS).click()
    (expect(quick_import.toolbar.get_by_test_id("importViewPane-toolbar-download-wordFile-text"))
     .to_be_enabled(enabled=True, timeout=1000))