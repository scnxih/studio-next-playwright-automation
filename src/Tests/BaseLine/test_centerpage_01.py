import time

from pip._internal.cli.cmdoptions import python

from src.Pages.Common.whole_page import WholePage
from src.Pages.StudioNext.Center.codeeditor_page import CodeEditorPage
from src.conftest import *
from src.Pages.Common.text import *
from src.Helper.page_factory import *


def test_init(page, init):
    PageHelper.init_environments(page)


def test_25_central_toolbar_run_cancel_save_saveas(page, init):
    # Original
    WholePage(page).screenshot_self("login")

    PageHelper.new_sas_program(page)

    editor = CodeEditorPage(page)

    # Cease hard-coded wait
    # time.sleep(1)

    editor.click_dialog_title_or_studionext_header()

    # WholePage(page).screenshot_self("newprogram")
    editor.prt_scn("newprogram")

    # editor.type_code_in_codeeditor("data test;set sashelp.class;run;")
    editor.editor.human_mimic_typing("proc iml;\n"
                                     "start row(x);\n"
                                     "return(repeat(T(1:nrow(x)), 1, ncol(x)));\n"
                                     "finish;\n"
                                     "start col(x);\n"
                                     "return(repeat(1:ncol(x), nrow(x)));\n"
                                     "finish;\n"
                                     "p=10;\n"
                                     "x=j(p, p, 0);\n"
                                     "r=row(x);\n"
                                     "c=col(x);\n"
                                     "lowerIdx=loc(r > c);\n"
                                     "call randseed(12345);\n"
                                     "y=j(1, ncol(lowerIdx));\n"
                                     "call randgen(y, \"Normal\");\n"
                                     "x[lowerIdx]=y;\n"
                                     "print x;")
    editor.run(True)

    editor.saveas(Helper.public_folder_path, "test.sas", True, True)

    editor.editor.human_mimic_typing("\n")
    editor.editor.human_mimic_typing("\nproc print data=sashelp.class;"
                                     "run;")
    editor.save()
    SASProgramPage(page).format_program()

    editor.save()
    editor.run(True)


