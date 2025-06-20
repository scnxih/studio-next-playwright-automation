# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.1st, 2023 """
import inspect
# Added by Jacky(ID: jawang) on Sept. 1st, 2023 """
# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.7th, 2023 """
from src.Pages.Common.editor_text_area import EditorTextArea
# Added by Jacky(ID: jawang) on Sept.7th, 2023 >>>"""
from src.Pages.Common.switch_button import SwitchButton

import time

from src.Helper.helper import Helper
from src.Pages.Common.dialog import Dialog

# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.12th, 2023 """
from src.Pages.Common.tab_group import TabGroup

# Added by Jacky(ID: jawang) on Sept.12th, 2023 >>>"""
from src.Pages.Common.dialog import Alert


class AutoexecDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.AUTOEXEC_FILE_F_Upper_Case)
        self.switch_button = SwitchButton(self.base_xpath, page)
        self.editor_text_area = EditorTextArea("", page)
        self.tab_group = TabGroup("", page)

    @property
    def time_info_in_log_tab(self):
        """
        Property used to mask CPU Time and Real Time in log
        NOTE: This might be UNSTABLE owing to the future change of data-testid
        """
        return ['//div[@data-testid="autoexecLogViewer-detail"]//span[@class="mtk25"][contains(text(),"CPU")]',
                '//div[@data-testid="autoexecLogViewer-detail"]//span[@class="mtk25"][contains(text(),"实际")]']

    @property
    def time_info_in_log_tab2(self):
        """
        Property used to mask CPU Time and Real Time in log
        Composed by base_xpath + time_info_xpath
        """
        return [self.base_xpath + '//span[@class="mtk25"][contains(text(),"实际")]',
                self.base_xpath + '//span[@class="mtk25"][contains(text(),"CPU")]']

    @property
    def btn_bgSubmission_switch(self):
        return self.get_by_test_id("backgroundSubmitSwitch-button")

    @property
    def tab_Code(self):
        return self.get_by_test_id("horizontalTabBar-tab0-text")

    @property
    def tab_log(self):
        return self.get_by_test_id("horizontalTabBar-tab1-text")

    @property
    def btn_run(self):
        return self.get_by_test_id("autoexec-runButton-StardardButton")

    @property
    def textarea(self):
        return self.locate_xpath('//textarea[@aria-label="' + Helper.data_locale.EDITOR_CONTENT + '"]')

    @property
    def div_first_line(self):
        return self.locate_xpath('//div[@class="view-line"]')

    @property
    def scroll_bar(self):
        """
        scroll bar in the dialog
        """
        return ['//div[@role="presentation"][@class="visible scrollbar vertical"]']

    def selfie(self, pic_name, clip=None, mask=None, mask_color=None):
        """
        Overwrite the vanilla screenshot_self method in BasePage
        """
        Helper.logger.debug("AutoexecDialog: Overwrite the vanilla screenshot_self method in BasePage")
        self.screenshot(self.base_xpath, pic_name, clip=clip,
                        # mask=[self.bread_crumb, self.content_selector_navigator_tree, self.temp_content_selector],
                        mask_color="#000000")

    def type_codes(self, text):
        self.click(self.tab_Code)
        self.editor_text_area.type_into_text_area(text)
        # self.fill(self.textarea, text)

    def run(self):
        self.click_dialog_title_or_studionext_header()

        if self.btn_run.is_enabled():
            Helper.logger.debug("Enabled Run button")
            self.click(self.btn_run)
            self.wait_for_page_load()
        else:
            Helper.logger.debug("Disabled Run button")
            self.close_dialog()

        Helper.logger.debug("Exit Autoexec run")

    def save(self):
        self.click(self.btn_in_dialog_footer(Helper.data_locale.SAVE))
        self.wait_for_page_load()
        time.sleep(3)

        if Alert(self.page).is_open():
            time.sleep(1)
            self.key_press("Tab")
            time.sleep(1)
            self.key_press("Tab")
            time.sleep(1)
            self.key_press("Enter")

    def cancel(self):
        self.click(self.btn_in_dialog_footer(Helper.data_locale.CANCEL))
        self.wait_for_page_load()

    def type_code_run_save(self, text):
        self.type_codes(text)
        Helper.logger.debug("complete type_codes:" + text)
        # time.sleep(1)

        self.screenshot("//div[@data-testid='autoexecCodeEditor-editor']", "critical_user_autoexe")
        self.screenshot("//div[@data-testid='basic-Dialog-header']", "uax_autoexec_header", user_assigned_xpath=True)
        self.wait_for_page_load()

        # time.sleep(1)
        self.run()
        Helper.logger.debug("complete run")
        self.wait_for_page_load()

        # time.sleep(1)
        self.save()
        Helper.logger.debug("complete save")

    def clear_for_editor(self, textarea):
        """
        Might be improved in the future.
        :param textarea:
        :return:
        """
        self.fill(textarea, "")

    def clear_editor_thru_keyboard(self, textarea):
        """
        Clear editor textarea thru keyboard
        :return:
        """
        # Step-1: Click
        # NOTE: To avoid base_page.py/force_click problem, this wait_for is necessary.
        self.wait_for(textarea)
        self.click_dialog_title_or_studionext_header()
        # time.sleep(1)
        self.force_click(textarea)

        # Step-2: Select all contents
        self.key_press("Control+A")
        # time.sleep(1)

        # Step-3 Delete all contents
        self.key_press("Delete")
        # time.sleep(1)

    def clear_autoexec_thru_keyboard(self):
        """
        Clear contents in Autoexec dialog
        :return:
        """
        if self.btn_run.is_disabled():
            Helper.logger.debug("Disabled [Run] button in Autoexec dlg")
            # return

        else:
            Helper.logger.debug("Enabled [Run] button in Autoexec dlg")
            # return

        # Step-1: Switch to Code tab page
        self.click(self.tab_Code)

        # Step-2: Delete contents thru keyboard
        # NOTE: To avoid base_page.py/force_click problem, this wait_for is necessary.
        self.wait_for(self.textarea)
        self.clear_editor_thru_keyboard(self.textarea)

        # Step-3: Click the save button
        self.save()

    # Added by Jacky(ID: jawang) on Oct.27th, 2023 >>>

    def clear_autoexec(self):
        self.click(self.tab_Code)
        # time.sleep(1)
        self.clear_for_editor(self.textarea)
        # time.sleep(1)
        self.save()

    """Added by Alice on 09/19/2023 start"""

    def turn_on_switch_button(self):
        self.switch_button.turn_on()
        self.wait_for_page_load()

    def turn_off_switch_button(self):
        self.switch_button.turn_off()
        self.wait_for_page_load()

    """Added by Alice on 09/19/2023 end"""

    def wait_for_open(self):
        self.wait_for(self.tab_Code)
        time.sleep(1)

    def click_tab_log(self):
        self.click(self.tab_log)
        self.wait_for_page_load()

    def click_tab_code(self):
        self.click(self.tab_Code)
        self.wait_for_page_load()
