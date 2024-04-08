"""
Author: Alice
Date: Apr 07, 2024
Description: This is factory of designer properties pane in custom step.
"""
from src.Pages.StudioNext.Center.CustomStep.DesignerProperties.properties_checkbox import PropertiesCheckbox
from src.Pages.StudioNext.Center.CustomStep.DesignerProperties.properties import Properties
from src.Utilities.enums import DesignerControlType
from playwright.sync_api import Page


def get_properties(page: Page,control_type: DesignerControlType) -> Properties:
    properties:Properties = None
    match control_type:
        case DesignerControlType.checkbox:
            properties = PropertiesCheckbox(page)
        # case DesignerControlType.color_picker:
        # case DesignerControlType.column_selector:
        # case DesignerControlType.date_and_time_picker:
        # case DesignerControlType.drop_down_list:
        # case DesignerControlType.file_or_folder_selector:
        # case DesignerControlType.input_table:
        # case DesignerControlType.link:
        # case DesignerControlType.list:
        # case DesignerControlType.new_column:
        # case DesignerControlType.numeric_stepper:
        # case DesignerControlType.output_table:
        # case DesignerControlType.radio_group:
        # case DesignerControlType.section:
        # case DesignerControlType.text:
        # case DesignerControlType.text_or_numeric_field:
        # case DesignerControlType.textarea:
    return properties
