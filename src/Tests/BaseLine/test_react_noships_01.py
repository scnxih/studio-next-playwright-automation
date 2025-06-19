import time

from src.Helper.page_helper import PageHelper, Helper
from src.Pages.Common.login_page import LoginPage
from src.Pages.Common.singed_out_page import SignedOutPage
from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import TopMenuItem, FlowNodeType, AccordionType
from playwright.sync_api import expect
from src.Pages.Common.dialog import Alert
from src.Pages.StudioNext.Center.start_page import StartPage
from src.Pages.StudioNext.Center.main_center_page import MainCenterPage


def test_init(page, init):
    PageHelper.init_environments(page)


def test_01_logout_wo_save(page, init):
    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.add_node(FlowNodeType.table)

    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)

    top_right.click_sign_out()

    alert = Alert(page, Helper.data_locale.SIGN_OUT)
    alert.wait_for_timeout(time_out=5000)

    # expect(alert.btn_in_dialog_footer(Helper.data_locale.CANCEL)).to_be_focused()
    expect(alert.btn_in_dialog_footer(Helper.data_locale.CANCEL)).to_be_enabled(timeout=1000)
    expect(alert.btn_in_dialog_footer(Helper.data_locale.DISCARD_AND_EXIT)).to_be_enabled(timeout=1000)

    alert.screenshot_self('unsaved_warning')

    # expect(alert).to_contain_text("SAS")
    alert.click_button_in_footer(Helper.data_locale.CANCEL)


def test_02_logout_wo_save(page, init):
    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    top_right = TopRightToolbar(page)
    top_right.click_sign_out()

    SignedOutPage(page).wait_for_page_load(time_out=3000)
    SignedOutPage(page).prt_scn('logout')

    expect(SignedOutPage(page).btn_sign_in).to_be_focused()

    SignedOutPage(page).btn_sign_in.click()

    LoginPage(page).prt_scn('sign_in')

    expect(LoginPage(page).user_name).to_be_empty()
    expect(LoginPage(page).user_name).to_be_editable()

    expect(LoginPage(page).user_password).to_be_empty()
    expect(LoginPage(page).user_password).to_be_editable()

    expect(LoginPage(page).btn_submit).to_be_enabled()
    expect(LoginPage(page).btn_compute_context).not_to_be_visible()

    LoginPage(page).login_studionext()


def test_03_logout_wo_save(page, init):
    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.add_node(FlowNodeType.table)

    # Step-1: Open settings dialog
    top_right = TopRightToolbar(page)

    top_right.click_sign_out()

    alert = Alert(page, Helper.data_locale.SIGN_OUT)
    alert.wait_for_timeout(time_out=5000)

    # expect(alert.btn_in_dialog_footer(Helper.data_locale.CANCEL)).to_be_focused()
    expect(alert.btn_in_dialog_footer(Helper.data_locale.CANCEL)).to_be_enabled(timeout=1000)
    expect(alert.btn_in_dialog_footer(Helper.data_locale.DISCARD_AND_EXIT)).to_be_enabled(timeout=1000)

    alert.screenshot_self('unsaved_warning')

    # expect(alert).to_contain_text("SAS")
    alert.click_button_in_footer(Helper.data_locale.DISCARD_AND_EXIT)

    SignedOutPage(page).wait_for_page_load(time_out=3000)
    SignedOutPage(page).prt_scn('logout')

    expect(SignedOutPage(page).btn_sign_in).to_be_focused()

    SignedOutPage(page).btn_sign_in.click()

    LoginPage(page).prt_scn('sign_in')

    expect(LoginPage(page).user_name).to_be_empty()
    expect(LoginPage(page).user_name).to_be_editable()

    expect(LoginPage(page).user_password).to_be_empty()
    expect(LoginPage(page).user_password).to_be_editable()

    expect(LoginPage(page).btn_submit).to_be_enabled()
    expect(LoginPage(page).btn_compute_context).not_to_be_visible()

    LoginPage(page).login_studionext()


def test_04_tab_for_new_flow_tab(page, init):
    """
    SASSTUDIO-28847
    With new flow, focus does not move to the tab header
    https://rndjira.sas.com/browse/SASSTUDIO-28847
    """
    top = TopMenuPage(page)
    top.check_view_item(TopMenuItem.view_start_page)
    StartPage(page).wait_for_timeout(time_out=3000)
    StartPage(page).build_a_flow()

    MainCenterPage(page).wait_for_timeout(time_out=3000)

    # tab of newly created flow
    # XPATH: //div[@role='tab'][contains(@aria-label, 'flw')]
    expect(
        MainCenterPage(page).tab_group.locate_xpath("//div[@role='tab'][contains(@aria-label, 'flw')]")).to_be_focused()


