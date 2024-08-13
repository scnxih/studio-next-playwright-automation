"""
Author: Alice
Date: Apr 15, 2024
Description: This is factory of all common components.
"""
from playwright.sync_api import Playwright, Page
from src.Pages.Common.numeric_stepper import NumericStepper
from src.Pages.Common.textarea import Textarea
from src.Pages.Common.text import Text
from src.Pages.Common.combobox import Combobox
from src.Pages.Common.checkbox import Checkbox
from src.Pages.Common.button import Button
from src.Pages.Common.treegrid import TreeGrid
from src.Pages.Common.treegrid_cont_menu import TreegridContextMenu
from src.Pages.Common.treeview_aggrid import TreeViewAGGrid
from src.Pages.Common.treeview_common import TreeViewCommon
from src.Pages.Common.treeview_flow import TreeViewFlow
from src.Pages.Common.treeview_nova import TreeViewNova
from src.Pages.Common.window_shade import WindowShade
from src.Pages.Common.color_picker import ColorPicker
from src.Pages.Common.toolbar import Toolbar
from src.Pages.Common.listbox import Listbox
from src.Pages.Common.radio_group import RadioGroup
from src.Pages.Common.switch_button import SwitchButton
from src.Pages.Common.tab_group import TabGroup
from src.Pages.Common.widget import Widget
from src.Pages.Common.grid import Grid


def get_numeric_stepper(container_base_xpath: str, page: Page, data_test_id="", supplement_base_xpath="",parent_label=""):
    return NumericStepper(container_base_xpath, page, data_test_id=data_test_id,
                          supplement_base_xpath=supplement_base_xpath,parent_label=parent_label)


def get_textarea(container_base_xpath: str, page: Page, data_test_id="", aria_label="", supplement_base_xpath="",
                 parent_label=""):
    return Textarea(container_base_xpath, page, data_test_id=data_test_id, aria_label=aria_label,
                    supplement_base_xpath=supplement_base_xpath,
                    parent_label=parent_label)


def get_text(container_base_xpath: str, page: Page, data_test_id="", aria_label="", supplement_base_xpath="",parent_label=""):
    return Text(container_base_xpath, page, aria_label=aria_label, data_test_id=data_test_id,
                supplement_base_xpath=supplement_base_xpath,parent_label=parent_label)



def get_combobox(container_base_xpath: str, page: Page, data_test_id="", items_count=20,supplement_base_xpath="",aria_label="",parent_label="",parent_label_level =3):
    return Combobox(container_base_xpath, page, data_test_id=data_test_id, items_count=items_count,supplement_base_xpath=supplement_base_xpath,aria_label=aria_label,parent_label=parent_label,parent_label_level= parent_label_level)


def get_checkbox(container_base_xpath: str, page: Page, data_test_id="", label="",supplement_base_xpath= ""):
    return Checkbox(container_base_xpath, page, data_test_id=data_test_id, label=label,supplement_base_xpath = supplement_base_xpath)


def get_button(container_base_xpath: str, page: Page, data_test_id="", aria_label="", title="",
               supplement_base_xpath=""):
    return Button(container_base_xpath, page, data_test_id=data_test_id, aria_label=aria_label, title=title,
                  supplement_base_xpath=supplement_base_xpath)


def get_windowshade(container_base_xpath: str, page: Page, supplement_base_xpath="",parent_label=""):

    return WindowShade(container_base_xpath, page, supplement_base_xpath=supplement_base_xpath,parent_label=parent_label)


def get_color_picker(container_base_xpath: str, page: Page):
    return ColorPicker(container_base_xpath, page)


def get_toolbar(container_base_xpath, page, class_attribute="", data_test_id="", supplement_base_xpath=""):
    return Toolbar(container_base_xpath, page, class_attribute=class_attribute, data_test_id=data_test_id,
                   supplement_base_xpath=supplement_base_xpath)


def get_listbox(container_base_xpath, page, data_test_id="", aria_label="", aria_labelledby="",supplement_base_xpath="",parent_label =""):
    return Listbox(container_base_xpath, page, data_test_id=data_test_id, aria_label=aria_label,
                   aria_labelledby=aria_labelledby,supplement_base_xpath=supplement_base_xpath,parent_label=parent_label)


def get_radio_group(container_base_xpath, page, data_test_id="",supplement_base_xpath="",parent_label=""):

    return RadioGroup(container_base_xpath, page, data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath,parent_label=parent_label)


def get_switch_button(container_base_xpath, page, data_test_id=""):
    return SwitchButton(container_base_xpath, page, data_test_id=data_test_id)


def get_tab_group(container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
    return TabGroup(container_base_xpath, page, data_test_id=data_test_id, supplement_base_xpath=supplement_base_xpath)


def get_widget(container_base_xpath, page):
    return Widget(container_base_xpath, page)

def get_grid(container_base_xpath, page,data_test_id=""):
    return Grid(container_base_xpath,page,data_test_id=data_test_id)


def get_treegrid(container_base_xpath, page, data_test_id=""):
    return TreeGrid(container_base_xpath,page,data_test_id=data_test_id)


def get_treegrid_cont_menu(container_base_xpath, page):
    return TreegridContextMenu(container_base_xpath,page)

def get_treeview_aggrid(container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
    return TreeViewAGGrid(container_base_xpath,page,data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)


def get_treeview_common(container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
    return TreeViewCommon(container_base_xpath,page,data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)


def get_treeview_flow(container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
    return TreeViewFlow(container_base_xpath,page,data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)

def get_treeview_nova(container_base_xpath, page, data_test_id="", supplement_base_xpath=""):
    return TreeViewNova(container_base_xpath,page,data_test_id=data_test_id,supplement_base_xpath=supplement_base_xpath)