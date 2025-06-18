from src.Helper.helper import Helper
from src.Pages.Common.dialog import Alert
from src.Pages.Common.tab_group import TabGroup
from src.Pages.Common.base_page import BasePage


class TopTabGroup(BasePage):
    def __init__(self, page):
        BasePage.__init__(self, page)
        self.tab_group = TabGroup(container_base_xpath="",page=page,supplement_base_xpath="[ancestor::div["
                                                                                          "@data-testid='tab-group-bar-_root_']]")

    def close_all_tabs(self):
        # original
        # if self.is_visible(self.tab_group.first_tab_page()):

        # Revised on June 18, 2025
        while self.is_visible(self.tab_group.first_tab_page()):
            # Original
            # self.click_context_menu_by_right_click(self.tab_group.first_tab_page(), Helper.data_locale.CLOSE_ALL)

            # Disabled 'Close All' menu item
            # Wednesday, June 4, 2025
            self.click_context_menu_by_right_click(self.tab_group.first_tab_page(), Helper.data_locale.CLOSE)

            alert = Alert(self.page, Helper.data_locale.CONFIRM_CLOSE)
            while alert.is_open() and self.is_visible(self.tab_group.first_tab_page()):
                alert.click_button_in_footer(Helper.data_locale.NO_SAVE)