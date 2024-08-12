"""
Author: Alice
Date: Mar 05, 2024
Description: This is base class of all Flow details pane.

"""

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

    def click_Tab(self, text: str):
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
        self.click_Tab(Helper.data_locale.NODE)
        Text(self.base_xpath, self.page,
             supplement_base_xpath="[../../../descendant::label[contains(text(),'" + Helper.data_locale.NODE_NAME + "')]]").fill_text(
            name)

    def set_node_description(self, description: str):
        """
        Description: set node description.
        @description: the description you want to specify for the node.
        """
        self.click_Tab(Helper.data_locale.NODE)
        Textarea(self.base_xpath, self.page).fill_text(description)

    def set_notes(self, notes: str):
        """
        Description: set node notes.
        @notes: the notes you want to specify for the node.
        """
        self.click_Tab(Helper.data_locale.NOTES)
        Textarea(self.base_xpath, self.page).fill_text(notes)

    def click_data_tab(self):
        """
        Description: click Data tab.
        """
        self.click_Tab(Helper.data_locale.DATA)

    def click_options_tab(self):
        """
        Description: click Options tab.
        """
        self.click_Tab(Helper.data_locale.OPTIONS)

    def click_output_tab(self):
        """
        Description: click Output tab.
        """
        self.click_Tab(Helper.data_locale.OUTPUT)

    def click_node_tab(self):
        """
        Description: click Node tab.
        """
        self.click_Tab(Helper.data_locale.NODE)

    def click_notes_tab(self):
        """
        Description: click Notes tab.
        """
        self.click_Tab(Helper.data_locale.NOTES)

    def _get_add_column_button(self, parent_label: str):
        return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(
                              Helper.data_locale.ADD_COLUMN, parent_label))

    def _get_add_exact_column_button(self, parent_label: str):
        return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']]".format(
                              Helper.data_locale.ADD_COLUMN, parent_label))

    def _get_delete_column_button(self, parent_label: str):
        return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[contains(text(),'{1}')]]".format(
                              Helper.data_locale.DELETE_COLUMNS, parent_label))

    def _get_delete_exact_column_button(self, parent_label: str):
        return get_button(self.base_xpath, self.page,
                          supplement_base_xpath="[@aria-label='{0}'][../../../descendant::label[text()='{1}']]".format(
                              Helper.data_locale.DELETE_COLUMNS, parent_label))

    def click_add_column_button(self, parent_label: str):
        """
        Description: click add column button.
        @parent_label: the label of the add column button. The colon is not required.
        """
        self._get_add_column_button(parent_label=parent_label).click_self()

    def delete_column(self, parent_label: str):
        """
        Description: click delete column button.
        @parent_label: the label of the delete column button. The colon is not required.
        """
        self._get_delete_column_button(parent_label=parent_label).click_self()

    def click_add_exact_column_button(self, parent_label: str):
        """
        Description: click add column button which label is exact the label(including colon:).
        The method is only used for the buttons which have duplicated parts in label,
        such as Weight when Auxiliary weight exists as well.
        Please note if use this method, the colon(:) should also be passed in the parent_label parameter since this is exact the label.
        @parent_label: the exact label of the add column button.
        """
        self._get_add_exact_column_button(parent_label=parent_label).click_self()

    def click_delete_exact_column_button(self, parent_label: str):
        """
        Description: click delete column button which label is exact the label(including colon:).
        The method is only used for the buttons which have duplicated parts in label,
        such as Weight when Auxiliary weight exists as well.
        Please note if use this method, the colon(:) should also be passed in the parent_label parameter since this is exact the label.
        @parent_label: the exact label of the delete column button.
        """
        self._get_delete_exact_column_button(parent_label=parent_label).click_self()

    def set_column(self, parent_label: str, column_name: str):
        """
        Description: add a column, pop up select a column dialog and choose a column and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label could be the part of the parent label, that is,
        the colon(:) can be omitted.
        @column_name: the column name of the added column.
        """
        self.click_add_column_button(parent_label=parent_label)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)

    def set_column_exact_label(self, parent_label: str, column_name: str):
        """
        Description: add a column, pop up select a column dialog and choose a column and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label should be exact the label, that is, the colon(:)
        could NOT be omitted. The method will be used only when there are labels which text has duplicate parts. For example,
        if there is weight and auxiliary weight, this method should be used for weight.
        @column_name: the column name of the added column.
        """
        self.click_add_exact_column_button(parent_label=parent_label)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)

    def set_columns(self, parent_label: str, check_column_name_list: list, uncheck_column_name_list: list):
        """
        Description: set columns, pop up select columns dialog and check columns defined in check_column_name_list,
        uncheck columns defined in uncheck_column_name_list and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label could be the part of the parent label, that is,
        the colon(:) can be omitted.
        @check_column_name_list: the list of columns which you want to check.
        @uncheck_column_name_list: the list of columns which you want to uncheck.
        """
        self.click_add_column_button(parent_label=parent_label)
        select_column_dialog = SelectColumnDialog(self.page)
        for check_column_name in check_column_name_list:
            select_column_dialog.set_check_in_a_row(check_column_name)

        for uncheck_column_name in uncheck_column_name_list:
            select_column_dialog.set_uncheck_in_a_row(uncheck_column_name)

        time.sleep(0.5)
        select_column_dialog.click_ok_button()
        time.sleep(0.5)

    def set_columns_exact_label(self, parent_label: str, check_column_name_list: list, uncheck_column_name_list: list):
        """
        Description: set columns, pop up select columns dialog and check columns defined in check_column_name_list,
        uncheck columns defined in uncheck_column_name_list and click OK to dismiss the dialog.
        @parent_label: the label of the add columns button, the label could be the part of the parent label, that is,
        the colon(:) can be omitted.
        @check_column_name_list: the list of columns which you want to check.
        @uncheck_column_name_list: the list of columns which you want to uncheck.
        """
        self.click_add_exact_column_button(parent_label=parent_label)
        select_column_dialog = SelectColumnDialog(self.page)
        for check_column_name in check_column_name_list:
            select_column_dialog.set_check_in_a_row(check_column_name)

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

    def set_option_for_radio_group(self, parent_label: str, item_index: int = None, item_value: str = None):
        """
        Description: set option for radio group by item index(index starts from 0) or by item value.
        @parent_label: the label of radio group.
        @item_index: index of selected option, starting from 0.
        @item_value: value of selected option.
        """
        if item_index != None:
            get_radio_group(self.base_xpath, self.page,
                            parent_label=parent_label).set_check_for_index(index=item_index)
            return
        if item_value != None:
            get_radio_group(self.base_xpath, self.page,
                            parent_label=parent_label).set_check(text=item_value)
            return

    def set_check_for_checkbox(self, label: str):
        """
        Description: set checked for check box.
        @label: the label of the checkbox.
        """

        get_checkbox(self.base_xpath, self.page, label=label).set_check()


    def set_uncheck_for_checkbox(self, label: str):
        """
        Description: set unchecked for check box.
        @label: the label of the checkbox.

        """
        get_checkbox(self.base_xpath, self.page, label=label).set_uncheck()


    def set_option_for_combobox(self, parent_label: str, section_label: str = None, item_index: int = None,
                                item_value: str = None):
        """
        Description: set option for combobox (dropdown list).
        @parent_label: the label of the combobox.
        @section_label: the parameter is used only when there are more than one combobox which have same parent label.
        @item_index: the index of the selected option of the combobox, starting from 0.
        @item_value: the value of the selected option of the combobox.
        """
        combobox = None
        if section_label == None:

            combobox = get_combobox(self.base_xpath, self.page,
                                supplement_base_xpath="[../../../../../../../../descendant::label[contains(text(),'{0}')]]".format(
                                    parent_label))

        else:
            combobox = get_combobox(self.base_xpath, self.page,
                                    supplement_base_xpath="[../../../../../../../../descendant::label[contains(text(),'{0}')]/../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{1}')]]]".format(
                                        parent_label,section_label))

        if item_index != None:
            combobox.select_item_by_index(item_index)
            return
        if item_value != None:
            combobox.select_item(item_value)
            return

    def set_text_for_text_control(self, parent_label: str,input_text:str):
        """
        Description: set text for text control.
        @parent_label: the label of the text control.
        @text: the text you want to input.
        """
        get_text(self.base_xpath,self.page,parent_label=parent_label).fill_text(input_text)
