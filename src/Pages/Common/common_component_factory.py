from playwright.sync_api import Playwright, Page
from src.Pages.Common.numeric_stepper import NumericStepper
from src.Pages.Common.textarea import Textarea
from src.Pages.Common.text import Text
from src.Pages.Common.combobox import Combobox
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.button import Button
from src.Pages.Common.window_shade import WindowShade
from src.Pages.Common.color_picker import ColorPicker
from src.Pages.Common.toolbar import Toolbar
from src.Pages.Common.listbox import Listbox
from src.Pages.Common.radio_group import RadioGroup
from src.Pages.Common.switch_button import SwitchButton
from src.Pages.Common.tab_group import TabGroup
from src.Pages.Common.widget import Widget


def get_numeric_stepper(container_base_xpath: str, page: Page, data_test_id="", supplement_base_xpath=""):
    return NumericStepper(container_base_xpath, page, data_test_id=data_test_id,
                          supplement_base_xpath=supplement_base_xpath)


def get_textarea(container_base_xpath: str, page: Page, data_test_id="", aria_label="", supplement_base_xpath="",
                 textarea_label=""):
    return Textarea(container_base_xpath, page, data_test_id=data_test_id, aria_label=aria_label,
                    supplement_base_xpath=supplement_base_xpath,
                    textarea_label=textarea_label)


def get_text(container_base_xpath: str, page: Page, data_test_id="", aria_label="", supplement_base_xpath=""):
    return Text(container_base_xpath, page, aria_label=aria_label, data_test_id=data_test_id,
                supplement_base_xpath=supplement_base_xpath)


def get_combobox(container_base_xpath: str, page: Page, data_test_id="", items_count=20,supplement_base_xpath=""):
    return Combobox(container_base_xpath, page, data_test_id=data_test_id, items_count=items_count,supplement_base_xpath=supplement_base_xpath)


def get_checkbox(container_base_xpath: str, page: Page, data_test_id="", label=""):
    return Checkbox(container_base_xpath, page, data_test_id=data_test_id, label=label)


def get_button(container_base_xpath: str, page: Page, data_test_id="", aria_label="", title="",
               supplement_base_xpath=""):
    return Button(container_base_xpath, page, data_test_id=data_test_id, aria_label=aria_label, title=title,
                  supplement_base_xpath=supplement_base_xpath)


def get_windowshade(container_base_xpath: str, page: Page, supplement_base_xpath=""):
    return WindowShade(container_base_xpath, page, supplement_base_xpath=supplement_base_xpath)


def get_color_picker(container_base_xpath: str, page: Page):
    return ColorPicker(container_base_xpath, page)


def get_toolbar(container_base_xpath, page, class_attribute="", data_test_id="", supplement_base_xpath=""):
    return Toolbar(container_base_xpath, page, class_attribute=class_attribute, data_test_id=data_test_id,
                   supplement_base_xpath=supplement_base_xpath)


def get_listbox(container_base_xpath, page, data_test_id="", aria_label="", aria_labelledby=""):
    return Listbox(container_base_xpath, page, data_test_id=data_test_id, aria_label=aria_label,
                   aria_labelledby=aria_labelledby)


def get_radio_group(container_base_xpath, page, data_test_id=""):
    return RadioGroup(container_base_xpath, page, data_test_id=data_test_id)


def get_switch_button(container_base_xpath, page, data_test_id=""):
    return SwitchButton(container_base_xpath, page, data_test_id=data_test_id)


def get_tab_group(container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
    return TabGroup(container_base_xpath, page, data_test_id=data_test_id, supplement_base_xpath=supplement_base_xpath)


def get_widget(container_base_xpath, page):
    return Widget(container_base_xpath, page)