def test_26_undo_redo_run_format_debug_codetoflow_snippets_clear(page, init):
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")
    page1: Page = page
    time.sleep(0.5)
    page1.keyboard.press("Enter")

    editor.click_dialog_title_or_studionext_header()
    time.sleep(0.5)

    editor.prt_scn('00')
    WholePage(page).screenshot_self("00")

    WholePage(page).screenshot_self("01")
    editor.prt_scn('01')

    time.sleep(0.5)

    editor.editor.force_click(editor.editor.get_text_area())
    page1.keyboard.press("End")

    # Former Version
    # page1.keyboard.press("/")
    # page1.keyboard.press("*")
    # page1.keyboard.press("T")
    # page1.keyboard.press("h")
    # page1.keyboard.press("i")
    # page1.keyboard.press("s")
    # page1.keyboard.press("Space")
    # page1.keyboard.press("i")
    # page1.keyboard.press("s")
    # page1.keyboard.press("Space")
    # page1.keyboard.press("t")
    # page1.keyboard.press("e")
    # page1.keyboard.press("s")
    # page1.keyboard.press("t")
    # page1.keyboard.press(".")
    # page1.keyboard.press("Space")
    # page1.keyboard.press("*")
    # page1.keyboard.press("/")

    # Replaced with press_consequentially
    editor.editor.human_mimic_typing("\n/* --- Mimic Human Typing --- */")
    editor.editor.human_mimic_typing("\n/*        *       */")
    editor.editor.human_mimic_typing("\n/*       **       */")
    editor.editor.human_mimic_typing("\n/*     * ** *     */")
    editor.editor.human_mimic_typing("\n/*    ** ** **    */")
    editor.editor.human_mimic_typing("\n/*  * ** ** ** *  */")
    editor.editor.human_mimic_typing("\n/* ** ** ** ** ** */")
    editor.editor.human_mimic_typing("\n/*  * ** ** ** *  */")
    editor.editor.human_mimic_typing("\n/*  * ** ** ** *  */")
    editor.editor.human_mimic_typing("\n/*    ** ** **    */")
    editor.editor.human_mimic_typing("\n/*     * ** *     */")
    editor.editor.human_mimic_typing("\n/*       **       */")
    editor.editor.human_mimic_typing("\n/*        *       */")
    editor.editor.human_mimic_typing("\n/* --- Mimic Human Typing --- */")
    # ** ** ** ** *
    # ** ** ** *
    # ** ** *
    # ** *
    # *
    WholePage(page).screenshot_self("02")
    editor.prt_scn('02')

    for i in range(3):
        editor.undo()
        time.sleep(0.5)
    WholePage(page).screenshot_self("03")
    editor.prt_scn('03')

    for i in range(3):
        editor.redo()
        time.sleep(0.5)

    WholePage(page).screenshot_self("04")
    editor.prt_scn('04')

    editor.run(True)
    time.sleep(0.5)

    editor.format_program()

    # Added to eliminate noise caused by scrollbar
    time.sleep(3.0)

    # Original
    WholePage(page).screenshot_self("05")
    editor.prt_scn('05')

    time.sleep(0.5)
    editor.debug()

    # Added to eliminate noise caused by scrollbar
    time.sleep(0.5)

    WholePage(page).screenshot_self("06")
    editor.prt_scn('06')

    time.sleep(0.5)
    editor.code_to_flow()
    time.sleep(1)

    WholePage(page).screenshot_self("07")
    editor.prt_scn('07')

    time.sleep(0.5)
    editor.add_to_snippets()

    # Original
    WholePage(page).screenshot_self("08")
    editor.prt_scn('08')

    time.sleep(1.0)
    editor.clear_code()

    if WholePage(page).wait_toast_pop():
        # Use the screenshot_self overwritten in WholePage
        WholePage(page).screenshot_self("09")
        editor.prt_scn('09')

    editor.clear_log()

    if WholePage(page).wait_toast_pop():
        WholePage(page).screenshot_self("10")
        editor.prt_scn('10')

    editor.clear_output_data()

    if WholePage(page).wait_toast_pop():
        WholePage(page).screenshot_self("11")
        editor.prt_scn('11')

    editor.clear_results()

    if WholePage(page).wait_toast_pop():
        # Take the screenshot when toast message popped up
        # Otherwise do not take the screenshots
        WholePage(page).screenshot_self("12")
        editor.prt_scn('12')

    editor.clear_listing()

    # Original
    # time.sleep(1.0)
    # WholePage(page).screenshot_self("13")

    if WholePage(page).wait_toast_pop():
        WholePage(page).screenshot_self("13")
        editor.prt_scn('13')

    editor.clear_all()

    # Original
    # time.sleep(1.0)
    # WholePage(page).screenshot_self("14")

    # '//div[@data-testid="programViewPane-toolbar"]'],
    if WholePage(page).wait_toast_pop():
        WholePage(page).screenshot_self("14")
        editor.prt_scn('14')


def test_27_run_open_in_browser_tab_schedule_as_job_analyze_and_create_flow_add_to_my_favorites(page, init):
    """
    Run a *.sas program, then open summary/code/log/results/listing in a new tab.
    """
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")
    editor.format_program()
    editor.run(True)
    editor.schedule_as_job()
    editor.analyze_and_create_flow()
    editor.add_to_my_favorites()
    editor.open_in_browser_tab_summary()
    editor.open_in_browser_tab_submitted_code()
    editor.open_in_browser_tab_log()
    editor.open_in_browser_tab_results()
    editor.open_in_browser_tab_listing()


def test_28_run_download(page, init):
    PageHelper.new_sas_program(page)
    editor = CodeEditorPage(page)
    editor.type_code_in_codeeditor("data test;set sashelp.class;run;\n proc print data=sashelp.cars;run;")
    editor.run(True)
    # editor.download_code_file()
    editor.download_submitted_code_file()
    editor.download_log_file_html()
    editor.download_log_file_text()
    editor.download_results_file()
    editor.download_pdf_file()
    editor.download_word_file()
    editor.download_rtf_file()
    editor.download_excel_file()
    editor.download_ppt_file()
    editor.download_listing_file()
    editor.download_generated_data()


