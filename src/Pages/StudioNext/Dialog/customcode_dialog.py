import time
from src.Pages.Common.dialog import Dialog

# ADDED
"""<<< Added by Jacky(ID: jawang) on Sept.11th, 2023 """
from src.Pages.Common.editor_text_area import EditorTextArea
from src.Helper.helper import Helper
""" Added by Jacky(ID: jawang) on Sept.11th, 2023 >>>"""



# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.13th, 2023
from src.Pages.Common.tab_group import TabGroup
# Added by Jacky(ID: jawang) on Sept.13th, 2023 >>>


# Modified by Liu Jia 20230821
from src.Pages.Common.dialog import *
from src.Utilities.enums import *
import time
class CustomCodeDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.CUSTOM_CODE_TITLE)
        # ADDED
        # <<< Added by Jacky(ID: jawang) on Sept.13th, 2023
        self.tab_group = TabGroup("", page)
        self.editor_text_area = EditorTextArea("", page)

    @property
    def tab_preamble(self):
        return self.get_by_test_id("vertical-Tab-tab0")

    @property
    def tab_postamble(self):
        return self.get_by_test_id("vertical-Tab-tab1")

    @property
    def btn_run(self):
        return self.get_by_test_id("customCode-runButton-StardardButton")

    @property
    def btn_save(self):
        return self.get_by_test_id('basic-Dialog-firstButton')

    @property
    def textarea(self):
        return self.locate_xpath('//textarea[@aria-label="' + Helper.data_locale.EDITOR_CONTENT + '"]')

    @property
    def div_first_line(self):
        return self.locate_xpath('//div[@class="view-line"]')

    def type_codes_in_preamble(self, text):
        self.click(self.tab_preamble)
        # self.click(self.textarea)
        self.fill(self.textarea, text)
        self.screenshot("//div[@data-testid='customCodeEditorPreamble-editor']", "critical_user_custom_code")

    def type_codes_in_postamble(self, text):
        self.click(self.tab_postamble)
        self.click(self.textarea)
        self.fill(self.textarea, text)

    # Added by Jacky(ID: jawang) on Sept.13th, 2023 >>>
    @property
    def tab_vertical_front(self):
        return self.get_by_test_id("vertical-Tab-tab0-text")

    @property
    def tab_vertical_back(self):
        return self.get_by_test_id("vertical-Tab-tab1-text")

    @property
    def tab_vertical_option(self):
        return self.get_by_test_id("vertical-Tab-tab2-text")

    @property
    def tab_Code(self):
        return self.get_by_test_id("horizontalTabBar-tab0-text")

    @property
    def tab_log(self):
        return self.get_by_test_id("horizontalTabBar-tab1-text")

    @property
    def option_programs(self):
        return self.locate_xpath(
            '//div[@role="checkbox"]/descendant::label[text()="' + Helper.data_locale.CUSCODE_PROGRAM + '"]')

    @property
    def option_steps(self):
        return self.locate_xpath(
            '//div[@role="checkbox"]/descendant::label[text()="' + Helper.data_locale.CUSCODE_STEP + '"]')

    @property
    def option_search(self):
        return self.locate_xpath(
            '//div[@role="checkbox"]/descendant::label[text()="' + Helper.data_locale.CUSCODE_SEARCH + '"]')

    @property
    def option_quickimports(self):
        return self.locate_xpath(
            '//div[@role="checkbox"]/descendant::label[text()="' + Helper.data_locale.CUSCODE_QUICKIMPORTS + '"]')

    @property
    def btn_backgroundsubmits(self):
        return self.locate_xpath('//button[@class="sas_components-Switch-Switch_switch-button"]')

    def run(self):
        self.click(self.btn_run)
        self.wait_for_page_load()

    def save(self):
        self.click(self.btn_in_dialog_footer(Helper.data_locale.SAVE))
        self.wait_for_page_load()
        time.sleep(1)

    def cancel(self):
        self.click(self.btn_in_dialog_footer(Helper.data_locale.CANCEL))
        self.wait_for_page_load()

    def type_front_codes(self, text):
        self.click(self.tab_vertical_front)
        self.click(self.tab_Code)
        self.fill(self.textarea, text)

    def type_back_codes(self, text):
        self.click(self.tab_vertical_back)
        self.click(self.tab_Code)
        self.fill(self.textarea, text)

    def type_code_run_save(self, text, tabenum: DialogTab):
        if tabenum == DialogTab.Tab_front:
            self.type_front_codes(text)
        if tabenum == DialogTab.Tab_back:
            self.type_back_codes(text)
        self.run()
        self.save()

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Oct.27th, 2023
    def clear_for_editor(self, textarea):
        """
        Might be improved in the future.
        :param textarea:
        :return:
        """
        self.fill(textarea, "")

    def clear_custom_code_editor_thru_keyboard(self, textarea):
        """
        Clear editor textarea thru keyboard
        :param textarea:
        :return:
        """

        # Step-1: Click
        self.force_click(textarea)
        # time.sleep(1)

        # Step-2: Select all contents
        self.key_press("Control+A")
        # time.sleep(1)

        # Step-3 Delete all contents
        self.key_press("Delete")
        # time.sleep(1)

    def clear_custom_code_thru_keyboard(self):
        """

        :return:
        """

        # Step-1: Clear Code Tab Page
        self.wait_for(self.tab_Code)
        # time.sleep(1)
        self.click(self.tab_Code)
        time.sleep(0.5)

        # Step-2: Clear contents in editor
        self.clear_custom_code_editor_thru_keyboard(self.textarea)
        time.sleep(0.5)

        # Step-3: Switch to the other tab page
        self.click(self.tab_vertical_back)

        self.click(self.tab_Code)
        time.sleep(0.5)

        # Step-4: Clearn contents in editor
        self.clear_custom_code_editor_thru_keyboard(self.textarea)
        time.sleep(0.5)

        self.save()


    # Added by Jacky(ID: jawang) on Oct.27th, 2023 >>>
    def clear_CustomCode(self):
        self.click(self.tab_Code)
        time.sleep(1)
        self.clear_for_editor(self.textarea)
        time.sleep(1)
        self.click(self.tab_vertical_back)
        self.click(self.tab_Code)
        time.sleep(1)
        self.clear_for_editor(self.textarea)
        time.sleep(1)
        self.save()

    def set_option(self):
        self.click(self.tab_vertical_option)
        time.sleep(1)
        self.click(self.option_programs)
        time.sleep(1)
        self.click(self.option_steps)
        time.sleep(1)
        self.click(self.option_search)
        time.sleep(1)
        self.click(self.option_quickimports)
        time.sleep(1)
        self.click(self.btn_backgroundsubmits)
        time.sleep(1)
        self.save()

    def wait_for_open(self):
        time.sleep(2)

    def click_tab_preamble(self):
        self.click(self.tab_preamble)

    def click_tab_postamble(self):
        self.click(self.tab_postamble)

    def click_tab_option(self):
        self.click(self.tab_vertical_option)