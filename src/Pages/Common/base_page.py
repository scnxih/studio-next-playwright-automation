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


def determine_importance():
    Helper.logger.info("Enter determine screenshot function")
    importance = inspect.currentframe().f_back.f_code.co_name.split("_")[-1]

    importance_dict = {
        "trivial": 1,
        "general": 2,
        "critical": 3
    }
    if importance_dict[importance] >= importance_dict[global_screenshot_importance]:
        if importance_dict[importance] == 1:
            Helper.logger.debug("Trivial screenshot level")
        elif importance_dict[importance] == 2:
            Helper.logger.debug("General screenshot level")
        elif importance_dict[importance] == 3:
            Helper.logger.debug("Critical screenshot level")

        return True


''' Added by Jacky(ID: jawang) on Sept. 5th, 2023 '''


class BasePage:
    current_frame = ""

    def __init__(self, page: Page):

        self.page: Page = page
        self.base_xpath = ""
        # self.data_locale = self.get_data_locale()

    @property
    def base_locator(self):
        if self.base_xpath == "":
            Helper.logger.debug("page_locator = None since base_path=''")
            return None
        return self.page.locator("xpath=" + self.base_xpath)

    def get_page(self):
        return self.page

    def set_iframe(self, xpath):
        pass

    def __resolve_xpath(self, xpath):

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
        self.clear(r_locator)
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

    # Modified by Jacky(ID: jawang) on Sept.22nd, 2023 >>>

    # -----Added by Frank 2023/09/18, begin----- #
    def combo_item_locator(self, combo_item_text: str):
        return self.locator("//span[contains(@class, 'ListBox-List')][text()='{0}']".format(combo_item_text))

    def click_combo_item(self, combo_item_text: str):
        self.click(self.combo_item_locator(combo_item_text))

    # -----Added by Frank 2023/09/18, end----- #

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.19th, 2023
    def __invoke_context_menu_by_right_click(self, locator_or_xpath):
        """
        Invoke context menu by right-click for sometimes Shift+F10 does not work
        :param locator_or_xpath: element ro right-click on
        :return: None
        """
        r_locator = self.transform_to_locator(locator_or_xpath)
        # r_locator.click()
        r_locator.click(button="right")

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
        return self.click_menu_item(*context_menu_text)

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.22nd, 2023
    def click_context_menu_by_right_click(self, locator_or_xpath, *context_menu_text):
        """

        :param locator_or_xpath:
        :param context_menu_text:
        :return:
        """
        r_locator = self.transform_to_locator(locator_or_xpath)
        r_locator.click()
        self.__invoke_context_menu_by_right_click(locator_or_xpath)
        time.sleep(0.3)
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

    # def screenshot_level_high(self,locator_or_xpath,pic_name):
    #     if global == low:

    # def wait_toast_disappear(self):
    #     # toaster = self.locator("xpath=.//div[@id='static-area']["
    #     #                        "@class='sas_components-MessageToast-MessageToaster_static-area']")
    #     toaster = self.locator("xpath=//span[contains(@id,'message-toast')]")
    #     Helper.logger.debug("wait_toast_disappear")
    #     if toaster is None:
    #         Helper.logger.debug("toast is none")
    #         return
    #     if toaster.is_visible():
    #         Helper.logger.debug("toast is_visible:")
    #     # if toaster.is_visible():
    #         toaster.wait_for(state="hidden")
    #         Helper.logger.debug("toast disappeared")
    #         time.sleep(2)
    #         Helper.logger.debug("toast disappeared 2 seconds later")

    # def screenshot(self,locator_or_xpath,pic_name):
    #
    #     class_name = type(self).__name__
    #     Helper.logger.debug("enter basepage::screenshot: type(self):"+class_name)
    #     current_test = os.environ.get('PYTEST_CURRENT_TEST')
    #     abs_path = os.path.abspath(__file__)
    #     Helper.logger.debug("PYTEST_CURRENT_TEST in base="+current_test)
    #     Helper.logger.debug("current abstract path="+abs_path)
    # here store_path is just an example, need to be handled to the Output folder and file name
    # need including test file prefix, test method prefix,class_name and pic_name
    # store_path = abs_path+current_test+class_name+pic_name
    #
    # if exist(store_path):
    #     store_path = store_path+"_1"

    # r_locator = self.transform_to_locator(locator)
    # r_locator.screenshot(path=store_path)

    # def screenshot_level_samll(self):
    #     if global_screenshot_level == ""
    # def screenshot_level_middle(self):
    # def screenshot_level_many(self):

    ''' Added by Jacky(ID: jawang) on Aug 30th, 2023 '''

    def screenshot(self, locator_or_xpath, pic_name, user_assigned_xpath=False):
        """
        :param locator_or_xpath: Element xpath used to take screenshots, which will be combined into final total xpath.
        :param pic_name: Picture name that will be appended to image file name
        :param user_assigned_xpath: If true, user assigned xpath will be used.
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
            # transform locator
            r_locator = self.transform_to_locator(locator_or_xpath)

        output_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../..")), "Output\\")
        # print("### Direct working dir: " + output_path)

        # Create Output folder
        # Should be ~/src/Output
        # Helper.create_folder(output_path, True)

        # Obtain Testcase Name from os.environ.get('PYTEST_CURRENT_TEST') which is:
        # Tests/CodeEditor/test_codeeditor_02.py::test_01_type_code (call)
        testfile_abbreviation = Helper.get_testfile_abbreviation()
        print("### Testcase Abbreviation: " + testfile_abbreviation)

        # Similar to testfile_abbreviation, obtain test method name from os.environ.get('PYTEST_CURRENT_TEST')
        testmethod_number = Helper.get_testmethod_number()
        print("### Testmethod Number: " + testmethod_number)

        class_name = type(self).__name__
        """Added by Alice on 2024/3/25 start"""
        function_name = inspect.currentframe().f_back.f_back.f_code.co_name
        """Added by Alice on 2024/3/25 end"""
        # print("### Test Class Name: " + class_name)

        # index to determine the duplicates
        index = 1
        ''' Revised by Jacky(ID: jawang) on Sept. 4th, 2023 '''

        # store path Last version INCORRECT screenshot_file_base = output_path + "\\" + testfile_abbreviation + "\\"
        # + testfile_abbreviation + "_" + testmethod_number + "_" + class_name + "_" + pic_name

        # Revised Version:
        # folder name = testfile_abbreviation + testmethod_number
        file_name = (testfile_abbreviation + "_" + testmethod_number + "_" +  # screenshot name part-1: same as directory name
                class_name + "_" +  # screenshot name part-2: Specific Class Name
                function_name + "_" +  # screenshot name part-3: Return function name which is calling generate_screenshot()
                pic_name)

        if len(file_name) >= 78:
            class_name = class_name[0:20]
            function_name = function_name[0:30]
            pic_name = pic_name[0:10]
            file_name = (testfile_abbreviation + "_" + testmethod_number + "_" +  # screenshot name part-1: same as directory name
                class_name + "_" +  # screenshot name part-2: Specific Class Name
                function_name + "_" +  # screenshot name part-3: Return function name which is calling generate_screenshot()
                pic_name)

        screenshot_file_base = (
            # directory name
                output_path + "\\" +  # screenshot storage root directory: ~src/Output
                testfile_abbreviation + "_" + testmethod_number + "\\" +file_name)  # directory for method of a testfile: ~src/Output/codeeditor_01_01


        """Added by Alice on 2024/3/25 start"""
        # When length is larger, truncate name.


        """Added by Alice on 2024/3/25 end"""
        # NOTE: CPython implementation detail:
        # This function relies on Python stack frame support in the interpreter,
        # which isn’t guaranteed to exist in all implementations of Python.
        # If running in an implementation without Python stack frame support this function returns None.
        # Reference Link: https://docs.python.org/3/library/inspect.html
        ''' Revised by Jacky(ID: jawang) on Sept. 4th, 2023 '''

        # print("### Screenshot path: " + screenshot_file_base)
        Helper.logger.debug("Screenshot path: " + screenshot_file_base)

        # Need to check if the screenshot already exist
        if not os.path.exists(f"{screenshot_file_base}{'_'}{index:02d}{'.png'}"):
            r_locator.screenshot(path=f"{screenshot_file_base}{'_'}{index:02d}{'.png'}")
            Helper.logger.debug("Generated Screenshot: " + f"{screenshot_file_base}{'_'}{index:02d}{'.png'}")

        else:
            # print("--- Need to manipulate ---")

            # Split File Name
            # file_base_name, extension = os.path.splitext(screenshot_file)
            while os.path.exists(f"{screenshot_file_base}{'_'}{index:02d}{'.png'}"):
                index += 1
            r_locator.screenshot(path=f"{screenshot_file_base}{'_'}{index:02d}{'.png'}")
            Helper.logger.debug("Generated Screenshot:" + f"{screenshot_file_base}{'_'}{index:02d}{'.png'}")

        Helper.logger.debug("Exit screenshot")

    ''' Added by Jacky(ID: jawang) on Aug 30th, 2023 '''

    ''' Added by Jacky(ID: jawang) on Aug 31st, 2023 '''

    # Screenshot Generation
    # Default level is 3, which can be omitted
    def generate_screenshot(self, locator_or_xpath, pic_name, screenshot_level=3):
        Helper.logger.info("Enter screenshot control function")
        if screenshot_level >= global_screenshot_level:
            if screenshot_level == 1:
                Helper.logger.debug("Lowest screenshot level")
            elif screenshot_level == 2:
                Helper.logger.debug("Low screenshot level")
            elif screenshot_level == 3:
                Helper.logger.debug("Middle screenshot level")
            elif screenshot_level == 4:
                Helper.logger.debug("High screenshot level")
            elif screenshot_level == 5:
                Helper.logger.debug("Highest screenshot level")

            self.screenshot(locator_or_xpath, pic_name)

    ''' Added by Jacky(ID: jawang) on Aug 31st, 2023 '''

    ''' Added by Jacky(ID: jawang) on Sept. 5th, 2023 '''

    # MODIFIED
    # Added new parameter user_assigned_xpath
    # If true, user-assigned xpath will be used for screenshot.
    # <<< Modified by Jacky(ID: jawang) on Sept.25th, 2023
    def screenshot_trivial(self, locator_or_xpath, pic_name, user_assigned_xpath=False):
        if determine_importance():
            Helper.logger.debug("Screenshot level: Trivial")
            self.screenshot(locator_or_xpath, pic_name, user_assigned_xpath)

    def screenshot_general(self, locator_or_xpath, pic_name, user_assigned_xpath=False):
        if determine_importance():
            Helper.logger.debug("Screenshot level: General")
            self.screenshot(locator_or_xpath, pic_name, user_assigned_xpath)

    def screenshot_critical(self, locator_or_xpath, pic_name, user_assigned_xpath=False):
        if determine_importance():
            Helper.logger.debug("Screenshot level: Critical")
            self.screenshot(locator_or_xpath, pic_name, user_assigned_xpath)

    # Modified by Jacky(ID: jawang) on Sept.25th, 2023 >>>

    """Added by Alice on 09/19/2023 start"""

    def right_click(self, locator_or_xpath):
        r_locator = self.transform_to_locator(locator_or_xpath)
        self.scroll_if_needed(r_locator)
        r_locator.click(button="right")

    def is_enabled(self, locator_or_xpath):
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
                self.__div_toast.wait_for(timeout=5000, state="visible")
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
        while not self.is_enabled(locator_or_xpath) and i < wait_time * 10:
            time.sleep(0.1)
            i = i + 1

        if self.is_enabled(locator_or_xpath):
            return True
        else:
            return False

    def screenshot_trivial_self(self, pic_name):
        self.screenshot_trivial(self.base_xpath, pic_name)

    def screenshot_general_self(self, pic_name):
        self.screenshot_general(self.base_xpath, pic_name)

    def screenshot_critical_self(self, pic_name):
        self.screenshot_critical(self.base_xpath, pic_name)