# def test_29_tree_common_in_query(page, init):
#     top_menu = TopMenuPage(page)
#     top_menu.new_item(TopMenuItem.new_query)
#     query = QueryPage(page)
#     select_table = SelectTableDialog(page)
#     query.click_add_table()
#     select_table.fill_input_table_name("CLASS")
#     time.sleep(1)
#     select_table.click_button_in_footer("选择")
#     time.sleep(1)
#
#     element_path = ["t1 (CLASS)", "Name"]
#     query.treeview.navigate_to_element_and_dblclick(element_path)
#     time.sleep(1)
#     element_path = ["t1 (CLASS)", "Age"]
#     query.treeview.navigate_to_element_and_click_context_menu(element_path, "添加列")
#     time.sleep(1)
#     element_path = ["t1 (CLASS)", "Weight"]
#     query.treeview.navigate_to_element_and_click_context_menu(element_path, "属性")
#     time.sleep(1)
#     Alert(page).click_button_in_footer("关闭")


def test_30_apply_detail_layout(page, init):
    PageHelper.new_sas_program(page)
    editor = CodeEditorPage(page)
    editor.type_code_in_codeeditor("proc print data=sashelp.class;\n run;")
    editor.run(True)

    editor.apply_detail_layout_standard()
    editor.apply_detail_layout_horizontal()
    editor.apply_detail_layout_vertical()


def test_31_show_or_hide_details_tab(page, init):
    PageHelper.new_sas_program(page)
    editor = CodeEditorPage(page)
    editor.type_code_in_codeeditor("proc print data=sashelp.class;\n run;")
    editor.run(True)

    editor.hide_detail_tabs_code()
    editor.hide_detail_tabs_log()
    editor.hide_detail_tabs_result()
    editor.hide_detail_tabs_output_data()
    editor.hide_detail_tabs_listing()

    editor.show_detail_tabs_code()
    editor.show_detail_tabs_log()
    editor.show_detail_tabs_result()
    editor.show_detail_tabs_output_data()
    editor.show_detail_tabs_listing()


def test_32_close_all_tabs(page, init):
    PageHelper.new_all_items(page)
    # PageHelper.new_item(page,TopMenuItem.new_quick_import)
    PageHelper.close_all_tabs(page)


def test_33_email_refresh(page, init):
    PageHelper.new_sas_program(page)
    editor = CodeEditorPage(page)
    editor.type_code_in_codeeditor("proc print data = sashelp.class;run;")
    editor.reload()
    editor.run(True, True)
    editor.email()


def test_34_sas_program(page, init):
    sas_program: SASProgramPage = PageHelper.new_item(page, TopMenuItem.new_sas_program)
    sas_program.editor.type_into_text_area("proc print data = sashelp.class;run;")
    sas_program.run(True)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    sas_program.saveas(Helper.public_folder_path, "test_sas_program.sas", True, True)
    sas_program.schedule_as_job()
    sas_program.analyze_and_create_flow()
    sas_program.add_to_my_favorites()
    sas_program.open_in_browser_tab_summary()
    sas_program.open_in_browser_tab_results()
    sas_program.open_in_browser_tab_listing()
    sas_program.open_in_browser_tab_log()
    sas_program.open_in_browser_tab_submitted_code()
    sas_program.download_ppt_file()
    sas_program.download_log_file_html()
    sas_program.download_submitted_code_file()
    sas_program.download_results_file()
    sas_program.download_rtf_file()
    sas_program.download_generated_data()
    sas_program.download_listing_file()
    sas_program.download_excel_file()
    sas_program.download_word_file()
    sas_program.download_pdf_file()
    sas_program.email()
    sas_program.apply_detail_layout_standard()
    sas_program.apply_detail_layout_vertical()
    sas_program.apply_detail_layout_horizontal()
    sas_program.hide_detail_tabs_listing()
    sas_program.hide_detail_tabs_submitted_code()
    sas_program.hide_detail_tabs_result()
    sas_program.hide_detail_tabs_log()
    sas_program.hide_detail_tabs_output_data()

    sas_program.show_detail_tabs_log()
    sas_program.show_detail_tabs_code()
    sas_program.show_detail_tabs_result()
    sas_program.show_detail_tabs_listing()
    sas_program.show_detail_tabs_output_data()

    sas_program.reload()

    sas_program.background_submit()

    sas_program.code_to_flow()
    sas_program.add_to_snippets()

    sas_program.clear_log()
    sas_program.clear_listing()
    sas_program.clear_results()
    sas_program.clear_output_data()
    sas_program.clear_code()
    sas_program.clear_all()


