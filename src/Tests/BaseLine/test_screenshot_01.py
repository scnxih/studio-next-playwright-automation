"""
Author: Alice
Date: Mar 22, 2024
Description: This is the test case file for screenshots.
"""

from src.Pages.Common.menu_page import MenuPage
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.conftest import *
from src.Helper.page_factory import *
def test_init(page,init):
    PageHelper.init_environments(page)

def test_01_screenshot_new_centerpages_more_options(page, init):
    program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    program.click_more_options()

    # Always cause noises
    # //button[@data-testid="programViewPane-toolbar-snippet"]
    WholePage(page).screenshot_self("program",
                                    mask=['//button[@data-testid="programViewPane-toolbar-snippet"]'],
                                    mask_color='#000000')
    MenuPage(page).screenshot_self("program_more_options")

    python: PythonProgramPage = PageHelper.new_item(page, TopMenuItem.new_python_program)
    python.click_more_options()
    WholePage(page).screenshot_self("python")
    MenuPage(page).screenshot_self("python_more_options")

    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.click_more_options()
    WholePage(page).screenshot_self("flow")
    MenuPage(page).screenshot_self("flow_more_options")

    query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)
    query.click_more_options()
    WholePage(page).screenshot_self("query")
    MenuPage(page).screenshot_self("query_more_options")

    importpage: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    importpage.click_more_options()
    WholePage(page).screenshot_self("import")
    MenuPage(page).screenshot_self("import_more_options")

    jsonpage: JsonPage = PageHelper.new_item(page, TopMenuItem.new_file_types_json)
    jsonpage.click_more_options()
    WholePage(page).screenshot_self("json")
    MenuPage(page).screenshot_self("json_more_options")

    text: TextPage = PageHelper.new_item(page, TopMenuItem.new_file_types_text)
    text.click_more_options()

    # Original
    WholePage(page).screenshot_self("text")

    # Mask added
    WholePage(page).screenshot_self("text",
                                    mask=["//button[@type='button'][.//span[contains(text(), '" + Helper.data_locale.OPERATE_RECOVERY + "')]]",
                                          '//span[contains(@class,"BaseButton" )][contains(text(), "列")]',
                                          '//button[@data-testid="programViewPane-toolbar-runButton"]'],
                                    mask_color='#000000')

    MenuPage(page).screenshot_self("text_more_options")

    xml: XMLPage = PageHelper.new_item(page, TopMenuItem.new_file_types_xml)
    xml.click_more_options()
    WholePage(page).screenshot_self("xml")
    MenuPage(page).screenshot_self("xml_more_options")

    workspace: WorkspacePage = PageHelper.new_item(page, TopMenuItem.new_file_types_workspace)
    workspace.click_more_options()
    WholePage(page).screenshot_self("workspace")
    MenuPage(page).screenshot_self("workspace_more_options")

    job: JobDefinitionPage = PageHelper.new_item(page, TopMenuItem.new_job_definition)
    job.click_more_options()
    WholePage(page).screenshot_self("job")
    MenuPage(page).screenshot_self("job_more_options")

    step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    step.click_more_options()
    WholePage(page).screenshot_self("step")
    MenuPage(page).screenshot_self("step_more_options")


def test_02_screenshot_top_menu(page, init):
    top_menu_page: TopMenuPage = TopMenuPage(page)
    top_menu_page.click_menu_item_new()
    time.sleep(1)
    MenuPage(page).screenshot_self("new")
    top_menu_page.click_menu_item_options()
    time.sleep(1)
    MenuPage(page).screenshot_self("options")
    top_menu_page.click_menu_item_view()
    time.sleep(1)
    MenuPage(page).screenshot_self("view")
    top_menu_page.click_menu_item_open()
    time.sleep(1)
    open_dlg = OpenDialog(page)
    time.sleep(1)
    open_dlg.screenshot_self("open_dialog")
    open_dlg.close_dialog()
    time.sleep(1)
    WholePage(page).screenshot_self("close_open")


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
    acc.screenshot_self("open_item")
    acc.show_accordion(AccordionType.sas_server)
    time.sleep(1)
    acc.screenshot_self("sas_server")
    acc.show_accordion(AccordionType.sas_content)
    time.sleep(1)
    acc.screenshot_self("sas_content")
    acc.show_accordion(AccordionType.steps)
    time.sleep(1)
    acc.screenshot_self("steps")
    acc.show_accordion(AccordionType.snippets)
    time.sleep(1)
    acc.screenshot_self("snippets")
    acc.show_accordion(AccordionType.libraries)
    time.sleep(1)
    acc.screenshot_self("libraries")
    acc.show_accordion(AccordionType.git)
    time.sleep(1)
    acc.screenshot_self("git")
    acc.show_accordion(AccordionType.clinical_repository)
    time.sleep(1)
    acc.screenshot_self("clinical_repository")
    acc.show_accordion(AccordionType.file_references)
    time.sleep(1)
    acc.screenshot_self("file_reference")


