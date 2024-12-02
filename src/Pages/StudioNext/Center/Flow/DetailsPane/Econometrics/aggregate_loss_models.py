"""
@author: Alice
@date: 2024/11/22
@description: Define Aggregate Loss Models pane
"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class AggregateLossModelsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Data tab"""

    def set_server(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SELECT_A_SERVER_FOR_THIS_STEP,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_severity(self):
        self.expand_windowshade(parent_label=Helper.data_locale.SEVERITY)

    def collapse_windowshade_severity(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.SEVERITY)

    def set_loss_severity_model(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SPECIFY_LOSS_SEVERITY_MODEL,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_count(self):
        self.expand_windowshade(parent_label=Helper.data_locale.COUNT)

    def collapse_windowshade_count(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.COUNT)

    def set_loss_count_model(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.SPECIFY_LOSS_COUNT_MODEL,
                                        item_index=item_index, item_value=item_value)

    def set_count_model_type(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.COUNT_MODEL_TYPE,
                                        item_index=item_index, item_value=item_value)

    """Methods in Severity tab"""

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_column_for_loss_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LOSS_VARIABLE, column_name=column_name)


    def add_columns_for_continuous_variables_in_severity(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns_with_supplement_xpath(supplement_xpath="[../../../descendant::label[contains(text(),'{0}')]/../../../../../.././../../../descendant::label[contains(text(),'{1}')]]".
                                               format(Helper.data_locale.CONTINUOUS_VARIABLES,Helper.data_locale.LOSS_VARIABLE),
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_categorical_variables_in_severity(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns_with_supplement_xpath(
            supplement_xpath="[../../../descendant::label[contains(text(),'{0}')]/../../../../../.././../../../descendant::label[contains(text(),'{1}')]]".
            format(Helper.data_locale.CATEGORICAL_VARIABLES, Helper.data_locale.LOSS_VARIABLE),
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)



    def set_check_left_censoring_limit(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SET_LEFT_CENSORING_LIMIT)

    def set_uncheck_left_censoring_limit(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SET_LEFT_CENSORING_LIMIT)

    """Methods in Count tab"""
    def add_column_for_dependent_count_variable(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.DEPENDENT_COUNT_VARIABLE, column_name=column_name)

    def add_columns_for_continuous_variables_in_count(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns_with_supplement_xpath(supplement_xpath="[../../../descendant::label[contains(text(),'{0}')]/../../../../../.././../../../descendant::label[contains(text(),'{1}')]]".
                                               format(Helper.data_locale.CONTINUOUS_VARIABLES,Helper.data_locale.DEPENDENT_COUNT_VARIABLE),
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def add_columns_for_categorical_variables_in_count(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns_with_supplement_xpath(
            supplement_xpath="[../../../descendant::label[contains(text(),'{0}')]/../../../../../.././../../../descendant::label[contains(text(),'{1}')]]".
            format(Helper.data_locale.CATEGORICAL_VARIABLES, Helper.data_locale.DEPENDENT_COUNT_VARIABLE),
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)
    def expand_windowshade_distribution(self):
        self.expand_windowshade(parent_label=Helper.data_locale.DISTRIBUTION)

    def collapse_windowshade_distribution(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.DISTRIBUTION)

    """Methods in Options tab"""
    def set_sample_size(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.SAMPLE_SIZE, input_text=input_text)

    def set_maxi_number_of_loss_count(self,input_text:str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_LOSS_COUNT_FOR_SIMULATING_ONE_AGGREGATE_LOSS_SAMPLE_POINT, input_text=input_text)

    def set_statistics_to_display(self, item_index=None, item_value=None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.STATISTICS_TO_DISPLAY,
                                        item_index=item_index, item_value=item_value)

    def set_check_probability_density_function(self):
        self.set_check_for_checkbox(label=Helper.data_locale.PROBABILITY_DENSITY_FUNCTION)
    def set_uncheck_probability_density_function(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.PROBABILITY_DENSITY_FUNCTION)
    def set_check_empirical_distribution_function(self):
        self.set_check_for_checkbox(label=Helper.data_locale.EMPIRICAL_DISTRIBUTION_FUNCTION)
    def set_uncheck_empirical_distribution_function(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.EMPIRICAL_DISTRIBUTION_FUNCTION)

    """Methods in Output tab"""
    def set_check_save_summary_statistics_of_aggregate_loss_sample_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_SUMMARY_STATISTICS_OF_AGGREGATE_LOSS_SAMPLES_DATA)

    def set_uncheck_save_summary_statistics_of_aggregate_loss_sample_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_SUMMARY_STATISTICS_OF_AGGREGATE_LOSS_SAMPLES_DATA)

    def set_check_save_aggregate_loss_samples_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SAVE_AGGREGATE_LOSS_SAMPLES_DATA)

    def set_uncheck_save_aggregate_loss_samples_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SAVE_AGGREGATE_LOSS_SAMPLES_DATA)


