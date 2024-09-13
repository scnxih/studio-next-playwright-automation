"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@sas.com
Date: August 13th, 2024
"""
# -*- coding: UTF-8 -*-
from src.Helper.helper import Helper
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane


class SameBirthdayProbabilityPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def set_number_of_people_in_a_room(self, filter_text: str):
        """
        set 'Number of people in a room'
        """
        self.click_tab(Helper.data_locale.OPTIONS)
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_PEOPLE_IN_A_ROOM, input_text=filter_text)
