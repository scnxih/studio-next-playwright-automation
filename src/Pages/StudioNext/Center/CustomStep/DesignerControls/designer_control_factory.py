"""
Author: Alice
Date: Feb 01, 2024
Description: This is factory of designer control.
"""
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_checkbox import DesignerCheckbox
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_control import DesignerControl
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_color_picker import DesignerColorPicker
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_column_selector import DesignerColumnSelector
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_date_and_time_picker import DesignerDateAndTimePicker
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_dropdown_list import DesignerDropDownList
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_file_or_folder_selector import DesignerFileOrFolderSelector
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_input_table import DesignerInputTable
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_link import DesignerLink
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_list import DesignerList
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_new_column import DesignerNewColumn
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_numeric_stepper import DesignerNumericStepper
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_output_table import DesignerOutputTable
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_radio_group import DesignerRadioGroup
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_section import DesignerSection
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_text import DesignerText
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_text_or_numeric_field import DesignerTextOrNumericField
from src.Pages.StudioNext.Center.CustomStep.DesignerControls.designer_textarea import DesignerTextArea
from src.Utilities.enums import DesignerControlType
from playwright.sync_api import Page


def get_designer_control(page: Page,control_type: DesignerControlType, control_number: int) -> DesignerControl:
    designer_control:DesignerControl = None
    match control_type:
        case DesignerControlType.checkbox:
            designer_control = DesignerCheckbox(page, control_number)
        case DesignerControlType.color_picker:
            designer_control = DesignerColorPicker(page, control_number)
        case DesignerControlType.column_selector:
            designer_control = DesignerColumnSelector(page, control_number)
        case DesignerControlType.date_and_time_picker:
            designer_control = DesignerDateAndTimePicker(page, control_number)
        case DesignerControlType.drop_down_list:
            designer_control = DesignerDropDownList(page, control_number)
        case DesignerControlType.file_or_folder_selector:
            designer_control = DesignerFileOrFolderSelector(page, control_number)
        case DesignerControlType.input_table:
            designer_control = DesignerInputTable(page, control_number)
        case DesignerControlType.link:
            designer_control = DesignerLink(page, control_number)
        case DesignerControlType.list:
            designer_control = DesignerList(page, control_number)
        case DesignerControlType.new_column:
            designer_control = DesignerNewColumn(page, control_number)
        case DesignerControlType.numeric_stepper:
            designer_control = DesignerNumericStepper(page, control_number)
        case DesignerControlType.output_table:
            designer_control = DesignerOutputTable(page, control_number)
        case DesignerControlType.radio_group:
            designer_control = DesignerRadioGroup(page, control_number)
        case DesignerControlType.section:
            designer_control = DesignerSection(page, control_number)
        case DesignerControlType.text:
            designer_control = DesignerText(page, control_number)
        case DesignerControlType.text_or_numeric_field:
            designer_control = DesignerTextOrNumericField(page, control_number)
        case DesignerControlType.textarea:
            designer_control = DesignerTextArea(page, control_number)
    return designer_control