def test_35_python(page, init):
    python_program: PythonProgramPage = PageHelper.new_item(page, TopMenuItem.new_python_program)

    # Former Version
    # python_program.editor.type_into_text_area("print('It is python.')")

    # New Version
    python_program.editor.human_mimic_typing("# ASCII number of 'A'")
    python_program.editor.human_mimic_typing("\nascii_number = 65")
    python_program.editor.human_mimic_typing("\nrows = 36")
    python_program.editor.human_mimic_typing("\nfor i in range(0, rows):")
    python_program.editor.human_mimic_typing("\nfor j in range(0, i + 1):")
    python_program.editor.human_mimic_typing("\ncharacter = chr(ascii_number)")
    python_program.editor.human_mimic_typing("\nprint(character, end=' ')")
    python_program.editor.human_mimic_typing("\nascii_number += 1")
    python_program.editor.human_mimic_typing("\nprint(" ")")
    python_program.editor.key_press("Home")
    python_program.editor.key_press("Shift+Tab")

    python_program.click_dialog_title_or_studionext_header()
    python_program.editor.screenshot_self('python_program')

    python_program.run(True)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    python_program.saveas(Helper.public_folder_path, "test_python_program.sas", True, True)
    python_program.schedule_as_job()

    python_program.add_to_my_favorites()
    python_program.open_in_browser_tab_summary()
    python_program.open_in_browser_tab_results()
    python_program.open_in_browser_tab_listing()
    python_program.open_in_browser_tab_log()
    python_program.open_in_browser_tab_submitted_code()
    python_program.download_ppt_file()
    python_program.download_log_file_html()
    python_program.download_submitted_code_file()
    python_program.download_results_file()
    python_program.download_rtf_file()
    python_program.download_generated_data()
    python_program.download_listing_file()
    python_program.download_excel_file()
    python_program.download_word_file()
    python_program.download_pdf_file()
    python_program.email()
    python_program.apply_detail_layout_standard()
    python_program.apply_detail_layout_vertical()
    python_program.apply_detail_layout_horizontal()
    python_program.hide_detail_tabs_listing()
    python_program.hide_detail_tabs_code()
    python_program.hide_detail_tabs_result()
    python_program.hide_detail_tabs_log()
    python_program.hide_detail_tabs_output_data()

    python_program.show_detail_tabs_log()
    python_program.show_detail_tabs_code()
    python_program.show_detail_tabs_result()
    python_program.show_detail_tabs_listing()
    python_program.show_detail_tabs_output_data()

    python_program.reload()

    python_program.background_submit()

    # Removed on Jan 24, 2025
    # Confluence Page Record:
    #  Diff #22: Removal of 'Code to Flow' button from the toolbar within python program page.

    # python_program.code_to_flow()
    python_program.add_to_snippets()

    python_program.clear_log()
    python_program.clear_listing()
    python_program.clear_results()
    python_program.clear_output_data()
    python_program.clear_code()
    python_program.clear_all()


