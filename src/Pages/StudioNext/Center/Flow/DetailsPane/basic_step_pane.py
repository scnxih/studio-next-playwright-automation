from src.Helper.helper import Helper
from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.details_pane import DetailsPane


class BasicStepPane(DetailsPane):
    def __init__(self, page):
        DetailsPane.__init__(self, page)

    def set_filter_input_data(self,filter:str):
        self.click_Tab(Helper.data_locale.DATA)
        get_text(self.base_xpath,self.page,parent_label=Helper.data_locale.FILTER_INPUT_DATA).fill_text(filter)


