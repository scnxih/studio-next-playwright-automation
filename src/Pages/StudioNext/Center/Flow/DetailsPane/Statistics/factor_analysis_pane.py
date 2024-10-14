"""
@author: Liu Jia
@date: 2024/09/29
@description: Define Factor Analysis pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class FactorAnalysisPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""
    def add_columns_for_analysis_variables(self, check_column_name_list: list = None,
                                           uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.ANALYSIS_VARIABLES,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_additional_roles(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)
    def unexpand_windowshade_additional_roles(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_columns_for_variables_partial_out(self, check_column_name_list: list = None,
                                              uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.VARIABLES_TO_PARTIAL_OUT,check_column_name_list=check_column_name_list,uncheck_column_name_list=uncheck_column_name_list)

    def add_column_frequency_count(self, parent_label: str, column_name: str, section_label: str = None):
        self.add_column(parent_label=Helper.data_locale.FREQUENCY_COUNT, column_name=column_name)

    def add_column_weight(self, parent_label: str, column_name: str, section_label: str = None):
        self.add_column(parent_label=Helper.data_locale.WEIGHT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,check_column_name_list=check_column_name_list, uncheck_column_name_list=uncheck_column_name_list)

    """Methods in Option tab"""
    def expand_windowshade_factor_extraction(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.FACTOR_EXTRACTION)
    def unexpand_windowshade_factor_extraction(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.FACTOR_EXTRACTION)
    def set_check_show_only_common_extraction_methods(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_ONLY_COMMON_EXTRACTION_METHODS)
    def set_uncheck_show_only_common_extraction_methods(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_ONLY_COMMON_EXTRACTION_METHODS)
    def set_select_factor_extraction_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.FACTOR_EXTRACTION_METHOD, item_index=item_index,item_value=item_value)
    def set_select_number_of_factors(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.NUMBER_OF_FACTORS, item_index=item_index,item_value=item_value)
    def set_value_for_custom_number_of_factors(self, value:str = None):
        self.set_value_for_numeric_stepper(parent_label=Helper.data_locale.CUSTOM_NUMBER_OF_FACTORS,value=value)

    def expand_windowshade_rotation(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.ROTATION)
    def unexpand_windowshade_rotation(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.ROTATION)
    def set_select_factor_rotation_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.ROTATION_METHOD, item_index=item_index,item_value=item_value)

    """Rotation methods==Biquartimax"""
    def set_select_type_of_rotation(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_TYPE_ROTATION,item_index=item_index,item_value=item_value)
    def expand_windowshade_rotation(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.DETAILS)
    def unexpand_windowshade_rotation(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.DETAILS)
    def set_select_method_to_normalize_factor_rows(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METHOD_TO_NORMALIZE_FACTOR_PATTERN_ROWS, item_index=item_index,item_value=item_value)
    def set_check_specify_maximum_number_of_rotation_cycles(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_MAXIMUM_NUMBER_OF_ROTATION_CYCLES)
    def set_uncheck_specify_maximum_number_of_rotation_cycles(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_MAXIMUM_NUMBER_OF_ROTATION_CYCLES)
    def set_maximum_number_of_rotation_cycles(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_ROTATION_CYCLES, input_text=input_text)

    """Rotation methods==Oblimin"""
    def set_check_specify_oblimin_weight(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_OBLIMIN_WEIGHT)
    def set_uncheck_specify_oblimin_weight(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_OBLIMIN_WEIGHT)
    def set_oblimin_weight(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.OBLIMIN_WEIGHT, input_text=input_text)

    """Rotation methods==Orthomax"""
    def set_check_specify_orthomax_weight(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_ORTHOMAX_WEIGHT)
    def set_uncheck_specify_orthomax_weight(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_ORTHOMAX_WEIGHT)
    def set_orthomax_weight(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.ORTHOMAX_WEIGHT, input_text=input_text)

    """Rotation methods==Promax"""
    def set_select_prerotation_method_for_promax_rotation(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.PREROTATION_METHOD_FOR_PROMAX_ROTATION, item_index=item_index,item_value=item_value)
    def set_check_specify_power_for_promax_rotation(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SPECIFY_POWER_FOR_PROMAX_ROTATION)
    def set_uncheck_specify_power_for_promax_rotationt(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SPECIFY_POWER_FOR_PROMAX_ROTATION)
    def set_power_for_promax_rotation(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.POWER_FOR_PROMAX_ROTATION, input_text=input_text)
    def expand_windowshade_statistics(self, parent_label: str):
        self.expand_windowshade(parent_label=Helper.data_locale.STATISTICS)
    def unexpand_windowshade_statistics(self, parent_label: str):
        self.collapse_windowshade(parent_label=Helper.data_locale.STATISTICS)
    def set_select_statistics_to_display(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SELECT_STATISTICS_TO_DISPLAY,item_index=item_index, item_value=item_value)
    def set_check_descriptive_statistics(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DESCRIPTIVE_STATISTICS)
    def set_uncheck_descriptive_statistics(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DESCRIPTIVE_STATISTICS)
    def set_check_correlations(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CORRELATIONS)
    def set_uncheck_correlations(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CORRELATIONS)
    def set_check_residual_correlations(self):
        self.set_check_for_checkbox(label=Helper.data_locale.RESIDUAL_CORRELATIONS)
    def set_uncheck_residual_correlation(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.RESIDUAL_CORRELATIONS)
    def set_check_eigenvectors(self):
        self.set_check_for_checkbox(label=Helper.data_locale.EIGENVECTORS)
    def set_uncheck_eigenvectors(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.EIGENVECTORS)
    def set_check_factor_scoring_coefficients(self):
        self.set_check_for_checkbox(label=Helper.data_locale.FACTOR_SCORING_COEFFICIENTS)
    def set_uncheck_factor_scoring_coefficient(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.FACTOR_SCORING_COEFFICIENTS)
    def set_check_kaisers_measure_of_sampling_adequacy(self):
        self.set_check_for_checkbox(label=Helper.data_locale.KAISER_MEASURE_SAMPLING_ADEQUACY)
    def set_uncheck_kaisers_measure_of_sampling_adequacy(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.KAISER_MEASURE_SAMPLING_ADEQUACY)
    def set_check_kaisers_measure_of_sampling_adequacy(self):
        self.set_check_for_checkbox(label=Helper.data_locale.KAISER_MEASURE_SAMPLING_ADEQUACY)
    def set_uncheck_kaisers_measure_of_sampling_adequacy(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.KAISER_MEASURE_SAMPLING_ADEQUACY)