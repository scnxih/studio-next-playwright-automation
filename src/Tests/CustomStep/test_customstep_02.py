import time

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
def test_01_common_controls(page, init):
    custom_step: CustomStepPage = PageHelper.new_item(page, TopMenuItem.new_custom_step)
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
    # properties.set_indent("1")
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
    time.sleep(0.5)
    WholePage(page).screenshot_self(pic_name="01_data")

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
    WholePage(page).screenshot_self(pic_name="02_controls1")
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
    WholePage(page).screenshot_self(pic_name="03_controls2")
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
    # properties.set_indent("1")
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
    WholePage(page).screenshot_self(pic_name="04_controls3")
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
    WholePage(page).screenshot_self(pic_name="05_controls4")
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
    WholePage(page).screenshot_self(pic_name="06_controls5")
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
    time.sleep(0.5)
    WholePage(page).screenshot_self(pic_name="07_dependency")
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
    WholePage(page).screenshot_self(pic_name="08_output")