def test_04_screenshot_top_menu_options(page, init):
    top_menu_page: TopMenuPage = TopMenuPage(page)
    top_menu_page.click_options(TopMenuItem.options_autoexec_file)
    time.sleep(1)
    auto = AutoexecDialog(page)

    # Original
    # auto.screenshot_self("auto_code")

    # Mask the switch button to eliminate diffs
    auto.screenshot_self("auto_code",
                         mask=[auto.btn_bgSubmission_switch],
                         mask_color="#000000")

    auto.click_tab_log()
    time.sleep(0.5)

    # Original
    # auto.screenshot_self("auto_log")

    auto.screenshot_self("auto_log",
                         mask=[auto.btn_bgSubmission_switch],
                         mask_color="#000000")

    auto.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_custom_code)
    time.sleep(1)
    cus = CustomCodeDialog(page)
    cus.screenshot_self("custom_pre")
    cus.click_tab_postamble()
    time.sleep(0.5)
    cus.screenshot_self("custom_post")
    cus.click_tab_option()
    time.sleep(0.5)
    cus.screenshot_self("custom_options")
    cus.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_manage_git_connections)
    git = ManageGitConnectionDialog(page)
    time.sleep(0.5)
    git.screenshot_self("git_profile")
    git.click_tab_repository()
    # Try to eliminate diff caused by focus indicator
    git.click_dialog_title_or_studionext_header()
    time.sleep(1.0)
    # //div[@data-testid="gitDialog-mgtConnection-spliter-splitterBar"]
    git.screenshot_self("git_repository")
    git.close_dialog()

    top_menu_page.click_options(TopMenuItem.options_manage_keyboard_shortcuts)
    short = ManageShortcutsDialog(page)
    short.screenshot_self("shortcut")
    short.close_dialog()


