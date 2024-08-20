"""
@File: one-way_frequencies
@Author: Allison
@Date: 8/19/2024 3:14 AM 
@Description: 

"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class OneWayFrequencies(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

        """Data tab"""

    def add_columns_for_analysis_variables(self, check_column_name_list: list = None,
                                           uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ANALYSIS_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additonal_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.Frequency_Count, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    """Options tab"""

    """Added by Alice on Aug 21, 2024 start"""
    def set_check_for_asymptotic_test_1(self):

        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../preceding-sibling::div[1][.//span[text()='{1}']]]".format(
                         "渐近检验", "二项式比例")).set_check()

    def set_uncheck_for_asymptotic_test_1(self):

        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../preceding-sibling::div[1][.//span[text()='{1}']]]".format(
                         "渐近检验", "二项式比例")).set_uncheck()

    def set_check_for_asymptotic_test_2(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../preceding-sibling::div[1][.//span[text()='{1}']]]".format(
                         "渐近检验", "卡方拟合优度")).set_check()

    def set_uncheck_for_asymptotic_test_2(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../preceding-sibling::div[1][.//span[text()='{1}']]]".format(
                         "渐近检验", "卡方拟合优度")).set_uncheck()

    def set_check_for_exact_test_1(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../following-sibling::div[1][.//span[contains(text(),'{1}')]]]".format(
                         "精确检验", "卡方拟合优度")).set_check()

    def set_uncheck_for_exact_test_1(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../following-sibling::div[1][.//span[contains(text(),'{1}')]]]".format(
                         "精确检验", "卡方拟合优度")).set_uncheck()

    def set_check_for_exact_test_2(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../preceding-sibling::div[1][.//label[contains(text(),'{1}')]]]".format(
                         "精确检验", "渐近检验")).set_check()

    def set_uncheck_for_exact_test_2(self):
        get_checkbox(self.base_xpath, self.page,
                     supplement_base_xpath="[.//label[text()='{0}']][../../preceding-sibling::div[1][.//label[contains(text(),'{1}')]]]".format(
                         "精确检验", "渐近检验")).set_uncheck()

    def expand_windowshade_statistics(self):
        self.expand_windowshade(parent_label="统计量")

    """Added by Alice on Aug 21, 2024 end"""