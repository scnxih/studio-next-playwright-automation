"""
Author: Jacky(Jiaqi) Wang
Contact: jiaqi.wang@esas.com
Date: September 5th, 2023
"""

from src.Pages.StudioNext.Center.base_editor import BaseEditor
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem

# ADDED
"""<<< Added by Jacky(ID: jawang) on Sept.7th, 2023 """
from src.Pages.StudioNext.Dialog.autoexec_dialog import AutoexecDialog

# from src.Helper.page_helper import PageHelper
""" Added by Jacky(ID: jawang) on Sept.7th, 2023 >>>"""


class XMLEditor(BaseEditor):
    pass


class JsonEditor(BaseEditor):
    pass


class TextEditor(BaseEditor):
    pass


class WorkspaceEditor(BaseEditor):
    pass


class AutoExecEditor(BaseEditor):
    pass


class CustomCodeEditor(BaseEditor):
    pass


class PlainEditorFactory:
    def create_editor(self, editor_type, page):
        """
        :param editor_type: xml, json, text, workspace, autoexec
        :param page: default
        :return: instance of specific editor
        """
        if editor_type == "xml":
            top_menu = TopMenuPage(page)
            top_menu.new_item(TopMenuItem.new_file_types_xml)
            return XMLEditor(page)

        elif editor_type == "json":
            top_menu = TopMenuPage(page)
            top_menu.new_item(TopMenuItem.new_file_types_json)
            return JsonEditor(page)

        elif editor_type == "text":
            top_menu = TopMenuPage(page)
            top_menu.new_item(TopMenuItem.new_file_types_text)
            return TextEditor(page)

        elif editor_type == "workspace":
            top_menu = TopMenuPage(page)
            top_menu.new_item(TopMenuItem.new_file_types_workspace)
            return WorkspaceEditor(page)

        # ADDED
        elif editor_type == "autoexec":
            # PageHelper.click_options(page, TopMenuItem.options_autoexec_file)
            return AutoExecEditor(page)

        # ADDED
        elif editor_type == "custom":
            return CustomCodeEditor(page)

        else:
            raise ValueError("Unsupported Editor Type!")


""" Added by Jacky(ID: jawang) on Sept. 5th, 2023 """
