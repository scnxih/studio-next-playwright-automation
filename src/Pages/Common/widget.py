"""
File: widget.py
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: 2023/9/19 11:01 
"""

from src.Pages.Common.common_component import CommonComponent


class Widget(CommonComponent):
    """
    For widgets, such as Find, Go to Line and Command Line.
    """

    def set_base_xpath(self):
        # self.base_xpath += "//div[contains(@class, 'widget')]"
        self.base_xpath += "//div[contains(@widgetid, 'Widget')]"

    def __init__(self, container_base_xpath, page):
        CommonComponent.__init__(self, container_base_xpath=container_base_xpath, page=page)

    def textarea_by_placeholder(self, placeholder):
        """
        Get textarea xpath according to placeholder.
        :param placeholder: placeholder text
        :return: textarea xpath
        """
        return self.locate_xpath(f"//textarea[@placeholder='" + placeholder + "']")

    def fill_textarea_by_placeholder(self, placeholder, user_input):
        """
        Fill in widget textarea with input from user
        :param user_input:
        :param placeholder:
        :return:
        """
        self.textarea_by_placeholder(placeholder).fill(user_input)

    def input_by_placeholder(self, placeholder):
        """
        Get input xpath according to placeholder.
        :param placeholder: placeholder text
        :return: input xpath
        """
        return self.locate_xpath(f"//input[@placeholder='" + placeholder + "']")

    def fill_input_by_placeholder(self, placeholder, user_input):
        """
        Fill in widget input with input from user
        :param placeholder:
        :param user_input:
        :return:
        """
        self.input_by_placeholder(placeholder).fill(user_input)

    def btn_by_title(self, title):
        """
        Get button xpath according to title.
        :param title: button title
        :return: button xpath
        """
        return self.locate_xpath(f"//div[@role='button'][@title='" + title + "']")

    def btn_by_aria_label(self, aria_label):
        """
        Get button xpath according to aria-label.
        :param aria_label: button aria-label
        :return: button xpath
        """
        return self.locate_xpath(f"//div[@role='button'][@aria-label='" + aria_label + "']")

    def checkbox_by_title(self, title):
        """
        Get checkbox(such as Match Case, Match Whole Word and Use Regular Expression in Code Editor Find widget) xpath
        according to title.
        :param title: checkbox title
        :return: checkbox
        """
        return self.locate_xpath(f"//div[@role='checkbox'][@title='" + title + "']")

    def click_btn_by_title(self, title):
        """
        Click button according to title.
        :param title:
        :return:
        """
        self.btn_by_title(title).click()

    def click_btn_by_aria_label(self, aria_label):
        """
        Click button according to aria-label.
        :param aria_label:
        :return:
        """
        self.btn_by_aria_label(aria_label).click()

    def toggle_checkbox_by_title(self, title):
        """
        Toggle checkbox according to title
        :param title:
        :return:
        """
        self.checkbox_by_title(title).click()

    """Added by Alice on Mar 15,2024 start"""
    def toggle_on_checkbox_by_title(self,title):
        """
        Make sure the checkbox is toggled on
        :param title:
        :return:
        """
        if self.checkbox_by_title(title).get_attribute("aria-checked").lower() == "true":
            return
        self.toggle_checkbox_by_title(title)

    def toggle_off_checkbox_by_title(self,title):
        """
        Make sure the checkbox is toggled off
        :param title:
        :return:
        """
        if self.checkbox_by_title(title).get_attribute("aria-checked").lower() == "true":
            self.toggle_checkbox_by_title(title)
    """Added by Alice on Mar 15,2024 end"""

