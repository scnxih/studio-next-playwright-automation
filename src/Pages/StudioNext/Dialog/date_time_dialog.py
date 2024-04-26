"""
@author: Alice
@date: Updated on 2024/04/16
@description: Define date and time dialog.
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

class DateTimeDialog(Dialog):
    def __init__(self, page):
        Dialog.__init__(self, page)


    def click_previous_month(self):
        get_button(self.base_xpath,self.page,aria_label=Helper.data_locale.PREVIOUS_MONTH).click_self()

    def click_next_month(self):
        get_button(self.base_xpath,self.page,aria_label=Helper.data_locale.NEXT_MONTH).click_self()
        
    def select_month(self,month:Month):
        item_value = get_month_value(month)
        get_combobox(self.base_xpath,self.page,data_test_id="calendarHeaderMonthSelect").select_item(item_value)

    def set_year(self,year:str):
        get_text(self.base_xpath,self.page,data_test_id="calendarHeaderYearInput-input").fill_text(year)

    def select_hour(self,hour:str):
        get_combobox(self.base_xpath,self.page,aria_label=Helper.data_locale.HOUR,items_count=24).select_item(hour)

    def select_minute(self,minute:str):
        get_combobox(self.base_xpath,self.page,aria_label=Helper.data_locale.MINUTE,items_count=60).select_item(minute)

    def select_second(self,second:str):
        get_combobox(self.base_xpath,self.page,aria_label=Helper.data_locale.SECOND,items_count=60).select_item(second)
