"""
@author: Frank (Feng) Jiang
@date: 2024/09/09
@description: define panes of t Tests step
"""
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class TTestsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def input_filter_input_data(self, filter_expression: str):
        self.set_filter_input_data(filter_expression)

    def empty_filter_input_data(self):
        self.set_filter_input_data("")

    def set_t_tests_type(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.T_TEST_LOWER, item_index=item_index,
                                     item_value=item_value)

    def add_column_for_analysis_var(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ANALYSIS_VARIABLE, column_name=column_name)

    def delete_column_for_analysis_var(self):
        self.delete_column(parent_label=Helper.data_locale.ANALYSIS_VARIABLE)

    def add_column_for_group1_var(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.GROUP_1_VAR, column_name=column_name)

    def delete_column_for_group1_var(self):
        self.delete_column(parent_label=Helper.data_locale.GROUP_1_VAR)

    def add_column_for_group2_var(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.GROUP_2_VAR, column_name=column_name)

    def delete_column_for_group2_var(self):
        self.delete_column(parent_label=Helper.data_locale.GROUP_2_VAR)

    def add_column_for_class_var(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.CLASS_VAR, column_name=column_name)

    def delete_column_for_class_var(self):
        self.delete_column(parent_label=Helper.data_locale.CLASS_VAR)

    """Methods in Options tab"""
    def expand_windowshade_tests(self):
        self.expand_windowshade(parent_label=Helper.data_locale.TESTS)

    def collapse_windowshade_tests(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.TESTS)

    def set_tails_type(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.TAILS, item_index=item_index,
                                     item_value=item_value)

    def input_alternative_hypothesis(self, alternative_hypothesis: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.ALTERNATIVE_HYPOTHESIS,
                                       input_text=alternative_hypothesis)

    def empty_alternative_hypothesis(self):
        self.set_text_for_text_control(parent_label=Helper.data_locale.ALTERNATIVE_HYPOTHESIS, input_text="")

    def set_check_tests_for_normality(self):
        self.set_check_for_checkbox(label=Helper.data_locale.TESTS_FOR_NORMALITY)

    def set_uncheck_tests_for_normality(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.TESTS_FOR_NORMALITY)

    def set_check_sign_test_Wilcoxon_signed_rank_test(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SIGN_TEST_WILCOXON_SIGNED_RANK_TEST)

    def set_uncheck_sign_test_Wilcoxon_signed_rank_test(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SIGN_TEST_WILCOXON_SIGNED_RANK_TEST)

    def set_check_cox_cochran_probability_approximation_for_unequal_variances(self):
        self.set_check_for_checkbox(label=Helper.data_locale.COX_COCHRAN_PROB_APPR_FOR_UNEQUAL_VARIANCES)

    def set_uncheck_cox_cochran_probability_approximation_for_unequal_variances(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.COX_COCHRAN_PROB_APPR_FOR_UNEQUAL_VARIANCES)

    def set_check_wilcoxon_rank_sum_test(self):
        self.set_check_for_checkbox(label=Helper.data_locale.WILCOXON_RANK_SUM_TEST)

    def set_uncheck_wilcoxon_rank_sum_test(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.WILCOXON_RANK_SUM_TEST)

    def expand_windowshade_plots(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PLOTS)

    def collapse_windowshade_plots(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PLOTS)

    def set_plots_combo(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.PLOTS, item_index=item_index, item_value=item_value)

    def set_check_histogram_and_box_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.HISTOGRAM_AND_BOX_PLOT)

    def set_uncheck_histogram_and_box_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.HISTOGRAM_AND_BOX_PLOT)

    def set_check_normality_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.NORMALITY_PLOT)

    def set_uncheck_normality_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.NORMALITY_PLOT)

    def set_check_confidence_interval_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CONFIDENCE_INTERVAL_PLOT)

    def set_uncheck_confidence_interval_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CONFIDENCE_INTERVAL_PLOT)

    def set_check_agreement_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.AGREEMENT_PLOT)

    def set_uncheck_agreement_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.AGREEMENT_PLOT)

    def set_check_response_profile_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.RESPONSE_PROFILE_PLOT)

    def set_uncheck_response_profile_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.RESPONSE_PROFILE_PLOT)

    def set_check_wilcoxon_box_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.WILCOXON_BOX_PLOT)

    def set_uncheck_wilcoxon_box_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.WILCOXON_BOX_PLOT)
