from src.Pages.Common.common_component_factory import *
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Pages.Common.textarea import *
from src.Pages.StudioNext.Dialog.select_column_dialog import SelectColumnDialog



class CentralityMetricsPane(BasicStepPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    """Below methods are in Data tab"""
    def set_link_direction_undirected(self):
        get_radio_group(self.base_xpath,self.page,parent_label=Helper.data_locale.LINK_DIRECTION).set_check(Helper.data_locale.UNDIRECTED)

    def set_link_direction_directed(self):
        get_radio_group(self.base_xpath,self.page,parent_label=Helper.data_locale.LINK_DIRECTION).set_check(Helper.data_locale.DIRECTED)

    def expand_windowshade_additional_roles(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.ADDITIONAL_ROLES).expand()

    def collapse_windowshade_additional_roles(self):
        get_windowshade(self.base_xpath, self.page, parent_label=Helper.data_locale.ADDITIONAL_ROLES).collapse()

    def set_column_for_from_node(self, column_name:str):
        self.click_add_column_button(parent_label=Helper.data_locale.FROM_NODE)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)
    def set_column_for_to_node(self,column_name:str):
        self.click_add_column_button(parent_label=Helper.data_locale.TO_NODE)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)

    def set_column_for_weight(self, column_name: str):
        self.click_add_exact_column_button(parent_label=Helper.data_locale.WEIGHT_WITH_COLON)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)

    def set_column_for_auxiliary_weight(self, column_name: str):
        self.click_add_column_button(parent_label=Helper.data_locale.AUXILIARY_WEIGHT)
        select_column_dialog = SelectColumnDialog(self.page)
        select_column_dialog.select_a_column_and_OK(column_name)

    def set_columns_for_group_analysis_by(self, check_column_name_list:list,uncheck_column_name_list:list):
        self.click_add_column_button(parent_label=Helper.data_locale.GROUP_ANALYSIS_BY)
        select_column_dialog = SelectColumnDialog(self.page)
        for check_column_name in check_column_name_list:
            select_column_dialog.set_check_in_a_row(check_column_name)

        for uncheck_column_name in uncheck_column_name_list:
            select_column_dialog.set_uncheck_in_a_row(uncheck_column_name)

        time.sleep(0.5)
        select_column_dialog.click_ok_button()
        time.sleep(0.5)

    def delete_column_for_from_node(self):
        self.click_delete_column_button(parent_label=Helper.data_locale.FROM_NODE)

    def delete_column_for_to_node(self):
        self.click_delete_column_button(parent_label=Helper.data_locale.TO_NODE)
    def delete_column_for_weight(self):
        self.click_delete_column_button(parent_label=Helper.data_locale.WEIGHT)

    def delete_column_for_auxiliary_weight(self):
        self.click_delete_column_button(parent_label=Helper.data_locale.AUXILIARY_WEIGHT)

    def expand_windowshade_links(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.LINKS).expand()

    def collapse_windowshade_links(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.LINKS).collapse()

    """Below methods are in Options tab"""
    def expand_centrality_metrics(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.STEP_CENTRALITY_METRICS).expand()

    def collapse_centrality_metrics(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.STEP_CENTRALITY_METRICS).collapse()


    def set_check_degree(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.DEGREE).set_check()

    def set_uncheck_degree(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.DEGREE).set_uncheck()

    def set_check_influence(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.INFLUENCE).set_check()

    def set_uncheck_influence(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.INFLUENCE).set_uncheck()

    def set_metric_type_for_influence(self,item_index:int= None, item_value:str= None):
        """
        Description: select metric type for influence by item index(index starts from 0) or by item value.
        """
        combobox = get_combobox(self.base_xpath, self.page,
                                supplement_base_xpath="[../../../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{0}')]]]".format(
                                    Helper.data_locale.INFLUENCE))

        if item_index!= None:
            return combobox.select_item_by_index(item_index)
        if item_value!= None:
            return combobox.select_item(item_value)

    def set_check_clustering_coefficient(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.CLUSTERING_COEFFICIENT).set_check()


    def set_uncheck_clustering_coefficient(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.CLUSTERING_COEFFICIENT).set_uncheck()

    def set_check_closeness(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.CLOSENESS).set_check()

    def set_uncheck_closeness(self):
        get_checkbox(self.base_xpath, self.page, label=Helper.data_locale.CLOSENESS).set_uncheck()

    def set_metric_type_for_closeness(self,item_index:int= None, item_value:str= None):
        """
        Description: select metric type for eigenvector by item index(index starts from 0) or by item value.
        """
        combobox = get_combobox(self.base_xpath,self.page,supplement_base_xpath="[../../../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{0}')]]]".format(Helper.data_locale.CLOSENESS))
        if item_index!= None:
            return combobox.select_item_by_index(item_index)
        if item_value!= None:
            return combobox.select_item(item_value)
    def set_shortest_path_distance_between_disconnected_nodes(self,item_index:int= None,item_value:str=None):
        combobox = get_combobox(self.base_xpath,self.page,parent_label=Helper.data_locale.SHORTEST_PATH_DISTANCE_BETWEEN_DISCONNECTED_NODES,parent_label_level=6)
        if item_index != None:
            return combobox.select_item_by_index(item_index)
        if item_value != None:
            return combobox.select_item(item_value)

    def set_check_betweenness(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.BETWEENNESS).set_check()

    def set_uncheck_betweenness(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.BETWEENNESS).set_uncheck()

    def set_metric_type_for_betweenness(self,item_index:int= None, item_value:str= None):
        """
        Description: select metric type for eigenvector by item index(index starts from 0) or by item value.
        """
        combobox = get_combobox(self.base_xpath,self.page,supplement_base_xpath="[../../../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{0}')]]]".format(Helper.data_locale.BETWEENNESS))
        if item_index!= None:
            return combobox.select_item_by_index(item_index)
        if item_value!= None:
            return combobox.select_item(item_value)
    def set_check_normalize_betweenness_centrality(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.NORMALIZE_BETWEENNESS_CENTRALITY).set_check()

    def set_uncheck_normalize_betweenness_centrality(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.NORMALIZE_BETWEENNESS_CENTRALITY).set_uncheck()

    def set_check_eigenvector(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.EIGENVECTOR).set_check()

    def set_uncheck_eigenvector(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.EIGENVECTOR).set_uncheck()

    def set_metric_type_for_eigenvector(self,item_index:int= None, item_value:str= None):
        """
        Description: select metric type for eigenvector by item index(index starts from 0) or by item value.
        """
        combobox = get_combobox(self.base_xpath,self.page,supplement_base_xpath="[../../../../../../../../preceding-sibling::div[1][.//label[contains(text(),'{0}')]]]".format(Helper.data_locale.EIGENVECTOR))
        if item_index!= None:
            combobox.select_item_by_index(item_index)
            return
        if item_value!= None:
            combobox.select_item(item_value)
            return

    def set_check_hub_score(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.HUB_SCORE).set_check()

    def set_uncheck_hub_score(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.HUB_SCORE).set_uncheck()

    def set_check_authority_score(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.AUTHORITY_SCORE).set_check()

    def set_uncheck_authority_score(self):
        get_checkbox(self.base_xpath,self.page,label=Helper.data_locale.AUTHORITY_SCORE).set_uncheck()

    def expand_windowshade_centrality_metrics(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.STEP_CENTRALITY_METRICS).expand()

    def collapse_windowshade_centrality_metrics(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.STEP_CENTRALITY_METRICS).collapse()

    def expand_windowshade_methods(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.METHODS).expand()

    def collapse_windowshade_methods(self):
        get_windowshade(self.base_xpath,self.page,parent_label=Helper.data_locale.METHODS).collapse()

    def set_eigenvector_calculation_method(self,item_index : int = None, item_value : str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.EIGENVECTOR_CALCULATION_METHOD,item_index=item_index,item_value=item_value)
    def set_maximum_number_of_iterations_for_eigenvector_calculations(self,item_index : int = None, item_value : str = None):
        self.set_option_for_radio_group(parent_label=Helper.data_locale.MAXIMUM_NUMBER_OF_ITERATIONS_FOR_EIGENVECTOR_CALCULATIONS,
                                        item_index=item_index, item_value=item_value)