def test_36_flow(page, init):
    flow: FlowPage = PageHelper.new_item(page, TopMenuItem.new_flow)
    flow.add_node(FlowNodeType.table)
    flow.add_node(FlowNodeType.file)
    # flow.add_node(FlowNodeType.branch_rows)
    flow.add_node(FlowNodeType.calculate_columns)
    flow.add_node(FlowNodeType.sas_program)
    # flow.add_node(FlowNodeType.execute_decisions)
    flow.add_node(FlowNodeType.export)
    flow.add_node(FlowNodeType.filter_rows)
    flow.add_node(FlowNodeType.implement_scd)
    flow.add_node(FlowNodeType.import_data)
    flow.add_node(FlowNodeType.insert_rows)
    flow.add_node(FlowNodeType.load_table)
    flow.add_node(FlowNodeType.manage_columns)
    flow.add_node(FlowNodeType.merge_table)
    flow.add_node(FlowNodeType.python_program)
    flow.add_node(FlowNodeType.query)
    flow.add_node(FlowNodeType.sort)
    # flow.add_node(FlowNodeType.union_rows)
    flow.add_node(FlowNodeType.notes)
    flow.add_node(FlowNodeType.union_rows)
    # flow.run(False)
    # PageHelper.close_alert_if_needed(page)
    # flow.run_single_node()
    # flow.run_nodes_downstream()
    flow.run_nodes_upstream()
    # flow.background_submit()
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    flow.saveas(Helper.public_folder_path, "test_flow.sas", True, True)

    flow.copy_step()
    flow.paste_step()
    flow.cut_step()

    flow.undo()
    flow.redo()

    flow.view_expand_all_ports()
    flow.view_collapse_all_ports()
    flow.arrange_nodes()
    flow.show_over_view_map()
    flow.hide_over_view_map()
    flow.schedule_as_job()
    flow.add_to_my_favorites()
    # since flow does not implement below methods, so comment these now.
    # flow.open_in_browser_tab_log()
    # flow.open_in_browser_tab_results()
    # flow.open_in_browser_tab_code()
    # flow.open_in_browser_tab_summary()
    # flow.open_in_browser_tab_listing()
    # flow.download_listing_file()
    # flow.download_code_file()
    # flow.download_pdf_file()
    # flow.download_rtf_file()
    # flow.download_ppt_file()
    # flow.download_word_file()
    # flow.download_excel_file()
    # flow.download_generated_data()
    # flow.download_results_file()
    # flow.download_log_file_html()
    # flow.download_log_file_text()
    flow.email()

    # Fow overflow menu changed
    # flow.apply_detail_layout_horizontal()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_horizontal()

    # Fow overflow menu changed
    # flow.apply_detail_layout_vertical()

    # New overflow menu: Apply flow layout
    flow.apply_flow_layout_vertical()

    flow.apply_main_layout_vertical()
    flow.apply_main_layout_standard()
    flow.apply_main_layout_horizontal()
    flow.reload()


# def test_37_query(page, init):
#     query: QueryPage = PageHelper.new_item(page, TopMenuItem.new_query)
#     select_table = SelectTableDialog(page)
#     query.click_add_table()
#     select_table.fill_input_table_name("CLASS")
#     time.sleep(1)
#     select_table.click_button_in_footer("选择")
#     time.sleep(1)
#
#     element_path = ["t1 (CLASS)", "Name"]
#     query.treeview.navigate_to_element_and_dblclick(element_path)
#     time.sleep(0.3)
#     element_path = ["t1 (CLASS)", "Age"]
#     query.treeview.navigate_to_element_and_click_context_menu(element_path, "添加列")
#     time.sleep(0.3)
#
#     query.run(True)
#     query.background_submit(False)
#     folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
#     # query.saveas(folder_path, "test_query.sas", True, True)
#     query.add_to_snippets()
#     query.schedule_as_job()
#     query.add_to_my_favorites()
#     query.open_in_browser_tab_results()
#     query.open_in_browser_tab_listing()
#     query.open_in_browser_tab_code()
#     query.open_in_browser_tab_summary()
#     query.open_in_browser_tab_log()
#     query.download_log_file_text()
#     query.download_excel_file()
#     query.download_log_file_html()
#     query.download_ppt_file()
#     query.download_word_file()
#     query.download_results_file()
#     query.download_generated_data()
#     query.download_rtf_file()
#     query.download_pdf_file()
#     query.download_code_file()
#     query.download_listing_file()
#
#     query.email()
#     # query.apply_main_layout_horizontal()
#     # query.apply_main_layout_vertical()
#     query.apply_detail_layout_horizontal()
#     query.apply_detail_layout_vertical()
#     query.apply_detail_layout_standard()
#     query.hide_detail_tabs_log()
#     query.hide_detail_tabs_code()
#     query.hide_detail_tabs_result()
#     query.hide_detail_tabs_listing()
#     query.hide_detail_tabs_output_data()
#
#     query.show_detail_tabs_log()
#     query.show_detail_tabs_code()
#     query.show_detail_tabs_result()
#     query.show_detail_tabs_listing()
#     query.show_detail_tabs_output_data()


