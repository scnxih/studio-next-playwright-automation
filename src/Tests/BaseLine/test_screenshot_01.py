import time

from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.conftest import *
from src.Helper.page_factory import *
def test_01_screenshot_new_centerpages(page, init):
    program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    program.click_more_options()
    WholePage(page).screenshot_trivial_self("program")

    python: PythonProgramPage = PageHelper.new_item(page, TopMenuItem.new_python_program)
    python.click_more_options()
    WholePage(page).screenshot_trivial_self("python")

    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.click_more_options()
    WholePage(page).screenshot_trivial_self("flow")

    query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)
    query.click_more_options()
    WholePage(page).screenshot_trivial_self("query")

    importpage: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    importpage.click_more_options()
    WholePage(page).screenshot_trivial_self("import")

    jsonpage: JsonPage = PageHelper.new_item(page, TopMenuItem.new_file_types_json)
    jsonpage.click_more_options()
    WholePage(page).screenshot_trivial_self("json")

    text: TextPage = PageHelper.new_item(page, TopMenuItem.new_file_types_text)
    text.click_more_options()
    WholePage(page).screenshot_trivial_self("text")

    xml: XMLPage = PageHelper.new_item(page, TopMenuItem.new_file_types_xml)
    xml.click_more_options()
    WholePage(page).screenshot_trivial_self("xml")

    workspace: WorkspacePage = PageHelper.new_item(page, TopMenuItem.new_file_types_workspace)
    workspace.click_more_options()
    WholePage(page).screenshot_trivial_self("workspace")

    job: JobDefinitionPage = PageHelper.new_item(page, TopMenuItem.new_job_definition)
    job.click_more_options()
    WholePage(page).screenshot_trivial_self("job")

    step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    step.click_more_options()
    WholePage(page).screenshot_trivial_self("step")

def test_02_top_menu(page,init):
    top_menu_page:TopMenuPage = TopMenuPage(page)
    top_menu_page.click_menu_item_new()
    time.sleep(1)
    WholePage(page).screenshot_trivial_self("new")
    top_menu_page.click_menu_item_options()
    time.sleep(1)
    WholePage(page).screenshot_trivial_self("options")
    top_menu_page.click_menu_item_view()
    time.sleep(1)
    WholePage(page).screenshot_trivial_self("view")
    top_menu_page.click_menu_item_open()
    time.sleep(1)
    open_dlg = OpenDialog(page)
    time.sleep(1)
    open_dlg.screenshot_trivial_self("open_dialog")
    open_dlg.close_dialog()
    time.sleep(1)
    WholePage(page).screenshot_trivial_self("close_open")

def test_03_navigation_panes(page,init):
    acc :AccordionPage = AccordionPage(page)
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

