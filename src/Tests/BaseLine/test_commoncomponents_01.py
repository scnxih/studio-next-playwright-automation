from src.Pages.StudioNext.Dialog.settings_dialog_just_for_test import SettingsDialogTest
from src.Pages.StudioNext.Top.top_right_toolbar import TopRightToolbar
from src.conftest import *
from src.Pages.Common.text import *
from src.Helper.page_factory import *


def test_init(page, init):
    PageHelper.init_environments(page)


def test_01_toolbar(page, init):
    PageHelper.show_settings_dialog(page)
    Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
    time.sleep(1)
    PageHelper.show_new_features_dialog(page)
    time.sleep(1)
    Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
    time.sleep(1)
    PageHelper.show_keyboard_shortcuts_dialog(page)
    time.sleep(1)

    Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
    # Dialog(page).click_button_in_footer("Close")
    time.sleep(1)
    PageHelper.show_document_recovery_dialog(page)
    time.sleep(1)
    # Dialog(page).click_button_in_footer(Helper.data_locale.CANCEL)
    Dialog(page).click_button_in_footer(Data.CLOSE)
    time.sleep(1)
    PageHelper.show_submission_status(page)


def test_02_combobox(page, init):
    PageHelper.new_sas_program(page)
    text = "data test;\n set sashelp.class;\n run;"
    PageHelper.type_code_in_codeeditor(page, text)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    PageHelper.save_program_test_tile_view_combobox(page, Helper.public_folder_path, "first.sas", True)


def test_03_combobox_checkbox_text_in_settings(page, init):
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting = SettingsDialogTest(page)
    if setting.is_open():
        setting.click_tab("区域和语言")
        setting.select_language("日语 (日本) - 日本語 (日本)‎")
        setting.select_offline_language("阿拉伯语 (巴林) - العربية (البحرين)‏")
        setting.select_language("芬兰语 (芬兰) - Suomi (Suomi)‎")
        setting.select_offline_language("德语 (德国) - Deutsch (Deutschland)‎")
        setting.select_language("浏览器语言/区域")
        setting.select_offline_language("Java 运行时环境的语言/区域")
        time.sleep(1)
        setting.click_tab("启动")
        setting.set_check("显示开始页")
        time.sleep(1)
        setting.set_check("自动消除")
        setting.set_uncheck("显示开始页")
        setting.set_uncheck("自动消除")
        setting.set_check("自动消除")
        setting.set_check("显示开始页")
        setting.set_uncheck("自动消除")
        setting.set_uncheck("显示开始页")
        time.sleep(1)
        setting.set_recent_items_count("30")
        time.sleep(1)
        setting.click_tab("代码和日志")
        alert = Alert(page, "离开该部分")
        time.sleep(1)
        if alert.is_open():
            alert.click_button_in_footer("继续")
        time.sleep(1)
        # setting.set_check("若日志大于指定长度或大小则显示警告")
        # setting.set_check("Display warning if log is larger than specified size")
        setting.set_check("若日志大于指定大小则显示警告")

        # setting.set_max_log_lines("30000")
        time.sleep(1)
        setting.set_max_size("2")
        time.sleep(1)
        setting.click_tab("结果")
        alert = Alert(page, "离开该部分")
        time.sleep(1)
        if alert.is_open():
            alert.click_button_in_footer("继续")
        time.sleep(1)
        setting.set_check("生成 PPT 输出")
        time.sleep(1)
        Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
    PageHelper.reset_all_settings_dialog(page)


def test_04_radio_group(page, init):
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting = SettingsDialogTest(page)
    if setting.is_open():
        setting.click_tab("代码和日志")
        setting.radiogroup("withEachSubmission-radioButton").set_check("追加日志")
        time.sleep(0.3)
        setting.click_tab("流")
        # setting.radiogroup("flowTabLayout-radioButton").set_check("水平")
        setting.radiogroup("flowTabLayout-radioButton").set_check(
            "Studio-gui-icu.flow.toolbar.flowlayout.horizontal.label")
        time.sleep(0.3)
        # setting.radiogroup("flowTabLayout-radioButton").set_check("垂直")
        setting.radiogroup("flowTabLayout-radioButton").set_check(
            "Studio-gui-icu.flow.toolbar.flowlayout.vertical.label")
        time.sleep(0.3)
        setting.click_tab("后台提交")
        count = setting.radiogroup("locationOfFiles-radioButton").get_radio_items_count()
        for i in range(count):
            setting.radiogroup("locationOfFiles-radioButton").set_check_for_index(i)
            time.sleep(0.3)

        count = setting.radiogroup("filesExist-radioButton").get_radio_items_count()
        for i in range(count):
            setting.radiogroup("filesExist-radioButton").set_check_for_index(i)
            time.sleep(0.3)

        Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
        alert = Alert(page, "退出设置")
        time.sleep(1)
        if alert.is_open():
            alert.click_button_in_footer("继续")
        time.sleep(1)
    PageHelper.reset_all_settings_dialog(page)


def test_05_numeric_stepper(page, init):
    top_right = TopRightToolbar(page)
    top_right.click_settings()
    setting = SettingsDialogTest(page)
    if setting.is_open():
        setting.click_tab("辅助功能")
        setting.set_check("调整弹出通知的显示持续时间")
        ns1 = setting.numeric_stepper(data_test_id="settings-global-AccessibilityForm-popupDuration")
        for i in range(5):
            ns1.click_decrement_value()
            time.sleep(0.2)
        for i in range(6):
            ns1.click_increment_value()
            time.sleep(0.2)
        value = ns1.get_value()
        Helper.logger.debug("current value=" + str(value))
        Dialog(page).click_button_in_footer(Helper.data_locale.CLOSE)
        alert = Alert(page, "退出设置")
        time.sleep(1)
        if alert.is_open():
            alert.click_button_in_footer("继续")
        time.sleep(1)
    PageHelper.reset_all_settings_dialog(page)


def test_06_switch_button(page, init):
    PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
    auto = AutoexecDialog(page)
    auto.turn_on_switch_button()
    time.sleep(1)
    auto.turn_off_switch_button()
    time.sleep(1)
    auto.turn_on_switch_button()
    time.sleep(1)
    auto.close_dialog()
