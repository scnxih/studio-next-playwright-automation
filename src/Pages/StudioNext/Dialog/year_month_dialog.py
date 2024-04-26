"""
@author: Alice
@date: Created on 2024/04/17
@description: Define year and month dialog.
"""

from src.Pages.Common.dialog import *
from src.Pages.Common.common_component_factory import *
from src.Utilities.enums import *


def get_month_value(month:Month):
    item_value = ""
    match month:
        case Month.january:
            item_value = Helper.data_locale.JANUARY
        case Month.february:
            item_value = Helper.data_locale.FEBRUARY
        case Month.march:
            item_value = Helper.data_locale.MARCH
        case Month.april:
            item_value = Helper.data_locale.APRIL
        case Month.may:
            item_value = Helper.data_locale.MAY
        case Month.june:
            item_value = Helper.data_locale.JUNE
        case Month.july:
            item_value = Helper.data_locale.JULY
        case Month.august:
            item_value = Helper.data_locale.AUGUST
        case Month.september:
            item_value = Helper.data_locale.SEPTEMBER
        case Month.october:
            item_value = Helper.data_locale.OCTOBER
        case Month.november:
            item_value = Helper.data_locale.NOVEMBER
        case Month.december:
            item_value = Helper.data_locale.DECEMBER
    return item_value


class YearMonthDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page)

    def set_year(self,year:str):
        get_text(self.base_xpath,self.page,supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]".format(Helper.data_locale.YEAR)).fill_text(year)

    def select_month(self,month:Month):
        combobox = get_combobox(self.base_xpath, self.page,
                     supplement_base_xpath="[../../../descendant::label[contains(text(),'{0}')]]"
                     .format(Helper.data_locale.MONTH))
        item_value = get_month_value(month)
        combobox.select_item(item_value)


