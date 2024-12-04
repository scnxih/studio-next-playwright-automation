"""
Author: Alice
Date: Mar 05, 2024
Description: This is base class of all Flow details pane.

"""
import time

from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.flow_canvas import *
from src.Pages.Common.text import *
from src.Pages.Common.textarea import *
from src.Pages.StudioNext.Dialog.select_column_dialog import SelectColumnDialog


class DetailsPane(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.base_xpath = "//div[@class='sas_components-views-dataflow-FlowView_selected-pane']"
        self.tab_group = TabGroup("", page)

    def click_tab(self, text: str):
        """
        Description: click the tab in details pane.
        @text: the text of the tab.
        """
        self.tab_group.click_tab_by_text(text)

    def set_node_name(self, name: str):
        """
        Description: set node name.
        @name: the name you want to specify for the node.
        """
        self.click_tab(Helper.data_locale.NODE)
        Text(self.base_xpath, self.page,
             supplement_base_xpath="[../../../descendant::label[contains(text(),'" + Helper.data_locale.NODE_NAME + "')]]").fill_text(
            name)

    def set_node_description(self, description: str):
        """
        Description: set node description.
        @description: the description you want to specify for the node.
        """
        self.click_tab(Helper.data_locale.NODE)
        Textarea(self.base_xpath, self.page).fill_text(description)

    def set_notes(self, notes: str):
        """
        Description: set node notes.
        @notes: the notes you want to specify for the node.
        """
        self.click_tab(Helper.data_locale.NOTES)
        Textarea(self.base_xpath, self.page).fill_text(notes)

    def click_data_tab(self):
        """
        Description: click Data tab.
        """
        self.click_tab(Helper.data_locale.DATA)

    def click_options_tab(self):
        """
        Description: click Options tab.
        """
        self.click_tab(Helper.data_locale.OPTIONS)

    def click_model_tab(self):
        """
        Description: click Options tab.
        """
        self.click_tab(Helper.data_locale.MODEL_TAB)

    def click_output_tab(self):
        """
        Description: click Output tab.
        """
        self.click_tab(Helper.data_locale.OUTPUT)

    def click_node_tab(self):
        """
        Description: click Node tab.
        """
        self.click_tab(Helper.data_locale.NODE)

    def click_notes_tab(self):
        """
        Description: click Notes tab.
        """
        self.click_tab(Helper.data_locale.NOTES)

    def click_plots_tab(self):
        """
        Description: click Notes tab.
        """
        self.click_tab(Helper.data_locale.PLOTS)

    def _add_column_button(self, parent_label: str, section_label:str = None):
        if section_label == None:
            return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(
                              Helper.data_locale.ADD_COLUMN, parent_label))
        else:
            return get_button(self.base_xpath, self.page,
                              supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]/../../../../../../../../../../../descendant::div[contains(@class,'sas_components-WindowShade-WindowShade_section-header')]//span[text()='{2}']]".format(
                                  Helper.data_locale.ADD_COLUMN, parent_label,section_label))

    def _add_exact_column_button(self, parent_label: str, section_label:str = None):
        if section_label == None:
            return get_button(self.base_xpath, self.page,
                              supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']]".format(
                                  Helper.data_locale.ADD_COLUMN, parent_label))

        else:
            return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']/../../../../../../../../../../../descendant::div[contains(@class,'sas_components-WindowShade-WindowShade_section-header')]//span[text()='{2}']]".format(
                              Helper.data_locale.ADD_COLUMN, parent_label,section_label))
    def _delete_column_button(self, parent_label: str,section_label:str = None):
        if section_label == None:
            return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(
                              Helper.data_locale.DELETE_COLUMNS, parent_label))
        else:
            return get_button(self.base_xpath, self.page,
                              supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]/../../../../../../../../../../../descendant::div[contains(@class,'sas_components-WindowShade-WindowShade_section-header')]//span[text()='{2}']]".format(
                                  Helper.data_locale.DELETE_COLUMNS, parent_label, section_label))
    def _delete_exact_column_button(self, parent_label: str, section_label:str = None):
        if section_label == None:
            return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']]".format(
                              Helper.data_locale.DELETE_COLUMNS, parent_label))
        else:
            return get_button(self.base_xpath, self.page,
                              supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']/../../../../../../../../../../../descendant::div[contains(@class,'sas_components-WindowShade-WindowShade_section-header')]//span[text()='{2}']]".format(
                                  Helper.data_locale.DELETE_COLUMNS, parent_label,section_label))

    def _move_up_column_button(self, parent_label: str, section_label:str = None):
        if section_label == None:
            return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(
                              Helper.data_locale.MOVE_COLUMN_UP, parent_label))
        else:
            return get_button(self.base_xpath, self.page,
                              supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]/../../../../../../../../../../../descendant::div[contains(@class,'sas_components-WindowShade-WindowShade_section-header')]//span[text()='{2}']]".format(
                                  Helper.data_locale.MOVE_COLUMN_UP, parent_label, section_label))

    def _move_down_column_button(self, parent_label: str, section_label:str = None):
        if section_label == None:
            return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(
                              Helper.data_locale.MOVE_COLUMN_DOWN, parent_label))
        else:
            return get_button(self.base_xpath, self.page,
                              supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]/../../../../../../../../../../../descendant::div[contains(@class,'sas_components-WindowShade-WindowShade_section-header')]//span[text()='{2}']]".format(
                                  Helper.data_locale.MOVE_COLUMN_DOWN, parent_label, section_label))
    def _click_move_up_column_button(self,parent_label:str, section_label:str = None):
        self._move_up_column_button(parent_label,section_label=section_label).click_self()

    def _click_move_down_column_button(self, parent_label: str , section_label:str = None):
        self._move_down_column_button(parent_label,section_label=section_label).click_self()
    def _click_add_column_button(self, parent_label: str , section_label:str = None):
        """
        Description: click add column button.
        @parent_label: the label of the add column button. The colon is not required.
        """
        self._add_column_button(parent_label=parent_label,section_label=section_label).click_self()

    def delete_column(self, parent_label: str , section_label:str = None):
        """
        Description: click delete column button.
        @parent_label: the label of the delete column button. The colon is not required.
        """
        self._delete_column_button(parent_label=parent_label,section_label=section_label).click_self()

    def _click_add_exact_column_button(self, parent_label: str, section_label:str = None):
        """
        Description: click add column button which label is exact the label(including colon:).
        The method is only used for the buttons which have duplicated parts in label,
        such as Weight when Auxiliary weight exists as well.
        Please note if use this method, the colon(:) should also be passed in the parent_label parameter since this is exact the label.
        @parent_label: the exact label of the add column button.
        """
        self._add_exact_column_button(parent_label=parent_label,section_label=section_label).click_self()

    def delete_column_exact_label(self, parent_label: str, section_label:str = None):
        """
        Description: click delete column button which label is exact the label(including colon:).
        The method is only used for the buttons which have duplicated parts in label,
        such as Weight when Auxiliary weight exists as well.
        Please note if use this method, the colon(:) should also be passed in the parent_label parameter since this is exact the label.
        @parent_label: the exact label of the delete column button.
        """
        self._delete_exact_column_button(parent_label=parent_label,section_label=section_label).click_self()

    def add_column(self, parent_label: str, column_name: str, section_label:str = None):
        """
        Description: add a column, pop up select a column dialog and choose a column and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label could be the part of the parent label, that is,
        the colon(:) can be omitted.
        @column_name: the column name of the added column.
        """
        self._click_add_column_button(parent_label=parent_label,section_label=section_label)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)

    def add_column_exact_label(self, parent_label: str, column_name: str, section_label:str = None):
        """
        Description: add a column, pop up select a column dialog and choose a column and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label should be exact the label, that is, the colon(:)
        could NOT be omitted. The method will be used only when there are labels which text has duplicate parts. For example,
        if there is weight and auxiliary weight, this method should be used for weight.
        @column_name: the column name of the added column.
        """
        self._click_add_exact_column_button(parent_label=parent_label,section_label=section_label)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)
    def add_columns_with_supplement_xpath(self,supplement_xpath, check_column_name_list: list=None, uncheck_column_name_list: list=None):
        get_button(self.base_xpath, self.page,
                   supplement_base_xpath="[@aria-label='{0}']{1}".format(
                       Helper.data_locale.ADD_COLUMN, supplement_xpath)).click_self()

        select_column_dialog = SelectColumnDialog(self.page)
        if check_column_name_list != None:
            for check_column_name in check_column_name_list:
                select_column_dialog.set_check_in_a_row(check_column_name)

        if uncheck_column_name_list != None:
            for uncheck_column_name in uncheck_column_name_list:
                select_column_dialog.set_uncheck_in_a_row(uncheck_column_name)

        time.sleep(0.5)
        select_column_dialog.click_ok_button()
        time.sleep(0.5)

    def add_columns(self, parent_label: str, section_label:str = None, check_column_name_list: list=None, uncheck_column_name_list: list=None):
        """
        Description: set columns, pop up select columns dialog and check columns defined in check_column_name_list,
        uncheck columns defined in uncheck_column_name_list and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label could be the part of the parent label, that is,
        the colon(:) can be omitted.
        @check_column_name_list: the list of columns which you want to check.
        @uncheck_column_name_list: the list of columns which you want to uncheck.
        """
        self._click_add_column_button(parent_label=parent_label,section_label=section_label)
        select_column_dialog = SelectColumnDialog(self.page)
        if check_column_name_list != None:
            for check_column_name in check_column_name_list:
               select_column_dialog.set_check_in_a_row(check_column_name)

        if uncheck_column_name_list!=None:
            for uncheck_column_name in uncheck_column_name_list:
                select_column_dialog.set_uncheck_in_a_row(uncheck_column_name)

        time.sleep(0.5)
        select_column_dialog.click_ok_button()
        time.sleep(0.5)

    def add_columns_exact_label(self, parent_label: str, section_label:str = None, check_column_name_list: list=None, uncheck_column_name_list: list=None):
        """
        Description: set columns, pop up select columns dialog and check columns defined in check_column_name_list,
        uncheck columns defined in uncheck_column_name_list and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label could be the part of the parent label, that is,
        the colon(:) can be omitted.
        @check_column_name_list: the list of columns which you want to check.
        @uncheck_column_name_list: the list of columns which you want to uncheck.
        """
        self._click_add_exact_column_button(parent_label=parent_label,section_label=section_label)
        select_column_dialog = SelectColumnDialog(self.page)
        if check_column_name_list!= None:
            for check_column_name in check_column_name_list:
                select_column_dialog.set_check_in_a_row(check_column_name)
        if uncheck_column_name_list!= None:
            for uncheck_column_name in uncheck_column_name_list:
                select_column_dialog.set_uncheck_in_a_row(uncheck_column_name)

        time.sleep(0.5)
        select_column_dialog.click_ok_button()
        time.sleep(0.5)

    def expand_windowshade(self, parent_label: str):
        """
        Description: expand window shade.
        @parent_label: the label of the window shade.
        """
        get_windowshade(self.base_xpath, self.page, parent_label=parent_label).expand()

    def collapse_windowshade(self, parent_label: str):
        """
        Description: collapse window shade.
        @parent_label: the label of the window shade.
        """
        get_windowshade(self.base_xpath, self.page, parent_label=parent_label).collapse()

    def set_option_for_radio_group(self, parent_label: str =None, section_label :str= None, item_index: int = None, item_value: str = None):
        """
        Description: set option for radio group by item index(index starts from 0) or by item value.
        @parent_label: the label of radio group.
        @item_index: index of selected option, starting from 0.
        @item_value: value of selected option.
        """
        if section_label == None:
            if parent_label != None:
                if item_index != None:
                    get_radio_group(self.base_xpath, self.page,
                                parent_label=parent_label).set_check_for_index(index=item_index)
                    return
                if item_value != None:
                    get_radio_group(self.base_xpath, self.page,
                                parent_label=parent_label).set_check(text=item_value)
                    return
            else:
                if item_index != None:
                    get_radio_group(self.base_xpath, self.page).set_check_for_index(index=item_index)
                    return
                if item_value != None:
                    get_radio_group(self.base_xpath, self.page).set_check(text=item_value)
        else:
            if parent_label != None:
                if item_index != None:
                    get_radio_group(self.base_xpath, self.page,
                                supplement_base_xpath="[../../descendant::label[contains(text(),'{0}')]][../../../../../preceding-sibling::div[1][.//span[text()='{1}']]]".format(parent_label,section_label)
                                    ).set_check_for_index(index=item_index)
                    return
                if item_value != None:
                    get_radio_group(self.base_xpath, self.page,
                                supplement_base_xpath="[../../descendant::label[contains(text(),'{0}')]][../../../../../preceding-sibling::div[1][.//span[text()='{1}']]]".format(
                                        parent_label, section_label)
                                    ).set_check(text=item_value)
                    return
            else:
                if item_index != None:
                    get_radio_group(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../preceding-sibling::div[1][.//span[text()='{0}']]]".format(
                                        section_label)
                                    ).set_check_for_index(index=item_index)
                    return
                if item_value != None:
                    get_radio_group(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../preceding-sibling::div[1][.//span[text()='{0}']]]".format(
                                        section_label)
                                    ).set_check(text=item_value)
                    return

    def set_check_for_checkbox(self, label: str, section_label:str=None):
        """
        Description: set checked for check box.
        @label: the label of the checkbox.
        @section_label: the label of the section of the checkbox, it's only used when there are same name checkboxes under different sections.
        """
        if section_label == None:
            get_checkbox(self.base_xpath, self.page, label=label).set_check()
        else:
            get_checkbox(self.base_xpath,self.page,supplement_base_xpath=
            "[.//label[text()='{0}']][../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()='{1}']]]".format(label,section_label)
            ).set_check()


    def set_uncheck_for_checkbox(self, label: str, section_label:str= None):
        """
        Description: set unchecked for check box.
        @label: the label of the checkbox.
        @section_label: the label of the section of the checkbox, it's only used when there are same name checkboxes under different sections.
        """
        if section_label == None:
            get_checkbox(self.base_xpath, self.page, label=label).set_uncheck()
        else:
            get_checkbox(self.base_xpath,self.page,supplement_base_xpath=
            "[.//label[text()='{0}']][../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()='{1}']]]".format(label,section_label)
            ).set_uncheck()
    def set_option_for_combobox(self, parent_label: str, preceding_label: str = None, section_label:str = None, item_index: int = None,
                                item_value: str = None):
        """
        Description: set option for combobox (dropdown list).
        @parent_label: the label of the combobox.
        @preceding_label: the preceding label of the combobox, the parameter is used only when there are more than one combobox with the same parent label but different preceding label under the same section.
        @section_label: the section label of the combobox, the parameter is used only when there are more than one combobox with the same parent label but different section label.
        @item_index: the index of the selected option of the combobox, starting from 0.
        @item_value: the value of the selected option of the combobox.
        """
        combobox = None
        if section_label == None:
            if preceding_label == None:
                combobox = get_combobox(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../../descendant::label[contains(text(),'{0}')]]".format(
                                        parent_label))
            else:
                combobox = get_combobox(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../../descendant::label[contains(text(),'{0}')]/../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{1}')]]]".format(
                                        parent_label, preceding_label))
        else:
            combobox= get_combobox(self.base_xpath,self.page,supplement_base_xpath=
            "[../../../../../../descendant::label[contains(text(),'{0}')]/../../../../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()='{1}']]]".format(parent_label,section_label))

        if item_index != None:
            combobox.select_item_by_index(item_index)
            return
        if item_value != None:
            combobox.select_item(item_value)
            return
    def set_option_for_combobox_exact_label(self, parent_label: str, preceding_label: str = None, section_label:str = None, item_index: int = None,
                                item_value: str = None):
        """
        Description: set option for combobox (dropdown list).
        @parent_label: the label of the combobox.
        @preceding_label: the preceding label of the combobox, the parameter is used only when there are more than one combobox with the same parent label but different preceding label under the same section.
        @section_label: the section label of the combobox, the parameter is used only when there are more than one combobox with the same parent label but different section label.
        @item_index: the index of the selected option of the combobox, starting from 0.
        @item_value: the value of the selected option of the combobox.
        """
        combobox = None
        if section_label == None:
            if preceding_label == None:
                combobox = get_combobox(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../../descendant::label[text()='{0}']]".format(
                                        parent_label))
            else:
                combobox = get_combobox(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../../descendant::label[text()='{0}']/../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{1}')]]]".format(
                                        parent_label, preceding_label))
        else:
            combobox= get_combobox(self.base_xpath,self.page,supplement_base_xpath=
            "[../../../../../../descendant::label[text()='{0}']/../../../../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()='{1}']]]".format(parent_label,section_label))

        if item_index != None:
            combobox.select_item_by_index(item_index)
            return
        if item_value != None:
            combobox.select_item(item_value)
            return

    def set_text_for_text_control(self, parent_label: str, input_text: str, section_label:str= None):
        """
        Description: set text for text control.
        @parent_label: the label of the text control.
        @text: the text you want to input.
        @section_label: the label of the section, the parameter is used only when there are more than one texts with the same parent_label but with different section
        """
        if section_label == None:
            get_text(self.base_xpath, self.page, parent_label=parent_label).fill_text(input_text)
        else:
            get_text(self.base_xpath,self.page,supplement_base_xpath=
                     "[../../../descendant::label[contains(text(),'{0}')]/../../../../../../../preceding-sibling::div[contains(@class,'WindowShade')][.//span[text()='{1}']]]".format(parent_label,section_label)).fill_text(input_text)

    def set_check_for_listbox_item(self, parent_label: str, item_text: str):
        """se
        Description: set check for listbox item.
        @parent_label: the label of the listbox control.
        @item_text: the text of list item.
        """
        get_listbox(self.base_xpath, self.page, parent_label=parent_label).set_check_li_item(item_text)

    def set_uncheck_for_listbox_item(self, parent_label: str, item_text: str):
        """
        Description: set check for listbox item.
        @parent_label: the label of the listbox control.
        @item_text: the text of list item.
        """
        get_listbox(self.base_xpath, self.page, parent_label=parent_label).set_uncheck_li_item(item_text)

    def set_check_and_uncheck_for_listbox(self, parent_label:str,check_column_name_list:list=None,uncheck_column_name_list:list=None):
        if check_column_name_list!=None:
            for check_column_name in check_column_name_list:
                self.set_check_for_listbox_item(parent_label=parent_label,item_text=check_column_name)
        if uncheck_column_name_list!= None:
            for uncheck_column_name in uncheck_column_name_list:
                self.set_uncheck_for_listbox_item(parent_label=parent_label,item_text=uncheck_column_name)

    def delete_columns_for_listbox(self,parent_label:str,check_column_name_list:list=None,uncheck_column_name_list:list=None):
        self.set_check_and_uncheck_for_listbox(parent_label=parent_label,check_column_name_list=check_column_name_list,
                                               uncheck_column_name_list=uncheck_column_name_list)
        self.delete_column(parent_label)

    def move_up_columns_for_listbox(self,parent_label:str,check_column_name_list:list=None,uncheck_column_name_list:list=None):
        self.set_check_and_uncheck_for_listbox(parent_label=parent_label, check_column_name_list=check_column_name_list,
                                               uncheck_column_name_list=uncheck_column_name_list)
        self._click_move_up_column_button(parent_label)

    def move_down_columns_for_listbox(self,parent_label:str,check_column_name_list:list=None,uncheck_column_name_list:list=None):
        self.set_check_and_uncheck_for_listbox(parent_label=parent_label, check_column_name_list=check_column_name_list,
                                               uncheck_column_name_list=uncheck_column_name_list)
        self._click_move_down_column_button(parent_label)

    def set_value_for_numeric_stepper(self, parent_label:str, value:str):
        get_numeric_stepper(self.base_xpath,self.page,parent_label=parent_label).set_value(value)

    def click_increment_value_for_numeric_stepper(self, parent_label:str, times:int):
        get_numeric_stepper(self.base_xpath, self.page, parent_label=parent_label).click_increment_value(times)

    def click_decrement_value_for_numeric_stepper(self, parent_label:str, times:int):
        get_numeric_stepper(self.base_xpath, self.page, parent_label=parent_label).click_decrement_value(times)

    def set_rgb_for_color_picker(self, red_value: int, green_value: int, blue_value: int, parent_label:str =None, section_label:str = None):
        if parent_label == None:
            if section_label == None:
                get_button(self.base_xpath, self.page, supplement_base_xpath=
                "[contains(@aria-label,'{0}')]".format(Helper.data_locale.CHOOSE_COLOR)).click_self()
            else:
                get_button(self.base_xpath, self.page, supplement_base_xpath=
                "[contains(@aria-label,'{0}')][../../../../../preceding-sibling::div[.//span[text()='{1}']]]".format(Helper.data_locale.CHOOSE_COLOR,section_label)).click_self()
        else:
            if section_label == None:
                get_button(self.base_xpath, self.page, supplement_base_xpath=
                "[contains(@aria-label,'{0}')][../following-sibling::div[.//label[text()='{1}']]]".format(Helper.data_locale.CHOOSE_COLOR,parent_label)).click_self()
            else:
                get_button(self.base_xpath, self.page, supplement_base_xpath=
                "[contains(@aria-label,'{0}')][../following-sibling::div[.//label[text()='{1}']]/../../../../preceding-sibling::div[.//span[text()='{2}']]]".
                           format(Helper.data_locale.CHOOSE_COLOR, parent_label, section_label)).click_self()
        time.sleep(1)
        color_picker = get_color_picker("", self.page)
        time.sleep(0.5)
        color_picker.click_custom()
        time.sleep(0.5)
        color_picker.set_red_value(red_value)
        time.sleep(0.5)
        color_picker.set_green_value(green_value)
        time.sleep(0.5)
        color_picker.set_blue_value(blue_value)
        time.sleep(0.5)
        color_picker.click_ok()
        time.sleep(0.5)

    # def set_uncheck_for_listbox_item(self, parent_label: str, item_text: str):
    #     """
    #     Description: set check for listbox item.
    #     @parent_label: the label of the listbox control.
    #     @item_text: the text of list item.
    #     """
    #     get_listbox(self.base_xpath, self.page, parent_label=parent_label).set_uncheck_li_item(item_text)
    #
    # # def set_check_for_grid_item(self,parent_label:str, item_index: int, item_text_str):
    #     get_grid(self.base_xpath,self.page,parent_label = parent_label).
