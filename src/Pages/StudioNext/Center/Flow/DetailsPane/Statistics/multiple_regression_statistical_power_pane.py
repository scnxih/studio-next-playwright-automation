""""
@author: Dommy (Fuying) Chen
@date: 2024/11/29
@description: define panes of Transform Columns step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class MultipleRegressionStatisticalPowerPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Options tab"""
    def set_solve_for(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SOLVE_FOR,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_analysis_details(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ANALYSIS_DETAILS)

    def collapse_windowshade_analysis_details(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ANALYSIS_DETAILS)

    def set_select_fixed_or_random_predictors(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_FIXED_OR_RANDOM_PREDICTORS,
                                        item_index=item_index, item_value=item_value)

    def set_check_include_intercept_in_model(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_THE_INTERCEPT_IN_THE_MODEL)

    def set_uncheck_include_intercept_in_model(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.INCLUDE_THE_INTERCEPT_IN_THE_MODEL)

    def expand_windowshade_significance_level(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SIGNIFICANCE_LEVEL)

    def collapse_windowshade_significance_level(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.SIGNIFICANCE_LEVEL)

    def set_alpha_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.ALPHA_VALUE, input_text=input_value)

    def expand_windowshade_number_of_predictors(self):
        self.expand_windowshade(parent_label=Helper.data_locale.NUMBER_OF_PREDICTORS)

    def collapse_windowshade_number_of_predictors(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NUMBER_OF_PREDICTORS)

    def set_number_of_full_model_predictors(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_FULL_MODEL_PREDICTORS, input_text=input_value)

    def set_number_of_reduced_model_predictors(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_REDUCED_MODEL_PREDICTORS, input_text=input_value)

    def expand_windowshade_variance_accounted_for(self):
        self.expand_windowshade(parent_label=Helper.data_locale.VARIANCE_ACCOUNTED_FOR)

    def collapse_windowshade_variance_accounted_for(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.VARIANCE_ACCOUNTED_FOR)

    def set_select_a_form(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SELECT_A_FORM,item_index=item_index,item_value=item_value)

    def set_full_model_rsquare_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.FULL_MODEL_RSQUARE_VALUE, input_text=input_value)

    def set_reduced_model_rsquare_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.REDUCED_MODEL_RSQUARE_VALUE, input_text=input_value)

    def set_partial_correlation_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.PARTIAL_CORRELATIONS_VALUE, input_text=input_value)

    def expand_windowshade_sample_size(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SAMPLE_SIZE)

    def collapse_windowshade_sample_size(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.SAMPLE_SIZE)

    def set_check_allow_fractional_sample_sizes(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ALLOW_FRACTIONAL_SAMPLE_SIZE)

    def set_uncheck_allow_fractional_sample_sizes(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ALLOW_FRACTIONAL_SAMPLE_SIZE)

    def set_sample_size_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.SAMPLE_SIZE_VALUE, input_text=input_value)

    def expand_windowshade_power(self):
        self.expand_windowshade(parent_label=Helper.data_locale.POWER)

    def collapse_windowshade_power(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.POWER)

    def set_power_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.POWER_VALUE, input_text=input_value)

    """Methods in Plots tab"""

    def expand_windowshade_plots(self):
        self.expand_windowshade(parent_label=Helper.data_locale.PLOTS)

    def collapse_windowshade_plots(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.PLOTS)

    def set_check_power_by_sample_size_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.POWER_BY_SAMPLE_SIZE_PLOT)

    def set_uncheck_power_by_sample_size_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.POWER_BY_SAMPLE_SIZE_PLOT)

    def set_check_minimum_sample_size(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MINIMUM_SAMPLE_SIZE)

    def set_uncheck_minimum_sample_size(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MINIMUM_SAMPLE_SIZE)

    def set_minimum_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MINIMUM_VALUE, input_text=input_value)

    def set_check_maximum_sample_size(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MAXIMUM_SAMPLE_SIZE)

    def set_uncheck_maximum_sample_size(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MAXIMUM_SAMPLE_SIZE)

    def set_maximum_value(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MAXMUM_VALUE, input_text=input_value)

    def set_check_power_by_effect_size_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.POWER_BY_EFFECT_SIZE_PLOT)

    def set_uncheck_power_by_effect_size_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.POWER_BY_EFFECT_SIZE_PLOT)

    def set_check_minimum_effect_size(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MINIMUM_EFFECT_SIZE)

    def set_uncheck_minimum_effect_size(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MINIMUM_EFFECT_SIZE)

    def set_minimum_rsquare(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MINIMUM_RSQUARE, input_text=input_value)

    def set_check_maximum_effect_size(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MAXIMUM_EFFECT_SIZE)

    def set_uncheck_maximum_effect_size(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MAXIMUM_EFFECT_SIZE)

    def set_maximum_rsquare(self, input_value: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MAXIMUM_RSQUARE, input_text=input_value)

    def set_check_minimum_power(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MINIMUM_POWER)

    def set_uncheck_minimum_power(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MINIMUM_POWER)

    def set_check_maximum_power(self):
        self.set_check_for_checkbox(label=Helper.data_locale.MAXIMUM_POWER)

    def set_uncheck_maximum_power(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.MAXIMUM_POWER)

    def set_check_sample_size_by_effect_size_plot(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAMPLE_SIZE_BY_EFFECT_SIZE_PLOT)

    def set_uncheck_sample_size_by_effect_size_plot(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAMPLE_SIZE_BY_EFFECT_SIZE_PLOT)
