import re
import time

from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.dialog import *
from src.Pages.Common.combobox import *
from src.Pages.Common.navigation_pane import NavigationPane
from src.Utilities.enums import SettingsTabPages


class SettingsDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page, Helper.data_locale.SETTINGS)
        self.navigation_pane = NavigationPane(self.base_xpath, page)

    # ADDED
    # BEGIN <<< Added by Jacky (ID: jawang) on Nov.7th, 2023
    def combobox(self, data_test_id="", items_count=4):
        """
        To handle combo boxes in Settings dialog
        :param data_test_id:
        :param items_count:
        :return: combo box instance
        """
        return Combobox(container_base_xpath=self.base_xpath, page=self.page, data_test_id=data_test_id,
                        items_count=items_count)

    def select_theme(self, theme):
        """

        :param theme:
        :return:
        """
        # Theme combo box data-testid: settings-global-generalForm-themes
        self.combobox(data_test_id="settings-global-generalForm-themes", items_count=4).select_item(theme)

    def select_tab_type_after_submission(self, tab_type):
        """
        Select tab type after submission
        :param tab_type: Code/Log/Results/Output data
        :return:
        """
        self.combobox(data_test_id="tabType-select", items_count=4).select_item(tab_type)

    def checkbox(self, label):
        return Checkbox(self.base_xpath, self.page, label=label)

    def check_checkbox(self, label):
        self.checkbox(label).set_check()

    def uncheck_checkbox(self, label):
        self.checkbox(label).set_uncheck()

        # Take __screenshot of the query tab page when reset button is not available, which means reset is done
        if self.is_visible(self.enabled_reset_btn_in_current_tab_page):
            self.screenshot(self.base_xpath, "uncheck")

    @property
    def disabled_reset_btn_in_current_tab_page(self):
        """
        Fetch the reset button in current tab page
        :return:
        """
        return self.locate_xpath('//div[contains(@style,"display: block")]//span[text()="'
                                 + Helper.data_locale.RESET
                                 + '"]/../../button[@aria-disabled="true"]')

    @property
    def enabled_reset_btn_in_current_tab_page(self):
        """
        Fetch the reset button in current tab page
        :return:
        """
        return self.locate_xpath('//div[contains(@style,"display: block")]//span[text()="'
                                 + Helper.data_locale.RESET
                                 + '"]/../../button[@aria-disabled="false"]')

    # END Added by Jacky (ID: jawang) on Nov.7th, 2023 >>>

    @property
    def btn_reset(self):
        # //span[text()="Reset"]/../../button
        return self.locate_xpath(
            '//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="false"]')

    def click_reset_button(self):
        """
        Reset settings in the current tab page
        :return:
        """
        if self.is_enabled(self.btn_reset):
            self.btn_reset.click()
            # TO-DO
            # Change to locale-dependent value
            alert = Alert(self.page, "重置为默认值")
            time.sleep(1)
            if alert.is_open():
                # alert.click_button_in_footer("重置")
                alert.click_button_in_footer(Helper.data_locale.RESET)

    '''
    
    @property
    def btn_close_dialog(self):
        """
        Close button at the bottom of the settings dialog
        :return:
        """
        return self.locate_xpath()
        
    '''

    def __assemble_tab_page_xpath(self, tab_page_text):
        print("Assembling xpath for tab page")
        return self.locate_xpath('//label[text()="' + tab_page_text + '"]')

    def tab_page(self, setting_tab_page: SettingsTabPages):
        tab_page_text = ""

        if setting_tab_page == SettingsTabPages.global_general:
            print("Global/General")

        elif setting_tab_page == SettingsTabPages.sas_studio_general:
            print("SAS Studio/General")

        elif setting_tab_page == SettingsTabPages.code_and_log:
            print("Code and Log")
            tab_page_text = Helper.data_locale.CODE_AND_LOG

        else:
            print("Tab Page DOES NOT EXIST")

        return self.__assemble_tab_page_xpath(tab_page_text)

        # pass

    def click_tab_page(self, page, setting_tab_page: SettingsTabPages):
        print("Click:")
        self.click(self.tab_page(setting_tab_page))
        # pass

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Nov.9th, 2023
    def __assemble_tab_page_aria_xpath_dict(self, setting_tab_page: SettingsTabPages):
        aria_dict = {
            "SettingsTabPages.global_general": ('2', '1', '3'),
            # "SettingsTabPages.sas_studio_general": ('2', '2', '10'),
            "SettingsTabPages.sas_studio_general": ('2', '2', '9'),
            "SettingsTabPages.code_and_log": ('3', '1', '2')
        }

        aria_level = aria_dict[str(setting_tab_page)][0]
        aria_posinset = aria_dict[str(setting_tab_page)][1]
        aria_setsize = aria_dict[str(setting_tab_page)][2]

        Helper.logger.debug(
            'Xpath-Aria Assembling: ' + '//div[@role="treeitem"][@aria-level="' + aria_level + '"][@aria-posinset="' +
            aria_posinset + '"][@aria-setsize="' + aria_setsize + '"]')

        return self.locate_xpath('//div[@role="treeitem"][@aria-level="' + aria_level + '"][@aria-posinset="' +
                                 aria_posinset + '"][@aria-setsize="' + aria_setsize + '"]')

    def __assemble_tab_page_aria(self, aria_tuple):
        """
        :return:
        """
        Helper.logger.debug(
            'Xpath-Aria Assembling: ' +
            '//div[@role="treeitem"][@aria-level="' + aria_tuple[0] + '"][@aria-posinset="' + aria_tuple[
                1] + '"][@aria-setsize="' + aria_tuple[2] + '"]')

        return self.locate_xpath(('//div[@role="treeitem"][@aria-level="' + aria_tuple[0] + '"][@aria-posinset="' +
                                  aria_tuple[1] + '"][@aria-setsize="' + aria_tuple[2] + '"]'))

    def switch_to_tab_page_via_aria(self, setting_tab_page: SettingsTabPages):
        """
        Generate xpath (tree-item aria) according to setting tab page
        :param setting_tab_page:
        :return:
        """

        tab_page_aria_combination = ('1', '1', '2')

        if setting_tab_page == SettingsTabPages.global_general:
            Helper.logger.debug("Switch to: Global/General via aira-composing")
            # self.switch_to_global_general()
            tab_page_aria_combination = ('2', '1', '3')

        elif setting_tab_page == SettingsTabPages.sas_studio_general:
            Helper.logger.debug("Switch to: SAS Studio/General via aira-composing")
            tab_page_aria_combination = ('2', '2', '9')
            # tab_page_aria_combination = ('2', '2', '10')

        else:

            if setting_tab_page == SettingsTabPages.code_and_log:
                Helper.logger.debug("Switch to: SAS Studio/SAS Program/Code and Log")
                tab_page_text = Helper.data_locale.CODE_AND_LOG
                tab_page_aria_combination = ('3', '1', '2')

            elif setting_tab_page == SettingsTabPages.results:
                Helper.logger.debug("Switch to: SAS Studio/SAS Program/Results")
                tab_page_text = Helper.data_locale.RESULTS

            elif setting_tab_page == SettingsTabPages.query:
                Helper.logger.debug("Switch to: SAS Studio/Query")
                tab_page_text = Helper.data_locale.QUERY

            # TO-DO
            elif setting_tab_page == SettingsTabPages.region_and_language:
                Helper.logger.debug("Switch to: Global/Region and Language")
                tab_page_text = "区域和语言"

            else:
                Helper.logger.exception("Tab page DOES NOT EXIST!")

        self.click(self.__assemble_tab_page_aria(tab_page_aria_combination))

    def switch_to_tab_page_aria_xpath_dict(self, setting_tab_page: SettingsTabPages):
        """

        :return:
        """
        self.click(self.__assemble_tab_page_aria_xpath_dict(setting_tab_page))

    def switch_to_global_general_via_aria(self):
        """
        Test tab-switching method via aria
        :return:
        """
        Helper.logger.debug("Switch to Global/General via aira-xpath")
        self.click('//div[@role="treeitem"][@aria-level="2"][@aria-posinset="1"][@aria-setsize="3"]')

    def switch_to_sas_studio_general_via_aria(self):
        """
        Test tab-switching method via aria
        :return:
        """
        Helper.logger.debug("Switch to Global/General via aira-xpath")
        self.click('//div[@role="treeitem"][@aria-level="2"][@aria-posinset="2"][@aria-setsize="9"]')
        # self.click('//div[@role="treeitem"][@aria-level="2"][@aria-posinset="2"][@aria-setsize="10"]')

    # END Added by Jacky(ID: jawang) on Nov.9th, 2023 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Nov.10th, 2023
    def switch_to_global_general_via_navigation_pane(self):
        """
        Test 'Global/General' switching by using encapsulated navigation pane
        :return:
        """
        self.navigation_pane.click_tree_item_testid('settings-layout-tree-G-0-C-1')

    def switch_to_sas_studio_general_via_navigation_pane(self):
        """
        Test 'SAS Studio/General' switching by using encapsulated navigation pane
        :return:
        """
        self.navigation_pane.click_tree_item_testid('settings-layout-tree-Custom-0-Child-1')

    # END Added by Jacky(ID: jawang) on Nov.10th, 2023 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Nov.6th, 2023
    def switch_to_global_general(self):
        """
        Switch to Global/General tab page in Settings dialog
        NOTE: Two General tab pages exist, so separate methods are used.
        :return:
        """
        self.click('//div[@data-testid="settings-layout-tree-G-0-C-1"]')

    def switch_to_sas_studio_general(self):
        """
        Switch to SAS Studio/General tab page in Settings dialog
        NOTE: Two General tab pages exist, so separate methods are used.
        :return:
        """
        self.click('//div[@data-testid="settings-layout-tree-Custom-0-Child-1"]')

    def switch_to_tab_page(self, setting_tab_page: SettingsTabPages):
        """
        Switch to certain tab page
        NOTE: This is a temporary version, need to change the implementation strategy in the future.
        LOGIC: IF tab page is SAS Studio/General or Global/General use the two methods defined above.
        :return:
        """
        tab_page_text = ""

        if setting_tab_page == SettingsTabPages.global_general:
            Helper.logger.debug("Switch to: Global/General")
            self.switch_to_global_general()

            # Since this would be used in initialization, comment out.
            # Otherwise, too many screenshots are generated.

            # time.sleep(1)
            # self.screenshot(self.base_xpath, "global_general")

        elif setting_tab_page == SettingsTabPages.sas_studio_general:
            Helper.logger.debug("Switch to: SAS Studio/General")
            self.switch_to_sas_studio_general()

            # Since this would be used in initialization, comment out.
            # Otherwise, too many screenshots are generated.

            # time.sleep(1)
            # self.screenshot(self.base_xpath, "sas_studio_general")

        else:

            if setting_tab_page == SettingsTabPages.code_and_log:
                Helper.logger.debug("Switch to: SAS Studio/SAS Program/Code and Log")
                tab_page_text = Helper.data_locale.CODE_AND_LOG

            elif setting_tab_page == SettingsTabPages.results:
                Helper.logger.debug("Switch to: SAS Studio/SAS Program/Results")
                tab_page_text = Helper.data_locale.RESULTS

            elif setting_tab_page == SettingsTabPages.query:
                Helper.logger.debug("Switch to: SAS Studio/Query")
                tab_page_text = Helper.data_locale.QUERY

            # TO-DO
            elif setting_tab_page == SettingsTabPages.region_and_language:
                Helper.logger.debug("Switch to: Global/Region and Language")
                tab_page_text = Helper.data_locale.REGION_AND_LANGUAGE
                # tab_page_text = "区域和语言"
                tab_page_text = Helper.data_locale.REGION_AND_LANGUAGE

            else:
                Helper.logger.exception("Tab page DOES NOT EXIST!")

            self.click(self.__assemble_tab_page_xpath(tab_page_text))

            time.sleep(2)
            self.screenshot(self.base_xpath, str(setting_tab_page).split('.')[-1])
            time.sleep(1)

    def reset_global_general(self):
        """
        Reset settings in 'Global/General' tab page of Settings dialog
        :return:
        """

        # Step-0: Open Settings dialog
        # Temporarily carry out in testcases.

        # Step-1: Switch to Global/General tab page
        self.switch_to_tab_page(setting_tab_page=SettingsTabPages.global_general)

        # Step-3: Click the reset button in the upper right corner
        # self.click_reset_button()
        if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="true"]'):
            Helper.logger.debug("Reset button is DISABLED!")

        if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="false"]'):
            Helper.logger.debug("Reset button is ENABLED!")
            self.click_reset_button()
            Helper.logger.debug("Reset button is CLICKED!")

    def reset_region_and_language(self):
        """
        Reset settings in 'Global/Region and Language' tab page of Settings dialog
        :return:
        """

        # Step-0: Open Settings dialog
        # Temporarily carry out in testcases.

        # Step-1: Switch to Global/General tab page
        self.switch_to_tab_page(setting_tab_page=SettingsTabPages.region_and_language)

        # Step-3: Click the reset button in the upper right corner
        # self.click_reset_button()
        if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="true"]'):
            Helper.logger.debug("Reset button is DISABLED!")

        if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="false"]'):
            Helper.logger.debug("Reset button is ENABLED!")
            self.click_reset_button()
            Helper.logger.debug("Reset button is CLICKED!")

    # END Added by Jacky(ID: jawang) on Nov.6th, 2023 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Nov.7th, 2023
    def reset_sas_studio_general(self):
        """
        Reset settings in 'SAS Studio/General' tab page of Settings dialog
        :return:
        """

        # Step-0: Open Settings dialog
        # Temporarily carry out in testcases.

        # Step-1: Switch to Global/General tab page
        self.switch_to_tab_page(setting_tab_page=SettingsTabPages.sas_studio_general)

        # Step-3: Click the reset button in the upper right corner
        # self.click_reset_button()
        if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="true"]'):
            Helper.logger.debug("Reset button is DISABLED!")

        if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="false"]'):
            Helper.logger.debug("Reset button is ENABLED!")
            self.click_reset_button()
            Helper.logger.debug("Reset button is CLICKED!")

    def reset_query(self):
        """
        Reset settings in 'SAS Studio/Query' tab page of Settings dialog
        :return:
        """

        # Step-0: Open Settings dialog
        # Temporarily carry out in testcases.

        # Step-1: Switch to 'SAS Studio/Query' tab page
        self.switch_to_tab_page(setting_tab_page=SettingsTabPages.query)

        # Step-3: Click the reset button in the upper right corner
        if self.is_visible(self.disabled_reset_btn_in_current_tab_page):
            Helper.logger.debug("Reset button is DISABLED!")

        if self.is_visible(self.enabled_reset_btn_in_current_tab_page):
            Helper.logger.debug("Reset button is ENABLED!")
            self.enabled_reset_btn_in_current_tab_page.click()

            # TO-DO
            # Change to locale-dependent value
            # alert = Alert(self.page, "重置为默认值")
            alert = Alert(self.page, Helper.data_locale.RESET_TO_DEFAULT_VALUES)
            time.sleep(1)
            if alert.is_open():
                # alert.click_button_in_footer("重置")
                alert.click_button_in_footer(Helper.data_locale.RESET)

            Helper.logger.debug("Reset button is CLICKED!")

        # Take __screenshot of the query tab page when reset button is not available, which means reset is done
        if self.is_visible(self.disabled_reset_btn_in_current_tab_page):
            self.screenshot(self.base_xpath, "reset")

    # END Added by Jacky(ID: jawang) on Nov.7th, 2023 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Nov.13th, 2023
    def get_number_of_expanded_icons(self):
        """

        :return:
        """
        self.navigation_pane.number_of_expanded_icons()

    # END Added by Jacky(ID: jawang) on Nov.13th, 2023 >>>

    def expand_all(self):
        """
        Expand all tree items
        :return:
        """
        self.navigation_pane.expand_all_treeitems()

    def collapse_all(self):
        """
        Collapse all tree items
        :return:
        """
        self.navigation_pane.debug_collapse_all_tree_items()

    def iterate_thru_treeitems(self):
        """
        Iterate thru tree-items in navigation pane.
        :return:
        """
        self.navigation_pane.iterate_thru_treeitems()

    def reset_settings_via_iteration(self):
        """
        Reset settings in 'Global/General' tab page of Settings dialog
        :return:
        """

        # Step-0: Open Settings dialog
        # Temporarily carry out in testcases.

        # Step-1: Switch tab page
        i = 1
        while i <= self.locator_count('//div[@role="treeitem"]'):
            Helper.logger.debug("Going through # " + str(i) + "tree-item")

            # Step-2: Switch tab pages
            self.click(self.locator('(//div[@role="treeitem"])[' + str(i) + ']'))
            # Formula: (xpath)[Number]
            # Exmaple: (//div[@role="treeitem"])[15]
            time.sleep(2)

            # Step-3: Click the reset button in the upper right corner
            # self.click_reset_button()
            if self.is_visible('//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="true"]'):
                Helper.logger.debug("Reset button is DISABLED!")

            if self.is_visible(
                    '//span[text()="' + Helper.data_locale.RESET + '"]/../../button[@aria-disabled="false"]'):
                Helper.logger.debug("Reset button is ENABLED!")
                self.click_reset_button()
                Helper.logger.debug("Reset button is CLICKED!")

            i = i + 1
