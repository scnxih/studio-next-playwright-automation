from src.Pages.StudioNext.Center.Flow.DetailsPane.OptimizationAndNetworkAnalysis.core_decomposition_pane import \
    CoreDecompositionPane
from src.Pages.StudioNext.Center.Flow.DetailsPane.basic_step_pane import BasicStepPane
from src.Helper.helper import Helper


class CommunityDetectionPane(CoreDecompositionPane):
    def __init__(self, page):
        BasicStepPane.__init__(self, page)

    def add_column_for_weight_in_nodes(self, column_name: str):
        self.add_column_exact_label(parent_label=Helper.data_locale.WEIGHT_WITH_COLON,
                                    column_name=column_name, section_label=Helper.data_locale.LINK)
