from enum import Enum


class AccordionType(Enum):
    open_item = 0
    sas_server = 1
    sas_content = 2
    steps = 3
    snippets = 4
    libraries = 5
    git = 6
    file_references = 7
    clinical_repository = 8


class TopMenuItem(Enum):
    new = 0
    new_sas_program = 1
    new_python_program = 2
    new_flow = 3
    new_query = 4
    new_custom_step = 5
    new_quick_import = 6
    new_job_definition = 7
    new_file_types = 8
    new_file_types_json = 9
    new_file_types_text = 10
    new_file_types_xml = 11
    new_file_types_workspace = 12

    options = 20
    options_autoexec_file = 21
    options_custom_code = 22
    options_manage_keyboard_shortcuts = 23
    # ----------Added by Dommy, 9/4/2023 begin---- #
    options_manage_git_connections = 24
    # ----------Added by Dommy, 9/4/2023 end---- #
    # need others

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Oct.30th, 2023
    options_change_perspective = 25
    options_change_perspective_standard = 26
    options_change_perspective_interactive = 27

    # Added by Jacky(ID: jawang) on Oct.30th, 2023 >>> END

    """Added by Alice on 11/02/2023 start"""
    view = 30
    view_search = 31
    view_submission_status = 32
    view_deployed_and_scheduled_jobs = 33
    view_command = 34
    view_console = 35
    view_start_page = 36
    view_navigation_panes = 37
    view_navigation_panes_open_items = 38
    view_navigation_panes_sas_server = 39
    view_navigation_panes_sas_content = 40
    view_navigation_panes_steps = 41
    view_navigation_panes_snippets = 42
    view_navigation_panes_library_connections = 43
    view_navigation_panes_git_repositories = 44
    view_navigation_panes_file_references = 45
    view_navigation_panes_clinical_repositories = 46
    view_document_recovery = 47
    view_startup_initialization_log = 48

    """Added by Alice on 11/02/2023 end"""


class AccountOptionsMenuItem(Enum):
    what_s_new = 0
    settings = 1
    about = 2
    sing_out = 3
    manege_features = 4


class SettingsTabPages(Enum):
    global_general = 0
    region_and_language = 1
    accessibility = 2
    start_up = 3
    sas_studio_general = 4
    code_and_log = 5
    results = 6
    editors = 7
    tables = 8
    flows = 9
    background_submit = 10
    query = 11
    quick_import = 12


class Platform(Enum):
    microsoft_windows = 0
    apple = 1
    linux = 2


log_options = {
    "showSASCodeInLog-checkbox-checkbox": "Show generated SAS code in the SAS log",
    # "displayErrorInGutter-checkbox-checkbox": "Display error and warning icons in the Code tab gutter"
    "displayErrorInGutter-checkbox-checkbox": "生成错误、警告和注意汇总"
}


# added by liu jia for custom code dialog
class DialogTab(Enum):
    Tab_front = 0
    Tab_back = 1
    Tab_option = 2


# End
"""added by Alice on 10/25/2023 start"""


class FlowNodeType(Enum):
    table = 0
    file = 1
    branch_rows = 2
    calculate_columns = 3
    sas_program = 4
    execute_decisions = 5
    export = 6
    filter_rows = 7
    implement_scd = 8
    import_data = 9
    insert_rows = 10
    load_table = 11
    manage_columns = 12
    merge_table = 13
    python_program = 14
    query = 15
    sort = 16
    union_rows = 17
    notes = 18


"""added by Alice on 10/25/2023 end"""

"""Added by Alice on 11/07/2023 start"""


class CenterPageType(Enum):
    sas_program_page = 0
    python_program_page = 1
    flow_page = 2
    query_page = 3
    quick_import_page = 4
    json_page = 5
    text_page = 6
    xml_page = 7
    work_space_page = 8
    deployed_scheduled_job_page = 9
    start_initialization_log_page = 10
    submission_status_page = 11
    job_definition_page = 12
    custom_step_page = 13


"""Added by Alice on 11/07/2023 end"""

"""Added by Alice on 11/09/2023 start"""


class DialogType(Enum):
    about_dialog = 0
    add_profile_dialog = 1
    autoexec_dialog = 2
    custom_code_dialog = 3
    document_recovery_dialog = 4
    keyboard_shortcuts_dialog = 5
    manage_git_connection_dialog = 6
    manage_shortcuts_dialog = 7
    new_folder_dialog = 8
    open_dialog = 9
    query_output_lib_dialog = 10
    query_select_table_dialog = 11
    save_as_dialog = 12
    search_dialog = 13
    settings_dialog = 14


"""Added by Alice on 11/09/2023 end"""


class DesignerControlType(Enum):
    checkbox = 0
    color_picker = 1
    date_and_time_picker = 2
    drop_down_list = 3
    file_or_folder_selector = 4
    link = 5
    list = 6
    numeric_stepper = 7
    radio_group = 8
    section = 9
    text = 10
    textarea = 11
    text_or_numeric_field = 12
    column_selector = 13
    input_table = 14
    new_column = 15
    output_table = 16


class SortWay(Enum):
    ascending = 0
    descending = 1
