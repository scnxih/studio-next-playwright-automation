from src.Pages.StudioNext.Dialog.settings_dialog import SettingsDialog
from src.Pages.StudioNext.Dialog.settings_dialog_code_and_log_tab_page import SettingsDialogCodeAndLogTabPage

from src.Utilities.enums import SettingsTabPages, AccountOptionsMenuItem
from src.conftest import *
from src.Pages.Common.dialog import *
from playwright.sync_api import expect



def test_01_open_settings_dialog(page, init):
    PageHelper.show_settings_dialog(page)
    setting_dialog = SettingsDialog(page)
    # setting_dialog.tab_page(page, "General")

    setting_dialog.click_tab_page(page, SettingsTabPages.code_and_log)
    # expect(setting_dialog.btn_reset()).to_be_disabled()
    setting_dialog.page.screenshot(path="01_Code_ad_Log_Page.png")

    code_and_log_tab_page = SettingsDialogCodeAndLogTabPage(page)

    code_and_log_tab_page.click_checkbox_display_error_in_gutter()
    setting_dialog.page.screenshot(path="02_Code_ad_Log_Page.png")

    code_and_log_tab_page.click_checkbox_show_sas_code_in_log()
    setting_dialog.page.screenshot(path="03_Code_ad_Log_Page.png")

    Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