def test_38_quick_import(page, init):
    quick_import: QuickImportPage = PageHelper.new_item(page, TopMenuItem.new_quick_import)
    quick_import.run(True)

    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]

    # Naming rule changed
    quick_import.saveas(Helper.public_folder_path, "test_import_sas", True, True)

    # Dec.26th 2024 'Add to Snippets' N/A
    # quick_import.add_to_snippets()

    quick_import.schedule_as_job()
    quick_import.add_to_my_favorites()
    quick_import.open_in_browser_tab_results()
    quick_import.open_in_browser_tab_listing()
    quick_import.open_in_browser_tab_submitted_code()
    quick_import.open_in_browser_tab_summary()
    quick_import.open_in_browser_tab_log()
    quick_import.download_submitted_code_file()
    quick_import.download_pdf_file()
    quick_import.download_rtf_file()
    quick_import.download_listing_file()
    quick_import.download_ppt_file()
    quick_import.download_generated_data()
    quick_import.download_results_file()
    quick_import.download_word_file()
    quick_import.download_log_file_html()
    quick_import.download_excel_file()
    quick_import.download_log_file_text()
    # quick_import.email()
    # quick_import.apply_main_layout_vertical()
    # quick_import.apply_main_layout_horizontal()
    quick_import.apply_detail_layout_standard()
    quick_import.apply_detail_layout_vertical()
    quick_import.apply_detail_layout_horizontal()
    quick_import.hide_detail_tabs_log()
    quick_import.hide_detail_tabs_listing()
    quick_import.hide_detail_tabs_submitted_code()
    quick_import.hide_detail_tabs_result()
    quick_import.hide_detail_tabs_output_data()
    quick_import.show_detail_tabs_log()
    quick_import.show_detail_tabs_listing()
    quick_import.show_detail_tabs_submitted_code()
    quick_import.show_detail_tabs_result()
    quick_import.show_detail_tabs_output_data()


def test_39_JsonPage(page, init):
    json: JsonPage = PageHelper.new_item(page, TopMenuItem.new_file_types_json)
    # json.editor.type_into_text_area('{\n"type":"json file",\n"name":"json example"\n}')

    # json.editor.type_into_text_area('{"\ntype":"json file",\n"name":"json example"')
    # json.editor.type_into_text_area('{\n"type":"json file",\n"name":"json example"')

    # json.editor.type_into_text_area('{')

    json.editor.type_into_text_area('''{"type":"json file","name":"json example"}''')

    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    json.saveas(Helper.public_folder_path, "test_json.json", True, True)
    time.sleep(1)
    json.undo()
    json.redo()
    json.add_to_snippets()
    json.add_to_my_favorites()
    json.open_in_browser_tab()
    json.email()
    json.reload()


def test_40_TextPage(page, init):
    text: TextPage = PageHelper.new_item(page, TopMenuItem.new_file_types_text)
    text.editor.type_into_text_area('This is text file.')
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    text.saveas(Helper.public_folder_path, "test_text.txt", True, True)
    time.sleep(1)
    text.undo()
    text.redo()
    text.add_to_snippets()
    text.add_to_my_favorites()
    text.open_in_browser_tab()
    text.email()
    text.reload()


def test_41_XMLPage(page, init):
    xml: XMLPage = PageHelper.new_item(page, TopMenuItem.new_file_types_xml)
    xml.editor.type_into_text_area('<?xml version="1.0" encoding="UTF-8"?>')
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    xml.saveas(Helper.public_folder_path, "test_xml.xml", True, True)
    time.sleep(1)
    xml.undo()
    xml.redo()
    xml.add_to_snippets()
    xml.add_to_my_favorites()
    xml.open_in_browser_tab()
    xml.email()
    xml.reload()


