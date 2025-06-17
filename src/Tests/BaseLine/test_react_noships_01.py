from src.Helper.page_helper import PageHelper, Helper
from src.Pages.Common.login_page import LoginPage
from src.Pages.Common.singed_out_page import SignedOutPage
from src.Pages.StudioNext.Center.Flow.flow_page import FlowPage
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.Utilities.enums import TopMenuItem, FlowNodeType
from playwright.sync_api import expect
from src.Pages.Common.dialog import Alert


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
    # flow.add_node(FlowNodeType.table)

    # Step-1: Open settings dialog
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
