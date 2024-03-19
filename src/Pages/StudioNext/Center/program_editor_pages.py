from src.Pages.StudioNext.Center.base_editor import BaseEditor
from src.Pages.StudioNext.Top.top_menu_page import TopMenuPage
from src.Utilities.enums import TopMenuItem

""" Added by Jacky(ID: jawang) on Sept. 5th, 2023 """


class SASProgramEditor(BaseEditor):
    pass


class PythonEditor(BaseEditor):
    pass


class ProgramEditorFactory:
    def create_program_editor(self, editor_type, page):
        """
        :param editor_type: sas_program, python
        :param page: default
        :return: instance of specific editor
        """
        if editor_type == "sas_program":
            top_menu = TopMenuPage(page)
            top_menu.new_item(TopMenuItem.new_sas_program)
            return SASProgramEditor(page)

        elif editor_type == "python":
            top_menu = TopMenuPage(page)
            top_menu.new_item(TopMenuItem.new_python_program)
            return PythonEditor(page)

        else:
            raise ValueError("Unsupported Editor Type!")