def test_42_WorkSapcePage(page, init):
    work_space: WorkspacePage = PageHelper.new_item(page, TopMenuItem.new_file_types_workspace)
    work_space.editor.type_into_text_area('This is work space file.')
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    # folder_path = ["SAS Content", "Public"]
    work_space.saveas(Helper.public_folder_path, "test_workspace.workspace", True, True)
    time.sleep(2)
    work_space.undo()
    work_space.redo()
    # work_space.add_to_snippets()
    work_space.add_to_my_favorites()
    work_space.open_in_browser_tab()
    work_space.email()
    work_space.reload()


def test_43_check_uncheck_menu_items_in_view(page, init):
    time.sleep(2)
    center_page: CenterPage = PageHelper.check_menu_item_in_view(page, TopMenuItem.view_deployed_and_scheduled_jobs)
    time.sleep(3)

    # MODIFIED
    # <<< Modified by Jacky(ID: jawang) on Apr.29th, 2024
    # Comment out Original Version
    # center_page.screenshot_self('deployed_and_scheduled')
    # Modified by Jacky(ID: jawang) on Apr.29th, 2024 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Apr.29th, 2024
    """
    # Comment out for lack of masks
    center_page.screenshot_self('deployed_and_scheduled',
                                mask=[center_page.get_by_test_id("scheduledJobsPane-lastRefreshLabel"),],
                                mask_color="#000000")
    """
    # END Added by Jacky(ID: jawang) on Apr.29th, 2024 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on May.27th, 2024
    # data-testid="scheduledJobsPane-monitoringTab-agGrid"
    center_page.screenshot_self('deployed_and_scheduled',
                                mask=['//div[@class="ag-center-cols-viewport"]',
                                      '//button[@data-testid="scheduledJobsPane-monitoringTab-refreshButton"]',
                                      center_page.get_by_test_id("scheduledJobsPane-monitoringTab-lastRefreshLabel")],
                                mask_color="#000000")
    # END Added by Jacky(ID: jawang) on May.27th, 2024 >>>

    time.sleep(1)
    center_page = PageHelper.check_menu_item_in_view(page, TopMenuItem.view_submission_status)
    time.sleep(2)

    # MODIFIED
    # <<< Modified by Jacky(ID: jawang) on Apr.29th, 2024
    # Comment out Original Version
    # center_page.screenshot_self('submission_status')
    # Modified by Jacky(ID: jawang) on Apr.29th, 2024 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on May.27th, 2024
    center_page.screenshot_self('submission_status',
                                mask=['//div[@class="ag-center-cols-viewport"]',
                                      center_page.get_by_test_id("scheduledJobsPane-monitoringTab-lastRefreshLabel")],
                                mask_color="#000000")
    # END Added by Jacky(ID: jawang) on May.27th, 2024 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Apr.29th, 2024
    # center_page.screenshot_self('subm_stat_clip',
    #                             clip={'x': 0, 'y': 0, 'width': 433, 'height': 1050})
    #

    # center_page.screenshot(center_page.base_xpath,
    #                        'subm_stat_clip',
    #                        clip={'x': 0, 'y': 0, 'width': 433, 'height': 1050})

    # center_page.screenshot(center_page.page,
    #                        'subm_stat_clip',
    #                        clip={'x': 0, 'y': 0, 'width': 433, 'height': 1050})

    center_page.screenshot_self('subm_stat_clip', clip={'x': 0, 'y': 0, 'width': 433, 'height': 1050})

    # END Added by Jacky(ID: jawang) on Apr.29th, 2024 >>>

    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_start_page)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_deployed_and_scheduled_jobs)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_submission_status)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_start_page)

    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_open_items)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_sas_server)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_sas_content)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_steps)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_snippets)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_library_connections)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_git_repositories)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_file_references)
    PageHelper.uncheck_menu_item_in_view(page, TopMenuItem.view_navigation_panes_clinical_repositories)

    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_open_items)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_sas_server)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_sas_content)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_steps)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_snippets)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_library_connections)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_git_repositories)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_file_references)
    PageHelper.check_menu_item_in_view(page, TopMenuItem.view_navigation_panes_clinical_repositories)

    PageHelper.show_accordion(page, AccordionType.open_item)


