"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 13th, 2024
"""
# -*- coding: UTF-8 -*-
from src.Helper.helper import Helper
from src.Pages.Common.common_component_factory import get_combobox, get_text
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class BoxPlotPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_option_for_combobox(self, parent_label: str, section_label: str = None, item_index: int = None,
                                item_value: str = None):
        """
        Overwrite
        """
        combobox = None
        if section_label is None:

            combobox = get_combobox(self.base_xpath,
                                    self.page,
                                    supplement_base_xpath="[../../../../../../../descendant::label[contains(text(),'{0}')]]".format(
                                        parent_label))
            Helper.logger.debug("*** Overwriting ***")

        else:
            combobox = get_combobox(self.base_xpath,
                                    self.page,
                                    supplement_base_xpath="[../../../../../../../../descendant::label[contains(text(),'{0}')]/../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{1}')]]]".format(
                                        parent_label, section_label))

        if item_index is not None:
            combobox.select_item_by_index(item_index)
            return
        if item_value is not None:
            combobox.select_item(item_value)
            return

    def set_filter_input_data(self, input_text: str):
        """
        First switch to Data tab page, then set filter input data.
        """

        # Switch to Data tab page
        self.click_Tab(Helper.data_locale.DATA)

        # Set filter input data
        self.set_text_for_text_control(parent_label=Helper.data_locale.FILTER_INPUT_DATA,
                                       input_text=input_text)

        self.screenshot_self("set_filter_input_data")

    def set_plot_orientation(self, item_index: int = None, item_value: str = None):
        """
        Data/Plot orientation
        0 = Vertical
        1 = Horizontal
        """
        self.click_Tab(Helper.data_locale.DATA)

        self.set_option_for_radio_group(parent_label=Helper.data_locale.PLOT_ORIENTATION,
                                        item_index=item_index,
                                        item_value=item_value)

    def set_analysis_variable(self, column_name: str):
        """
        Data/Analysis variable
        """
        self.click_Tab(Helper.data_locale.DATA)
        self.add_column(parent_label=Helper.data_locale.ANALYSIS_VARIABLE, column_name=column_name)

    def set_subcategory(self, column_name: str):
        """
        Data/Category
        """
        self.click_Tab(Helper.data_locale.DATA)
        self.add_column(parent_label=Helper.data_locale.SUBCATEGORY, column_name=column_name)

    def set_group_analysis_by(self, column_name: str):
        """
        Data/Group analysis by
        """
        self.click_Tab(Helper.data_locale.DATA)
        self.expand_windowshade(Helper.data_locale.ADDITIONAL_ROLES)
        self.add_column(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, column_name=column_name)

        # Collapse Additional Roles window shade
        self.collapse_windowshade(Helper.data_locale.ADDITIONAL_ROLES)

    def set_width_to(self, width: str):
        """

        """
        self.click_Tab(Helper.data_locale.OPTIONS)

        # TO-DO

    def set_check_notches(self):
        """
        Check notches in Options tab page
        """
        self.click_Tab(Helper.data_locale.OPTIONS)
        self.expand_windowshade(Helper.data_locale.BOX)
        self.set_check_for_checkbox(label=Helper.data_locale.NOTCHES)

        # Collapse Box window shade
        self.collapse_windowshade(Helper.data_locale.BOX)

    def set_color_transparency_percentage(self, item_index: int = None, item_value: str = None):
        """

        """
        self.click_Tab(Helper.data_locale.OPTIONS)
        self.expand_windowshade(Helper.data_locale.BOX)
        self.set_option_for_combobox(parent_label=Helper.data_locale.COLOR_TRANSPARENCY,
                                     item_index=item_index, item_value=item_value)
        # Collapse Box window shade
        self.collapse_windowshade(Helper.data_locale.BOX)

    def set_effect(self, item_index: int = None, item_value: str = None):
        """

        """
        # Switch to Options tab page
        self.click_Tab(Helper.data_locale.OPTIONS)

        # Expand the Box window shade
        self.expand_windowshade(Helper.data_locale.BOX)

        # Set Effect in Combo-Box
        self.set_option_for_combobox(parent_label=Helper.data_locale.EFFECT,
                                     item_index=item_index,
                                     item_value=item_value)

        # Collapse Box window shade
        self.collapse_windowshade(Helper.data_locale.BOX)

    def set_title_as(self, input_text: str):
        """
        Set the title in 'Options' tab page as
        """
        self.click_Tab(Helper.data_locale.OPTIONS)
        self.expand_windowshade(Helper.data_locale.TITLE_AND_FOOTNOTE)
        self.set_text_for_text_control(parent_label=Helper.data_locale.TITLE,
                                       input_text=input_text)

        # Collapse window shade: Title and FootNote
        self.collapse_windowshade(Helper.data_locale.TITLE_AND_FOOTNOTE)

    def set_footnote_as(self, input_text: str):
        """
        Set the title in 'Options' tab page as
        """
        self.click_Tab(Helper.data_locale.OPTIONS)
        self.expand_windowshade(Helper.data_locale.TITLE_AND_FOOTNOTE)
        self.set_text_for_text_control(parent_label=Helper.data_locale.FOOTNOTE,
                                       input_text=input_text)

        # Collapse window shade: Title and FootNote
        self.collapse_windowshade(Helper.data_locale.TITLE_AND_FOOTNOTE)

    def set_graph_size_unit(self, item_index: int = None, item_value: str = None):
        """

        """
        self.click_Tab(Helper.data_locale.OPTIONS)
        self.expand_windowshade(Helper.data_locale.GRAPH_SIZE)
        self.set_option_for_combobox(parent_label=Helper.data_locale.UNIT,
                                     item_index=item_index,
                                     item_value=item_value)

        # Collapse window shade: Graph Size
        self.collapse_windowshade(Helper.data_locale.GRAPH_SIZE)

    def set_graph_size_width_to(self, width: str):
        """

        """
        self.click_Tab(Helper.data_locale.OPTIONS)

        self.expand_windowshade(Helper.data_locale.GRAPH_SIZE)

        # self.set_text_for_text_control(parent_label=Helper.data_locale.WIDTH, input_text=width)

        # get_text(self.base_xpath, self.page, supplement_base_xpath="[../../../../descendant::label[contains(text(), '宽度')]]").fill_text(width)
        get_text(self.base_xpath,
                 self.page,
                 supplement_base_xpath="[../../../../descendant::label[text()='宽度:']]").fill_text(width)

        self.screenshot_self("set_graph_size_width")

        # Collapse window shade: Graph Size
        self.collapse_windowshade(Helper.data_locale.GRAPH_SIZE)
