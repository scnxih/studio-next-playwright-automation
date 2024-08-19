from src.Pages.StudioNext.Center.Flow.DetailsPane.Develop.sasprogram_pane import SASProgramPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.TransformData.sort_pane import SortPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.DataInputAndOutput.table_pane import *
from src.Pages.StudioNext.Center.CustomStep.custom_step_page import *
from src.Helper.page_helper import *

def insert_section(page: Page, section_number: int, label: str):
    custom_step: CustomStepPage = CustomStepPage(page)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.defocus_designer_control()
    time.sleep(0.3)
    custom_step.insert_control(DesignerControlType.section)
    time.sleep(0.5)
    custom_step.select_control(DesignerControlType.section, section_number)
    properties.set_label(label)

def insert_text(page: Page, text_number: int, text: str):
    custom_step: CustomStepPage = CustomStepPage(page)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    #properties.set_indent("1")
    properties.set_enter_text(text)

def test_01_flow_en_US(page, init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)
    time.sleep(1.5)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)
    # time.sleep(1)
    sasprogram_pane = SASProgramPane(page)
    str = """
/***************************************************
This is demo for flow.
First, create data set class in work library in sas program step.
Then user will sort this table work.class by name descending.
Next sorted table will be generated.
***************************************************/

data cars;
set sashelp.cars;
run;
"""
    time.sleep(2)
    sasprogram_pane.type_into_text_area(str)
    WholePage(page).screenshot_self(pic_name="01_before_fold")
    # time.sleep(1)
    sasprogram_pane.fold_all_regions()
    time.sleep(1)
    WholePage(page).screenshot_self(pic_name="02_after_fold")
    sasprogram_pane.unfold_all_regions()
    time.sleep(1)
    WholePage(page).screenshot_self(pic_name="03_after_unfold")
    sasprogram_pane.pop_find_widget()
    sasprogram_pane.find("cars", False, False)
    time.sleep(1)
    WholePage(page).screenshot_self(pic_name="04_after_find")
    sasprogram_pane.replace_all("cars", "class", False, False, False)
    time.sleep(2)
    WholePage(page).screenshot_self(pic_name="05_after_replace")
    sasprogram_pane.set_node_name("Create class")
    # time.sleep(1)
    sasprogram_pane.set_notes("This is SAS program notes for expo.")
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    # time.sleep(1)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    # time.sleep(1)
    table_pane.set_table("CLASS")
    # time.sleep(1)
    table_pane.set_node_name("CLASS")
    # time.sleep(1)
    table_pane.set_node_description("This is class table created by SAS program.")
    # time.sleep(1)
    flow.link_two_nodes_in_flow("Create class", "CLASS")
    # time.sleep(1)
    flow.arrange_nodes()
    WholePage(page).screenshot_self(pic_name="06_after_link_two_nodes")
    flow.run(True)
    flow.select_node_in_flow_canvas("CLASS")
    # table_pane.click_Tab("预览数据")
    table_pane.click_Tab("Preview Data")
    time.sleep(3)
    WholePage(page).screenshot_self(pic_name="07_preview_before_sorted")
    flow.add_node(FlowNodeType.sort)
    # time.sleep(1)
    flow.arrange_nodes()
    # flow.link_two_nodes_in_flow("CLASS","排序")
    flow.link_two_nodes_in_flow("CLASS", "Sort")
    # time.sleep(1)
    flow.arrange_nodes()
    # flow.select_node_in_flow_canvas("排序")
    flow.select_node_in_flow_canvas("Sort")

    sort_pane = SortPane(page)

    list1 = ["Class", "Name"]
    sort_pane.add_sort(list1, SortWay.descending)
    # time.sleep(1)
    WholePage(page).screenshot_self(pic_name="08_add_sort")
    flow.add_node(FlowNodeType.table)
    # flow.select_node_in_flow_canvas("表")
    flow.select_node_in_flow_canvas("Table")

    table_pane.set_node_name("SORTED")
    table_pane.set_library("WORK")
    table_pane.set_table("SORTED")
    table_pane.refresh_table()
    # flow.link_two_nodes_in_flow("排序","SORTED")
    flow.link_two_nodes_in_flow("Sort", "SORTED")
    # time.sleep(1)
    flow.arrange_nodes()
    # time.sleep(1)
    flow.run(False)
    time.sleep(3)
    flow.select_node_in_flow_canvas("SORTED")
    time.sleep(1)
    # table_pane.click_Tab("预览数据")
    table_pane.click_Tab("Preview Data")
    time.sleep(2)
    WholePage(page).screenshot_self(pic_name="09_preview_sorted_table")
    # Helper.call_SDSTest()

