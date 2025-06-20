import time

from playwright.sync_api import Locator
from src.Pages.Common.base_page import BasePage
from src.Utilities.enums import *
from src.Pages.Common.toolbar import *


class AccordionPage(BasePage):

    def __init__(self, page, title=''):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-AppRoot-AppLayout_content']/descendant::section[1]"
        # if self.current_frame == "":
        #     self.set_iframe("//iframe")
        if title != '':
            self.title = title
            self.base_xpath += f"[.//span[text()='" + title + "']]"
        self.toolbar = Toolbar(self.base_xpath, page)

    @property
    def icon_show_tab_labels(self):
        """
        Icon used to expand the Left Accordion by clicking the button in the lower left corner
        :return:
        """
        return self.locate_xpath(f"//button[@aria-label='" + Helper.data_locale.SHOW_TAB_LABELS + "']")

    @property
    def icon_hide_tab_labels(self):
        """
        Icon used to collapse the Left Accordion by clicking the button in the lower left corner
        :return:
        """
        return self.locate_xpath(f"//button[@aria-label='" + Helper.data_locale.HIDE_TAB_LABELS + "']")

    @property
    def ag_body_vertical_scroll_bar(self):
        """
        Vertical scroll bar xpath: //div[@class="ag-body-vertical-scroll"]
        """
        return self.locate_xpath("//div[@class='ag-body-vertical-scroll']")

    @property
    def tab_open_item(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-openItems-tabItem']")

    @property
    def tab_sas_server(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-sasServer-tabItem']")

    @property
    def tab_sas_content(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-sasContent-tabItem']")

    @property
    def tab_steps(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-steps-tabItem']")

    @property
    def tab_snippets(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-snippets-tabItem']")

    @property
    def tab_libraries(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-libraries-tabItem']")

    @property
    def tab_git(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-gitRepositories-tabItem']")

    @property
    def tab_file_references(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-fileReferences-tabItem']")

    @property
    def tab_clinical_repository(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-clinicalRepository-tabItem']")

    @property
    def accordion_pane(self):
        return self.page.locator(
            "//div[@class='sas_components-PropertyPaneLayout-PropertyPaneLayout_start-pane-container "
            "sas_components-PropertyPaneLayout-PropertyPaneLayout_without-start-pane-container-start-border']")

    @property
    def pane_open_item(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-openItems']")

    @property
    def pane_sas_server(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-sasServer-container']")

    @property
    def pane_sas_content(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-sasContent-container']")

    @property
    def pane_steps(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-steps']")

    @property
    def pane_snippets(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-snippets']")

    @property
    def pane_libraries(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-libraries']")

    @property
    def pane_git(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-gitRepositories']")

    @property
    def pane_file_references(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-fileReferences']")

    @property
    def pane_clinical_repository(self):
        return self.locate_xpath("//div[@data-testid='studioPropertiesLayout-clinicalRepository']")

    def get_pane(self, accordion_type: AccordionType):
        pane = self.pane_open_item
        match accordion_type:
            case accordion_type.open_item:
                pane = self.pane_open_item
            case accordion_type.sas_content:
                pane = self.pane_sas_content
            case accordion_type.sas_server:
                pane = self.pane_sas_server
            case accordion_type.steps:
                pane = self.pane_steps
            case accordion_type.snippets:
                pane = self.pane_snippets
            case accordion_type.libraries:
                pane = self.pane_libraries
            case accordion_type.git:
                pane = self.pane_git
            case accordion_type.file_references:
                pane = self.pane_file_references
            case accordion_type.clinical_repository:
                pane = self.pane_clinical_repository
        return pane

    def get_tab(self, accordion_type: AccordionType):
        tab = self.tab_open_item
        match accordion_type:
            case accordion_type.open_item:
                tab = self.tab_open_item
            case accordion_type.sas_content:
                tab = self.tab_sas_content
            case accordion_type.sas_server:
                tab = self.tab_sas_server
            case accordion_type.steps:
                tab = self.tab_steps
            case accordion_type.snippets:
                tab = self.tab_snippets
            case accordion_type.libraries:
                tab = self.tab_libraries
            case accordion_type.git:
                tab = self.tab_git
            case accordion_type.file_references:
                tab = self.tab_file_references
            case accordion_type.clinical_repository:
                tab = self.tab_clinical_repository

        return tab

    def show_accordion(self, accordion_type: AccordionType):
        pane: Locator = self.get_pane(accordion_type)
        tab: Locator = self.get_tab(accordion_type)

        if self.is_visible(pane):
            return

        self.click(tab)

        while True:
            if self.is_visible(pane):
                break
            self.click(tab)
            self.get_pane(accordion_type).page.wait_for_timeout(timeout=500)

            # time.sleep(0.5)
        # time.sleep(0.5)
        self.get_tab(accordion_type).page.wait_for_timeout(timeout=500)

    def hide_accordion(self, accordion_type: AccordionType):
        """
        Hide Left Accordion to eliminate any possible noises.
        """
        pane: Locator = self.get_pane(accordion_type)
        tab: Locator = self.get_tab(accordion_type)

        if not self.is_visible(pane):
            return

        self.click(tab)

        while True:
            if not self.is_visible(pane):
                break
            self.click(tab)
            # self.get_pane(accordion_type).page.wait_for_timeout(timeout=500)

            # time.sleep(0.5)
        # time.sleep(0.5)
        # self.get_tab(accordion_type).page.wait_for_timeout(timeout=500)

    def collapse_all(self):
        self.toolbar.click_menu_in_more_options(Helper.data_locale.COLLAPSE_ALL)

    def show_tab_labels(self):
        """
        Expand the Accordion by clicking the button in the lower left corner
        :return:
        """
        self.locate_xpath(f"//button[@aria-label='" + Helper.data_locale.SHOW_TAB_LABELS + "']").click()

    def hide_tab_labels(self):
        """
        Collapse the Accordion by clicking the button in the lower left corner
        :return:
        """
        self.locate_xpath(f"//button[@aria-label='" + Helper.data_locale.HIDE_TAB_LABELS + "']").click()

    def click_more_options(self):
        self.toolbar.click_more_options()
