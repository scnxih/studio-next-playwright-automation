"""This is test case file for step Verify with Loqate"""
"""Added by Dommy 2024-9-25"""
from src.Pages.StudioNext.Center.Flow.DetailsPane.Enrichment.verify_with_loqate_pane import VerifyWithLoqate
from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import TablePane
from src.conftest import *
from src.Helper.page_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *


@pytest.mark.level0_step
def test_01_verify_with_loqate_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.set_check_enable_address_verification()
    verify_with_loqate_pane.expand_windowshade_map_the_fields_for_address_verification()
    verify_with_loqate_pane.add_column_for_country("Country'测试")
    verify_with_loqate_pane.add_column_for_address_1("City'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)

@pytest.mark.level1_step
def test_02_verify_with_loqate_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.set_check_enable_address_verification()
    verify_with_loqate_pane.set_check_geocode_the_address()
    verify_with_loqate_pane.set_check_perform_country_ISO_standardization_before_processing_address()
    verify_with_loqate_pane.set_check_show_api_input_and_output_json_in_the_log()
    verify_with_loqate_pane.set_batch_size_500_max("300")

    verify_with_loqate_pane.expand_windowshade_map_the_fields_for_address_verification()
    verify_with_loqate_pane.add_column_for_country("Country'测试")
    verify_with_loqate_pane.add_column_for_address_1("Street Name'测试")
    verify_with_loqate_pane.add_column_for_postal_code("Postal_Code'测试")
    verify_with_loqate_pane.add_column_for_locality_city_municipality("City'测试")
    verify_with_loqate_pane.add_column_for_administrative_area_state_province("State'测试")
    verify_with_loqate_pane.add_column_for_sub_administrative_area_county_region("Regione'测试")
    verify_with_loqate_pane.add_column_for_organization("Organization'测试")
    verify_with_loqate_pane.add_column_for_building("Building'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)

@pytest.mark.level1_step
def test_03_verify_with_loqate_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.click_verify_email_tab()
    verify_with_loqate_pane.set_check_enable_email_verification()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_email()
    verify_with_loqate_pane.set_batch_size_100_max("50")
    verify_with_loqate_pane.add_column_for_email_address("Email'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)

@pytest.mark.level1_step
def test_04_verify_with_loqate_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.click_verify_phone_numbers_tab()
    verify_with_loqate_pane.set_check_enable_phone_verification()
    verify_with_loqate_pane.set_check_perform_country_iso_standardization_before_processing_phone()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_phone()
    verify_with_loqate_pane.add_column_for_phone_number("Phone'测试")
    verify_with_loqate_pane.add_column_for_country_phone("Country'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)

@pytest.mark.level1_step
def test_05_verify_with_loqate_in_flow(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    step_path = [Helper.data_locale.STEP_CATEGORY_DEVELOP, Helper.data_locale.STEP_SAS_PROGRAM]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM)
    sas_program_pane = SASProgramPane(page)
    code = """ 
libname AUTOLIB '/segatest/I18N/Autolib' ;
run;
"""
    sas_program_pane.type_into_text_area(code)

    flow.add_node(FlowNodeType.table)
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    table_pane = TablePane(page)
    table_pane.set_library("AUTOLIB")
    table_pane.set_table("LOQATE.数据'TEST")
    time.sleep(0.8)
    flow.link_two_nodes_in_flow(Helper.data_locale.SAS_PROGRAM, "LOQATE.数据'TEST")
    flow.arrange_nodes()
    flow.run(True)

    step_path = [Helper.data_locale.STEP_CATEGORY_ENRICHMENT, Helper.data_locale.STEP_VERIFY_WITH_LOQATE]
    flow.add_step_from_stepspane_to_flow(step_path)
    flow.link_two_nodes_in_flow("LOQATE.数据'TEST", Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    flow.click_on_canvas_in_flow()
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.STEP_VERIFY_WITH_LOQATE)
    verify_with_loqate_pane = VerifyWithLoqate(page)
    verify_with_loqate_pane.set_check_enable_address_verification()
    verify_with_loqate_pane.set_check_geocode_the_address()
    verify_with_loqate_pane.set_check_perform_country_ISO_standardization_before_processing_address()
    verify_with_loqate_pane.set_check_show_api_input_and_output_json_in_the_log()
    verify_with_loqate_pane.set_batch_size_500_max("300")

    verify_with_loqate_pane.expand_windowshade_map_the_fields_for_address_verification()
    verify_with_loqate_pane.add_column_for_country("Country'测试")
    verify_with_loqate_pane.add_column_for_address_1("Street Name'测试")
    verify_with_loqate_pane.add_column_for_postal_code("Postal_Code'测试")
    verify_with_loqate_pane.add_column_for_locality_city_municipality("City'测试")
    verify_with_loqate_pane.add_column_for_administrative_area_state_province("State'测试")
    verify_with_loqate_pane.add_column_for_sub_administrative_area_county_region("Regione'测试")
    verify_with_loqate_pane.add_column_for_organization("Organization'测试")
    verify_with_loqate_pane.add_column_for_building("Building'测试")

    verify_with_loqate_pane.click_verify_email_tab()
    verify_with_loqate_pane.set_check_enable_email_verification()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_email()
    verify_with_loqate_pane.set_batch_size_100_max("50")
    verify_with_loqate_pane.add_column_for_email_address("Email'测试")

    verify_with_loqate_pane.click_verify_phone_numbers_tab()
    verify_with_loqate_pane.set_check_enable_phone_verification()
    verify_with_loqate_pane.set_check_perform_country_iso_standardization_before_processing_phone_both()
    verify_with_loqate_pane.set_check_show_api_input_and_output_csv_in_the_log_phone_both()
    verify_with_loqate_pane.add_column_for_phone_number("Phone'测试")

    verify_with_loqate_pane.click_loqate_key_tab()
    verify_with_loqate_pane.set_loqate_key("YG77-BY96-PA11-KM34")
    verify_with_loqate_pane.set_uncheck_test_mode()
    flow.run(True)
