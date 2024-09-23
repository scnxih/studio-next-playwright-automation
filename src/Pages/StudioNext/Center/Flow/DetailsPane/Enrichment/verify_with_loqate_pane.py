"""
@author: Dommy (Fuying) Chen
@date: 2024/09/23
@description: define panes of Verify with Loqate step
"""
from src.Pages.Common.common_component_factory import get_checkbox
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *


class VerifyWithLoqate(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Methods in Verify Address tab"""

    def set_check_enable_address_verification(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ENABLE_ADDRESS_VERIFICATION)

    def set_uncheck_enable_address_verification(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ENABLE_ADDRESS_VERIFICATION)

    def set_check_geocode_the_address(self):
        self.set_check_for_checkbox(label=Helper.data_locale.GEOCODE_THE_ADDRESS)

    def set_uncheck_geocode_the_address(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.GEOCODE_THE_ADDRESS)

    def set_check_perform_country_ISO_standardization_before_processing_address(self):
        self.set_check_for_checkbox(label=Helper.data_locale.PERFORM_COUNTRY_ISO_STANDARDIZATION_BEFORE_PROCESSING)

    def set_uncheck_perform_country_ISO_standardization_before_processing_address(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.PERFORM_COUNTRY_ISO_STANDARDIZATION_BEFORE_PROCESSING)

    def set_check_show_api_input_and_output_json_in_the_log(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_API_INPUT_AND_OUTPUT_JSON_IN_THE_LOG)

    def set_uncheck_show_api_input_and_output_json_in_the_log(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_API_INPUT_AND_OUTPUT_JSON_IN_THE_LOG)

    def set_batch_size_500_max(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.BATCH_SIZE_500_MAX,
                                       input_text=input_text)

    def expand_windowshade_map_the_fields_for_address_verification(self):
        self.expand_windowshade(parent_label=Helper.data_locale.MAP_THE_FIELDS_FOR_ADDRESS_VERIFICATION)

    def collapse_windowshade_map_the_fields_for_address_verification(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.MAP_THE_FIELDS_FOR_ADDRESS_VERIFICATION)

    def add_column_for_country(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.COUNTRY, column_name=column_name)

    def add_column_for_address_1(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ADDRESS_1, column_name=column_name)

    def add_column_for_postal_code(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.POSTAL_CODE, column_name=column_name)

    def add_column_for_locality_city_municipality(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.LOCALITY_CITY_MUNICIPALITY, column_name=column_name)

    def add_column_for_administrative_area_state_province(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ADMINISTRATIVE_AREA_STATE_PROVINCE, column_name=column_name)

    def add_column_for_organization(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.ORGANIZATION, column_name=column_name)

    def add_column_for_building(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.BUILDING, column_name=column_name)

    def add_column_for_post_box(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.POST_BOX, column_name=column_name)

    """Methods in Verify Email tab"""

    def click_verify_email_tab(self):
        self.click_tab(Helper.data_locale.VERIFY_EMAIL)

    def set_check_enable_email_verification(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ENABLE_EMAIL_VERIFICATION)

    def set_uncheck_enable_email_verification(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.ENABLE_EMAIL_VERIFICATION)

    def set_check_show_api_input_and_output_csv_in_the_log_email(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_API_INPUT_AND_OUTPUT_CSV_IN_THE_LOG)

    def set_uncheck_show_api_input_and_output_csv_in_the_log_email(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_API_INPUT_AND_OUTPUT_CSV_IN_THE_LOG)

    def set_batch_size_100_max(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.BATCH_SIZE_100_MAX,
                                       input_text=input_text)

    def add_column_for_email_address(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.EMAIL_ADDRESS, column_name=column_name)

    """Methods in Verify Phone Numbers tab"""

    def click_verify_phone_numbers_tab(self):
        self.click_tab(Helper.data_locale.VERIFY_PHONE_NUMBERS)

    def set_check_enable_phone_verification(self):
        self.set_check_for_checkbox(label=Helper.data_locale.ENABLE_PHONE_VERIFICATION)

    def set_check_perform_country_ISO_standardization_before_processing_phone(self):
        self.set_check_for_checkbox(label=Helper.data_locale.PERFORM_COUNTRY_ISO_STANDARDIZATION_BEFORE_PROCESSING)

    def set_uncheck_perform_country_ISO_standardization_before_processing_phone(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.PERFORM_COUNTRY_ISO_STANDARDIZATION_BEFORE_PROCESSING)

    def set_check_show_api_input_and_output_csv_in_the_log_phone(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_API_INPUT_AND_OUTPUT_CSV_IN_THE_LOG)

    def set_uncheck_show_api_input_and_output_csv_in_the_log_phone(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_API_INPUT_AND_OUTPUT_CSV_IN_THE_LOG)

    def add_column_for_phone_number(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.PHONE_NUMBER, column_name=column_name)

    def add_column_for_country_phone(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.COUNTRY, column_name=column_name)

    """Methods in Loqate Key tab"""

    def click_loqate_key_tab(self):
        self.click_tab(Helper.data_locale.LOQATE_KEY_UPPERCASE)

    def set_loqate_key(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.LOQATE_KEY,
                                       input_text=input_text)

    def set_check_test_mode(self):
        self.set_check_for_checkbox(label=Helper.data_locale.TEST_MODE)

    def set_uncheck_test_mode(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.TEST_MODE)

    """Methods in Options tab"""

    def set_check_Show_detailed_log_information(self):
        self.set_check_for_checkbox(label=Helper.data_locale.SHOW_DETAILED_LOG_INFORMATION)

    def set_uncheck_Show_detailed_log_information(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.SHOW_DETAILED_LOG_INFORMATION)