def test_05_screenshot_top_menu_view(page, init):
    top = TopMenuPage(page)
    top.check_view_item(TopMenuItem.view_submission_status)

    # Mask the icon to eliminate noises
    # //div[@class="sas_components-SearchField-SearchField_search-button-container"]
    WholePage(page).screenshot_self("submission_status",
                                    mask=[
                                        '//div[@class="sas_components-SearchField-SearchField_search-button-container"]'],
                                    mask_color="#000000")

    top.check_view_item(TopMenuItem.view_deployed_and_scheduled_jobs)

    # Original
    # WholePage(page).screenshot_self("deployed_and_scheduled_jobs")

    # Added Mask and Mask Color
    WholePage(page).screenshot_self("deployed_and_scheduled_jobs",
                                    # mask=['//div[@data-testid="scheduledJobsPane-lastRefreshLabel"]'], # Changed
                                    mask=[
                                        '//div[@data-testid="scheduledJobsPane-monitoringTab-agGrid"]',
                                        '//div[@data-testid="scheduledJobsPane-monitoringTab-lastRefreshLabel"]'
                                    ],
                                    mask_color="#000000")

    top.uncheck_view_item(TopMenuItem.view_start_page)
    top.check_view_item(TopMenuItem.view_start_page)

    # Oritinal
    # WholePage(page).screenshot_self("start")

    # Mask recent files listed on the RHS
    # xpath for mask: //div[@class='sas_components-views-StartViewPane-RightView_welcome-container']
    WholePage(page).screenshot_self("start",
                                    mask=[
                                        "//div[@class='sas_components-views-StartViewPane-RightView_welcome-container']"],
                                    mask_color="#000000")

    top.check_view_item(TopMenuItem.view_startup_initialization_log)

    # Original
    # WholePage(page).screenshot_self("init")

    # Added mask for time displayed in log
    # Note: class value in xpath
    CenterPage(page).screenshot_self("times",
                                     mask=['//span[@class="mtk1"][contains(text(),"CPU")]/..',
                                           '//span[@class="mtk1"][contains(text(),"实际")]/..'],
                                     mask_color="#000000")

    top.show_document_recovery()
    doc = DocumentRecoveryDialog(page)
    time.sleep(1)

    # Original
    # doc.screenshot_self("document")

    '''
    # ONLY mask the first row
    doc.screenshot_self("document",
                        mask=['//div[@role="gridcell"][@col-id="dateModified"][contains(text(),"年")]'],
                        mask_color="#000000")
    '''

    # Hide the files listed in the dialog, since these seem to be used for demonstration ONLY
    doc.screenshot_self("document",
                        mask=[
                            '//div[@role="row"][@row-index="3"][@aria-rowindex="5"][contains(@row-id, "Public")]',
                            '//div[@role="row"][@row-index="2"][@aria-rowindex="4"][contains(@row-id, "Public")]',
                            '//div[@role="row"][@row-index="1"][@aria-rowindex="3"][contains(@row-id, "Public")]',
                            '//div[@role="row"][@row-index="0"][@aria-rowindex="2"][contains(@row-id, "Public")]'],
                        mask_color="#000000")

    doc.close_dialog()

    top.click_menu_item_view_navigation()
    time.sleep(0.5)

    MenuPage(page, data_test_id="appHeaderToolbar-navigationPanes-menu-content").screenshot_self("navigation")


def test_06_screenshot_top_right_items(page, init):
    p: Page = page
    top = TopRightToolbar(page)
    top.click_search()
    time.sleep(1)

    # Dialog(page).screenshot_self("search")

    # //div[@data-testid='qa-testId-quick-access']
    Dialog(page).screenshot_self("search",
                                 mask=["//div[@data-testid='qa-testId-quick-access']"],
                                 mask_color="#000000")

    Dialog(page).close_dialog()

    top.click_unread_notifications()
    time.sleep(1)
    Dialog(page).screenshot_self("unread_notification")
    Dialog(page).close_dialog()

    top.click_help()
    time.sleep(1)
    WholePage(page).screenshot_self("help")

    time.sleep(1)
    top.click_new_features()
    time.sleep(2)
    Dialog(page).screenshot_self("new_features")

    Dialog(page).close_dialog()

    top.click_about()
    time.sleep(2)
    # Dialog(page).screenshot_self("about")
    Dialog(page).screenshot_self("about",
                                 mask=['//span[@id="release_sas_RC-about-field-0"]',
                                       '//span[@id="site-number_sas_RC-about-field-0"]'],
                                 mask_color="#000000")
    Dialog(page).close_dialog()

    top.click_manage_features()
    time.sleep(2)
    Dialog(page).screenshot_self("manage_features")
    Dialog(page).screenshot_self("manage_features_clip",
                                 clip={'x': 196, 'y': 136, 'width': 1113, 'height': 679})

    Dialog(page).close_dialog()

    top.click_user_option()
    time.sleep(2)
    WholePage(page).screenshot_self("user_option")


def test_07_mask(page, init):
    top_menu_page = TopMenuPage(page)
    top_menu_page.click_options(TopMenuItem.options_custom_code)
    time.sleep(1)
    cus = CustomCodeDialog(page)
    cus.screenshot_self("custom_pre", mask=[cus.tab_Code, cus.tab_log, cus.tab_preamble, cus.btn_save])
    cus.screenshot_self("custom_pre", mask=[cus.tab_Code, cus.tab_log, cus.tab_preamble, cus.btn_save])
    cus.screenshot_self("custom_pre", mask=[cus.tab_Code, cus.tab_log, cus.tab_preamble, cus.btn_save])
    cus.close_dialog()


