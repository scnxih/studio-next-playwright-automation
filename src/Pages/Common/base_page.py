import inspect
import os.path
import time
import sys
from playwright.sync_api import Page, Locator

from src.Helper.helper import *
from src.Utilities.vars import global_screenshot_importance
from src.Utilities.vars import global_screenshot_level


def is_locator(locator_or_xpath):
    if isinstance(locator_or_xpath, Locator):
        return True
    else:
        return False


''' Added by Jacky(ID: jawang) on Sept. 5th, 2023 '''


class BasePage:
    current_frame = ""

    def __init__(self, page: Page):

        self.page: Page = page
        self.base_xpath = ""
        # self.data_locale = self.get_data_locale()

    @property
    def doorbell_icon_in_toast_message(self):
        """
        Return mask[] of the doorbell icon in toast message
        """
        return [self.page.locator('//div[@data-testid="appMessageToast"]//span[''@role="img"]')]

    @property
    def base_locator(self):
        if self.base_xpath == "":
            Helper.logger.debug("page_locator = None since base_path=''")
            return None
        return self.page.locator("xpath=" + self.base_xpath)

    @property
    def recovery_number(self):
        """
        The number of recoveries in status bar.
        """
        return [self.page.locator("//button[@type='button'][.//span[contains(text(), '" +
                                  Helper.data_locale.OPERATE_RECOVERY + "')]]")]

    @property
    def status_bar(self):
        """
        Return: mask STRING of status bar locator by using @data-landmark-label
        """
        return "//div[@data-landmark-label='" + Helper.data_locale.STATUS_BAR + "']"

    @property
    def ln_col_number(self):
        """
        Return: mask[] of 'line & column number' in status bar
        Line & Column number of mouse cursor in code editor
        //div[@data-landmark-label="状态栏"]//h6[@data-testid="appFooterToolbar-caretLabel"]
        """

        return [self.page.locator(self.status_bar + "//h6[@data-testid='appFooterToolbar-caretLabel']")]

    def get_page(self):
        return self.page

    def set_iframe(self, xpath):
        pass

    def __resolve_xpath(self, xpath):

        if hasattr(self, 'base_xpath') and xpath.startswith(self.base_xpath):
            return xpath
        if hasattr(self, 'base_xpath') and xpath != self.base_xpath:
            return self.base_xpath + xpath
        return xpath

    def __get_xpath(self, xpath):
        selector_xpath = f"xpath={self.__resolve_xpath(xpath)}"
        Helper.logger.debug("selector_xpath:" + selector_xpath)
        return selector_xpath

    def locator_count(self, xpath):
        selector_xpath = self.__get_xpath(xpath)
        if self.current_frame == "":
            # print(f"Locating xpath 1 {xpath_selector}")
            return self.page.locator(selector_xpath).count()
        else:
            # print(f"Locating xpath {xpath_selector} within {self.current_frame}")
            return self.page.frame_locator(self.current_frame).locator(selector_xpath).count()

    def locator_nth(self, xpath, index: int):
        selector_xpath = self.__get_xpath(xpath)
        if self.current_frame == "":
            # print(f"Locating xpath 1 {xpath_selector}")
            return self.page.locator(selector_xpath).nth(index)
        else:
            # print(f"Locating xpath {xpath_selector} within {self.current_frame}")
            return self.page.frame_locator(self.current_frame).locator(selector_xpath).nth(index)

    def locate_xpath(self, xpath):

        selector_xpath = self.__get_xpath(xpath)
        if self.current_frame == "":
            # print(f"Locating xpath 1 {xpath_selector}")
            return self.page.locator(selector_xpath).first
        else:
            # print(f"Locating xpath {xpath_selector} within {self.current_frame}")
            return self.page.frame_locator(self.current_frame).locator(selector_xpath).first

    # def locate_xpath_all(self, xpath):
    #
    #     xpath_selector = f"xpath={self.resolve_xpath(xpath)}"
    #     if self.current_frame == "":
    #         # print(f"Locating xpath 1 {xpath_selector}")
    #         return self.page.locator(xpath_selector)
    #     else:
    #         # print(f"Locating xpath {xpath_selector} within {self.current_frame}")
    #         return self.page.frame_locator(self.current_frame).locator(xpath_selector)

    # def wait_for_xpath(self, xpath):
    #
    #     element_xpath = self.resolve_xpath(xpath)
    #     # print(f"Waiting for xpath {element_xpath}")
    #     return self.page.wait_for_selector(f"xpath={element_xpath}")

    def goto(self, url):

        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for(self, locator_or_xpath, timeout=300000):
        r_locator = self.transform_to_locator(locator_or_xpath)
        return r_locator.wait_for(timeout=timeout, state="visible")

    """"Added by Alice on 2024/03/26 start"""

    def transform_to_locators_list(self, list_locator_or_xpath: list):
        if list_locator_or_xpath is None:
            return None
        if len(list_locator_or_xpath) == 0:
            return []
        locators: list = []
        for element in list_locator_or_xpath:
            locator = self.transform_to_locator(element)
            locators.append(locator)
        return locators

    """"Added by Alice on 2024/03/26 end"""

    def transform_to_locator(self, locator_or_xpath) -> Locator:
        if is_locator(locator_or_xpath):
            return locator_or_xpath
        else:
            r_locator = self.locate_xpath(locator_or_xpath)
            return r_locator

    def is_visible(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        if r_locator.is_visible():
            return True
        return False

    def get_by_test_id(self, test_id: str):
        return self.page.get_by_test_id(test_id)
        # xpath_test_id = "xpath = self.resolve_xpath("//*[@data-testid='" + test_id + "']")"
        # Helper.logger.debug("get_by_test_id:" + xpath_test_id)
        # if self.current_frame == "":
        #     # print(f"Locating xpath 1 {xpath_selector}")
        #     return self.page.locator(xpath_test_id).first
        # else:
        #     # print(f"Locating xpath {xpath_selector} within {self.current_frame}")
        #     return self.page.frame_locator(self.current_frame).locator(xpath_test_id).first

    def locator(self, xpath_no_prefix):
        return self.page.locator(xpath_no_prefix).first

    # def get_by_label(self, label):
    #     return self.page.get_by_label(label).first
    #
    # def get_by_text(self, text):
    #     return self.page.get_by_text(text).first

    def pause(self):
        self.page.pause()

    def wait_for_timeout(self, time_out):
        self.page.wait_for_timeout(time_out)

    def wait_for_page_load(self, time_out=20000):

        # if not self.page.wait_for_load_state("domcontentloaded", timeout=time_out):
        #     page_reload(self)
        self.page.wait_for_load_state("domcontentloaded", timeout=time_out)
        # self.page.wait_for_load_state("networkidle", timeout=time_out)

    # Key Press methods

    def key_press(self, key):

        self.page.keyboard.press(key)

    def key_down(self, key):

        self.page.keyboard.down(key)

    def key_up(self, key):

        self.page.keyboard.up(key)

    def page_reload(self):

        self.page.reload()

    def fill(self, locator_or_xpath, text):
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.fill(text)

    #
    # '''Work round for code editor clear problem'''
    #
    # def clear_for_editor(self, textarea):
    #     self.fill(textarea, "")

    def clear(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        Helper.logger.debug("enter BasePage::clear()")
        # r_locator.click()
        r_locator.clear()

    def click(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.click()

    def force_click(self, locator_or_xpath):
        time.sleep(1)
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.click(force=True)

    def dblclick(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.dblclick()

    # MODIFIED
    # Changed to private s.t. this method wouldn't be called explicitly.
    # use click_context_menu() or click_context_menu_by_right_click() instead.
    # <<< Modified by Jacky(ID: jawang) on Sept.22nd, 2023
    def __invoke_context_menu(self):
        self.key_press('Shift+F10')

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr.12th, 2024

        # Wait for 0.5 sec
        time.sleep(0.5)

        # Whole page xpath: //div[@id='app']
        self.screenshot("//div[@id='app']", 'context_menu', user_assigned_xpath=True)

        # END Added by Jacky(ID: jawang) on Apr.12th, 2024 >>>

    # Modified by Jacky(ID: jawang) on Sept.22nd, 2023 >>>

    # -----Added by Frank 2023/09/18, begin----- #
    def combo_item_locator(self, combo_item_text: str):
        return self.locator("//span[contains(@class, 'ListBox-List')][text()='{0}']".format(combo_item_text))

    def click_combo_item(self, combo_item_text: str):
        self.click(self.combo_item_locator(combo_item_text))

    # -----Added by Frank 2023/09/18, end----- #

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.19th, 2023
    def __invoke_context_menu_by_right_click(self, locator_or_xpath, take_screenshot):
        """
        Invoke context menu by right-click for sometimes Shift+F10 does not work
        :param locator_or_xpath: element ro right-click on
        :return: None
        """
        r_locator = self.transform_to_locator(locator_or_xpath)
        # r_locator.click()
        r_locator.click(button="right")

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr.12th, 2024

        # Wait for 0.5 sec
        time.sleep(0.5)

        if take_screenshot is True:
            # Whole page xpath: //div[@id='app']
            self.screenshot("//div[@id='app']", 'true_context_menu', user_assigned_xpath=True)

        # END Added by Jacky(ID: jawang) on Apr.12th, 2024 >>>

    # Added by Jacky(ID: jawang) on Sept.19th, 2023 >>>
    """Added by Alice on 10/20/2023 start"""

    def is_menu_item_checked(self, menu_item_text):
        xpath = ""
        if Helper.if_contain_quotation(menu_item_text):
            xpath = "xpath=//span[(contains(@class,'menu') or contains(@class,'Menu')) and text()=" + Helper.escape_quotation_for_xpath(
                menu_item_text) + "]/../preceding-sibling::span[1][@role='img'][contains(@class,'checkmark')]"
        else:
            xpath = (
                    "xpath=//span[(contains(@class,'menu') or contains(@class,'Menu')) and text()='" + menu_item_text +
                    "']/../preceding-sibling::span[1][@role='img'][contains(@class,'checkmark')]")
        if self.is_visible(self.locator(xpath)):
            return True
        return False

    """If the menu item is unchecked, then click it to check, if menu item is already checked, then click dialog_title_or_studionext_header
    to dismiss the menu item. Please note that the checked/unchecked menu item is the latest item in cascade menu items"""

    def check_menu_item(self, *menu_item_text):
        item_count = len(menu_item_text)
        i = 0
        for item in menu_item_text:
            if i == item_count - 1:
                if not self.is_menu_item_checked(item):
                    if self.is_enabled(self.menu_item_locator(item)):
                        self.menu_item_locator(item).click()
                    else:
                        self.click_dialog_title_or_studionext_header()
                else:
                    self.click_dialog_title_or_studionext_header()
            else:
                if self.is_enabled(self.menu_item_locator(item)):
                    self.menu_item_locator(item).click()
                    i = i + 1
                else:
                    self.click_dialog_title_or_studionext_header()
                    time.sleep(0.3)
                    return
        time.sleep(0.5)

    def uncheck_menu_item(self, *menu_item_text):
        item_count = len(menu_item_text)
        i = 0
        for item in menu_item_text:
            if i == item_count - 1:
                if self.is_menu_item_checked(item):
                    if self.is_enabled(self.menu_item_locator(item)):
                        self.menu_item_locator(item).click()
                    else:
                        self.click_dialog_title_or_studionext_header()
                else:
                    self.click_dialog_title_or_studionext_header()
            else:
                if self.is_enabled(self.menu_item_locator(item)):
                    self.menu_item_locator(item).click()
                    i = i + 1
                else:
                    self.click_dialog_title_or_studionext_header()
                    time.sleep(0.5)
                    return
        time.sleep(0.5)

    """Added by Alice on 10/20/2023 end"""

    def menu_item_locator(self, menu_item_text):
        """Updated by Alice on 10/08/2023 start"""
        xpath = ""
        if Helper.if_contain_quotation(menu_item_text):
            xpath = "xpath=//span[(contains(@class,'menu') or contains(@class,'Menu')) and text()=" + Helper.escape_quotation_for_xpath(
                menu_item_text) + "]"
        else:
            xpath = "xpath=//span[(contains(@class,'menu') or contains(@class,'Menu')) and text()='" + menu_item_text + "']"
        """Updated by Alice on 10/08/2023 end"""
        menu_item = self.locator(xpath)
        return menu_item

    """Added by Alice on 09/26/2023 Start"""

    def is_menu_item_enabled(self, menu_item_text):
        menu_item = self.menu_item_locator(menu_item_text)
        if self.get_attribute(menu_item, "class").lower().find("disabled") >= 0:
            return False
        return True

    """Added by Alice on 09/26/2023 End"""
    """Added by Alice on 20/20/2023 start"""

    """Added by Alice on 20/20/2023 end"""
    """Updated by Alice on 09/26/2023 Start"""

    def click_menu_item_wait_until_enabled(self, *menu_item_text):
        enabled = True
        for item in menu_item_text:
            if self.wait_until_enabled(self.menu_item_locator(item)):
                self.menu_item_locator(item).click()
            else:
                enabled = False
                break
        if not enabled:
            self.click_dialog_title_or_studionext_header()
        return enabled

    # support cascade menu items, e.g. "More File Types","XML"

    def click_menu_item(self, *menu_item_text):
        enabled = True
        for item in menu_item_text:
            if self.is_menu_item_enabled(item):
                self.menu_item_locator(item).click()
            else:
                enabled = False
                break
        if not enabled:
            self.click_dialog_title_or_studionext_header()
        return enabled

    # support cascade context menu items
    def click_context_menu(self, locator_or_xpath, *context_menu_text):
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.click()
        self.__invoke_context_menu()
        time.sleep(0.3)

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr.12th, 2024

        # NOTE: This implementation assumes that there is ONLY ONE menu in the main page.
        # self.screenshot("//div[@role='menu']", "context_menu", user_assigned_xpath=True)

        # NOTE: To save time and pinpoint any possible problem, use whole page screenshot at the moment.
        # Implemented in: self.__invoke_context_menu()

        # END Added by Jacky(ID: jawang) on Apr.12th, 2024 >>>

        return self.click_menu_item(*context_menu_text)

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.22nd, 2023
    def click_context_menu_by_right_click(self, locator_or_xpath, *context_menu_text, take_screenshot=False):
        """

        """
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.click()
        self.__invoke_context_menu_by_right_click(locator_or_xpath, take_screenshot)
        time.sleep(0.3)

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr.12th, 2024

        # NOTE: This implementation assumes that there is ONLY ONE menu in the main page.
        # self.screenshot("//div[@role='menu']", "right_click_context_menu_", user_assigned_xpath=True)

        # NOTE: To save time and pinpoint any possible problem, use whole page screenshot at the moment.
        # Implemented in: self.__invoke_context_menu_by_right_click()

        # END Added by Jacky(ID: jawang) on Apr.12th, 2024 >>>

        return self.click_menu_item(*context_menu_text)

    # Added by Jacky(ID: jawang) on Sept.22nd, 2023 >>>
    """Updated by Alice on 09/26/2023 End"""

    # def scroll_into_view_if_needed(self, locator_or_xpath):
    #     r_locator = self.transform_to_locator(locator_or_xpath)
    #     r_locator.scroll_into_view_if_needed()

    def scroll_if_needed(self, locator_or_xpath):
        self.scroll_vertical_if_needed(locator_or_xpath)
        self.scroll_horizontal_if_needed(locator_or_xpath)

    def scroll_horizontal_if_needed(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        i = 0
        while not r_locator.is_visible() and i < 30:
            self.page.mouse.wheel(200, 0)
            i = i + 1
        if r_locator.is_visible():
            return True
        return False

    def scroll_vertical_if_needed(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        i = 0
        while not r_locator.is_visible() and i < 30:
            self.page.mouse.wheel(0, 200)
            i = i + 1
        if r_locator.is_visible():
            return True
        return False

    # def check(self, locator_or_xpath):
    #     r_locator = self.transform_to_locator(locator_or_xpath)
    #     r_locator.check()
    #
    # def uncheck(self, locator_or_xpath):
    #     r_locator = self.transform_to_locator(locator_or_xpath)
    #     r_locator.uncheck()

    # def is_checked(self, locator_or_xpath):
    #     r_locator = self.transform_to_locator(locator_or_xpath)
    #     return r_locator.is_checked()

    def get_attribute(self, locator_or_xpath, attribute_name):
        r_locator = self.transform_to_locator(locator_or_xpath)
        return r_locator.get_attribute(name=attribute_name)

    def get_inner_text(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        return r_locator.inner_text()

    """Added by Alice on 09/19/2023 start"""

    def right_click(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        self.scroll_if_needed(r_locator)
        r_locator.click(button="right")

    def is_enabled(self, locator_or_xpath):
        # On Feb 21 2025
        # It was found that BaseLine.test_centerpage_01.test_38_quick_import would fall into an endless loop
        # which was caused by this function.
        # TODO
        # One possible solution is to implement a time-out mechanism.
        r_locator = self.transform_to_locator(locator_or_xpath)
        self.wait_for(r_locator)
        time.sleep(0.3)
        self.scroll_if_needed(r_locator)
        if r_locator.get_attribute("aria-disabled") is not None:
            if r_locator.get_attribute("aria-disabled").lower() == "false":
                return True
            return False
        elif self.get_attribute(r_locator, "class").find("menu") != -1 or self.get_attribute(r_locator, "class").find(
                "Menu") != -1:
            if self.get_attribute(r_locator, "class").find("disabled") != -1:
                return False
            else:
                return True
        else:
            Helper.logger.debug("The locator has no aria-disabled attribute, so enabled")
            return True

    """Added by Alice on 09/19/2023 end"""

    @property
    def span_studionext_header(self):
        return self.locator(
            "//span[text()='{0}']".format(Helper.data_locale.STUDIO_NEXT_DEV_CODE_AND_FLOW))

    @property
    def __div_toast(self):
        return self.locator("//div[@data-testid='appMessageToast']")

    @property
    def div_dialog_title(self):
        return self.locator("//div[@class='sas_components-Dialog-Dialog_dialog-header "
                            "sas_components-Dialog-Dialog_drag-cursor']")

    def click_dialog_title_or_studionext_header(self):
        if self.div_dialog_title.is_visible():
            try:
                # Helper.logger.debug("1. before click dialog title")
                self.div_dialog_title.click()
                # Helper.logger.debug("2. after click dialog title")
            except Exception as e:
                # Helper.logger.debug("3. click dialog title exception:" + type(e).__name__)
                print(e)
            finally:
                time.sleep(0.01)
        else:
            try:
                # Helper.logger.debug("4. before click header span")
                self.span_studionext_header.click()
                # Helper.logger.debug("5. after click header span")
            except Exception as e:
                Helper.logger.debug("6. click header span exception:" + type(e).__name__)
                print(e)
            finally:
                time.sleep(0.01)

    def wait_toast_disappear(self):
        if self.__div_toast is None:
            # Helper.logger.debug("0. toast is none")
            return
        else:
            # Helper.logger.debug("1. toast is not none")
            try:
                self.__div_toast.wait_for(timeout=2000, state="visible")
            except Exception as e:
                # Helper.logger.debug("2. toast visible exception:" + type(e).__name__)
                print(e)
            else:
                # Helper.logger.debug("3. toast shown")
                i = 0
                while self.__div_toast.is_visible():
                    i = i + 1
                    # Helper.logger.debug("i=" + str(i))
                    self.click_dialog_title_or_studionext_header()
                # Helper.logger.debug("10. toast disappear")

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on May.29th, 2024
    def wait_toast_pop(self):
        """
        Wait until the toast message popped up
        """
        if self.__div_toast is not None:
            Helper.logger.debug("0. toast is shown")
            time.sleep(0.5)

            # self.__div_toast.wait_for(timeout=1500, state="visible")
            # self.__div_toast.wait_for(timeout=1500, state="attached")
            return True
        else:
            Helper.logger.debug("1. toast is invisible")
            try:
                self.__div_toast.wait_for(timeout=1000, state="visible")
            except Exception as e:
                Helper.logger.debug("2. toast visible exception:" + type(e).__name__)
                print(e)

    # END Added by Jacky(ID: jawang) on May.29th, 2024 >>>

    def is_read_only(self, locator_or_xpath):
        read_only = self.get_attribute(locator_or_xpath, "aria-readonly")
        if read_only.lower() == "true":
            return True
        return False

    def is_button_pressed(self, locator_or_xpath):
        is_pressed = self.get_attribute(locator_or_xpath, "aria-pressed")
        if is_pressed.lower() == "true":
            return True
        return False

    def wait_until_enabled(self, locator_or_xpath, wait_time=5):
        i = 0
        wait = True
        Helper.logger.debug("Enter  wait_until_enabled,  wait_time*100={0}".format(str(wait_time * 100)))

        while i < 3000 and wait:
            Helper.logger.debug("before i={0}".format(i))
            time.sleep(0.1)
            if self.is_enabled(locator_or_xpath):
                wait = False
                break
            i = i + 1
            Helper.logger.debug("after i={0}".format(i))
        # while (( not self.is_enabled(locator_or_xpath)) and i < 6000):
        #     Helper.logger.debug("before i={0}".format(i))
        #     time.sleep(0.1)
        #     i = i + 1
        #     Helper.logger.debug("after i={0}".format(i))

        time.sleep(0.5)
        i = 0
        wait = True
        while i < 3000 and wait:
            Helper.logger.debug("before i={0} second".format(i))
            time.sleep(0.1)
            if self.is_enabled(locator_or_xpath):
                wait = False
                break
            i = i + 1
            Helper.logger.debug("after i={0} second".format(i))

        if self.is_enabled(locator_or_xpath):
            if not is_locator(locator_or_xpath):
                Helper.logger.debug("{0} is enabled, i = {1}".format(locator_or_xpath, i))
            else:
                Helper.logger.debug("{0} is enabled, i = {1}".format(str(locator_or_xpath), i))
            return True

        else:
            if not is_locator(locator_or_xpath):
                Helper.logger.debug("{0} is not enabled, i = {1}".format(locator_or_xpath, i))
            else:
                Helper.logger.debug("{0} is not enabled, i = {1}".format(str(locator_or_xpath), i))
            return False

    """Updated by Alice on 2024/03/26 start, below are __screenshot related methods"""

    def get_screenshot_full_path(self, pic_name):
        output_path = "C:\\studio-next-playwright-automation\\src\\Output\\"
        testfile_abbreviation = Helper.get_testfile_abbreviation()
        testmethod_number = Helper.get_testmethod_number()
        class_name = type(self).__name__
        function_name = inspect.currentframe().f_back.f_back.f_back.f_code.co_name
        index = 1
        file_name = (testfile_abbreviation + "_" + testmethod_number + "_" +
                     class_name + "_" +
                     function_name + "_" +
                     pic_name)
        if len(file_name) >= 78:
            class_name = class_name[0:20]
            function_name = function_name[0:30]
            pic_name = pic_name[0:10]
            file_name = (testfile_abbreviation + "_" + testmethod_number + "_" +
                         class_name + "_" +
                         function_name + "_" +
                         pic_name)
        screenshot_file_base = (output_path + "\\" +
                                testfile_abbreviation + "_" + testmethod_number + "\\" + file_name)
        final_full_path = f"{screenshot_file_base}{'_'}{index:02d}{'.png'}"
        while os.path.exists(final_full_path):
            index += 1
            final_full_path = f"{screenshot_file_base}{'_'}{index:02d}{'.png'}"
        Helper.logger.debug("Screenshot final full path: " + final_full_path)
        return final_full_path

    def __screenshot(self, locator_or_xpath, pic_name, user_assigned_xpath=False, clip=None, mask=None,
                     mask_color=None):
        """
        :param locator_or_xpath: Element xpath used to take screenshots, which will be combined into final total xpath.
        :param pic_name: Picture name that will be appended to image file name.
        :param user_assigned_xpath: If true, user assigned xpath will be used.
        :param mask: list of xpath or locators or mixture of them.
        :return:
        """
        if user_assigned_xpath:
            Helper.logger.debug("User did not assign xpath")
            if is_locator(locator_or_xpath):
                r_locator = locator_or_xpath
            else:
                r_locator = self.locator(locator_or_xpath)
        else:
            Helper.logger.debug("User assigned xpath")
            r_locator = self.transform_to_locator(locator_or_xpath)
        final_full_path = self.get_screenshot_full_path(pic_name)

        # MODIFIED
        # <<< Modified by Jacky(ID: jawang) on Apr.26th, 2024
        # if mask is None:
        #     r_locator.screenshot(path=final_full_path)
        #     return
        # Modified by Jacky(ID: jawang) on Apr.26th, 2024 >>>

        locators_mask = self.transform_to_locators_list(mask)

        # ADDED
        # BEGIN <<< Added by Jacky(ID: jawang) on Apr.26th, 2024
        if clip is None:
            r_locator.screenshot(path=final_full_path, mask=locators_mask, mask_color=mask_color)
            return
        # END Added by Jacky(ID: jawang) on Apr.26th, 2024 >>>

        # Original
        # r_locator.screenshot(path=final_full_path, mask=locators_mask, mask_color=mask_color)

        print('###: __screenshot clip: ' + str(clip))
        print('###: __screenshot mask: ' + str(mask))
        print('###: __screenshot path: ' + str(final_full_path))

        # Revised
        # self.page.screenshot(clip=clip, mask=locators_mask, mask_color=mask_color)
        self.page.screenshot(path=final_full_path, clip=clip, mask=locators_mask, mask_color=mask_color)

    def screenshot(self, locator_or_xpath, pic_name, user_assigned_xpath=False, clip=None, mask=None, mask_color=None):
        print('@@@: screenshot clip: ' + str(clip))
        print('@@@: screenshot mask: ' + str(mask))
        self.__screenshot(locator_or_xpath, pic_name, user_assigned_xpath, clip, mask, mask_color)

    def screenshot_self(self, pic_name, clip=None, mask=None, mask_color=None):
        self.screenshot(self.base_xpath, pic_name, clip=clip, mask=mask, mask_color=mask_color)

    # Since it does NOT work (and I don't know why), comment it temporarily. Will investigate it later.
    # def screenshot_full_page(self,pic_name,mask=None):
    #     """"
    #     :param pic_name: Picture name that will be appended to image file name.
    #     :param mask: list of xpath or locators or mixture of them.
    #     :return:
    #     """
    #     final_full_path = self.get_screenshot_full_path(pic_name)
    #     if mask is None:
    #         self.page.screenshot(path=final_full_path,full_page=True)
    #         return
    #     locators_mask = self.transform_to_locators_list(mask)
    #     self.page.screenshot(path=final_full_path,mask=mask,full_page=True)

    """Updated by Alice on 2024/03/26 end"""

    def click_self(self):
        self.click(self.base_locator)
