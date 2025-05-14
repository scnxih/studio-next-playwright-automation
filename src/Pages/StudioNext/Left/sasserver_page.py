from src.Pages.StudioNext.Left.sas_content_server_page import *


class SASServerPage(SASContentServerPage):
    def __init__(self, page):
        SASContentServerPage.__init__(self, page,Helper.data_locale.SAS_SERVER)

    def click_upload_to_server_btn(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.UPLOAD_FILES_TO_SAS_SERVER)