# def test_08_full_page(page, init):
#     p:Page = page
#     top = TopRightToolbar(page)
#     top.click_manage_features()
#     time.sleep(2)
#     Dialog(page).screenshot_self("manage_features")
#     BasePage(page).screenshot_full_page("full_page")
#     Dialog(page).close_dialog()
#
#     top = TopMenuPage(page)
#
#
#     top.check_view_item(TopMenuItem.view_start_page)
#     WholePage(page).screenshot_self("start")
#     BasePage(page).screenshot_full_page("start_full")
#
#
#     top.check_view_item(TopMenuItem.view_startup_initialization_log)
#     WholePage(page).screenshot_self("init")
#     BasePage(page).screenshot_full_page("init_full")
#     p.screenshot(path="C:\studio-next-playwright-automation\src\Output\screenshot_01_08\init_full_AAA.png",
#                  full_page=True)

# Comment this since sas server is not working fine, will run this once sas server is ready.
# def test_08_accordion_sas_server(page, init):
#     dialog: Dialog = Dialog(page)
#     base: BasePage = BasePage(page)
#     whole: WholePage = WholePage(page)
#     PageHelper.show_accordion(page, AccordionType.sas_server)
#     sas_server = SASServerPage(page)
#     folder_path: list = ["SAS Server", "Home", "segatest", "I18N", "自动化测试_SASCompute"]
#     element = sas_server.navigate_to_folder_or_file(folder_path)
#
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("folder_context_menu")
#     base.click_menu_item(Helper.data_locale.NEW_FOLDER)
#     time.sleep(2)
#     dialog.screenshot_self("new_folder")
#     dialog.close_dialog()
#
#     sas_server.navigate_and_click_context_menu_on_folder_or_file(folder_path, Helper.data_locale.PROPERTIES)
#     time.sleep(2)
#     dialog.screenshot_self("folder_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("创建dataset代码.log")
#
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("log_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("log_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("AB.xlsx")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("xlsx_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("xlsx_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("class.sas7bdat")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("sasdata_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("sasdata_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("CHClass.csv")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("csv_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("csv_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("AB.txt")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("txt_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("txt_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("CLASS.tsv")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("tsv_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("tsv_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("CLASS_EN.dlm")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("dlm_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("dlm_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("CLASS_GB2312.tab")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("tab_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("tab_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("class_中文.jmp")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("jmp_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("jmp_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("等待5分钟.sas")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("sas_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("sas_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("测试流.flw")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("flow_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("flow_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("查询.cqy")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("query_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("query_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("Python.py")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("python_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("python_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("饼图.ctk")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("ctk_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("ctk_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("中文测试数据.xls")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("xls_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("xls_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("导入.ctl")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("ctl_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("ctl_properties")
#     dialog.close_dialog()
#
#     file_path = folder_path.copy()
#     file_path.append("创建dataset代码.html")
#     element = sas_server.navigate_to_folder_or_file(file_path)
#     base.right_click(element)
#     time.sleep(2)
#     whole.screenshot_self("html_context_menu")
#     base.click_menu_item(Helper.data_locale.PROPERTIES)
#     # time.sleep(2)
#     whole.screenshot_self("html_properties")
#     dialog.close_dialog()
#
#     sas_server.click_more_options()
#     time.sleep(2)
#     whole.screenshot_self("more_options")
#     sas_server.click_more_options()
#     time.sleep(2)
#     sas_server.show_column_settings()


def test_09_accordion_steps(page, init):
    dialog: Dialog = Dialog(page)
    base: BasePage = BasePage(page)
    whole: WholePage = WholePage(page)
    PageHelper.show_accordion(page, AccordionType.steps)
    time.sleep(1)
    whole.screenshot_self("steps_pane")
    steps = StepsPage(page)
    # steps.new(NewStepsType.quick_start)
    # steps.new(NewStepsType.sample_controls)
    # steps.new(NewStepsType.basic_rank)
    # steps.new(NewStepsType.advanced_rank)
    # steps.new(NewStepsType.advanced_define_column_structure)
    # steps.show_menu_starter_templates()
    # time.sleep(1)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA, Helper.data_locale.STEP_TABLE]
    steps.navigate_to_step(step_path)

    # Original
    AccordionPage(page).screenshot_self("Data")

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Data_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DATA_QUALITY, Helper.data_locale.STEP_PARSE_DATA]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Data_Quality")
    AccordionPage(page).screenshot_self("Data_Quality",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_PYTHON_PROGRAM]
    steps.navigate_to_step(step_path)
    AccordionPage(page).screenshot_self("Develop")
    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Develop_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ECONOMETRICS, Helper.data_locale.STEP_CAUSAL_MODELS]
    steps.navigate_to_step(step_path)
    AccordionPage(page).screenshot_self("Econometrics")

    step_path: list = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_PHONE_NUMBERS]
    steps.navigate_to_step(step_path)
    AccordionPage(page).screenshot_self("Enrichment")

    step_path: list = [Helper.data_locale.STEP_CATEGORY_EXAMINE_DATA, Helper.data_locale.STEP_LIST_TABLE_ATTRIBUTES]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Examine_Data")
    AccordionPage(page).screenshot_self("Examine_Data",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_INTEGRATE, Helper.data_locale.STEP_MERGE_TABLE]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Merge_Table")
    AccordionPage(page).screenshot_self("Merge_Table",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MACHINE_LEARNING,
                       Helper.data_locale.STEP_ROBUST_PRINCIPAL_COMPONENT_ANALYSIS]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Machine_Learning")
    AccordionPage(page).screenshot_self("Machine_Learning",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Machine_Learning_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_MANAGE_MODELS,
                       Helper.data_locale.STEP_REGISTER_PYTHON_MODEL]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Register_Python")
    AccordionPage(page).screenshot_self("Register_Python",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Register_Python_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_OPTIMIZATION_AND_NETWORK_ANALYSIS,
                       Helper.data_locale.STEP_CORE_DECOMPOSITION]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Core")
    AccordionPage(page).screenshot_self("Core",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Core_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_PREPARE_AND_EXPLORE_DATA,
                       Helper.data_locale.STEP_STANDARDIZE_DATA]
    steps.navigate_to_step(step_path)

    # AccordionPage(page).screenshot_self("Standardize_Data")
    AccordionPage(page).screenshot_self("Standardize_Data",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Standardize_Data_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICAL_PROCESS_CONTROL,
                       Helper.data_locale.STEP_PARETO_ANALYSIS]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Pareto")
    AccordionPage(page).screenshot_self("Pareto",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Pareto_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_STATISTICS,
                       Helper.data_locale.STEP_MULTIDIMENSIONAL_PREFERENCE_ANALYSIS]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Multidimensional")
    AccordionPage(page).screenshot_self("Multidimensional",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Multidimensional_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_TRANSFORM_DATA,
                       Helper.data_locale.STEP_TRANSPOSE_DATA]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Transpose")
    AccordionPage(page).screenshot_self("Transpose",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Transpose_Narrow",
    #                                user_assigned_xpath=True)

    step_path: list = [Helper.data_locale.STEP_CATEGORY_VISUALIZE_DATA,
                       Helper.data_locale.STEP_TEXT_MAP]
    steps.navigate_to_step(step_path)
    # AccordionPage(page).screenshot_self("Text_Map")
    AccordionPage(page).screenshot_self("Text_Map",
                                        mask=[AccordionPage(page).ag_body_vertical_scroll_bar],
                                        mask_color='#000000')

    # AccordionPage(page).screenshot(AccordionPage(page).get_by_test_id("sasstepsNavPane-agGrid"),
    #                                "Text_Map_Narrow",
    #                                user_assigned_xpath=True)


def test_10_flow_details_pane(page, init):
    """
    Test flow detail pane screenshots.
    This is the same as src.Tests.Flow.test_flow_03_canvas_operations.test_04_details_pane_table
    """
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.table)

    # Fow overflow menu changed
    # flow.apply_detail_layout_vertical()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_vertical()
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    time.sleep(1)
    table = TablePane(page)
    table.set_library("sashelp")
    time.sleep(1)
    table.set_table("class")
    time.sleep(1)
    table.set_node_name("class表")
    time.sleep(1)
    table.set_node_description("这是sashelp.class表。")
    time.sleep(1)
    table.set_notes("这是sashelp.class表的注释信息。")
    time.sleep(1)
    table.preview_data()
    time.sleep(1)
    table.refresh_table()
