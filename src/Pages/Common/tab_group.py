"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: September 11th, 2023
"""
from src.Pages.Common.base_page import *
from src.Pages.Common.common_component import CommonComponent

from src.Pages.StudioNext.Left.accordion_page import AccordionPage


class TabGroup(CommonComponent):
    """
    Used to define tab groups for SAS Program/Python Program/Quick Import/Flow/Custom Code Dialog/Autoexec Dialog
    """

    def set_base_xpath(self):
        self.base_xpath += "//ul[contains(@class, 'Scrollable')]"

    # Added supplement xpath to differentiate tab groups
    def __init__(self, container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
        CommonComponent.__init__(self,
                                 container_base_xpath=container_base_xpath,
                                 page=page,
                                 data_test_id=data_test_id,
                                 supplement_base_xpath=supplement_base_xpath)

    # TO-DO: Change to private
    def current_tab_group_by_descendant_text(self, tab_text):
        """
        Private
        :param tab_text:
        :return:
        """
        Helper.logger.debug("Get tab group from a tab page text.")
        Helper.logger.debug(f"[.//span[text()='{tab_text}']]")
        return self.locate_xpath(f"[.//span[text()='{tab_text}']]")

    # TO-DO: Change to private
    def current_tab_group_by_ancestor_div_test_id(self, test_id):
        """
        Private
        :param test_id:
        :return:
        """
        Helper.logger.debug("Get tab group from ancestor div testid.")
        Helper.logger.debug(f"[ancestor::div[@data-testid='{test_id}']]")

        return self.locate_xpath(f"[ancestor::div[@data-testid='{test_id}']]")

    def lower_left_corner_show_tab_labels_btn(self):
        """

        :return:
        """
        # return self.locate_xpath(f"/../../../../button[@title='显示选项卡标签'][contains(@data-testid, 'property')]")
        # acc: AccordionPage = AccordionPage(page)
        # return self.locate_xpath(f"[.//span[text()='打开项']]/../../../../button[@title='显示选项卡标签']")

        # WORKS FINE
        return self.locator("//ul[contains(@class, 'Scrollable')][.//span[text()='打开项']]/../../../../button[@aria-label='显示选项卡标签']")

        # NOT WORK
        # //ul[contains(@class, 'Scrollable')][.//span[text()='打开项']]/../../../../button[@title='显示选项卡标签']
        # Helper.logger.debug("Assembling left corner icon: " + self.base_xpath + "[.//span[text()='打开项']]/../../../../button[@aria-label='显示选项卡标签']")
        # return self.locate_xpath(f"[.//span[text()='打开项']]/../../../../button[@aria-label='显示选项卡标签']")

    def lower_right_show_corner_tab_labels_btn(self):
        """

        :return:
        """
        return self.locate_xpath(f"/../../../../button[@title='显示选项卡标签'][contains(@data-testid, 'property')]")

    def click_lower_left_corner_show_tab_labels_btn(self):
        """
        NOTE: This button is invisible at times
        :return:
        """
        self.lower_left_corner_show_tab_labels_btn().click()

    def click_lower_right_show_corner_tab_labels_btn(self):
        """

        :return:
        """
        self.lower_right_show_corner_tab_labels_btn().click()

    def nth_tab_page_by_text(self, tab_text, nth=1):
        """

        :param nth:
        :param tab_text:
        :return:
        """
        if self.locator_count(f"[.//span[text()='{tab_text}']]//li") >= nth:
            Helper.logger.debug(self.locator_count(f"[.//span[text()='{tab_text}']]//li"))
            return self.locate_xpath(f"[.//span[text()='{tab_text}']]//li[{nth}]")
        else:
            Helper.logger.debug("Index larger than number.")
            Helper.logger.debug(self.locator_count(f"[.//span[text()='{tab_text}']]//li"))
            Helper.logger.debug(f"[.//span[text()='{tab_text}']]//li[{nth}]")

    def first_tab_page_by_text(self, tab_text):
        """
        Return xpath of the FIRST tab page in a tab-group which contains the tab page with tab_text

        :return: FIRST tab page xpath
        """
        return self.locate_xpath(f"[.//span[text()='{tab_text}']]//li[1]")

    def last_tab_page_by_text(self, tab_text):
        """
        Return xpath of the LAST tab page in a tab-group which contains the tab page with tab_text
        :return: LAST tab page xpath
        """
        return self.locate_xpath(f"[.//span[text()='{tab_text}']]//li[last()]")

    def selected_tab_page_text(self, tab_text):
        """
        Return xpath of the selected tab page
        :param tab_text:
        :return:
        """
        return self.locate_xpath(f"[.//span[text()='{tab_text}']]/descendant::div[@aria-selected='true']")

    def tab_by_title(self, tab_title):
        """
        Tab page by specified tab title
        :param tab_title
        :return: Tab xpath
        """
        return self.locate_xpath(f"/descendant::li/descendant::span[@title='{tab_title}']")

    def tab_by_text(self, tab_text):
        """
        Tab from specified text
        :param tab_text:
        :return:
        """
        return self.locate_xpath(f"/descendant::li/descendant::span[text()='{tab_text}']")
    def tab_contains_text(self, tab_text):
        """
        Tab from specified text
        :param tab_text:
        :return:
        """
        return self.locate_xpath(f"/descendant::li/descendant::span[contains(text(),'{tab_text}')]")

    def click_first_tab_page_by_text(self, tab_text):
        """
        Click the FIRST tab page according to tab text as the input
        :param tab_text:
        :return:
        """
        self.first_tab_page_by_text(tab_text).click()

    def click_last_tab_page_by_text(self, tab_text):
        """
        Click the LAST tab page according to tab text as the input
        :param tab_text:
        :return:
        """
        self.last_tab_page_by_text(tab_text).click()

    def click_tab_by_title(self, tab_title):
        """
        Click tab page by specified tab title
        :param tab_title:
        :return:
        """
        self.click(self.tab_by_title(tab_title))

    def click_tab_by_text(self, tab_text):
        """
        Click tab page by specified tab text
        :param tab_text:
        :return:
        """
        self.click(self.tab_by_text(tab_text))

    def click_tab_contains_text(self, tab_text):
        """
        Click tab page by specified tab text
        :param tab_text:
        :return:
        """
        self.click(self.tab_contains_text(tab_text))

    def tag_group_layout_by_text(self, tab_text):
        """
        Return layout(Horizontal/Vertical) of tab-group
        NOTE: When opening some dialogs,
        the elements might take some time to appear.
        :param tab_text:
        :return:
        """

        self.wait_for_timeout(5 * 1000)
        if self.locator_count(
                f"[.//span[text()='{tab_text}']]/../../../../div[contains(@class, 'horizontal')]") is not 0:
            return "Horizontal"

        if self.locator_count(f"[.//span[text()='{tab_text}']]/../../../../div[contains(@class, 'vertical')]") is not 0:
            return "Vertical"

    def click_the_nth_tab_in_a_group_containing_text(self, tab_text, nth=1):
        self.nth_tab_page_by_text(tab_text, nth).click()

    """added by Alice on 10/24/2023 start"""
    def first_tab_page(self):
        """
        Return xpath of the FIRST tab page in a tab-group
        :return: FIRST tab page xpath
        """
        return self.locate_xpath(f"//li[1]")

    def click_first_tab_page(self):
        """
        Click the FIRST tab page
        :return:
        """
        self.first_tab_page().click()
    """added by Alice on 10/24/2023 end"""