def test_02_custom_step_en_US(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    time.sleep(1.5)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.check_show_single_page_as_tab()
    properties.set_label("Data")
    section_number = 1
    text_number = 1


    insert_section(page, section_number, "Input data control")
    section_number += 1
    insert_text(page, text_number, "Use the input table control to select a source table. An input table is required for this example.")
    text_number += 1

    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.select_control(DesignerControlType.input_table, 1)
    #properties.set_indent("1")
    properties.set_label("Select the source table:")
    properties.set_default_library("SASHELP")
    properties.set_default_table("CLASS")

    insert_section(page, section_number, "Column selector controls")
    section_number += 1
    insert_text(page, text_number,
                "Use the column selector control to add columns from a linked input table. You can control how many columns can be added, the type of columns, and if columns can be reordered or not.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.column_selector)
    custom_step.select_control(DesignerControlType.column_selector, 1)
    #properties.set_indent("1")
    properties.set_label("Select a single column:")
    properties.select_link_input_table("Input table label 1  (inputtable1)")
    properties.select_column_type("Character")
    properties.set_max_columns("1")

    # custom_step.insert_control(DesignerControlType.column_selector)
    # custom_step.select_control(DesignerControlType.column_selector, 2)
    # #properties.set_indent("1")
    # properties.set_label("选择多个列:")
    # properties.select_link_input_table("输入表标签 1  (inputtable1)")
    # properties.set_min_columns("1")
    # properties.set_max_columns("3")
    # properties.set_check_allow_order_column()

    insert_section(page, section_number, "New column control")
    section_number += 1
    insert_text(page, text_number,
                "Use a new column control to add a column to an output table. You can define the default column properties and specify whether these properties can be edited by the user of the custom step. If the properties can be edited, the user clicks the Edit icon to open the Column Properties window and edit any properties.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.select_control(DesignerControlType.new_column, 1)
    #properties.set_indent("1")
    properties.set_label("Add a new column:")
    properties.set_default_column_name("Grade")
    properties.set_default_column_label("Grade")
    properties.select_default_type("Numeric")
    properties.set_default_length("8")
    properties.set_default_format("Best12.")
    properties.set_default_informat("Best12.")

    custom_step.add_page_by_toolbar()
    properties.set_label("Controls 1")
    insert_section(page, section_number, "Check box control")
    section_number += 1
    insert_text(page, text_number, "Use a check box to choose between two opposite states, actions, or values.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 1)
    properties.set_label("Check box")
    #properties.set_indent("1")
    properties.set_check_by_default()

    insert_section(page, section_number, "Color picker control")
    section_number += 1
    insert_text(page, text_number, "Use a color picker control to choose a color.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.select_control(DesignerControlType.color_picker, 1)
    #properties.set_indent("1")
    properties.click_select_color()
    properties.set_RGB(160, 95, 238)

    # insert_section(page,6,"日期和时间控件")
    # insert_text(page,6, "使用日期和时间控件选择日期和时间。")

    insert_section(page, section_number, "File or folder selector control")
    section_number += 1
    insert_text(page, text_number, """Use a file or folder selector control to specify a path for a file or a folder. The path must be in a URL format. As part of the path, you must specify whether the file or folder is in SAS Content or on the SAS server.

Examples:
sascontent:/path/to/fileorfolder
sasserver:/path/to/fileorfolder""")
    text_number += 1
    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.select_control(DesignerControlType.file_or_folder_selector, 1)
    #properties.set_indent("1")
    properties.set_label("File selector:")
    properties.select_selector_type(FileOrFolder.file)

    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.select_control(DesignerControlType.file_or_folder_selector, 2)
    #properties.set_indent("1")
    properties.set_label("Folder selector:")
    properties.select_selector_type(FileOrFolder.folder)
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("Controls 2")
    insert_section(page, section_number, "Link control")
    section_number += 1
    insert_text(page, text_number,
                "Use a link control to support hyperlinks in custom steps.  For security, links are disabled by default.  Administrators use SAS Environment Manager to enable this functionality and specify the validation rules for links.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.link)
    custom_step.select_control(DesignerControlType.link, 1)
    #properties.set_indent("1")
    properties.set_label("SAS Website：")
    properties.set_link("https://www.sas.com")
    time.sleep(1)

    insert_section(page, section_number, "Text control")
    section_number += 1
    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    text_number += 1
    #properties.set_indent("1")
    properties.set_enter_text("Use the text control to provide static explanatory text.")

    insert_section(page, section_number, "Text area control")
    section_number += 1
    insert_text(page, text_number, "Use a text area control to enter or edit one or more lines of text.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.select_control(DesignerControlType.textarea, 1)
    #properties.set_indent("1")
    properties.set_placeholder_text_for_textarea("Type one or more lines here.")
    time.sleep(2)

    insert_section(page, section_number, "Text field controls")
    section_number += 1

    insert_text(page, text_number, "An example of a basic input text field.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field, 1)
    #properties.set_indent("1")
    properties.set_label("Validation:")
    properties.select_type_for_text_or_numeric_field(TextNumericValidation.validation)
    properties.set_regular_expression("\w{5}")
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("Controls 3")
    insert_section(page, section_number, "Date and time control")
    section_number += 1
    insert_text(page, text_number, "Use a date and time control to choose a date and time.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 1)
    #properties.set_indent("1")
    properties.set_label("Date and time:")
    properties.select_date_time_type(DateTimeType.date_and_time)
    properties.click_default_value(DateTimeType.date_and_time)
    date_time_dialog: DateTimeDialog = get_dialog_page(page, DialogType.date_time_dialog)
    date_time_dialog.set_year("2025")
    for i in range(5):
        date_time_dialog.click_next_month()
    date_time_dialog.select_hour("03")
    date_time_dialog.select_minute("10")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 2)
    #properties.set_indent("1")
    properties.set_label("Month:")
    properties.select_date_time_type(DateTimeType.month)
    properties.click_default_value(DateTimeType.month)
    year_month_dialog: YearMonthDialog = get_dialog_page(page, DialogType.year_month_dialog)
    year_month_dialog.set_year("2010")
    year_month_dialog.select_month(Month.october)
    year_month_dialog.click_button_in_footer(Helper.data_locale.OK)

    # custom_step.insert_control(DesignerControlType.date_and_time_picker)
    # custom_step.select_control(DesignerControlType.date_and_time_picker, 3)
    # #properties.set_indent("1")
    # properties.set_label("时间:")
    # properties.select_date_time_type(DateTimeType.time)
    # properties.click_default_value(DateTimeType.time)
    # date_time_dialog.select_hour("03")
    # date_time_dialog.select_minute("08")
    # date_time_dialog.select_second("00")
    # date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    insert_section(page, section_number, "Drop-down list control")
    section_number += 1
    insert_text(page, text_number,
                "Use a drop-down list control when you want to display a menu containing a list of choices. The list of choices can either be a static list of items or a dynamic list of items.")
    text_number += 1
    insert_text(page, text_number,
                "Use a static drop-down list to populate the list with a set of predefined values.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list, 1)
    #properties.set_indent("1")
    properties.set_label("Static drop-down list:")
    properties.add_many_items("Judy\nWilliam\nHenry")
    properties.select_default_item("Henry")

    insert_text(page, text_number,
                "Use a dynamic drop-down list to populate the items in the list with distinct values from a linked column selector. For example, the following drop-down list is populated with distinct values from the column selected in the first column selector on the Data page.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list, 2)
    #properties.set_indent("1")
    properties.set_label("Dynamic drop-down list:")
    properties.set_check_dynamic_list()
    properties.select_reference_column_selector("Column selector label 1  (columnselector1)")
    properties.set_default_item("Carol")
    time.sleep(2)

    custom_step.add_page_by_toolbar()
    properties.set_label("Controls 4")
    insert_section(page, section_number, "List control")
    section_number += 1
    insert_text(page, text_number,
                "Use a list control when you want to allow the selection of multiple choices from a list of items. The list of choices can either be a static list of items or a dynamic list of items.")
    text_number += 1
    insert_text(page, text_number,
                "Use a static list to populate the list with a set of predefined values.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.list)
    custom_step.select_control(DesignerControlType.list, 1)
    #properties.set_indent("1")
    properties.add_many_items("Primary school\nJunior high school\nSenior high school")
    properties.set_minimum_number_of_values("1")
    properties.set_maximum_number_of_values("4")
    insert_text(page, text_number,
                "Use a dynamic list to populate the items in the list with distinct values from a linked column selector. For example, the following list is populated with distinct values from the column selected in the first column selector on the Data page.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.list)
    custom_step.select_control(DesignerControlType.list, 2)
    #properties.set_indent("1")
    properties.set_check_dynamic_list()
    properties.select_reference_column_selector("Column selector label 1  (columnselector1)")
    properties.set_minimum_number_of_values("1")
    properties.set_maximum_number_of_values("5")

    custom_step.add_page_by_toolbar()
    properties.set_label("Controls 5")
    insert_section(page, section_number, "Numeric field controls")
    section_number += 1
    insert_text(page, text_number,
                "Use a number field to input a numeric value. The minimum value is 0, and the maximum value is 100. When the field is empty, placeholder text provides instructions to the user.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field, 2)
    #properties.set_indent("1")
    properties.set_label("Numeric field:")
    properties.select_type_for_text_or_numeric_field(TextNumericValidation.numeric)
    properties.set_check_allow_integer_values_only()
    properties.set_default_value("5")
    properties.set_minimum_value("0")
    properties.set_maximum_value("100")
    properties.set_placeholder_text("Enter a number between 0 and 100.")
    properties.set_check_exclude_minimum_in_range()
    properties.set_check_exclude_maximum_in_range()

    insert_text(page, text_number,
                "Use a numeric stepper to move through numbers at a specified increment by using the up and down arrows. The default value is 10. The minimum value is 0, and the maximum value is 20.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.numeric_stepper)
    custom_step.select_control(DesignerControlType.numeric_stepper, 1)
    #properties.set_indent("1")
    properties.set_label("Numeric stepper:")
    properties.set_check_allow_integer_values_only()
    properties.set_default_value("10")
    properties.set_minimum_value("0")
    properties.set_maximum_value("20")
    properties.set_step_size("2")

    insert_section(page, section_number, "Radio button group control")
    section_number += 1
    insert_text(page, text_number, "Use a radio button group control to display a list of mutually exclusive choices as radio buttons.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.radio_group)
    custom_step.select_control(DesignerControlType.radio_group, 1)
    #properties.set_indent("1")
    properties.set_label("Radio button group:")
    properties.add_many_items("Radio button 2")
    properties.select_default_radio_button("Radio button 2")
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("Dependencies")

    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    properties.set_enter_text("Dependencies enable you to show or hide prompts based on the values of another prompt.")
    text_number += 1

    insert_section(page, section_number, "Check box example")
    section_number += 1
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 2)
    #properties.set_indent("1")
    properties.set_label("Check the box to show a text field")
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field, 3)
    #properties.set_indent("1")
    properties.set_label("Text field:")
    properties.set_placeholder_text("Shown when the check box is checked")
    properties.set_visibility("\"$checkbox2\"")
    time.sleep(1)

    insert_section(page, section_number, "Drop-down list example")
    section_number += 1
    insert_text(page, text_number, "The category selected from the drop-down list determines the check boxes that appear.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list, 3)
    #properties.set_indent("1")
    properties.set_label("Select a fruit category:")
    properties.add_many_items("Berries\nMelons")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 3)
    #properties.set_indent("1")
    properties.set_label("Strawberries")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"Berries\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 4)
    #properties.set_indent("1")
    properties.set_label("Blueberries")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"Berries\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 5)
    #properties.set_indent("1")
    properties.set_label("Watermelon")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"Melons\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 6)
    #properties.set_indent("1")
    properties.set_label("Hami melon")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"Melons\"]")

    custom_step.add_page_by_toolbar()
    properties.set_label("Output")
    insert_section(page, section_number, "Output data control")
    section_number += 1
    insert_text(page, text_number, "Use the output table control to specify an output table. In flows, output table controls are represented as output ports.")
    text_number += 1
    custom_step.insert_control(DesignerControlType.output_table)
    custom_step.select_control(DesignerControlType.output_table, 1)
    #properties.set_indent("1")
    properties.set_label("Output data control:")
    properties.set_check_required()
    properties.set_placeholder_text("Select output data:")
    time.sleep(1)

def test_03_flow_zh_CN(page,init):
    flow: FlowPage = PageHelper.new_flow(page)
    flow.add_node(FlowNodeType.sas_program)

    # flow.add_node(FlowNodeType.sort)
    # flow.apply_detail_layout_vertical()
    time.sleep(1)
    flow.select_node_in_flow_canvas(Helper.data_locale.SAS_PROGRAM_Upper_case)
    # time.sleep(1)
    sasprogram_pane = SASProgramPane(page)
    str = """
/***************************************************
This is demo for flow.
First, create data set class in work library in sas program step.
Then user will sort this table work.class by age descending.
Next sorted table will be generated.
***************************************************/
data cars;
set sashelp.cars;
run;"""
    sasprogram_pane.type_into_text_area(str)
    # time.sleep(1)
    sasprogram_pane.fold_all_regions()
    time.sleep(1)
    sasprogram_pane.unfold_all_regions()
    time.sleep(1)
    sasprogram_pane.pop_find_widget()
    sasprogram_pane.find("cars", False, False)
    time.sleep(1)
    sasprogram_pane.replace_all("cars", "class", False, False, False)
    time.sleep(2)
    sasprogram_pane.set_node_name("Create class")
    # time.sleep(1)
    sasprogram_pane.set_notes("This is SAS program notes for expo.")
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    flow.arrange_nodes()

    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)
    # time.sleep(1)
    table_pane = TablePane(page)
    table_pane.set_library("WORK")
    # time.sleep(1)
    table_pane.set_table("CLASS")
    # time.sleep(1)
    table_pane.set_node_name("CLASS")
    # time.sleep(1)
    table_pane.set_node_description("This is class table created by SAS program.")
    # time.sleep(1)
    flow.link_two_nodes_in_flow("Create class", "CLASS")
    # time.sleep(1)
    flow.arrange_nodes()

    flow.run(True)
    flow.select_node_in_flow_canvas("CLASS")
    # table_pane.click_Tab("预览数据")
    table_pane.click_Tab(Helper.data_locale.PREVIEW_DATA)
    time.sleep(3)
    flow.add_node(FlowNodeType.sort)
    # time.sleep(1)
    flow.arrange_nodes()
    # flow.link_two_nodes_in_flow("CLASS","排序")
    flow.link_two_nodes_in_flow("CLASS", Helper.data_locale.SORT)
    # time.sleep(1)
    flow.arrange_nodes()
    # flow.select_node_in_flow_canvas("排序")
    flow.select_node_in_flow_canvas(Helper.data_locale.SORT)

    sort_pane = SortPane(page)

    list1 = ["Class", "Name"]
    sort_pane.add_sort(list1, SortWay.descending)
    # time.sleep(1)

    flow.add_node(FlowNodeType.table)
    # flow.select_node_in_flow_canvas("表")
    flow.select_node_in_flow_canvas(Helper.data_locale.TABLE)

    table_pane.set_node_name("SORTED")
    table_pane.set_library("WORK")
    table_pane.set_table("SORTED")
    table_pane.refresh_table()
    # flow.link_two_nodes_in_flow("排序","SORTED")
    flow.link_two_nodes_in_flow(Helper.data_locale.SORT, "SORTED")
    # time.sleep(1)
    flow.arrange_nodes()
    # time.sleep(1)
    flow.run(False)
    time.sleep(3)
    flow.select_node_in_flow_canvas("SORTED")
    time.sleep(2)
    # table_pane.click_Tab("预览数据")
    table_pane.click_Tab(Helper.data_locale.PREVIEW_DATA)
    time.sleep(2)
    WholePage(page).screenshot_self("test")

    # Dialog(page).screenshot_self()
    # PageHelper.show_accordion(page,AccordionType.libraries)
    # lib = LibraryPage(page)
    # lib.open_table("WORK","SORTED")
    # time.sleep(2)
def test_04_custom_step_zh_CN(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
    time.sleep(1.5)
    properties: CustomStepPropertiesPage = CustomStepPropertiesPage(page)
    custom_step.check_show_single_page_as_tab()
    properties.set_label("数据")
    section_number = 1
    text_number = 1

    insert_section(page, section_number, "输入数据控件")
    section_number += 1
    insert_text(page, text_number, "使用输入表控件选择源表。该示例需要输入表。")
    text_number += 1

    custom_step.insert_control(DesignerControlType.input_table)
    custom_step.select_control(DesignerControlType.input_table, 1)
    # properties.set_indent("1")
    properties.set_label("选择源表:")
    properties.set_default_library("SASHELP")
    properties.set_default_table("CLASS")

    insert_section(page, section_number, "列选择器控件")
    section_number += 1
    insert_text(page, text_number,
                "使用列选择器控件从链接的输入表添加列。您可以控制可以添加的列数、列的类型以及是否可以对列重新排序。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.column_selector)
    custom_step.select_control(DesignerControlType.column_selector, 1)
    # properties.set_indent("1")
    properties.set_label("选择一列:")
    properties.select_link_input_table("输入表标签 1  (inputtable1)")
    properties.select_column_type("字符")
    properties.set_max_columns("1")

    # custom_step.insert_control(DesignerControlType.column_selector)
    # custom_step.select_control(DesignerControlType.column_selector, 2)
    # #properties.set_indent("1")
    # properties.set_label("选择多个列:")
    # properties.select_link_input_table("输入表标签 1  (inputtable1)")
    # properties.set_min_columns("1")
    # properties.set_max_columns("3")
    # properties.set_check_allow_order_column()

    insert_section(page, section_number, "新建列控件")
    section_number += 1
    insert_text(page, text_number,
                "使用新的列控件向输出表添加列。您可以定义默认列属性，并指定自定义步骤的用户是否可以编辑这些属性。若可以编辑属性，则用户点击“编辑”图标以打开“列属性”窗口并编辑任何属性。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.new_column)
    custom_step.select_control(DesignerControlType.new_column, 1)
    # properties.set_indent("1")
    properties.set_label("添加新列:")
    properties.set_default_column_name("Grade")
    properties.set_default_column_label("年级")
    properties.select_default_type("数字")
    properties.set_default_length("8")
    properties.set_default_format("Best12.")
    properties.set_default_informat("Best12.")

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 1")
    insert_section(page, section_number, "复选框控件")
    section_number += 1
    insert_text(page, text_number, "使用复选框在两个相反的状态、操作或值之间进行选择。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 1)
    properties.set_label("复选框")
    # properties.set_indent("1")
    properties.set_check_by_default()

    insert_section(page, section_number, "颜色选取器控件")
    section_number += 1
    insert_text(page, text_number, "使用颜色选取器控件选择一个颜色。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.color_picker)
    custom_step.select_control(DesignerControlType.color_picker, 1)
    # properties.set_indent("1")
    properties.click_select_color()
    properties.set_RGB(160, 95, 238)

    # insert_section(page,6,"日期和时间控件")
    # insert_text(page,6, "使用日期和时间控件选择日期和时间。")

    insert_section(page, section_number, "文件或文件夹选择器控件")
    section_number += 1
    insert_text(page, text_number, """使用文件或文件夹选择器控件指定文件或文件夹的路径。路径必须是 URL 格式。作为路径的一部分，您必须指定文件或文件夹是在“SAS 内容”中还是在 SAS 服务器上。

示例:
sascontent:/path/to/fileorfolder
sasserver:/path/to/fileorfolder""")
    text_number += 1
    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.select_control(DesignerControlType.file_or_folder_selector, 1)
    # properties.set_indent("1")
    properties.set_label("文件选择器:")
    properties.select_selector_type(FileOrFolder.file)

    custom_step.insert_control(DesignerControlType.file_or_folder_selector)
    custom_step.select_control(DesignerControlType.file_or_folder_selector, 2)
    # properties.set_indent("1")
    properties.set_label("文件夹选择器:")
    properties.select_selector_type(FileOrFolder.folder)
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 2")
    insert_section(page, section_number, "链接控件")
    section_number += 1
    insert_text(page, text_number,
                "使用链接控件支持自定义步骤中的超链接。为了安全起见，默认情况下禁用链接。管理员使用 SAS Environment Manager 启用该功能并为链接指定验证规则。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.link)
    custom_step.select_control(DesignerControlType.link, 1)
    # properties.set_indent("1")
    properties.set_label("SAS网站：")
    properties.set_link("https://www.sas.com")
    time.sleep(1)

    insert_section(page, section_number, "文本控件")
    section_number += 1
    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    text_number += 1
    # properties.set_indent("1")
    properties.set_enter_text("使用文本控件提供静态解释文本。")

    insert_section(page, section_number, "文本区域控件")
    section_number += 1
    insert_text(page, text_number, "使用文本区域控件输入或编辑一行或多行文本。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.textarea)
    custom_step.select_control(DesignerControlType.textarea, 1)
    # properties.set_indent("1")
    properties.set_placeholder_text_for_textarea("这里可以输入一行或多行文字")
    time.sleep(2)

    insert_section(page, section_number, "文本字段控件")
    section_number += 1

    insert_text(page, text_number, "验证文本的示例。已应用包含 5 个字符的正则表达式。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field, 1)
    # properties.set_indent("1")
    properties.set_label("验证:")
    properties.select_type_for_text_or_numeric_field(TextNumericValidation.validation)
    properties.set_regular_expression("\w{5}")
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 3")
    insert_section(page, section_number, "日期和时间控件")
    section_number += 1
    insert_text(page, text_number, "使用日期和时间控件选择日期和时间。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 1)
    # properties.set_indent("1")
    properties.set_label("日期和时间:")
    properties.select_date_time_type(DateTimeType.date_and_time)
    properties.click_default_value(DateTimeType.date_and_time)
    date_time_dialog: DateTimeDialog = get_dialog_page(page, DialogType.date_time_dialog)
    date_time_dialog.set_year("2025")
    for i in range(5):
        date_time_dialog.click_next_month()
    date_time_dialog.select_hour("03")
    date_time_dialog.select_minute("10")
    date_time_dialog.select_second("00")
    time.sleep(1)
    date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    custom_step.insert_control(DesignerControlType.date_and_time_picker)
    custom_step.select_control(DesignerControlType.date_and_time_picker, 2)
    # properties.set_indent("1")
    properties.set_label("月:")
    properties.select_date_time_type(DateTimeType.month)
    properties.click_default_value(DateTimeType.month)
    year_month_dialog: YearMonthDialog = get_dialog_page(page, DialogType.year_month_dialog)
    year_month_dialog.set_year("2010")
    year_month_dialog.select_month(Month.october)
    year_month_dialog.click_button_in_footer(Helper.data_locale.OK)

    # custom_step.insert_control(DesignerControlType.date_and_time_picker)
    # custom_step.select_control(DesignerControlType.date_and_time_picker, 3)
    # #properties.set_indent("1")
    # properties.set_label("时间:")
    # properties.select_date_time_type(DateTimeType.time)
    # properties.click_default_value(DateTimeType.time)
    # date_time_dialog.select_hour("03")
    # date_time_dialog.select_minute("08")
    # date_time_dialog.select_second("00")
    # date_time_dialog.click_button_in_footer(Helper.data_locale.OK)

    insert_section(page, section_number, "下拉列表控件")
    section_number += 1
    insert_text(page, text_number,
                "当您想要显示包含选项列表的菜单时，使用下拉列表控件。选项列表可以是项的静态列表，也可以是项的动态列表。")
    text_number += 1
    insert_text(page, text_number,
                "使用静态下拉列表用一组预定义值填充列表。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list, 1)
    # properties.set_indent("1")
    properties.set_label("静态下拉列表:")
    properties.add_many_items("Judy\nWilliam\nHenry")
    properties.select_default_item("Henry")

    insert_text(page, text_number,
                "使用动态下拉列表用来自链接列选择器的非重复值填充列表中的项。例如，以下下拉列表填充了来自“数据”页面上第一个列选择器中所选列的非重复值。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list, 2)
    # properties.set_indent("1")
    properties.set_label("动态下拉列表:")
    properties.set_check_dynamic_list()
    properties.select_reference_column_selector("列选择器标签 1  (columnselector1)")
    properties.set_default_item("Carol")
    time.sleep(2)

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 4")
    insert_section(page, section_number, "列表控件")
    section_number += 1
    insert_text(page, text_number,
                "当您想要允许从项列表中选择多个选项时，使用列表控件。选项列表可以是项的静态列表，也可以是项的动态列表。")
    text_number += 1
    insert_text(page, text_number,
                "使用静态列表用一组预定义值填充列表。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.list)
    custom_step.select_control(DesignerControlType.list, 1)
    # properties.set_indent("1")
    properties.add_many_items("小学\n初中\n高中\n大学")
    properties.set_minimum_number_of_values("1")
    properties.set_maximum_number_of_values("4")
    insert_text(page, text_number,
                "使用动态列表用来自链接列选择器的非重复值填充列表中的项。例如，以下列表填充了来自“数据”页面上第一个列选择器中所选列的非重复值。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.list)
    custom_step.select_control(DesignerControlType.list, 2)
    # properties.set_indent("1")
    properties.set_check_dynamic_list()
    properties.select_reference_column_selector("列选择器标签 1  (columnselector1)")
    properties.set_minimum_number_of_values("1")
    properties.set_maximum_number_of_values("5")

    custom_step.add_page_by_toolbar()
    properties.set_label("控件 5")
    insert_section(page, section_number, "数值字段控件")
    section_number += 1
    insert_text(page, text_number,
                "使用数值字段输入数值。最小值为 0，最大值为 100。当字段为空时，占位符文本向用户提供说明。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field, 2)
    # properties.set_indent("1")
    properties.set_label("数值字段:")
    properties.select_type_for_text_or_numeric_field(TextNumericValidation.numeric)
    properties.set_check_allow_integer_values_only()
    properties.set_default_value("5")
    properties.set_minimum_value("0")
    properties.set_maximum_value("100")
    properties.set_placeholder_text("输入 0 和 100 之间的数值。")
    properties.set_check_exclude_minimum_in_range()
    properties.set_check_exclude_maximum_in_range()

    insert_text(page, text_number,
                "使用数字步进器的向上和向下箭头以指定的增量变换数字。默认值为 10。最小值为 0，最大值为 20。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.numeric_stepper)
    custom_step.select_control(DesignerControlType.numeric_stepper, 1)
    # properties.set_indent("1")
    properties.set_label("数字步进器:")
    properties.set_check_allow_integer_values_only()
    properties.set_default_value("10")
    properties.set_minimum_value("0")
    properties.set_maximum_value("20")
    properties.set_step_size("2")

    insert_section(page, section_number, "单选按钮组控件")
    section_number += 1
    insert_text(page, text_number, "使用单选按钮组控件将互斥选项列表显示为单选按钮。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.radio_group)
    custom_step.select_control(DesignerControlType.radio_group, 1)
    # properties.set_indent("1")
    properties.set_label("单选按钮组:")
    properties.add_many_items("单选按钮 2")
    properties.select_default_radio_button("单选按钮 2")
    time.sleep(1)

    custom_step.add_page_by_toolbar()
    properties.set_label("依赖关系")

    custom_step.insert_control(DesignerControlType.text)
    custom_step.select_control(DesignerControlType.text, text_number)
    properties.set_enter_text("依赖关系使您能够根据另一个提示的值显示或隐藏提示。")
    text_number += 1

    insert_section(page, section_number, "复选框示例")
    section_number += 1
    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 2)
    # properties.set_indent("1")
    properties.set_label("选中框以显示文本字段")
    custom_step.insert_control(DesignerControlType.text_or_numeric_field)
    custom_step.select_control(DesignerControlType.text_or_numeric_field, 3)
    # properties.set_indent("1")
    properties.set_label("文本字段:")
    properties.set_placeholder_text("选中复选框时显示")
    properties.set_visibility("$checkbox2")
    time.sleep(1)

    insert_section(page, section_number, "下拉列表示例")
    section_number += 1
    insert_text(page, text_number, "从下拉列表中选择的类别决定了出现的复选框。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.drop_down_list)
    custom_step.select_control(DesignerControlType.drop_down_list, 3)
    # properties.set_indent("1")
    properties.set_label("选择水果类别:")
    properties.add_many_items("浆果类\n瓜类")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 3)
    # properties.set_indent("1")
    properties.set_label("草莓")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"浆果类\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 4)
    # properties.set_indent("1")
    properties.set_label("蓝莓")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"浆果类\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 5)
    # properties.set_indent("1")
    properties.set_label("西瓜")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"瓜类\"]")

    custom_step.insert_control(DesignerControlType.checkbox)
    custom_step.select_control(DesignerControlType.checkbox, 6)
    # properties.set_indent("1")
    properties.set_label("哈密瓜")
    properties.set_visibility("[\"$dropdown3\",\"=\",\"瓜类\"]")

    custom_step.add_page_by_toolbar()
    properties.set_label("输出")
    insert_section(page, section_number, "输出数据控件")
    section_number += 1
    insert_text(page, text_number, "使用输出表控件指定输出表。在流中，输出表控件表示为输出端口。")
    text_number += 1
    custom_step.insert_control(DesignerControlType.output_table)
    custom_step.select_control(DesignerControlType.output_table, 1)
    # properties.set_indent("1")
    properties.set_label("输出数据控件:")
    properties.set_check_required()
    properties.set_placeholder_text("请选择输出数据")
    time.sleep(1)

