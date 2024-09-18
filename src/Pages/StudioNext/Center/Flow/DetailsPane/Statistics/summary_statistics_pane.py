"""
@author: Liu Jia
@date: 2024/09/05
@description: Define summary statistics pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *

class SummaryStatisticsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_columns_for_analysis_variables(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ANALYSIS_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_classification_variable(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.CLASSIFICATION_VARIABLE,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
    def set_combinations_of_classification_variables(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.COMBINAIONS_OF_CLASSIFICATION_VARIABLE, item_index=item_index,
                                     item_value=item_value)
    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_columns_for_copy_variables(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.COPY_VARIABLES, check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)
    def add_column_for_frequency_count(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)
    def add_column_for_weight_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.WEIGHT_VARIABLE, column_name=column_name)

    """Methods in Option tab"""
    def expand_windowshade_basic_statistics(self):
        self.expand_windowshade(parent_label=Helper.data_locale.BASIC_STATISTICS)
    def collape_windowshade_basic_statistics(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.BASIC_STATISTICS)
    def set_check_mean(self):
        self.set_check_for_checkbox(Helper.data_locale.MEAN)
    def set_uncheck_mean(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.MEAN)
    def set_check_standard_deviation(self):
        self.set_check_for_checkbox(Helper.data_locale.STANDARD_DEVIATION)
    def set_uncheck_standard_deviation(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.STANDARD_DEVIATION)
    def set_check_minimum_value(self):
        self.set_check_for_checkbox(Helper.data_locale.MINIMUM_VALUE)
    def set_uncheck_minimum_value(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.MINIMUM_VALUE)
    def set_check_maximum_value(self):
        self.set_check_for_checkbox(Helper.data_locale.MAXIMUM_VALUE)
    def set_uncheck_maximum_value(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.MAXIMUM_VALUE)
    def set_check_number_of_observations(self):
        self.set_check_for_checkbox(Helper.data_locale.NUMBER_OF_OBSERVATIONS)
    def set_uncheck_number_of_observations(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.NUMBER_OF_OBSERVATIONS)
    def set_check_number_of_missing_values(self):
        self.set_check_for_checkbox(Helper.data_locale.NUMBER_OF_MISSING_VALUES)
    def set_uncheck_number_of_missing_values(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.NUMBER_OF_MISSING_VALUES)
    def set_maximum_decimal(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.MAXIMUM_DECIMAL, item_index=item_index,
                                     item_value=item_value)
    def set_divisor_for_standard_deviation_variance(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.DIVISOR_FOR_STANDARD_DEVIATION_AND_VARIANCE, item_index=item_index,
                                     item_value=item_value)
    """ Additional_statistics """
    def expand_windowshade_additional_statistics(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_STATISTICS)
    def collape_windowshade_additional_statistics(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_STATISTICS)
    def set_check_standard_error(self):
        self.set_check_for_checkbox(Helper.data_locale.STANDARD_ERROR)
    def set_uncheck_standard_error(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.STANDARD_ERROR)
    def set_check_variance(self):
        self.set_check_for_checkbox(Helper.data_locale.VARIANCE)
    def set_uncheck_variance(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.VARIANCE)
    def set_check_mode(self):
            self.set_check_for_checkbox(Helper.data_locale.MODE)
    def set_uncheck_mode(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.MODE)
    def set_check_range(self):
            self.set_check_for_checkbox(Helper.data_locale.RANGE)
    def set_uncheck_range(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.RANGE)
    def set_check_sum(self):
            self.set_check_for_checkbox(Helper.data_locale.SUM)
    def set_uncheck_sum(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.SUM)
    def set_check_sum_of_weights(self):
            self.set_check_for_checkbox(Helper.data_locale.SUM_OF_WEIGHTS)
    def set_uncheck_sum_of_weights(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.SUM_OF_WEIGHTS)
    def set_check_confidence_limits_for_mean(self):
            self.set_check_for_checkbox(Helper.data_locale.CONFIDENCE_LIMITS_FOR_MEAN)
    def set_uncheck_confidence_limits_for_mean(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.CONFIDENCE_LIMITS_FOR_MEAN)
    def set_check_t_statistic_and_prob(self):
            self.set_check_for_checkbox(Helper.data_locale.T_STATISTIC_PROB)
    def set_uncheck_t_statistic_and_prob(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.T_STATISTIC_PROB)
    def set_check_coefficient_of_variation(self):
            self.set_check_for_checkbox(Helper.data_locale.COEFFICIENT_OF_VARIATION)
    def set_uncheck_coefficient_of_variation(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.COEFFICIENT_OF_VARIATION)
    def set_check_corrected_sum_squares(self):
            self.set_check_for_checkbox(Helper.data_locale.CORRECTED_SUM_SQUARES)
    def set_uncheck_corrected_sum_squares(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.CORRECTED_SUM_SQUARES)
    def set_check_uncorrected_sum_squares(self):
            self.set_check_for_checkbox(Helper.data_locale.UNCORRECTED_SUM_SQUARES)
    def set_uncheck_uncorrected_sum_squaress(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.UNCORRECTED_SUM_SQUARES)
    def set_check_skewness(self):
            self.set_check_for_checkbox(Helper.data_locale.SKEWNESS)
    def set_uncheck_skewness(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.SKEWNESS)
    def set_check_kurtosis(self):
            self.set_check_for_checkbox(Helper.data_locale.KURTOSIS)
    def set_uncheck_kurtosis(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.KURTOSIS)
    """ Percentiles """
    def expand_windowshade_percentiles(self):
            self.expand_windowshade(parent_label=Helper.data_locale.PERCENTILES)
    def collapse_windowshade_percentiles(self):
            self.collapse_windowshade(parent_label=Helper.data_locale.PERCENTILES)
    def set_check_first(self):
            self.set_check_for_checkbox(Helper.data_locale.FIRST)
    def set_uncheck_first(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.FIRST)
    def set_check_fifth(self):
            self.set_check_for_checkbox(Helper.data_locale.FIFTH)
    def set_uncheck_fifth(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.FIFTH)
    def set_check_tenth(self):
            self.set_check_for_checkbox(Helper.data_locale.TENTH)
    def set_uncheck_tenth(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.TENTH)
    def set_check_tenth(self):
            self.set_check_for_checkbox(Helper.data_locale.TENTH)
    def set_uncheck_tenth(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.TENTH)
    def set_check_lower_quartile(self):
            self.set_check_for_checkbox(Helper.data_locale.LOWER_QUARTILE)
    def set_uncheck_lower_quartile(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.LOWER_QUARTILE)
    def set_check_median(self):
            self.set_check_for_checkbox(Helper.data_locale.MEDIAN)
    def set_uncheck_mediane(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.MEDIAN)
    def set_check_upper_quartile(self):
            self.set_check_for_checkbox(Helper.data_locale.UPPER_QUARTILE)
    def set_uncheck_upper_quartile(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.UPPER_QUARTILE)
    def set_check_ninetieth(self):
            self.set_check_for_checkbox(Helper.data_locale.NINETIETH)
    def set_uncheck_ninetieth(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.NINETIETH)
    def set_check_ninety_fifth(self):
            self.set_check_for_checkbox(Helper.data_locale.NINETY_FIFTH)
    def set_uncheck_ninety_fifth(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.NINETY_FIFTH)
    def set_check_ninety_ninth(self):
            self.set_check_for_checkbox(Helper.data_locale.NINETY_NINTH)
    def set_uncheck_ninety_ninth(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.NINETY_NINTH)
    def set_check_interquartile_range(self):
            self.set_check_for_checkbox(Helper.data_locale.INTERQUARTILE_RANGE)
    def set_uncheck_interquartile_range(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.INTERQUARTILE_RANGE)
    def set_quantile_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.QUANTILE_METHOD, item_index=item_index,
                                     item_value=item_value)
    """ Plots """
    def expand_windowshade_plots(self):
            self.expand_windowshade(parent_label=Helper.data_locale.PLOTS)
    def collapse_windowshade_plots(self):
            self.collapse_windowshade(parent_label=Helper.data_locale.PLOTS)
    def expand_windowshade_histogram(self):
            self.expand_windowshade(parent_label=Helper.data_locale.HISTOGRAM)
    def collapse_windowshade_histogram(self):
            self.collapse_windowshade(parent_label=Helper.data_locale.HISTOGRAM)
    def set_check_histogram(self):
            self.set_check_for_checkbox(Helper.data_locale.HISTOGRAM)
    def set_uncheck_histogram(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.HISTOGRAM)
    def set_check_add_normal_density_curve(self):
            self.set_check_for_checkbox(Helper.data_locale.ADD_NORMAL_DENSITY_CURVE)
    def set_uncheck_add_normal_density_curve(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.ADD_NORMAL_DENSITY_CURVE)
    def set_check_add_kernel_density_estimate(self):
            self.set_check_for_checkbox(Helper.data_locale.ADD_KERNEL_DENSITY_ESTIMATE)
    def set_uncheck_add_kernel_density_estimate(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.ADD_KERNEL_DENSITY_ESTIMATE)
    def set_check_add_inset_statistics(self):
            self.set_check_for_checkbox(Helper.data_locale.ADD_INSET_STATISTICS)
    def set_uncheck_add_inset_statistics(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.ADD_INSET_STATISTICS)
    def set_position_at(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.POSITION_AT, item_index=item_index,
                                     item_value=item_value)
    def set_start(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.START, input_text=input_text)
    def set_end(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.END, input_text=input_text)
    def set_step(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.STEP, input_text=input_text)

    """ Box Plots """
    def expand_windowshade_box_plot(self):
            self.expand_windowshade(parent_label=Helper.data_locale.STEP_BOX_PLOT)
    def collapse_windowshade_box_plot(self):
            self.collapse_windowshade(parent_label=Helper.data_locale.STEP_BOX_PLOT)
    def set_check_box_plot(self):
            self.set_check_for_checkbox(Helper.data_locale.STEP_BOX_PLOT)
    def set_uncheck_box_plot(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.STEP_BOX_PLOT)
    def set_check_add_overall_inset_statistics(self):
            self.set_check_for_checkbox(Helper.data_locale.ADD_OVERALL_INSET_STATISTICS)
    def set_uncheck_add_overall_inset_statistics(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.ADD_OVERALL_INSET_STATISTICS)

    """Methods in Titles tab"""
    def expand_windowshade_analysis(self):
            self.expand_windowshade(parent_label=Helper.data_locale.ANALYZE)
    def collape_windowshade_analysis(self):
            self.collapse_windowshade(parent_label=Helper.data_locale.ANALYZE)
    def set_check_use_default_text(self):
            self.set_check_for_checkbox(Helper.data_locale.USE_DEFAULT_TEXT)
    def set_uncheck_use_default_text(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.USE_DEFAULT_TEXT)
    def set_analysis_text(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TEXT_FOR_ANALYSIS, input_text=input_text)
    def set_Histogram_text(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TEXT_FOR_HISTOGRAM, input_text=input_text)
    def set_boxt_plot_text(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TEXT_FOR_BOX_PLOT, input_text=input_text)
    def set_footnote_text(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.TEXT_FOR_FOOTNOTE, input_text=input_text)
    """Methods in OUTPUT tab"""
    def set_check_create_output_data(self):
            self.set_check_for_checkbox(Helper.data_locale.CREATE_OUTPUT_DATA)
    def set_uncheck_create_output_data(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.CREATE_OUTPUT_DATA)
    def set_check_replace_existing_output_table(self):
            self.set_check_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_uncheck_replace_existing_output_table(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.REPLACE_EXISTING_OUTPUT_TABLE)
    def set_check_show_statistics(self):
        self.set_check_for_checkbox(Helper.data_locale.SHOW_STATISTICS)
    def set_uncheck_show_statistics(self):
        self.set_uncheck_for_checkbox(Helper.data_locale.SHOW_STATISTICS)
    def set_check_show_analysis_labels(self):
            self.set_check_for_checkbox(Helper.data_locale.SHOW_ANALYSIS_LABELS)
    def set_uncheck_show_analysis_labelse(self):
            self.set_uncheck_for_checkbox(Helper.data_locale.SHOW_ANALYSIS_LABELS)