def test_44_deployed_and_scheduled_job(page, init):
    time.sleep(2)
    deployed_page: DeployedScheduledJobPage = PageHelper.check_menu_item_in_view(page,
                                                                                 TopMenuItem.view_deployed_and_scheduled_jobs)

    """
    # Comment out temporarily because of the UI change
    
    time.sleep(3)
    deployed_page.run_now()
    time.sleep(1)
    deployed_page.edit_schedule()
    deployed_page.remove_schedule()
    deployed_page.refresh_list()
    deployed_page.column_setting()
    """


def test_45_startup_initialization_log(page, init):
    startup_page = PageHelper.show_view_startup_initialization_log(page)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]

    # NOTE: Saving initialization file does not work at the moment
    # startup_page.saveas(Helper.public_folder_path, "startup_initialization_log.log", True, True)
    # startup_page.add_to_snippets()
    startup_page.add_to_my_favorites()

    # Used the one with screenshot function
    startup_page.open_in_browser_tab2(page)

    # Replace with src.Pages.StudioNext.Center.startup_initialization_log_page.StartupInitializationLogPage.prt_scn
    startup_page.prt_scn("open_in_browser_tab_page_masked")

    # startup_page.email()
    startup_page.reload()


def test_46_job_definition(page, init):
    job_page: JobDefinitionPage = PageHelper.new_item(page, TopMenuItem.new_job_definition)
    # folder_path = [Helper.data_locale.SAS_CONTENT, "Public"]
    job_page.saveas(Helper.public_folder_path, "JobDefinition", True, True)

    #

    '''
    # April 22nd 2024: 
    # Since 'Job Definition' is changed to what is like in Custom Step and the editor textarea is removed,
    # the following operations are commented out.
    
    job_page.editor.type_into_text_area("This is job definition.")
    time.sleep(1)
    job_page.undo()
    job_page.redo()
    job_page.add_to_snippets()
    '''

    job_page.schedule_as_job()
    job_page.open_in_browser_tab_code()
    job_page.open_in_browser_tab_job_form()
    job_page.apply_main_layout_standard()
    job_page.apply_main_layout_horizontal()
    job_page.apply_main_layout_vertical()
    job_page.reload()


def test_47_run_big_program(page, init):
    """
    Mimic long-time execution
    """
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    # editor.editor.human_mimic_typing(
    editor.editor.type_into_text_area(
        """%macro blink_lights(num_blinks=5);
%do i=1 %to &num_blinks;

data _null_;
length line1-line7 $50;
array lights[7] $50 _temporary_ (' ', ' ', ' ', ' ', ' ', ' ', ' ');
array patterns[3] $1 _temporary_ ('o', '*', '+');
call streaminit(&i);

do j=1 to 7;

if rand("Bernoulli", 0.1 + (0.1 * (8 - j))) then 
lights[j]=patterns[ceil(rand('uniform') * 3)];
else lights[j]=' ';
end;
line0='|-----------------|';
line1='|        *        |';
line2='|       ***       |';
line3='|      *****      |';
line4='|     *******     |';
line5='|    *********    |';
line6='|   ***********   |';
line7='|  *************  |';
put line0;
put line1;
put line2;
put line3;
put line4;
put line5;
put line6;
put line7;
put '      |||||';

do j=1 to 7;

if lights[j] ne ' ' then put '        ' lights[j];
else put '       ***';
end;
run;

data _null_;
call sleep(100);
run;

%end;
%mend blink_lights;

%blink_lights(num_blinks=300);
""")
    editor.click_dialog_title_or_studionext_header()
    editor.format_program()
    editor.run(True)
    time.sleep(2)
    editor.prt_scn('long_time_execution')


def test_48_run_big_program(page, init):
    """
    Original
    """
    PageHelper.new_sas_program(page)
    editor = SASProgramPage(page)
    editor.editor.type_into_text_area("data null; call sleep(5,1);run;")
    editor.run(True)
    time.sleep(2)
