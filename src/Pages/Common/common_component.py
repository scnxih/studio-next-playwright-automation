from src.Pages.Common.base_page import *
from abc import ABC, abstractmethod


class CommonComponent(BasePage, ABC):

    def __init__(self, container_base_xpath, page, data_test_id="", label="", aria_label="", class_attribute="",
                 aria_labelledby="", supplement_base_xpath=""):
        BasePage.__init__(self, page)
        self.base_xpath = container_base_xpath
        self.set_base_xpath()
        if self.current_frame == "":
            self.set_iframe("//iframe")
        if data_test_id != "":
            self.base_xpath += f"[@data-testid='{data_test_id}']"
        if label != "":
            self.label = label
            self.base_xpath += f"[.//label[text()='{label}']]"
        if aria_label != "":
            self.base_xpath += f"[@aria-label='{aria_label}']"
        if class_attribute != '':
            self.base_xpath += f"[@class='{class_attribute}']"
        if aria_labelledby != '':
            self.base_xpath += f"[@aria-labelledby='{aria_labelledby}']"
        if supplement_base_xpath != "":
            self.base_xpath += supplement_base_xpath
        class_name = type(self).__name__
        Helper.logger.debug("base_xpath of {0}:{1}".format(class_name,self.base_xpath))

    @abstractmethod
    def set_base_xpath(self):
        pass
