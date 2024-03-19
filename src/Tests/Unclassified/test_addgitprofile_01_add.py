from src.conftest import *
from src.Utilities.vars import *
from src.Helper.page_helper import *
from src.Pages.StudioNext.Dialog.manage_git_connection_dialog import *
from src.Pages.StudioNext.Dialog.add_profile_dialog import *


def test_01_add_git_profile(page, init):
    manage_git_conn = ManageGitConnectionDialog(page)
    PageHelper.click_options(page, TopMenuItem.options_manage_git_connections)
    PageHelper.add_git_profile_ssh(page,'test1', 'aa', 'sss@sas.com', 'ss1.pub', 'ss1')
    PageHelper.add_git_profile_ssh(page, 'test2', 'aa', 'sss@sas.com', 'ss1.pub', 'ss1')
    data = {'profile_name': 'New_Test', 'user_name': 'New_Dommy'}
    PageHelper.edit_git_profile_ssh(page,'test1',**data)
    PageHelper.delete_profile(page,'New_Test')
    PageHelper.set_profile_as_default(page, 'test2')
    time.sleep(2)
    manage_git_conn.close_manage_git_connection_dialog()