def test_05_table_icon_after_flow_reopen(page, init):
    """
    SASSTUDIO-35173
    The table icon is not correct after reopen the flow if the table is not exist and not SAS table
    https://rndjira.sas.com/browse/SASSTUDIO-35173
    """

    # Create a new flow from new start page
    top = TopMenuPage(page)
    top.check_view_item(TopMenuItem.view_start_page)
    StartPage(page).wait_for_timeout(time_out=3000)
    StartPage(page).build_a_flow()

    # Wait for a while
    MainCenterPage(page).wait_for_timeout(time_out=3000)

    flow: FlowPage = FlowPage(page)
    flow.wait_for_page_load()

    flow.add_node(FlowNodeType.sas_program)
    flow.wait_for_page_load()

    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)

    sas_program_pane = SASProgramPane(page)

    flow.wait_for_page_load()

    file_name = 'noship_01_test05'

    cas_snippet = """
cas;\n
caslib _all_ assign;\n
\n
data CASUSER.CAS_MYCLASS;\n
set SASHELP.CLASS;\n
run;\n
    """

    sas_program_pane.type_into_text_area(cas_snippet)
    flow.prt_scn("sas_program")

    sas_program_pane.set_node_name("创建班级表")
    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    flow.wait_for_page_load()
    table_pane = TablePane(page)
    table_pane.set_library("CASUSER")
    flow.wait_for_page_load()
    table_pane.set_table("CAS_MYCLASS")
    flow.wait_for_page_load()
    table_pane.set_node_name("班级")
    flow.wait_for_page_load()
    table_pane.set_node_description("Table on CAS")
    flow.wait_for_page_load()

    flow.link_two_nodes_in_flow("创建班级表", "班级")
    flow.wait_for_page_load()
    flow.arrange_nodes()
    flow.prt_scn("after_link_two_nodes")

    flow.saveas(Helper.public_folder_path,file_name, True, True)
    flow.run(False)
    flow.select_node_in_flow_canvas("班级")

    table_pane.click_tab(Helper.data_locale.PREVIEW_DATA)
    flow.wait_for_page_load()
    flow.prt_scn("after_file_saving")

    PageHelper.close_all_tabs(MainCenterPage(page))
    PageHelper.open_file(page, Helper.public_folder_path, file_name)
    flow.wait_for_page_load()

    flow.select_node_in_flow_canvas("班级")
    flow.wait_for_page_load()

    table_pane.refresh_table()
    flow.wait_for_page_load()

    flow.prt_scn("reopen")

    top_right = TopRightToolbar(page)
    top_right.click_sign_out()

    if Alert(page, Helper.data_locale.SIGN_OUT).is_open():
        alert = Alert(page, Helper.data_locale.SIGN_OUT)
        alert.wait_for_timeout(time_out=5000)

        if alert.btn_in_dialog_footer(Helper.data_locale.DISCARD_AND_EXIT).is_enabled(timeout=3000):

            alert.screenshot_self('unsaved_warning')
            alert.click_button_in_footer(Helper.data_locale.DISCARD_AND_EXIT)

    SignedOutPage(page).wait_for_page_load(time_out=3000)

    expect(SignedOutPage(page).btn_sign_in).to_be_focused()

    SignedOutPage(page).btn_sign_in.click()

    expect(LoginPage(page).user_name).to_be_empty()
    expect(LoginPage(page).user_name).to_be_editable()

    expect(LoginPage(page).user_password).to_be_empty()
    expect(LoginPage(page).user_password).to_be_editable()

    expect(LoginPage(page).btn_submit).to_be_enabled()
    expect(LoginPage(page).btn_compute_context).not_to_be_visible()

    LoginPage(page).login_studionext()

    # Navigate to the file and open again
    PageHelper.open_file(page, Helper.public_folder_path, file_name)

    flow.select_node_in_flow_canvas("班级")
    flow.wait_for_page_load()

    table_pane.refresh_table()
    flow.wait_for_page_load()

    flow.prt_scn("relogon_n_reopen")



