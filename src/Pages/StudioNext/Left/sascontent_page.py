from src.Pages.StudioNext.Left.sas_content_server_page import *


class SASContentPage(SASContentServerPage):
    def __init__(self, page):
        SASContentServerPage.__init__(self, page,Helper.data_locale.SAS_CONTENT)

    def click_upload_to_content_btn(self):
        self.toolbar.click_btn_by_title(Helper.data_locale.UPLOAD_FILES_TO_SAS_CONTENT)
