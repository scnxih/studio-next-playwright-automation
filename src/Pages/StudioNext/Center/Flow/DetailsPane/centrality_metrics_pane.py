from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *
from src.Pages.StudioNext.Dialog.select_column_dialog import SelectColumnDialog


class CentralityMetricsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Below methods are in Data tab"""

    def set_link_direction(self, item_index=None, item_value=None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.LINK_DIRECTION,
                                        item_index=item_index, item_value=item_value)

    def expand_windowshade_additional_roles(self):
        self.expand_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def collapse_windowshade_additional_roles(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.ADDITIONAL_ROLES)

    def add_column_for_from_node(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.FROM_NODE, column_name=column_name)

    def add_column_for_to_node(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.TO_NODE, column_name=column_name)

    def add_column_for_weight_in_links(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.WEIGHT_WITH_COLON,section_label=Helper.data_locale.LINKS, column_name=column_name)

    def add_column_for_auxiliary_weight(self, column_name: str):
        self.add_column(parent_label=Helper.data_locale.AUXILIARY_WEIGHT, column_name=column_name)

    def add_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                          uncheck_column_name_list: list = None):
        self.add_columns(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                         check_column_name_list=check_column_name_list,
                         uncheck_column_name_list=uncheck_column_name_list)

    def delete_column_for_from_node(self):
        self.delete_column(parent_label=Helper.data_locale.FROM_NODE)

    def delete_column_for_to_node(self):
        self.delete_column(parent_label=Helper.data_locale.TO_NODE)

    def delete_column_for_weight_in_links(self):
        self.delete_column_exact_label(parent_label=Helper.data_locale.WEIGHT_WITH_COLON,section_label=Helper.data_locale.LINKS)

    def delete_column_for_auxiliary_weight(self):
        self.delete_column(parent_label=Helper.data_locale.AUXILIARY_WEIGHT)

    def delete_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                             uncheck_column_name_list: list = None):
        self.delete_columns_for_listbox(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                                        check_column_name_list=check_column_name_list,
                                        uncheck_column_name_list=uncheck_column_name_list)

    def move_up_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                              uncheck_column_name_list: list = None):
        self.move_up_columns_for_listbox(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                                         check_column_name_list=check_column_name_list,
                                         uncheck_column_name_list=uncheck_column_name_list)

    def move_down_columns_for_group_analysis_by(self, check_column_name_list: list = None,
                                                uncheck_column_name_list: list = None):
        self.move_down_columns_for_listbox(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY,
                                           check_column_name_list=check_column_name_list,
                                           uncheck_column_name_list=uncheck_column_name_list)

    def expand_windowshade_links(self):
        self.expand_windowshade(parent_label=Helper.data_locale.LINKS)

    def collapse_windowshade_links(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.LINKS)

    def expand_windowshade_nodes(self):
        self.expand_windowshade(parent_label=Helper.data_locale.NODES)

    def collapse_windowshade_nodes(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.NODES)

    def set_check_include_nodes_data(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INCLUDE_NODES_DATA)

    def set_uncheck_include_nodes_data(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.INCLUDE_NODES_DATA)

    def add_column_for_node(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.NODE_WITH_COLON, column_name=column_name)

    def delete_column_for_node(self):
        self.delete_column_exact_label(parent_label=Helper.data_locale.NODE_WITH_COLON)

    def add_column_for_weight_in_nodes(self,column_name:str):
        self.add_column_exact_label(parent_label=Helper.data_locale.WEIGHT_WITH_COLON,section_label=Helper.data_locale.NODES,column_name = column_name)

    def delete_column_for_weight_in_nodes(self):
        self.delete_column_exact_label(parent_label=Helper.data_locale.WEIGHT_WITH_COLON, section_label=Helper.data_locale.NODES)


    """Below methods are in Options tab"""
    def set_check_degree(self):
        self.set_check_for_checkbox(label=Helper.data_locale.DEGREE)

    def set_uncheck_degree(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.DEGREE)

    def set_check_influence(self):
        self.set_check_for_checkbox(label=Helper.data_locale.INFLUENCE)

    def set_uncheck_influence(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.INFLUENCE)

    def set_metric_type_for_influence(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METRIC_TYPE,
                                     section_label=Helper.data_locale.INFLUENCE,
                                     item_index=item_index, item_value=item_value)

    def set_check_clustering_coefficient(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CLUSTERING_COEFFICIENT)

    def set_uncheck_clustering_coefficient(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CLUSTERING_COEFFICIENT)

    def set_check_closeness(self):
        self.set_check_for_checkbox(label=Helper.data_locale.CLOSENESS)

    def set_uncheck_closeness(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.CLOSENESS)

    def set_metric_type_for_closeness(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METRIC_TYPE,
                                     section_label=Helper.data_locale.CLOSENESS,
                                     item_index=item_index, item_value=item_value)

    def set_shortest_path_distance_between_disconnected_nodes(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.SHORTEST_PATH_DISTANCE_BETWEEN_DISCONNECTED_NODES,
                                     item_index=item_index, item_value=item_value)

    def set_check_betweenness(self):
        self.set_check_for_checkbox(label=Helper.data_locale.BETWEENNESS)

    def set_uncheck_betweenness(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.BETWEENNESS)

    def set_metric_type_for_betweenness(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METRIC_TYPE,
                                     section_label=Helper.data_locale.BETWEENNESS, item_index=item_index,
                                     item_value=item_value)

    def set_check_normalize_betweenness_centrality(self):
        self.set_check_for_checkbox(label=Helper.data_locale.NORMALIZE_BETWEENNESS_CENTRALITY)

    def set_uncheck_normalize_betweenness_centrality(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.NORMALIZE_BETWEENNESS_CENTRALITY)

    def set_check_eigenvector(self):
        self.set_check_for_checkbox(label=Helper.data_locale.EIGENVECTOR)

    def set_uncheck_eigenvector(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.EIGENVECTOR)

    def set_metric_type_for_eigenvector(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.METRIC_TYPE,
                                     section_label=Helper.data_locale.EIGENVECTOR, item_index=item_index,
                                     item_value=item_value)

    def set_check_hub_score(self):
        self.set_check_for_checkbox(label=Helper.data_locale.HUB_SCORE)

    def set_uncheck_hub_score(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.HUB_SCORE)

    def set_check_authority_score(self):
        self.set_check_for_checkbox(label=Helper.data_locale.AUTHORITY_SCORE)

    def set_uncheck_authority_score(self):
        self.set_uncheck_for_checkbox(label=Helper.data_locale.AUTHORITY_SCORE)

    def expand_windowshade_centrality_metrics(self):
        self.expand_windowshade(parent_label=Helper.data_locale.STEP_CENTRALITY_METRICS)

    def collapse_windowshade_centrality_metrics(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.STEP_CENTRALITY_METRICS)

    def expand_windowshade_methods(self):
        self.expand_windowshade(parent_label=Helper.data_locale.METHODS)

    def collapse_windowshade_methods(self):
        self.collapse_windowshade(parent_label=Helper.data_locale.METHODS)

    def set_eigenvector_calculation_method(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.EIGENVECTOR_CALCULATION_METHOD,
                                        item_index=item_index, item_value=item_value)

    def set_maximum_number_of_iterations_for_eigenvector_calculations(self, item_index: int = None,
                                                                      item_value: str = None):
        self.set_option_for_radio_group(
            parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS_FOR_EIGENVECTOR_CALCULATIONS,
            item_index=item_index, item_value=item_value)

    def set_log_details(self, item_index: int = None, item_value: str = None):
        self.set_option_for_combobox(parent_label=Helper.data_locale.LOG_DETAILS, item_index=item_index,
                                     item_value=item_value)

    def set_code_generation(self, item_index: int = None, item_value: str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.CODE_GENERATION, item_index=item_index,
                                        item_value=item_value)

    def set_number_of_iterations(self, input_text: str):
        self.set_text_for_text_control(parent_label=Helper.data_locale.NUMBER_OF_ITERATIONS, input_text=input_text)




