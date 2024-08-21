"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 19th, 2024
"""
import time

# -*- coding: UTF-8 -*-
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class TextParsingAndTopicAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_input_table_contains(self, item_index: int = None, item_value: str = None):
        """
        The input table contains:
        0  Unparsed Text
        1  Term-by-document matrix

        """
        self.click_Tab(Helper.data_locale.DATA)

        self.set_option_for_radio_group(parent_label=Helper.data_locale.THE_INPUT_TABLE_CONTAINS,
                                        item_index=item_index,
                                        item_value=item_value)

        self.screenshot_self("set_plot_orientation")

    def set_language(self, item_index: int = None, item_value: str = None):
        """

        """
        # Switch to Data tab page
        self.click_Tab(Helper.data_locale.DATA)

        # Select Language
        self.set_option_for_combobox(parent_label=Helper.data_locale.LANGUAGE,
                                     item_index=item_index, item_value=item_value)

        time.sleep(0.5)
        self.screenshot_self("set_language")

    def set_text_variable(self, column_name: str):
        """
        Data/Text variable
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.add_column(parent_label=Helper.data_locale.TEXT_VARIABLE,
                        column_name=column_name)

        self.screenshot_self("set_text_variable")

    def set_topic_model(self, item_index: int = None, item_value: str = None):
        """
        Check '' in Options tab page
        """
        # Switch to Options tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        self.set_option_for_radio_group(parent_label=Helper.data_locale.TOPIC_MODEL,
                                        item_index=item_index,
                                        item_value=item_value)

        self.screenshot_self("set_topic_model")

    def set_number_of_topics_to(self, input_text: str):
        """
        Set 'Number of Topics' to
        xpath: //div[@class='sas_components-views-dataflow-FlowView_selected-pane']//input[@type='text' or @type='tel'][../../../../descendant::label[contains(text(), '主题数')]]
        """
        self.click_Tab(Helper.data_locale.OPTIONS)

        # self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_TOPICS, input_text=input_text)

        self.locate_xpath("//div[@class='sas_components-views-dataflow-FlowView_selected-pane']//input[@type='text' or @type='tel'][../../../../descendant::label[contains(text(), '主题数')]]").fill(input_text)

        self.screenshot_self("set_number_of_topics_to")


    def set_scree_plot_of_singular_values(self):
        """
        Check '' in Options tab page
        """
        # Switch to Options tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        # Collapse window shade 'Parse text'
        # self.collapse_windowshade(Helper.data_locale.PARSE_TEXT

        # Collapse window shade 'Discover Topics'
        # self.collapse_windowshade(Helper.data_locale.DISCOVER_TOPICS)

        self.set_check_for_checkbox(label=Helper.data_locale.SCREE_PLOT_OF_SINGULAR_VALUES)

        self.screenshot_self("set_scree_plot_of_singular_values")

    def set_save_term_by_document_matrix(self):
        """
        Check combobox Save term-by-document matrix
        """
        # Switch to Output tab page
        self.click_Tab(Helper.data_locale.OUTPUT)

        # Check combobox Output/Save term-by-document matrix
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_TERM_BY_DOCUMENT_MATRIX)

        self.screenshot_self("set_save_term_by_document_matrix")

    def set_save_term_information(self):
        """
        Check combobox Output/Save term information
        """
        # Switch to Output tab page
        self.click_Tab(Helper.data_locale.OUTPUT)

        # Check combobox Output/Save term information
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_TERM_INFORMATION)

        self.screenshot_self("set_save_term_information")

