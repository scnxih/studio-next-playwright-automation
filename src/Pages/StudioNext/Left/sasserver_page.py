from src.Pages.StudioNext.Left.sas_content_server_page import *


class SASServerPage(SASContentServerPage):
    def __init__(self, page):
        SASContentServerPage.__init__(self, page,Helper.data_locale.SAS_SERVER)
