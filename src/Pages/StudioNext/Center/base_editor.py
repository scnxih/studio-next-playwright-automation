from src.Pages.Common.toolbar import *
from src.Pages.StudioNext.Dialog.saveas_dialog import SaveAsDialog

""" Added by Jacky(ID: jawang) on Sept. 4th, 2023 """
from src.Pages.StudioNext.Center.center_page import CenterPage
# <--------- Added by Jacky(ID: jawang) on Sept. 7th, 2023 --------- #
from src.Pages.Common.editor_text_area import EditorTextArea
# ---------- Added by Jacky(ID: jawang) on Sept. 7th, 2023 --------> #

# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.12th, 2023 """
from src.Pages.Common.tab_group import TabGroup
# Added by Jacky(ID: jawang) on Sept.12th, 2023 >>>"""

# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.15th, 2023
from src.Pages.Common.context_menu import ContextMenu
# Added by Jacky(ID: jawang) on Sept.15th, 2023 >>>

# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.19th, 2023
from src.Pages.Common.widget import Widget
# Added by Jacky(ID: jawang) on Sept.19th, 2023 >>>

# ADDED
# <<< Added by Jacky(ID: jawang) on Sept.21st, 2023
from src.Pages.Common.treegrid import TreeGrid


# Added by Jacky(ID: jawang) on Sept.21st, 2023 >>>

# class BaseEditor(CenterPage):
class BaseEditor(BasePage):
    """
    Editor = TextArea + Toolbar
    """

    def __init__(self, page):
        # CenterPage.__init__(self, page)
        BasePage.__init__(self, page)
        self.toolbar = Toolbar("", page)
        self.editor_text_area = EditorTextArea("", page)
        # self.editor_text_area = EditorTextArea(self.base_xpath, page)
        self.context_menu = ContextMenu("", page)

        # ADDED
        # <<< Added by Jacky(ID: jawang) on Sept.12th, 2023
        self.tab_group = TabGroup("", page)
        # Added by Jacky(ID: jawang) on Sept.12th, 2023 >>>

        # ADDED
        # <<< Added by Jacky(ID: jawang) on Sept.19th, 2023
        self.widget = Widget("", page)
        # Added by Jacky(ID: jawang) on Sept.19th, 2023 >>>

        # ADDED
        # <<< Added by Jacky(ID: jawang) on Sept.21st, 2023
        self.tree_grid_table = TreeGrid("", page)
        # Added by Jacky(ID: jawang) on Sept.21st, 2023 >>>

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.15th, 2023
    @property
    def div_first_line(self):
        return self.locate_xpath('//div[@class="view-line"]')

    # Added by Jacky(ID: jawang) on Sept.15th, 2023 >>>

    def save_file(self, folder_path, file_name, if_replace):
        """
        Save file by clicking the Save As button

        :param folder_path:
        :param file_name: file name with extension
        :param if_replace: True-Replace
        :return:
        """
        self.toolbar.click_btn_by_title(Helper.data_locale.SAVE_AS)
        Helper.logger.debug("after click save as button")

        """ Added by Jacky(ID: jawang) on Sept. 6th, 2023 """
        # time.sleep(3)
        save_as_dialog = SaveAsDialog(self.page)
        save_as_dialog.wait_for(save_as_dialog.input_file_name)
        """ Added by Jacky(ID: jawang) on Sept. 6th, 2023 """

        Helper.logger.debug("create SaveAsDialog instance")
        if save_as_dialog.is_open():
            return save_as_dialog.save_file(folder_path, file_name, if_replace)
        Helper.logger.error("save as failed.")
        return False

    def fill_text_area_with(self, input_from_user):
        self.editor_text_area.type_into_text_area(input_from_user)

    # ADDED
    """<<< Added by Jacky(ID: jawang) on Sept.12th, 2023 """
    # ! This is NOT WORKING now ! And would be removed in the future.
    #

    def run_and_check_results(self):
        """
        Check log after run
        :return:
        """
        self.toolbar.click_btn_by_title(Helper.data_locale.RUN)
        Helper.logger.debug("after click RUN button")

        # if self.toolbar.btn_by_title(Helper.data_locale.RUN).is_enabled():
        self.tab_group.click_tab_by_title(Helper.data_locale.RESULTS)
        Helper.logger.debug("after click RESULTS tab page")

    def run_and_return_to_code(self):
        """
        Check log after run
        :return:
        """
        self.toolbar.click_btn_by_title(Helper.data_locale.RUN)
        Helper.logger.debug("after click RUN button")

        # if self.toolbar.btn_by_title(Helper.data_locale.RUN).is_enabled():
        self.tab_group.click_tab_by_title(Helper.data_locale.CODE)
        Helper.logger.debug("after click CODE tab page")

    """ Added by Jacky(ID: jawang) on Sept.12th, 2023 >>>"""

    # ADDED
    # <<< Added by Jacky(ID: jawang) on Sept.15th, 2023
    def open_context_menu(self):
        """
        Open code editor context menu
        :return:
        """

        # WORKS FINE
        # self.toolbar.btn_by_title(Helper.data_locale.RUN).click(button="right")

        # WORKS FINE
        # NOTE:  This might be influenced by network performance
        # self.__invoke_context_menu()

        # WORKS FINE
        # NOTE: Right-click on textarea DOES NOT WORK, so first line was used instead.
        # self.__invoke_context_menu_by_right_click(self.div_first_line)

        # WORKS FINE
        # self.div_first_line.click(button="right")

        # DOES NOT WORK
        # xpath //textarea CANNOT be right-clicked on
        # self.editor_text_area.right_click(self.editor_text_area)

    def select_context_menu_item(self, menu_item_text):
        """
        First open context menu, then select menu item based upon user's input
        :param menu_item_text:
        :return:
        """
        self.open_context_menu()
        self.context_menu.click_menu_item_by_text(menu_item_text)

    # Added by Jacky(ID: jawang) on Sept.15th, 2023 >>>
